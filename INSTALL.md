# Installation and project selection

This guide helps you choose a Liberu project, download it from GitHub, install dependencies, and select the modules and interface technology you need.

For the documentation tour, see [GETTING-STARTED.md](GETTING-STARTED.md). For the complete solution catalogue, see [TECHNOLOGIES.md](TECHNOLOGIES.md).

## 1. Choose a project

Liberu application repositories are published under the [liberusoftware](https://github.com/liberusoftware) GitHub organization. Each repository README and lock file is authoritative for exact requirements.

| Project | GitHub repository | Scope and module indexes |
|---|---|---|
| Boilerplate | [boilerplate-laravel](https://github.com/liberusoftware/boilerplate-laravel) | [Foundation](projects/boilerplate/BOILERPLATE.md) |
| Accounting | [accounting-erp-laravel](https://github.com/liberusoftware/accounting-erp-laravel) | [Scope](projects/accounting/ACCOUNTING.md) · [Features](projects/accounting/features/README.md) · [API](projects/accounting/api/README.md) |
| Automation | [automation-laravel](https://github.com/liberusoftware/automation-laravel) | [Scope](projects/automation/AUTOMATION.md) · [Features](projects/automation/features/README.md) · [API](projects/automation/api/README.md) |
| Billing | [billing-laravel](https://github.com/liberusoftware/billing-laravel) | [Scope](projects/billing/BILLING.md) · [Features](projects/billing/features/README.md) · [API](projects/billing/api/README.md) |
| Browser Game | [browser-game-laravel](https://github.com/liberusoftware/browser-game-laravel) | [Scope](projects/browser-game/BROWSER-GAME.md) · [Features](projects/browser-game/features/README.md) · [API](projects/browser-game/api/README.md) |
| CMS | [cms-laravel](https://github.com/liberusoftware/cms-laravel) | [Scope](projects/cms/CMS.md) · [Features](projects/cms/features/README.md) · [API](projects/cms/api/README.md) |
| Control Panel | [control-panel-laravel](https://github.com/liberusoftware/control-panel-laravel) | [Scope](projects/control-panel/CONTROL-PANEL.md) · [Features](projects/control-panel/features/README.md) · [API](projects/control-panel/api/README.md) |
| CRM | [crm-laravel](https://github.com/liberusoftware/crm-laravel) | [Scope](projects/crm/CRM.md) · [Features](projects/crm/features/README.md) · [API](projects/crm/api/README.md) |
| Ecommerce | [ecommerce-laravel](https://github.com/liberusoftware/ecommerce-laravel) | [Scope](projects/ecommerce/ECOMMERCE.md) · [Features](projects/ecommerce/features/README.md) · [API](projects/ecommerce/api/README.md) |
| Genealogy | [genealogy-laravel](https://github.com/liberusoftware/genealogy-laravel) | [Scope](projects/genealogy/GENEALOGY.md) · [Features](projects/genealogy/features/README.md) · [API](projects/genealogy/api/README.md) |
| Maintenance | [maintenance-laravel](https://github.com/liberusoftware/maintenance-laravel) | [Scope](projects/maintenance/MAINTENANCE.md) · [Features](projects/maintenance/features/README.md) · [API](projects/maintenance/api/README.md) |
| Real Estate | [real-estate-laravel](https://github.com/liberusoftware/real-estate-laravel) | [Scope](projects/real-estate/REAL-ESTATE.md) · [Features](projects/real-estate/features/README.md) · [API](projects/real-estate/api/README.md) |
| Social Network | [social-network-laravel](https://github.com/liberusoftware/social-network-laravel) | [Scope](projects/social-network/SOCIAL-NETWORK.md) · [Features](projects/social-network/features/README.md) · [API](projects/social-network/api/README.md) |

The organization’s [repositories page](https://github.com/orgs/liberusoftware/repositories) is the current catalogue. SAP-style Enterprise Suite and Liberu cross-product modules are currently documentation/planning scopes without a separately listed application repository.

## 2. Choose modules and interfaces

Start with the framework-neutral feature specification, then add only the matching adapters required by the application.

| Need | Index | Standard |
|---|---|---|
| Domain capabilities | [Feature specifications](features/README.md) | [Modules architecture](architecture/MODULES.md) |
| HTTP/API contracts | [API implementations](modules/api/README.md) | [API architecture](architecture/API.md) |
| Administration | [Filament implementations](modules/filament/README.md) | [Filament](standards/FILAMENT.md) |
| Server-driven UI | [Livewire implementations](modules/livewire/README.md) | [Livewire](standards/LIVEWIRE.md) |
| React application UI | [React + Inertia implementations](modules/react/README.md) | [React](standards/REACT.md) · [Inertia](standards/INERTIA.md) |
| Vue application UI | [Vue + Inertia implementations](modules/vue/README.md) | [Vue](standards/VUE.md) · [Inertia](standards/INERTIA.md) |
| Vue SSR/API application | [Nuxt implementations](modules/nuxt/README.md) | [Nuxt](standards/NUXT.md) |

The same module may have API, Filament, Livewire, React, Vue, and Nuxt adapters. Each adapter presents only its matching module and never duplicates its domain rules or private data.

## 3. Prerequisites

Confirm the selected project README and CI matrix before installing. The current Liberu baseline is:

- PHP 8.5 and Composer 2
- Laravel 13
- Node.js 22+ and the project’s locked package manager
- Filament 5 and Livewire 4 where selected
- React 19.2 + Inertia 3, Vue 3 + Inertia 3, or Nuxt 4 where selected
- A supported database, cache/queue backend, mail transport, and filesystem

Read [PHP](standards/PHP.md), [Laravel](standards/LARAVEL.md), [Database](standards/DATABASE.md), and [technology references](technologies/README.md) for detail.

## 4. Download and install

Replace REPOSITORY_URL with one of the GitHub repositories above:

~~~bash
git clone REPOSITORY_URL application
cd application
cp .env.example .env
composer install
php artisan key:generate
~~~

Configure database, cache, queue, mail, OAuth, storage, and application URL values in the .env file. Never commit credentials, tokens, or production data.

Run the project’s documented database setup:

~~~bash
php artisan migrate
php artisan db:seed
~~~

Only run seeders documented by the selected project in a shared or production environment. Review [Database](standards/DATABASE.md) for migrations, seeders, factories, backfills, rollback, and restore rules.

Build frontend assets when required:

~~~bash
npm install
npm run build
~~~

Run the project’s verification commands:

~~~bash
php artisan test
~~~

Follow the project README for workers, Horizon, Reverb, scheduled tasks, storage links, local services, and environment-specific commands.

## 5. Select the frontend technology

Choose one primary application UI approach for a given surface:

- **Filament:** administrative panels and operational dashboards; read [standards/FILAMENT.md](standards/FILAMENT.md).
- **Livewire:** server-driven interaction with minimal client application code; read [standards/LIVEWIRE.md](standards/LIVEWIRE.md).
- **React + Inertia:** React components with Laravel-owned routing, authorization, and page props; read [standards/REACT.md](standards/REACT.md) and [standards/INERTIA.md](standards/INERTIA.md).
- **Vue + Inertia:** Vue SFCs with Laravel-owned routing, authorization, and page props; read [standards/VUE.md](standards/VUE.md) and [standards/INERTIA.md](standards/INERTIA.md).
- **Nuxt:** independently SSR-rendered/API-consuming Vue applications with file-based routing and deliberate server/BFF boundaries; read [standards/NUXT.md](standards/NUXT.md).

Themes are technology-neutral and selected separately. Read [standards/THEMES.md](standards/THEMES.md) before adding assets, tokens, layouts, or presentation overrides.

## 6. Verify and recover safely

Before production, verify migrations, seed data, queues, mail, storage, OAuth callbacks, health checks, authorization, team/tenant isolation, frontend builds, and backups. Use [Testing](standards/TESTING.md), [deployment](deployment/README.md), and [security policy](architecture/SECURITY.md).

If installation fails, preserve the error and version information, correct the dependency or configuration issue, and rerun from a clean working tree. Remove only failed disposable application state; never delete shared or production data as a troubleshooting shortcut.

## Related indexes

- [Getting started](GETTING-STARTED.md)
- [Technology and solution map](TECHNOLOGIES.md)
- [Architecture index](architecture/README.md)
- [Standards index](standards/README.md)
- [Technology references](technologies/README.md)
- [Deployment index](deployment/README.md)
- [Contributing](standards/CONTRIBUTING.md)
