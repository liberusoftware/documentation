#!/usr/bin/env python3
"""Build package references from pinned tracked source, without executing package code."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
ROLE_ROOTS = ('Contracts', 'Actions', 'Queries', 'Policies', 'Services', 'Support', 'Http/Controllers', 'Livewire', 'Filament')
METHOD = re.compile(r'(?:(public|protected|private)\s+)?(?:static\s+)?function\s+([A-Za-z_]\w*)\s*\([^{};]*?\)\s*(?::\s*[^{};]+)?(?=[{;])', re.S)


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()


def safe(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def slug(identity):
    return identity.replace('/', '--').replace('@', '')


def source_url(record, relative, line=None):
    url = f'https://github.com/liberusoftware/{record["repository"]}/blob/{record["commit"]}/{quote(relative, safe="/")}'
    return url + (f'#L{line}' if line else '')


def link(record, relative, label=None, line=None):
    return f'[{safe(label or relative)}]({source_url(record, relative, line)})'


def methods(content):
    # This is a source index, not a PHP parser or declaration of stable public API.
    content = re.sub(r'/\*.*?\*/|//[^\n]*', lambda m: ' ' * len(m.group()), content, flags=re.S)
    result = []
    for match in METHOD.finditer(content):
        if match.group(1) in ('private', 'protected'):
            continue
        signature = re.sub(r'\s+', ' ', match.group()).strip()
        if len(signature) > 360:
            signature = signature[:357] + '...'
        result.append((signature, content[:match.start()].count('\n') + 1))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects', type=Path, default=Path('/home/liberu/projects'))
    args = parser.parse_args()
    inventory = json.loads((ROOT / 'architecture/source-inventory.json').read_text())
    groups = defaultdict(list)
    nonpackages = []
    for record in inventory['repositories']:
        repo = args.projects / record['repository']
        if git(repo, 'rev-parse', 'HEAD') != record['commit'] or git(repo, 'status', '--porcelain'):
            raise SystemExit(f'{repo}: source differs from clean inventory')
        tracked = git(repo, 'ls-files').splitlines()
        for module in record['modules']:
            if module.get('alias_of'):
                continue
            prefix = f'modules/{module["directory"]}/'
            files = {p.removeprefix(prefix): repo / p for p in tracked if p.startswith(prefix) and (repo / p).is_file()}
            manifests = module['manifests']
            identity = manifests.get('composer.json', {}).get('name') or manifests.get('package.json', {}).get('name')
            if not identity:
                nonpackages.append({'project': record['project'], 'repository': record['repository'], 'commit': record['commit'], 'directory': module['directory'], 'files': list(files)})
                continue
            full_manifests = {name: json.loads(path.read_text()) for name, path in files.items() if name in ('composer.json', 'package.json', 'module.json')}
            evidence = {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in files.items()
                        if name in full_manifests or name.startswith(('src/', 'database/', 'config/', 'routes/', 'resources/', 'tests/', 'lang/', 'openapi/'))}
            fingerprint = hashlib.sha256(json.dumps(evidence, sort_keys=True).encode()).hexdigest()
            groups[identity].append({'record': record, 'module': module, 'files': files, 'manifests': full_manifests, 'fingerprint': fingerprint})
    outdir = ROOT / 'modules/source'
    outdir.mkdir(exist_ok=True)
    package_index = {}
    for identity, locations in sorted(groups.items()):
        variants = defaultdict(list)
        for location in locations:
            variants[location['fingerprint']].append(location)
        php = locations[0]['manifests'].get('composer.json', {})
        lines = [f'# {identity}: observed package reference', '',
                 '**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.', '',
                 str(php.get('description', 'No Composer description declared.')), '',
                 '## Source locations', '', '| Application | Actual directory | Commit | Reference variant | Test files |', '| --- | --- | --- | --- | ---: |']
        variant_numbers = {fingerprint: i + 1 for i, fingerprint in enumerate(sorted(variants))}
        for location in locations:
            record, module = location['record'], location['module']
            n = variant_numbers[location['fingerprint']]
            tests = [p for p in location['files'] if p.startswith('tests/')]
            source = link(record, f'modules/{module["directory"]}/composer.json', module['directory'])
            lines.append(f'| [{record["project"]}](../../projects/{record["project"]}/SOURCE-MODULES.md) | {source} | `{record["commit"][:12]}` | [Variant {n}](#variant-{n}) | {len(tests)} |')
        lines += ['', f'Physical source locations: **{len(locations)}**. Reference variants: **{len(variants)}**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).', '',
                  'Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).']
        for fingerprint in sorted(variants):
            location = variants[fingerprint][0]
            record, module, files, manifests = (location[k] for k in ('record', 'module', 'files', 'manifests'))
            prefix = f'modules/{module["directory"]}/'
            n = variant_numbers[fingerprint]
            composer, manifest = manifests.get('composer.json', {}), manifests.get('module.json', {})
            lines += ['', f'## Variant {n}', '', f'Representative: {record["repository"]}, `{module["directory"]}`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.', '',
                      '### Manifest and registration', '', '| Property | Observed value |', '| --- | --- |',
                      f'| Composer name | `{safe(composer.get("name", "not declared"))}` |',
                      f'| Composer version field | `{safe(composer.get("version", "not declared; may be VCS-derived"))}` |',
                      f'| Package type | `{safe(composer.get("type", "not declared"))}` |',
                      f'| Module manifest name | `{safe(manifest.get("name", "not declared"))}` |',
                      f'| Module version field | `{safe(manifest.get("version", "not declared"))}` |',
                      f'| Category / layers | `{safe(json.dumps(manifest.get("category", manifest.get("layers", "not declared"))))}` |',
                      f'| Manifest provider(s) | `{safe(json.dumps(manifest.get("provider", manifest.get("service_providers", "not declared"))))}` |',
                      f'| Composer Laravel provider registration | `{safe(json.dumps(composer.get("extra", {}).get("laravel", {}).get("providers", [])))}` |',
                      f'| default_enabled field | `{safe(json.dumps(manifest.get("default_enabled", "not declared")))}` |', '',
                      'The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.', '',
                      'Source metadata: ' + ' · '.join(link(record, prefix + name, name) for name in ('composer.json', 'module.json', 'package.json') if name in files) + '.', '']
            for key in ('capabilities', 'features'):
                values = manifest.get(key, [])
                if values:
                    lines += [f'**Declared {key}:** ' + safe(', '.join(map(str, values)) if isinstance(values, list) else json.dumps(values)), '']
            lines += ['### Dependencies and namespace mapping', '', '| Dependency | Constraint |', '| --- | --- |']
            for name, constraint in sorted(composer.get('require', {}).items()):
                lines.append(f'| `{safe(name)}` | `{safe(constraint)}` |')
            if not composer.get('require'):
                lines.append('| — | No Composer runtime requirements declared |')
            lines += ['', 'PSR-4 mappings: `' + safe(json.dumps(composer.get('autoload', {}).get('psr-4', {}), sort_keys=True)) + '`.', '']
            if manifest.get('requires'):
                lines += ['Module resolver requirements: `' + safe(json.dumps(manifest['requires'], sort_keys=True)) + '`.', '']
            # Callable indexes describe source evidence, not a promise that every class is a public extension point.
            lines += ['### Source entry points', '',
                      'The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.', '']
            entries = []
            for name, path in sorted(files.items()):
                if not name.endswith('.php') or not any(name.startswith(f'src/{role}/') for role in ROLE_ROOTS):
                    continue
                signatures = methods(path.read_text())
                entries.append((name, signatures))
            if entries:
                lines += ['| Source file | Public method signatures observed |', '| --- | --- |']
                for name, signatures in entries:
                    values = '<br>'.join(f'`{safe(signature)}`' for signature, _ in signatures) or 'No named public method detected by the static index.'
                    lines.append(f'| {link(record, prefix + name, name)} | {values} |')
            else:
                lines += ['No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.']
            other = [name for name in files if name.startswith('src/') and name.endswith('.php') and '/Legacy/' not in name and not any(name.startswith(f'src/{role}/') for role in ROLE_ROOTS)]
            lines += ['', 'Other non-legacy PHP sources: ' + (' · '.join(link(record, prefix + name, name) for name in sorted(other)) or 'none observed') + '.', '']
            legacy = [name for name in files if name.startswith('src/Legacy/')]
            if legacy:
                lines += [f'**Legacy review:** {len(legacy)} files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.', '']
            routes = [name for name in files if name.startswith(('routes/', 'openapi/'))]
            if routes:
                lines += ['### HTTP and schema sources', '',
                          'Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.', '',
                          *[f'- {link(record, prefix + name, name)}' for name in sorted(routes)], '']
            schema = [name for name in files if name.startswith(('database/migrations/', 'database/settings/'))]
            lines += ['### Persistence and lifecycle evidence', '']
            if schema:
                lines += ['Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.', '',
                          *[f'- {link(record, prefix + name, name)}' for name in sorted(schema)], '']
            else:
                lines += ['No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.', '']
            enums = [(name, re.findall(r'\bcase\s+(\w+)\s*(?:=\s*([^;]+))?;', path.read_text())) for name, path in files.items() if name.startswith('src/Enums/') and name.endswith('.php')]
            for name, cases in sorted(enums):
                if cases:
                    lines += [link(record, prefix + name, name) + ': ' + ', '.join(f'`{safe(key)}' + (f' = {safe(value)}' if value else '') + '`' for key, value in cases) + '.', '']
            lines += ['### Verification and consumer use', '']
            scripts = composer.get('scripts', {})
            lines += ['Declared Composer scripts: `' + safe(json.dumps(scripts, sort_keys=True)) + '`.', '']
            tests = [name for name in files if name.startswith('tests/')]
            if tests:
                lines += [f'Tracked files under `tests/`: **{len(tests)}**. Presence and counts do not establish assertions, coverage or a passing run.', '',
                          *[f'- {link(record, prefix + name, name)}' for name in sorted(tests)], '']
            else:
                lines += ['No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.', '']
            lines += ['Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.', '']
        (outdir / f'{slug(identity)}.md').write_text('\n'.join(lines).rstrip()+'\n')
        package_index[identity] = {'reference': f'modules/source/{slug(identity)}.md', 'locations': [
            {'project': l['record']['project'], 'repository': l['record']['repository'], 'directory': l['module']['directory'], 'commit': l['record']['commit']} for l in locations], 'variants': len(variants)}
    (ROOT / 'architecture/source-reference-index.json').write_text(json.dumps({'packages': package_index, 'nonpackage_directories': nonpackages}, indent=2)+'\n')
    lines = ['# Observed package implementation references', '',
             f'This catalogue contains **{len(groups)} manifest identities** across **{sum(len(v) for v in groups.values())} physical package locations**. It records metadata, source signatures, migrations, route/schema sources and verification entry points. Repeated identities share one reference with source variants instead of separate claimed owners per application.', '',
             '## How to use the references', '',
             'Start with a project\'s source mapping or the package identity below. Read the pinned source for actual behavior and the project feature documents for target requirements. Static extraction is not a substitute for reviewing business invariants or running tests. Packages without tracked tests and differing registration mechanisms are called out directly.', '',
             'Reproduce with `python3 tools/build_source_reference.py --projects /home/liberu/projects` after refreshing the clean inventory. The tool reads tracked files only, skips compatibility aliases, and never executes package code. The method-signature index is lexical rather than a complete PHP parser; import resolution, dynamic calls and final routes require code review.', '',
             'See the [inventory](../../architecture/SOURCE-INVENTORY.md), [shared source comparison](../../architecture/SHARED-MODULE-COMPARISON.md), [Composer guide](../../guides/COMPOSER.md), and [machine-readable reference index](../../architecture/source-reference-index.json).', '',
             '| Identity | Physical locations | Reference variants |', '| --- | ---: | ---: |']
    for identity, info in sorted(package_index.items()):
        lines.append(f'| [{identity}]({slug(identity)}.md) | {len(info["locations"])} | {info["variants"]} |')
    lines += ['', '## Non-package directories under modules/', '',
              'These physical directories have no direct Composer/npm manifest. They may contain documentation, tests, metadata or other implementation material; they are preserved in inventory rather than treated as independently installable packages.', '',
              '| Project | Directory | Tracked files |', '| --- | --- | ---: |']
    for item in nonpackages:
        lines.append(f'| {item["project"]} | `{item["directory"]}` | {len(item["files"])} |')
    (outdir / 'README.md').write_text('\n'.join(lines)+'\n')
    print(f'Built {len(groups)} package references for {sum(len(v) for v in groups.values())} physical locations; preserved {len(nonpackages)} non-package directories separately.')


if __name__ == '__main__':
    main()
