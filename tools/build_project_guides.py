#!/usr/bin/env python3
"""Build project checkout guides from pinned root manifests and tracked setup files."""
import argparse
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def main():
    records = json.loads((ROOT/'architecture/source-inventory.json').read_text())['repositories']
    for record in records:
        repo = args.projects/record['repository']
        commit = subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
        dirty = subprocess.check_output(['git','-C',str(repo),'status','--porcelain'],text=True).strip()
        if commit != record['commit'] or dirty:
            raise SystemExit(f'{repo}: differs from pinned clean inventory')
        composer = json.loads((repo/'composer.json').read_text())
        npm = json.loads((repo/'package.json').read_text()) if (repo/'package.json').exists() else {}
        base = f'https://github.com/liberusoftware/{record["repository"]}/blob/{commit}/'
        def source(path):
            return f'[{path}]({base}{path})'
        project = ROOT/'projects'/record['project']
        title = record['project'].replace('-',' ').title()
        lines = [f'# {title}: work with a project clone', '',
                 f'**Source snapshot:** `{record["repository"]}` at `{commit}`. This guide reads the root manifests and setup paths; it does not claim a completed local installation or passing application tests. Start with the [project documentation](README.md) and [source mapping](SOURCE-MAPPING.md).', '',
                 '## Choose the source and environment', '',
                 f'The requested clone is available at `/home/liberu/projects/{record["repository"]}`. It is a shallow application checkout; deepen history when a migration or implementation review needs earlier commits. Read its README and contribution instructions before changing it.', '',
                 '| Requirement | Observed constraint or source |', '| --- | --- |',
                 f'| PHP | `{cell(composer.get("require",{}).get("php","not declared"))}` |',
                 f'| Laravel | `{cell(composer.get("require",{}).get("laravel/framework","not declared"))}` |',
                 f'| Installer | `{cell(composer.get("require",{}).get("liberusoftware/composer-installer","not directly required"))}` |',
                 f'| Node/npm engines | `{cell(json.dumps(npm.get("engines",{}),sort_keys=True))}` |',
                 f'| npm application private flag | `{cell(json.dumps(npm.get("private","not declared")))}` |',
                 f'| PHP dependency lock | {source("composer.lock") if (repo/"composer.lock").exists() else "No committed root lockfile found"} |',
                 f'| npm dependency lock | {source("package-lock.json") if (repo/"package-lock.json").exists() else "No committed npm lockfile found"} |', '',
                 'Use the actual package constraints and CI/build images to select runtime versions. A PHP constraint does not list every required extension; `composer check-platform-reqs` checks the resolved installation. A missing Node engine field is not proof of compatibility with every Node release.', '',
                 'Setup entry points: ' + ' · '.join(source(p) for p in ('README.md','CONTRIBUTING.md','AGENTS.md','docs/INSTALLATION.md','docs/OPERATIONS.md','docker-compose.yml','.env.example','config/database.php') if (repo/p).is_file()) + '.', '',
                 '## First local setup', '',
                 'Work in the clone root. For a new local environment, create `.env` from the example only if it is absent, then configure application URL, database, cache, queues, mail and any required integration sandbox settings. Use the source setup guide for its service topology; a Compose file may have additional environment requirements.', '',
                 '```bash', f'cd /home/liberu/projects/{record["repository"]}', 'test -f .env || cp .env.example .env', 'composer install', 'composer check-platform-reqs', 'npm ci', 'npm run build', '```', '',
                 'These commands install the locked dependencies and compile assets. Composer may run the scripts listed below, including package discovery. If the host cannot boot during installation, inspect the first resolver/provider error and the lockfile/module version contract instead of suppressing platform or dependency checks.', '',
                 'For a newly created local environment whose application key is empty, generate its key with `php artisan key:generate`. Connect a local/disposable database before running `php artisan migrate`. Seed only the datasets explicitly documented by the source project. Existing deployment keys and databases follow their own upgrade/recovery procedure rather than the new-install sequence.', '',
                 'Inspect available Artisan commands with `php artisan list`. Start the application using its README or declared development script. `npm run dev` runs the asset development server; it is not, by itself, a Laravel application server or queue worker.', '',
                 '## Root Composer scripts', '',
                 f'These script definitions come from {source("composer.json")}; they are reported without execution.', '',
                 '| Script | Declared command(s) |', '| --- | --- |']
        for name, value in composer.get('scripts',{}).items():
            commands = value if isinstance(value,list) else [value]
            lines.append(f'| `{cell(name)}` | '+ '<br>'.join(f'`{cell(command)}`' for command in commands)+' |')
        lines += ['', '## JavaScript build scripts', '',
                  f'These definitions come from {source("package.json")}. The root application can be private while separate presentation libraries are independently publishable.', '',
                  '| Script | Command |', '| --- | --- |']
        for name,value in npm.get('scripts',{}).items():
            lines.append(f'| `{cell(name)}` | `{cell(value)}` |')
        lines += ['', '## Select modules and presentation', '',
                  'Use the [source mapping](SOURCE-MAPPING.md) to find actual identities and the [package references](../../modules/source/README.md) to inspect dependencies, providers, migrations and callables. Package installation, manifest discovery, deployment enablement, database migration and user authorization are separate steps. Apply the host resolver configuration and the [Composer lifecycle guide](../../guides/COMPOSER.md).', '',
                  'Choose only the presentation surfaces the application needs. PHP-based API, Filament and Livewire packages may ship assets without an npm package. React/Inertia and Vue/Inertia use Laravel-owned navigation. Next.js and Nuxt have independent routing and session integration; share framework-independent UI and API contracts, then implement the transport boundary explicitly.', '',
                  'If a local module edit changes an installed tracked copy, make the durable change in its canonical package repository and update the application through the lockfile. Unextracted application-owned code is changed with the application. Source compatibility symlinks are alternate paths, not another package to publish.', '',
                  '## Verify the changed behavior', '']
        if (repo/'phpunit.xml').exists():
            try:
                tree=ET.parse(repo/'phpunit.xml')
                suites=[s.attrib.get('name','unnamed') for s in tree.findall('.//testsuite')]
                lines += [f'The root {source("phpunit.xml")} declares test suites: '+', '.join(f'`{cell(s)}`' for s in suites)+'. Read its bootstrap and environment configuration before running database tests.', '']
            except ET.ParseError:
                lines += ['The root PHPUnit configuration could not be parsed by this guide generator; inspect it directly.', '']
        if 'test' in composer.get('scripts',{}):
            lines += ['The root declares a `test` script. Run `composer run test` in the configured test environment, plus the relevant module/consumer checks. Use targeted test selection supported by the declared runner when validating a focused change.', '']
        else:
            lines += ['The root does not declare a Composer `test` script. Use its documented PHPUnit/Artisan runner and test configuration instead of assuming `composer test` exists. Module-local scripts and host tests may use different bootstraps.', '']
        lines += ['Select assertions for the actual change: successful domain actions, invalid input, wrong actor/tenant, stale state, duplicate/retried work, affected migrations and recovery. Rebuild the selected UI and exercise its loading, validation, denied and failure states. Record commands and results; the presence of a test file is not execution evidence.', '',
                  '## Update a working clone', '',
                  'Preserve local edits, fetch/review upstream changes, and integrate according to the project contribution process. After an accepted lockfile change, reinstall from the lockfile (`composer install`, `npm ci`) and run the affected checks. To change a dependency deliberately, use a targeted update, review the complete lockfile diff and migration notes, and verify the consumer before promotion.', '',
                  'Independent package checkouts need their own Git update and release; updating an application branch does not update every separately cloned module. Test a released artifact without local path/link overrides before relying on it. Use [Composer updates and Packagist publishing](../../guides/COMPOSER.md) and [npm local development and publishing](../../guides/NPM.md) for the full lifecycle.', '',
                  '## Operate the selected capability', '',
                  'For queued/provider work, identify the owning queue/job, retry policy, operation identity, correlation reference and recovery action before deployment. Configure only the workers/services the enabled modules require. Long-lived processes and configuration/module caches follow the host deployment procedure after updates.', '',
                  'Use role-scoped accounts and explicit tenant/entity context when verifying an administrative or customer workflow. Confirm authorized read/write/export behavior and reconcile downstream references where a change crosses Billing, Accounting, CRM, Commerce, Maintenance or infrastructure boundaries. Operations must use published owner contracts rather than editing another module\'s private tables.', '']
        (project/'DEVELOPMENT.md').write_text('\n'.join(lines))
        readme=project/'README.md'
        if '(DEVELOPMENT.md)' not in readme.read_text():
            readme.write_text(readme.read_text()+'\n- [Project clone development guide](DEVELOPMENT.md) — requirements, actual scripts, setup, module selection, verification and updates.\n')
    print(f'Built source-backed development guides for {len(records)} application checkouts.')


if __name__=='__main__':
    main()
