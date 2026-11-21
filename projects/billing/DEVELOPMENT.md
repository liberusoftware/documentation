# Billing: work with a project clone

**Source snapshot:** `project-billing-laravel-filament` at `4743bdfebd1c122e10bf80171d0210ab27e34a54`. This guide reads the root manifests and setup paths; it does not claim a completed local installation or passing application tests. Start with the [project documentation](README.md) and [source mapping](SOURCE-MAPPING.md).

## Choose the source and environment

The requested clone is available at `/home/liberu/projects/project-billing-laravel-filament`. It is a shallow application checkout; deepen history when a migration or implementation review needs earlier commits. Read its README and contribution instructions before changing it.

| Requirement | Observed constraint or source |
| --- | --- |
| PHP | `^8.5` |
| Laravel | `^13.0` |
| Installer | `^1.1` |
| Node/npm engines | `{}` |
| npm application private flag | `true` |
| PHP dependency lock | [composer.lock](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/composer.lock) |
| npm dependency lock | [package-lock.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/package-lock.json) |

Use the actual package constraints and CI/build images to select runtime versions. A PHP constraint does not list every required extension; `composer check-platform-reqs` checks the resolved installation. A missing Node engine field is not proof of compatibility with every Node release.

Setup entry points: [README.md](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/README.md) · [CONTRIBUTING.md](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/CONTRIBUTING.md) · [AGENTS.md](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/AGENTS.md) · [docker-compose.yml](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/docker-compose.yml) · [.env.example](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/.env.example) · [config/database.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/config/database.php).

## First local setup

Work in the clone root. For a new local environment, create `.env` from the example only if it is absent, then configure application URL, database, cache, queues, mail and any required integration sandbox settings. Use the source setup guide for its service topology; a Compose file may have additional environment requirements.

