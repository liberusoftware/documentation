#!/usr/bin/env python3
"""Record local module manifests without treating source presence as a release claim."""
import argparse
import collections
import json
from pathlib import Path
import subprocess

DOCS = Path(__file__).resolve().parents[1]


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects', type=Path, default=Path('/home/liberu/projects'))
    args = parser.parse_args()
    repositories = json.loads((args.projects / 'repositories.json').read_text())
    records = []
    identities = collections.defaultdict(list)
    for repository in sorted(repositories, key=lambda r: r['name']):
        repo = args.projects / repository['name']
        commit = git(repo, 'rev-parse', 'HEAD')
        if git(repo, 'status', '--porcelain'):
            raise SystemExit(f'{repo}: dirty checkout; commit links would not describe the source')
        project = repository['name'].removesuffix('-laravel')
        project = {'accounting-erp': 'accounting', 'enterprise-sap': 'sap'}.get(project, project)
        modules = []
        directory = repo / 'modules'
        for module in sorted(directory.iterdir() if directory.exists() else []):
            if not module.is_dir():
                continue
            resolved = module.resolve()
            if not resolved.is_relative_to(repo.resolve()):
                raise SystemExit(f'{module}: module alias escapes its repository')
            alias_of = str(resolved.relative_to(directory.resolve())) if module.is_symlink() else None
            manifests = {}
            for filename in ('composer.json', 'package.json'):
                path = module / filename
                if path.is_file():
                    data = json.loads(path.read_text())
                    manifests[filename] = {k: data[k] for k in ('name', 'description', 'version', 'require', 'dependencies', 'peerDependencies', 'scripts') if k in data}
                    if data.get('name') and not alias_of:
                        identities[(filename, data['name'])].append((repository['name'], module.name))
            modules.append({'directory': module.name, 'alias_of': alias_of, 'manifests': manifests})
        tracked = git(repo, 'ls-files').splitlines()
        application_sources = {
            prefix: [p for p in tracked if p.startswith(prefix + '/')]
            for prefix in ('app', 'routes', 'resources', 'database', 'tests', 'packages')
        }
        other_manifests = [p for p in tracked
                           if Path(p).name in ('composer.json', 'package.json', 'module.json')
                           and not p.startswith('modules/')]
        record = {'repository': repository['name'], 'commit': commit, 'project': project,
                  'modules': modules, 'application_sources': application_sources,
                  'other_manifest_paths': other_manifests}
        records.append(record)
        output = DOCS / 'projects' / project / 'SOURCE-MODULES.md'
        output.parent.mkdir(parents=True, exist_ok=True)
        lines = [f'# {project.replace("-", " ").title()}: observed source modules', '',
                 f'Observed repository: [{repository["name"]}](https://github.com/liberusoftware/{repository["name"]}/tree/{commit}).', '',
                 'This is a manifest inventory, not a claim that a module is complete, tested, independently released, or available from a registry. Planned feature specifications may use different names. Use the exact manifest identity for dependency resolution.', '',
                 f'Found **{len(modules)} immediate directories under `modules/`**. This count does not measure capabilities implemented elsewhere in the application. Existing documented modules are preserved independently of their current source location. See [inventory method and shared identities](../../architecture/SOURCE-INVENTORY.md).', '',
                 f'Of these, **{sum(bool(m["alias_of"]) for m in modules)} are symlink aliases**, not additional package implementations. Their target directories are recorded below and are counted once in shared-package comparisons.', '',
                 '## Other source locations', '',
                 'Application-owned implementation can precede package extraction. These tracked locations must also be reviewed before making availability or ownership claims.', '',
                 '| Source root | Tracked files |', '| --- | ---: |',
                 *[f'| [{prefix}/](https://github.com/liberusoftware/{repository["name"]}/tree/{commit}/{prefix}) | {len(files)} |'
                   for prefix, files in application_sources.items() if files], '',
                 'Other manifest paths: ' + ', '.join(f'`{p}`' for p in other_manifests) + '.', '',
                 *(['Ecommerce capabilities also live in `app/`, routes, views, and application services. Read the [application capability map](SOURCE-APPLICATION.md); absence from this package table never authorizes removing a documented module.', ''] if project == 'ecommerce' else []),
                 '## Immediate module manifests', '',
                 '| Module directory | Composer identity | npm identity | Alias target | Description |',
                 '| --- | --- | --- | --- | --- |']
        for module in modules:
            manifests = module['manifests']
            php, js = manifests.get('composer.json', {}), manifests.get('package.json', {})
            description = str(php.get('description', js.get('description', 'No manifest description'))).replace('|', '\\|').replace('\n', ' ')
            source = f'https://github.com/liberusoftware/{repository["name"]}/tree/{commit}/modules/{module["directory"]}'
            lines.append(f'| [{module["directory"]}]({source}) | {php.get("name", "—")} | {js.get("name", "—")} | {module["alias_of"] or "—"} | {description} |')
        output.write_text('\n'.join(lines) + '\n')
    target = DOCS / 'architecture' / 'source-inventory.json'
    target.write_text(json.dumps({'repositories': records}, indent=2) + '\n')
    lines = ['# Source module inventory', '',
             'These records come from public `liberusoftware` repositories ending in `-laravel`, discovered through the paginated GitHub organization repositories API on 2026-10-25 and cloned into `/home/liberu/projects`. Commit-pinned links identify the scanned source. Source presence does not establish stability or registry availability.', '',
             '## Reproduce the scan', '',
             'Keep `repositories.json` in the projects directory as the discovery input. Refresh that list from every page of `https://api.github.com/orgs/liberusoftware/repos?per_page=100`, selecting names ending in `-laravel`. Clone missing repositories, then run:', '',
             '```bash', 'python3 tools/sync_source_inventory.py --projects /home/liberu/projects', '```', '',
             'The scanner rejects dirty checkouts, records each HEAD, inspects immediate children of `modules/`, and reads their `composer.json` and `package.json`. It also records tracked files under application source roots and manifest paths outside `modules/`. It does not install or execute package code. Directories without either manifest remain visible. Dependencies, scripts, and source path lists are preserved in [the machine-readable snapshot](source-inventory.json). Semantic capability mapping still requires reading the code: a directory count cannot establish whether a capability exists.', '',
             'Compatibility symlinks are recorded as aliases of their repository-local target. They remain visible in project tables, but shared-identity and source comparisons count the actual target once. Non-package directories are not installable packages merely because they occur under `modules/`.', '',
             '**Ecommerce preservation rule:** its documented module catalogue remains intact. Its implementations also live under `app/`, routes, and resources; see the [Ecommerce application capability map](../projects/ecommerce/SOURCE-APPLICATION.md). Do not remove or downgrade a documented module because it is absent from the immediate `modules/` scan.', '',
             '## Project coverage', '', '| Repository | Commit | Immediate module directories | Inventory |', '| --- | --- | ---: | --- |']
    for record in records:
        lines.append(f'| {record["repository"]} | `{record["commit"]}` | {len(record["modules"])} | [{record["project"]}](../projects/{record["project"]}/SOURCE-MODULES.md) |')
    lines += ['', '## Repeated package identities', '',
              'The same identity in multiple applications is a candidate for one shared owner and release stream. Compare source, migrations, dependencies, tests, and compatibility before consolidating. Matching names alone do not prove identical behavior. Applications should consume shared packages rather than publish divergent copies under the same identity.', '',
              '| Manifest | Package | Source applications |', '| --- | --- | --- |']
    for (manifest, identity), locations in sorted(identities.items()):
        if len(locations) > 1:
            lines.append(f'| {manifest} | `{identity}` | ' + ', '.join(repo for repo, _ in locations) + ' |')
    (DOCS / 'architecture' / 'SOURCE-INVENTORY.md').write_text('\n'.join(lines) + '\n')
    print(f'Recorded {len(records)} repositories, {sum(len(r["modules"]) for r in records)} module directories, and {sum(len(v)>1 for v in identities.values())} repeated package identities.')


if __name__ == '__main__':
    main()
