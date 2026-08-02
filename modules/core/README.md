# Core module implementations

## Canonical domain package boundary

Core modules are the reusable, presentation-neutral Composer packages in the Liberu architecture. Each package is named `module-{independent-module-name}` and owns one cohesive domain capability: its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and tests.

The target is Laravel 13, PHP 8.5, Composer 2, and Pest 5. Core packages are suitable for enterprise deployments and for SMEs or personal users because the same boundary supports strong authorization, auditability, migration safety, clear workflows, low operational overhead, localization, accessibility in adapters, and safe data export.

## Dependency direction

```text
Application / project
        ↓
Optional API, Filament, Livewire, React, Vue, Nuxt, and theme adapters
        ↓
module-{independent-module-name} core package
        ↓
Foundation contracts and provider-neutral abstractions
        ↓
Laravel 13 / PHP 8.5 runtime
```

Core packages never depend on API, Filament, Livewire, React, Vue, Nuxt, themes, an application's `App\\` classes, or provider SDKs. They communicate with other modules through stable contracts, commands, queries, registries, identifiers, and events—not private models or tables. Provider and regional behavior belongs in separately installed adapters.

## Implementation standard

1. Define one bounded context and authoritative owner. Record aggregates, entities, value objects, enums, invariants, lifecycle states, tenant/team context, permissions, data classification, and integration contracts before coding.
2. Implement domain rules with small aggregates and domain services. Use application actions for mutations, purpose-built query/read models for reads, immutable DTOs at boundaries, and repositories only where an abstraction is meaningful.
3. Use Laravel service providers, configuration, contracts, validation, policies, events, queues, notifications, and console integration at the infrastructure boundary. Keep Eloquent models as persistence mappings rather than aggregates or API resources.
4. Make local changes transactional and dispatch events after commit. Make jobs retryable and idempotent, carry authorized context, expose progress/failure state, and use outbox/inbox, sagas, or compensation for distributed workflows.
5. Treat migrations, constraints, indexes, factories, seeders, retention, export, deletion, and upgrade paths as module-owned contracts. Released migrations are immutable; production changes document locks, backfills, deployment order, rollback limits, and recovery.
6. Apply the same policy to HTTP, UI, console, queue, exports, searches, notifications, and bulk actions. Scopes and UI visibility never override domain authorization, tenancy, ownership, consent, entitlement, or field sensitivity.
7. Design operator and end-user workflows with safe defaults, actionable errors, previews or reversibility where practical, localization/timezone/currency support, accessibility through adapters, and clear recovery guidance.

## Required package evidence

Each independent module repository owns its Composer metadata, module manifest, PSR-4 namespace, service provider, configuration, migrations, tests, changelog, README, compatibility matrix, and runbook. Its suite runs independently through the shared package testbench and repository-owned Composer scripts.

Testing covers pure domain rules, actions, policies, validation, persistence, tenancy, events, jobs, commands, migrations, upgrades, security, failure recovery, contracts, compatibility, and representative host composition. Architecture tests reject application coupling, private cross-module access, provider leakage, presentation dependencies, and dependency cycles. Meaningful owned PHP receives coverage; coverage does not replace risk-based assertions.

## Project indexes

| Project         | Core module index                                            |
| --------------- | ------------------------------------------------------------ |
| Accounting      | [Core modules](../../projects/accounting/core/README.md)     |
| Automation      | [Core modules](../../projects/automation/core/README.md)     |
| Billing         | [Core modules](../../projects/billing/core/README.md)        |
| Browser Game    | [Core modules](../../projects/browser-game/core/README.md)   |
| CMS             | [Core modules](../../projects/cms/core/README.md)            |
| Control Panel   | [Core modules](../../projects/control-panel/core/README.md)  |
| CRM             | [Core modules](../../projects/crm/core/README.md)            |
| Ecommerce       | [Core modules](../../projects/ecommerce/core/README.md)      |
| Genealogy       | [Core modules](../../projects/genealogy/core/README.md)      |
| Liberu platform | [Core modules](../../projects/liberu/core/README.md)         |
| Maintenance     | [Core modules](../../projects/maintenance/core/README.md)    |
| Real Estate     | [Core modules](../../projects/real-estate/core/README.md)    |
| SAP             | [Core modules](../../projects/sap/core/README.md)            |
| Social Network  | [Core modules](../../projects/social-network/core/README.md) |

See [MODULES.md](../../architecture/MODULES.md), [Laravel 13](../../standards/LARAVEL.md), [PHP 8.5](../../standards/PHP.md), [DDD patterns](../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [database](../../standards/DATABASE.md), [security](../../architecture/SECURITY.md), and [testing](../../standards/TESTING.md) for the governing details.