```bash
cd /home/liberu/projects/project-billing-laravel-filament
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

These script definitions come from [composer.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/composer.json); they are reported without execution.

| Script | Declared command(s) |
| --- | --- |
| `post-autoload-dump` | `Illuminate\Foundation\ComposerScripts::postAutoloadDump`<br>`@php artisan package:discover --ansi`<br>`@php artisan filament:upgrade` |
| `post-update-cmd` | `@php artisan vendor:publish --tag=laravel-assets --ansi --force` |
| `post-root-package-install` | `@php -r "file_exists('.env') \|\| copy('.env.example', '.env');"` |
| `post-create-project-cmd` | `@php artisan key:generate --ansi` |
| `test` | `vendor/bin/pest` |

## JavaScript build scripts

These definitions come from [package.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/package.json). The root application can be private while separate presentation libraries are independently publishable.

| Script | Command |
| --- | --- |
| `build` | `vite build` |
| `dev` | `vite` |

## Select modules and presentation

Use the [source mapping](SOURCE-MAPPING.md) to find actual identities and the [package references](../../modules/source/README.md) to inspect dependencies, providers, migrations and callables. Package installation, manifest discovery, deployment enablement, database migration and user authorization are separate steps. Apply the host resolver configuration and the [Composer lifecycle guide](../../guides/COMPOSER.md).

Choose only the presentation surfaces the application needs. PHP-based API, Filament and Livewire packages may ship assets without an npm package. React/Inertia and Vue/Inertia use Laravel-owned navigation. Next.js and Nuxt have independent routing and session integration; share framework-independent UI and API contracts, then implement the transport boundary explicitly.

If a local module edit changes an installed tracked copy, make the durable change in its canonical package repository and update the application through the lockfile. Unextracted application-owned code is changed with the application. Source compatibility symlinks are alternate paths, not another package to publish.

## Application module layout

Source: [Billing Filament capability split](https://github.com/liberusoftware/project-billing-laravel-filament/commit/aa96378dab533806d1efe5c53227e8ee3a6ab303).

Billing Filament's project-specific code is split by capability. `billing-application`
holds Laravel composition and shared entry points. Capability-specific Filament
resources sit with their owners and the host's panel providers discover them.

| Directory under `modules/` | Specification | Application ownership |
| --- | --- | --- |
| `billing-application` | [Application](features/application.md) | Laravel composition, shared entry points and cross-capability integration tests |
| `billing-audit` | [Audit](features/audit.md) | Billing audit log and application adapters |
| `billing-catalog` | [Catalog](features/catalog.md) | Products, services and package groups |
| `billing-collections` | [Collections](features/collections.md) | Invoice reminders, late fees, disputes and suspension |
| `billing-communications` | [Communications](features/communications.md) | VoIP billing, call rates, email and SMS |
| `billing-customer-portal` | [Customer Portal](features/customer-portal.md) | Client records, portal services and storefront |
| `billing-domains` | [Domains](features/domains.md) | Availability, renewals, registrars and DNS |
| `billing-files` | [Files and Media](features/files-media.md) | Application files, folders and shares |
| `billing-filament` | Filament composition | Panel registration, discovery and shared UI |
| `billing-hosting` | [Hosting](features/hosting.md) | Hosting fulfillment and control-panel integration |
| `billing-identity` | [Identity and Teams](features/identity-core.md) | Billing users, teams, roles and account access |
| `billing-integrations` | [Integrations](features/integrations.md) | External connections, Git, webhooks and domain event transport |
| `billing-invoicing` | [Invoicing](features/invoicing.md) | Invoices, credits, recurring invoice generation and templates |
| `billing-isp` | [ISP](features/isp.md) | Access services, RADIUS and IP address management |
| `billing-licensing` | Licensing | License validation, release delivery and the licensing SDK |
| `billing-money` | [Billing Core](features/billing-core.md) | Application currency and tax workflows and Billing Core integration tests |
| `billing-orders` | [Orders](features/orders.md) | Orders, quotes and order forms |
| `billing-payments` | [Payments](features/payments.md) | Gateways, checkout, refunds and payment reconciliation |
| `billing-pricing` | [Pricing](features/pricing.md) | Price and discount calculation |
| `billing-projects` | Projects | Projects, tasks, time tracking and project billing |
| `billing-provisioning` | [Provisioning](features/provisioning.md) | Service provisioning and automation |
| `billing-referrals` | [Referrals](features/referrals.md) | Affiliate accounts, transactions and referral reporting |
| `billing-reporting` | [Reporting](features/reporting.md) | Reports, generation and export |
| `billing-search` | [Search](features/search.md) | Saved searches and project search integration |
| `billing-settings` | [Settings](features/settings.md) | Application site settings and administration |
| `billing-subscriptions` | [Subscriptions](features/subscriptions.md) | Subscription lifecycle and change processing |
| `billing-support` | Support | Tickets, knowledge base, canned replies and inbound email |
| `billing-usage` | [Usage](features/usage.md) | Usage records and import |

Each capability contains its source and, where applicable, its migrations,
factories, seeders, views, and tests. Composer preserves the existing `App\` and
`Database\` class identities. Existing migration filenames, routes and command
names carry forward. The application extension loader remains at `app/Modules/`.

The [module architecture specification](../../architecture/MODULES.md) defines a
module as an independently released Composer package with a manifest, declared
dependencies and a standalone suite. The `billing-*` areas above are host-owned
implementations and integration code that still use Billing application classes.
They follow the capability split. Published packages such as
`liberusoftware/module-billing-billing-core` keep their independent lifecycle and
public contracts. Licensing, projects, and ticket support are Billing Filament
capabilities with application-owned persistence and UI.

## Module management

The Composer package `liberusoftware/module-manager` loads the registered Billing
packages. Its `php artisan module:list` and `module:validate` commands inspect
that registry. The separate `php artisan module …` commands still use
`app/Modules/` to manage the existing extension format, including `BlogModule`.

## Verify the changed behavior

The root `phpunit.xml` declares the `Unit`, `Feature`, `Architecture`, and `Modules` suites. The first three use the host-owned tests under `modules/billing-*/tests`. The `Modules` suite exercises reusable package tests. Read the root bootstrap and environment configuration before running database tests.

```bash
vendor/bin/pest modules/billing-application/tests/Architecture
vendor/bin/pest modules/billing-money/tests/Feature/BillingCore
XDEBUG_MODE=coverage php -d memory_limit=1G vendor/bin/pest --coverage --min=100 --coverage-clover=coverage.xml
```

The coverage gate measures executable lines in `app/` and `modules/*/src`. Billing Core and its HTTP adapter can be measured in the focused host integration suite. The full release scope remains subject to the 100% gate.

The root declares a `test` script. Run `composer run test` in the configured test environment, plus the relevant module/consumer checks. Use targeted test selection supported by the declared runner when validating a focused change.

Select assertions for the actual change: successful domain actions, invalid input, wrong actor/tenant, stale state, duplicate/retried work, affected migrations and recovery. Rebuild the selected UI and exercise its loading, validation, denied and failure states. Record commands and results; the presence of a test file is not execution evidence.

## Update a working clone

Preserve local edits, fetch/review upstream changes, and integrate according to the project contribution process. After an accepted lockfile change, reinstall from the lockfile (`composer install`, `npm ci`) and run the affected checks. To change a dependency deliberately, use a targeted update, review the complete lockfile diff and migration notes, and verify the consumer before promotion.

Independent package checkouts need their own Git update and release; updating an application branch does not update every separately cloned module. Test a released artifact without local path/link overrides before relying on it. Use [Composer updates and Packagist publishing](../../guides/COMPOSER.md) and [npm local development and publishing](../../guides/NPM.md) for the full lifecycle.

## Operate the selected capability

For queued/provider work, identify the owning queue/job, retry policy, operation identity, correlation reference and recovery action before deployment. Configure only the workers/services the enabled modules require. Long-lived processes and configuration/module caches follow the host deployment procedure after updates.

Use role-scoped accounts and explicit tenant/entity context when verifying an administrative or customer workflow. Confirm authorized read/write/export behavior and reconcile downstream references where a change crosses Billing, Accounting, CRM, Commerce, Maintenance or infrastructure boundaries. Operations must use published owner contracts rather than editing another module's private tables.
