# Liberu documentation

This repository is the documentation hub for the Liberu ecosystem: Laravel applications, independent domain modules, APIs, presentation adapters, themes, engineering standards, deployment, and product scopes.

If you are new, start with [GETTING-STARTED.md](GETTING-STARTED.md). If you already know the solution or technology you need, use the indexes below.

## Choose your path

| You want to… | Start here |
|---|---|
| Understand the whole Liberu platform | [Liberu platform scope](projects/LIBERU.md) · [Technology and solution map](TECHNOLOGIES.md) |
| Build a new application or package | [Modules](architecture/MODULES.md) · [Laravel standard](standards/LARAVEL.md) · [Coding guidelines](standards/GUIDELINES.md) |
| Find a product capability | [Application scopes](#application-scopes) · [Feature indexes](features/README.md) |
| Add an API or UI adapter | [API index](modules/api/README.md) · [Presentation indexes](#presentation-indexes) |
| Choose React, Vue, Nuxt, Livewire, or Filament | [Technology standards](#technology-standards) · [Technology map](TECHNOLOGIES.md) |
| Design or extend a theme | [Theme standard](standards/THEMES.md) |
| Run tests, CI, or a release | [Testing](standards/TESTING.md) · [CI](standards/CI.md) · [Deployment](deployment/README.md) |
| Contribute or report a vulnerability | [Contributing](standards/CONTRIBUTING.md) · [Security](architecture/SECURITY.md) |

## How the documentation fits together

Liberu separates concerns so the same domain capability can be used by multiple applications and interfaces:

```text
Application composition
        ↓
Domain module → API contract → React/Vue/Nuxt/Livewire/Filament adapter
        ↓                         ↓
Persistence, policies, events     Theme and design-system adapter
```

- **Architecture** records boundaries and decisions: [architecture/README.md](architecture/README.md), [modules](architecture/MODULES.md), [API contracts](architecture/API.md), tenancy, teams, policies, repositories, and security.
- **Standards** define implementation quality: [standards/README.md](standards/README.md), coding, PHP, Laravel, frontend frameworks, database, themes, testing, documentation, and operations.
- **Technologies** provide language references: [technologies/README.md](technologies/README.md), [JavaScript](technologies/JAVASCRIPT.md), [TypeScript](technologies/TYPESCRIPT.md), [PHP](technologies/PHP.md), and the root [technology map](TECHNOLOGIES.md).
- **Projects** define product and application scope. Feature documents are framework-neutral; API and presentation documents are optional one-to-one adapters.

## Technology standards

Use the latest stable versions supported by the ecosystem and the consuming repository’s lock file and CI matrix. The current documentation baseline is PHP 8.5, Laravel 13, Filament 5, Livewire 4, React 19.2, Inertia 3, Vue 3, Nuxt 4, and Node.js 22+.

| Technology | Liberu standard | Official documentation |
|---|---|---|
| PHP and PSR | [PHP](standards/PHP.md) · [PSR](standards/PSR.md) · [Pint](standards/PINT.md) | [PHP](https://www.php.net/docs.php) · [PHP-FIG](https://www.php-fig.org/psr/) |
| Laravel | [Laravel](standards/LARAVEL.md) | [Laravel 13 docs](https://laravel.com/docs/13.x) · [Laravel GitHub](https://github.com/laravel/laravel) |
| Filament | [Filament](standards/FILAMENT.md) | [Filament 5 docs](https://filamentphp.com/docs/5.x) · [GitHub](https://github.com/filamentphp/filament) |
| Livewire | [Livewire](standards/LIVEWIRE.md) | [Documentation](https://livewire.laravel.com/docs) · [GitHub](https://github.com/livewire/livewire) |
| React | [React](standards/REACT.md) | [React docs](https://react.dev/) · [GitHub](https://github.com/facebook/react) |
| Inertia | [Inertia](standards/INERTIA.md) | [Inertia 3 docs](https://inertiajs.com/docs/v3) · [GitHub](https://github.com/inertiajs/inertia) |
| Vue | [Vue](standards/VUE.md) | [Vue docs](https://vuejs.org/) · [GitHub](https://github.com/vuejs/core) |
| Nuxt | [Nuxt](standards/NUXT.md) | [Nuxt 4 docs](https://nuxt.com/docs/4.x) · [GitHub](https://github.com/nuxt/nuxt) |
| JavaScript and TypeScript | [JavaScript](technologies/JAVASCRIPT.md) · [TypeScript](technologies/TYPESCRIPT.md) | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript) · [TypeScript](https://www.typescriptlang.org/docs/) |

## Application scopes

Each application scope identifies its domain modules and links to the corresponding API and presentation indexes.

| Application | Modules | API | Filament | Livewire | React | Vue |
|---|---:|---:|---:|---:|---:|---:|
| [Accounting](projects/accounting/ACCOUNTING.md) | [105](projects/accounting/features/README.md) | [105](projects/accounting/api/README.md) | [105](projects/accounting/filament/README.md) | [105](projects/accounting/livewire/README.md) | [105](projects/accounting/react/README.md) | [105](projects/accounting/vue/README.md) |
| [Automation](projects/automation/AUTOMATION.md) | [11](projects/automation/features/README.md) | [11](projects/automation/api/README.md) | [11](projects/automation/filament/README.md) | [11](projects/automation/livewire/README.md) | [11](projects/automation/react/README.md) | [11](projects/automation/vue/README.md) |
| [Billing](projects/billing/BILLING.md) | [16](projects/billing/features/README.md) | [16](projects/billing/api/README.md) | [16](projects/billing/filament/README.md) | [16](projects/billing/livewire/README.md) | [16](projects/billing/react/README.md) | [16](projects/billing/vue/README.md) |
| [Browser Game](projects/browser-game/BROWSER-GAME.md) | [15](projects/browser-game/features/README.md) | [15](projects/browser-game/api/README.md) | [15](projects/browser-game/filament/README.md) | [15](projects/browser-game/livewire/README.md) | [15](projects/browser-game/react/README.md) | [15](projects/browser-game/vue/README.md) |
| [CMS](projects/cms/CMS.md) | [81](projects/cms/features/README.md) | [81](projects/cms/api/README.md) | [81](projects/cms/filament/README.md) | [81](projects/cms/livewire/README.md) | [81](projects/cms/react/README.md) | [81](projects/cms/vue/README.md) |
| [Control Panel](projects/control-panel/CONTROL-PANEL.md) | [15](projects/control-panel/features/README.md) | [15](projects/control-panel/api/README.md) | [15](projects/control-panel/filament/README.md) | [15](projects/control-panel/livewire/README.md) | [15](projects/control-panel/react/README.md) | [15](projects/control-panel/vue/README.md) |
| [CRM](projects/crm/CRM.md) | [95](projects/crm/features/README.md) | [95](projects/crm/api/README.md) | [95](projects/crm/filament/README.md) | [95](projects/crm/livewire/README.md) | [95](projects/crm/react/README.md) | [95](projects/crm/vue/README.md) |
| [Ecommerce](projects/ecommerce/ECOMMERCE.md) | [105](projects/ecommerce/features/README.md) | [105](projects/ecommerce/api/README.md) | [105](projects/ecommerce/filament/README.md) | [105](projects/ecommerce/livewire/README.md) | [105](projects/ecommerce/react/README.md) | [105](projects/ecommerce/vue/README.md) |
| [Genealogy](projects/genealogy/GENEALOGY.md) | [14](projects/genealogy/features/README.md) | [14](projects/genealogy/api/README.md) | [14](projects/genealogy/filament/README.md) | [14](projects/genealogy/livewire/README.md) | [14](projects/genealogy/react/README.md) | [14](projects/genealogy/vue/README.md) |
| [Maintenance](projects/maintenance/MAINTENANCE.md) | [14](projects/maintenance/features/README.md) | [14](projects/maintenance/api/README.md) | [14](projects/maintenance/filament/README.md) | [14](projects/maintenance/livewire/README.md) | [14](projects/maintenance/react/README.md) | [14](projects/maintenance/vue/README.md) |
| [Real Estate](projects/real-estate/REAL-ESTATE.md) | [15](projects/real-estate/features/README.md) | [15](projects/real-estate/api/README.md) | [15](projects/real-estate/filament/README.md) | [15](projects/real-estate/livewire/README.md) | [15](projects/real-estate/react/README.md) | [15](projects/real-estate/vue/README.md) |
| [SAP-style Enterprise Suite](projects/sap/SAP.md) | [16](projects/sap/features/README.md) | [16](projects/sap/api/README.md) | [16](projects/sap/filament/README.md) | [16](projects/sap/livewire/README.md) | [16](projects/sap/react/README.md) | [16](projects/sap/vue/README.md) |
| [Social Network](projects/social-network/SOCIAL-NETWORK.md) | [15](projects/social-network/features/README.md) | [15](projects/social-network/api/README.md) | [15](projects/social-network/filament/README.md) | [15](projects/social-network/livewire/README.md) | [15](projects/social-network/react/README.md) | [15](projects/social-network/vue/README.md) |

The Liberu platform adds only new cross-product capabilities under [projects/liberu/features](projects/liberu/features/README.md): [Platform Orchestration](projects/liberu/features/platform-orchestration.md), [Executive Insights](projects/liberu/features/executive-insights.md), and [Business Workflow Reconciliation](projects/liberu/features/business-workflow-reconciliation.md), with matching API, Filament, Livewire, React, Vue, and Nuxt indexes.

## Presentation indexes

These root indexes cover the complete existing module matrix. Select only the adapters needed by an application surface.

- [Feature specifications](features/README.md) — framework-neutral domain capability.
- [Module indexes](modules/README.md) · [Generic domain feature scopes](modules/features/README.md) — domain-to-implementation mapping.
- [API modules](modules/api/README.md) — HTTP/API contracts and adapters.
- [Filament implementations](modules/filament/README.md) — administrative and operational UI.
- [Livewire implementations](modules/livewire/README.md) — server-driven Laravel UI.
- [React + Inertia implementations](modules/react/README.md) — React application UI over Laravel routes.
- [Vue + Inertia implementations](modules/vue/README.md) — Vue application UI over Laravel routes.
- [Nuxt implementations](modules/nuxt/README.md) — Vue SSR/API-consuming applications.

## Operating and contributing

- Read [GETTING-STARTED.md](GETTING-STARTED.md) for the recommended workflow.
- Use [DATABASE.md](standards/DATABASE.md) for migrations, seeders, factories, ownership, and database operations.
- Use [TRANSLATIONS.md](standards/TRANSLATIONS.md) for localization ownership, catalogs, formatting, and RTL behavior.
- Use [deployment documentation](deployment/README.md) for Docker, Kubernetes, web servers, queues, workers, and observability.
- Update the relevant source-of-truth document in the same change as code or contract changes.
- Keep examples safe: never commit secrets, production data, or private identifiers.

## Governance

- [License](LICENSE.md)
- [Contributing](standards/CONTRIBUTING.md)
- [Security policy](architecture/SECURITY.md)
- [Documentation standard](standards/DOCUMENTATION.md)
