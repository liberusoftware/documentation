# Domain module implementation

Generic feature specifications define domain behavior, ownership, invariants, contracts, and verification. They do not replace the Laravel implementation required to run a feature.

## Package boundary

Each independent feature is implemented as a cohesive core domain module. The core Composer package is named `module-{independent-module-name}`, owns its business rules and persistence, and is consumed by optional presentation packages. Presentation packages depend on the core module and never the other way around.

```text
module-{independent-module-name}/
├── src/
│   ├── Domain/          # entities, value objects, events, policies, contracts
│   ├── Application/     # actions, services, commands, queries, DTOs
│   └── Infrastructure/  # persistence, providers, integrations, adapters
├── database/
│   ├── migrations/
│   ├── factories/
│   └── seeders/
├── tests/
├── composer.json
└── module.json
```

The exact directories may be reduced when a feature does not need a layer. Do not create empty layers or move reusable domain behavior into an application’s root `app/` directory. Core module packages are installed under `/modules/{module-name}` according to [MODULES.md](../../architecture/MODULES.md).

## Laravel responsibilities

Use the following implementation responsibilities when a feature requires them:

| Responsibility                  | Implementation location                                              | Rule                                                           |
| ------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| Domain invariants and use cases | Domain/application classes, actions, services, contracts             | Keep business rules independent from presentation.             |
| Persistence                     | Models, migrations, factories, seeders, database constraints         | The module owns its tables and upgrade path.                   |
| HTTP/API access                 | API package controllers, requests, resources, routes, policies       | Controllers stay thin and expose documented contracts.         |
| Administration                  | Filament package resources, pages, widgets, schemas, tables, actions | Filament presents one matching domain module.                  |
| Interactive Laravel UI          | Livewire components, views, actions, and policies                    | Livewire coordinates presentation state, not domain ownership. |
| Asynchronous work               | Jobs, events, listeners, notifications, queue configuration          | Jobs are safe to retry and preserve tenant/team context.       |
| Views and assets                | Blade views and theme assets in the relevant presentation package    | Follow the shared theme tokens and accessibility rules.        |
| Verification                    | Unit, feature, integration, presentation, and contract tests         | Test domain behavior and each exposed adapter.                 |

Do not add controllers, Filament resources, Livewire components, React/Vue/Nuxt pages, or theme assets directly to the core package. Put them in the matching `api/`, `filament/`, `livewire/`, `react/`, `vue/`, or `nuxt/` presentation package under the relevant project scope.

## Required design checks

Before implementation, confirm the feature’s [domain specification](../../features/README.md), ownership, tenancy, teams, policies, settings, database lifecycle, API contract, and module dependencies. Check for an existing capability and extend its owner rather than creating a duplicate.

Apply the relevant [Laravel](../../standards/LARAVEL.md), [domain-driven design](../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [services](../../standards/SERVICES.md), [controllers](../../standards/CONTROLLERS.md), [models](../../standards/MODELS.md), [jobs](../../standards/JOBS.md), [queues](../../standards/QUEUES.md), [database](../../standards/DATABASE.md), [API](../../architecture/API.md), [Filament](../../standards/FILAMENT.md), [Livewire](../../standards/LIVEWIRE.md), [themes](../../standards/THEMES.md), and [testing](../../standards/TESTING.md) standards.

The project’s `features/` README remains the domain scope index, while `core/` is the core implementation index and `api/`, `filament/`, `livewire/`, `react/`, `vue/`, and `nuxt/` are presentation indexes. This guide explains how they fit together; it does not duplicate their feature definitions.
