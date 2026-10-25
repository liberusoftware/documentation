# Control Panel: work with a project clone

**Source snapshot:** `control-panel-laravel` at `1797f25d705f780bacddcdf228c9a1dc995c3580`. This guide reads the root manifests and setup paths; it does not claim a completed local installation or passing application tests. Start with the [project documentation](README.md) and [source mapping](SOURCE-MAPPING.md).

## Choose the source and environment

The requested clone is available at `/home/liberu/projects/control-panel-laravel`. It is a shallow application checkout; deepen history when a migration or implementation review needs earlier commits. Read its README and contribution instructions before changing it.

| Requirement | Observed constraint or source |
| --- | --- |
| PHP | `^8.5` |
| Laravel | `^13.0` |
| Installer | `^1.1` |
| Node/npm engines | `{}` |
| npm application private flag | `true` |
| PHP dependency lock | [composer.lock](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/composer.lock) |
| npm dependency lock | [package-lock.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/package-lock.json) |

Use the actual package constraints and CI/build images to select runtime versions. A PHP constraint does not list every required extension; `composer check-platform-reqs` checks the resolved installation. A missing Node engine field is not proof of compatibility with every Node release.

Setup entry points: [README.md](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/README.md) · [CONTRIBUTING.md](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/CONTRIBUTING.md) · [AGENTS.md](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/AGENTS.md) · [docker-compose.yml](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/docker-compose.yml) · [.env.example](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/.env.example) · [config/database.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/config/database.php).

## First local setup

Work in the clone root. For a new local environment, create `.env` from the example only if it is absent, then configure application URL, database, cache, queues, mail and any required integration sandbox settings. Use the source setup guide for its service topology; a Compose file may have additional environment requirements.

```bash
cd /home/liberu/projects/control-panel-laravel
test -f .env || cp .env.example .env
composer install
composer check-platform-reqs
npm ci
npm run build
```

These commands install the locked dependencies and compile assets. Composer may run the scripts listed below, including package discovery. If the host cannot boot during installation, inspect the first resolver/provider error and the lockfile/module version contract instead of suppressing platform or dependency checks.

For a newly created local environment whose application key is empty, generate its key with `php artisan key:generate`. Connect a local/disposable database before running `php artisan migrate`. Seed only the datasets explicitly documented by the source project. Existing deployment keys and databases follow their own upgrade/recovery procedure rather than the new-install sequence.

Inspect available Artisan commands with `php artisan list`. Start the application using its README or declared development script. `npm run dev` runs the asset development server; it is not, by itself, a Laravel application server or queue worker.

## Root Composer scripts

These script definitions come from [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/composer.json); they are reported without execution.

| Script | Declared command(s) |
| --- | --- |
| `post-autoload-dump` | `Illuminate\Foundation\ComposerScripts::postAutoloadDump`<br>`@php artisan package:discover --ansi`<br>`@php artisan filament:upgrade` |
| `post-update-cmd` | `@php artisan vendor:publish --tag=laravel-assets --ansi --force` |
| `post-root-package-install` | `@php -r "file_exists('.env') \|\| copy('.env.example', '.env');"` |
| `post-create-project-cmd` | `@php artisan key:generate --ansi` |
| `test` | `vendor/bin/pest` |

## JavaScript build scripts

These definitions come from [package.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/package.json). The root application can be private while separate presentation libraries are independently publishable.

| Script | Command |
| --- | --- |
| `build` | `vite build` |
| `dev` | `vite` |

## Select modules and presentation

Use the [source mapping](SOURCE-MAPPING.md) to find actual identities and the [package references](../../modules/source/README.md) to inspect dependencies, providers, migrations and callables. Package installation, manifest discovery, deployment enablement, database migration and user authorization are separate steps. Apply the host resolver configuration and the [Composer lifecycle guide](../../guides/COMPOSER.md).

Choose only the presentation surfaces the application needs. PHP-based API, Filament and Livewire packages may ship assets without an npm package. React/Inertia and Vue/Inertia use Laravel-owned navigation. Next.js and Nuxt have independent routing and session integration; share framework-independent UI and API contracts, then implement the transport boundary explicitly.

If a local module edit changes an installed tracked copy, make the durable change in its canonical package repository and update the application through the lockfile. Unextracted application-owned code is changed with the application. Source compatibility symlinks are alternate paths, not another package to publish.

## Verify the changed behavior

The root [phpunit.xml](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/phpunit.xml) declares test suites: `Unit`, `Feature`, `Architecture`. Read its bootstrap and environment configuration before running database tests.

The root declares a `test` script. Run `composer run test` in the configured test environment, plus the relevant module/consumer checks. Use targeted test selection supported by the declared runner when validating a focused change.

Select assertions for the actual change: successful domain actions, invalid input, wrong actor/tenant, stale state, duplicate/retried work, affected migrations and recovery. Rebuild the selected UI and exercise its loading, validation, denied and failure states. Record commands and results; the presence of a test file is not execution evidence.

## Update a working clone

Preserve local edits, fetch/review upstream changes, and integrate according to the project contribution process. After an accepted lockfile change, reinstall from the lockfile (`composer install`, `npm ci`) and run the affected checks. To change a dependency deliberately, use a targeted update, review the complete lockfile diff and migration notes, and verify the consumer before promotion.

Independent package checkouts need their own Git update and release; updating an application branch does not update every separately cloned module. Test a released artifact without local path/link overrides before relying on it. Use [Composer updates and Packagist publishing](../../guides/COMPOSER.md) and [npm local development and publishing](../../guides/NPM.md) for the full lifecycle.

## Operate the selected capability

For queued/provider work, identify the owning queue/job, retry policy, operation identity, correlation reference and recovery action before deployment. Configure only the workers/services the enabled modules require. Long-lived processes and configuration/module caches follow the host deployment procedure after updates.

Use role-scoped accounts and explicit tenant/entity context when verifying an administrative or customer workflow. Confirm authorized read/write/export behavior and reconcile downstream references where a change crosses Billing, Accounting, CRM, Commerce, Maintenance or infrastructure boundaries. Operations must use published owner contracts rather than editing another module's private tables.
