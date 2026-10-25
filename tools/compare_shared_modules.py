#!/usr/bin/env python3
"""Compare repeated package identities at the inventory's pinned source commits."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess

DOCS = Path(__file__).resolve().parents[1]
RUNTIME_ROOTS = ('src/', 'database/', 'routes/', 'resources/', 'config/', 'lang/')


def digest_map(files):
    payload = json.dumps(files, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(payload).hexdigest()


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects', type=Path, default=Path('/home/liberu/projects'))
    args = parser.parse_args()
    inventory = json.loads((DOCS / 'architecture/source-inventory.json').read_text())
    groups = defaultdict(list)
    for record in inventory['repositories']:
        repo = args.projects / record['repository']
        if git(repo, 'rev-parse', 'HEAD') != record['commit'] or git(repo, 'status', '--porcelain'):
            raise SystemExit(f'{repo}: source differs from pinned inventory; regenerate the inventory first')
        for module in record['modules']:
            if module.get('alias_of'):
                continue
            for manifest, data in module['manifests'].items():
                if data.get('name'):
                    groups[(manifest, data['name'])].append((record, module))
    comparisons = []
    for (manifest, identity), locations in sorted(groups.items()):
        if len(locations) < 2:
            continue
        observations = []
        for record, module in locations:
            repo = args.projects / record['repository']
            base = repo / 'modules' / module['directory']
            files = git(repo, 'ls-files', '--', f'modules/{module["directory"]}/').splitlines()
            runtime, tests = {}, {}
            for file in files:
                path = repo / file
                if not path.is_file():
                    continue
                relative = path.relative_to(base).as_posix()
                if relative == 'module.json' or relative.startswith(RUNTIME_ROOTS):
                    runtime[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
                elif relative.startswith('tests/'):
                    tests[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
            data = json.loads((base / manifest).read_text())
            metadata = {k: data[k] for k in ('name', 'type', 'require', 'conflict', 'replace', 'provide', 'autoload', 'extra', 'dependencies', 'peerDependencies', 'exports') if k in data}
            observations.append({
                'repository': record['repository'], 'project': record['project'],
                'commit': record['commit'], 'directory': module['directory'],
                'runtime_files': runtime, 'runtime_digest': digest_map(runtime),
                'test_digest': digest_map(tests), 'test_file_count': len(tests),
                'metadata_digest': digest_map(metadata),
            })
        runtime_variants = len({o['runtime_digest'] for o in observations})
        metadata_variants = len({o['metadata_digest'] for o in observations})
        all_files = set().union(*(o['runtime_files'] for o in observations))
        differences = sorted(p for p in all_files if len({o['runtime_files'].get(p) for o in observations}) > 1)
        comparisons.append({'manifest': manifest, 'identity': identity,
                            'runtime_variants': runtime_variants, 'metadata_variants': metadata_variants,
                            'differing_runtime_paths': differences, 'observations': observations})
    (DOCS / 'architecture/shared-module-comparison.json').write_text(json.dumps({'comparisons': comparisons}, indent=2) + '\n')
    same = sum(c['runtime_variants'] == 1 and c['metadata_variants'] == 1 for c in comparisons)
    lines = ['# Shared module source comparison', '',
             'This report compares repeated manifest identities in the [source inventory](SOURCE-INVENTORY.md). It measures tracked file equality at pinned commits; it does not execute code or establish behavioral compatibility.', '',
             f'Compared **{len(comparisons)} repeated identities**: **{same} have matching runtime files and selected runtime metadata**; **{len(comparisons)-same} differ in at least one of those dimensions**. Equal files still require consumer integration and migration checks before consolidation.', '',
             '## Method and reproduction', '',
             'Run `python3 tools/compare_shared_modules.py --projects /home/liberu/projects` after regenerating the source inventory. Dirty checkouts and changed HEADs are rejected.', '',
             'Runtime comparison includes `src/`, `database/`, `routes/`, `resources/`, `config/`, `lang/`, and `module.json`. Each relative filename and its SHA-256 content digest contribute to the group fingerprint. Selected Composer/npm runtime metadata is compared separately; tests have separate fingerprints. Documentation, release metadata, root build tools, and other files outside those roots are not part of the runtime equality claim. A version/default change in `module.json` counts as a difference.', '',
             'See [the machine-readable comparisons](shared-module-comparison.json) for all locations, digests, file counts, and differing paths. Read the [reuse and consolidation guide](SHARED-MODULES.md) before changing dependencies.', '',
             '## Identity summary', '', '| Package | Copies | Runtime variants | Metadata variants | Differing runtime paths |', '| --- | ---: | ---: | ---: | ---: |']
    for index, item in enumerate(comparisons):
        lines.append(f'| [{item["identity"]}](#package-{index+1}) | {len(item["observations"])} | {item["runtime_variants"]} | {item["metadata_variants"]} | {len(item["differing_runtime_paths"])} |')
    lines += ['', '## Source locations and review paths']
    for index, item in enumerate(comparisons):
        lines += ['', f'<a id="package-{index+1}"></a>', '', f'### {item["identity"]}', '',
                  '| Application | Module source | Runtime files | Test files |', '| --- | --- | ---: | ---: |']
        for o in item['observations']:
            url=f'https://github.com/liberusoftware/{o["repository"]}/tree/{o["commit"]}/modules/{o["directory"]}'
            lines.append(f'| [{o["project"]}](../projects/{o["project"]}/SOURCE-MODULES.md) | [{o["directory"]}]({url}) | {len(o["runtime_files"])} | {o["test_file_count"]} |')
        if item['differing_runtime_paths']:
            lines += ['', 'Review paths: ' + ', '.join(f'`{p}`' for p in item['differing_runtime_paths'][:12]) + (f' (plus {len(item["differing_runtime_paths"])-12} more in the JSON report).' if len(item['differing_runtime_paths'])>12 else '.')]
        else:
            lines += ['', 'The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.']
    (DOCS / 'architecture/SHARED-MODULE-COMPARISON.md').write_text('\n'.join(lines)+'\n')
    print(f'Compared {len(comparisons)} repeated identities: {same} matching runtime/metadata, {len(comparisons)-same} divergent.')


if __name__ == '__main__':
    main()
