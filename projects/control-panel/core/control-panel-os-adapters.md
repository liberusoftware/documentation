# Control Panel: Control Panel Os Adapters Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-os-adapters). Observed identity: [`liberusoftware/module-control-panel-os-adapters`](../../../modules/source/liberusoftware--module-control-panel-os-adapters.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-control-panel-control-panel-os-adapters`
**Domain specification:** [Control Panel Os Adapters](../features/control-panel-os-adapters.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Control Panel Os Adapters. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

## Domain-driven implementation plan

- Model the capability with small aggregates, entities, value objects, enums, domain services, and explicit lifecycle states. Enforce invariants inside the domain boundary and keep invalid transitions impossible or rejected with typed exceptions.
- Implement one application action per meaningful mutation/use case and purpose-built query/read-model classes for reads. Use typed immutable DTOs and stable identifiers at public boundaries; use repositories only where persistence abstraction adds value.
- Publish past-tense domain events after a successful local transaction. Use an outbox/inbox, idempotent handlers, sagas, or compensating actions for cross-module and distributed work; never mutate another module's private tables.

## Laravel and persistence plan

- Use PHP 8.5 strict types, PSR-compatible names, constructor injection, Laravel contracts, service providers, configuration, policies, validation, and route-independent application services. Format with the repository's Pint rules and keep static analysis clean.
- Keep Eloquent models as persistence mappings, not domain aggregates or API resources. The module owns migrations, constraints, indexes, casts, factories, seeders, retention, export, deletion, and upgrade behavior. Released migrations are immutable; production-safe follow-up migrations document locks, backfills, deployment order, and rollback limits.
- Queue work that exceeds the request budget or depends on external systems. Jobs carry authorized tenant/actor context, have explicit retry/backoff/timeout/idempotency rules, and emit structured logs, metrics, traces, correlation IDs, and operator-visible failure state.

## Security and user outcomes

- Apply policies consistently to HTTP, UI, console, queue, export, search, notification, and bulk paths. Enforce tenant/team/resource ownership, field sensitivity, consent, entitlement, and break-glass auditing; scopes never override domain authorization.
- Treat imports, files, webhooks, provider responses, and user input as untrusted. Redact credentials and protected data from logs, exceptions, events, snapshots, metrics, and test artifacts.
- Make normal workflows understandable for SMEs and personal users: actionable validation, safe defaults, reversible or previewable operations, clear status and recovery guidance, localization/timezone/currency support where relevant, accessibility in adapters, low operational overhead, and export/retention controls.

## Public boundary and adapters

Expose only stable contracts, actions, queries, events, resource data, and capability metadata needed by consumers. Keep provider SDKs, credentials, webhook mappings, and provider identifiers in separate adapter packages. Presentation packages may add validation at their boundary, but the core revalidates invariants and authorization and remains free of presentation dependencies.

## Verification and delivery plan

- Use unit tests for value objects, entities, aggregates, policies, and pure rules; feature/integration tests for actions, persistence, validation, tenancy, events, jobs, commands, migrations, upgrades, and recovery; and shared contract tests for adapters.
- Add architecture tests for forbidden App classes, private cross-module access, provider leakage, presentation dependencies, and dependency cycles. Test empty installs, supported upgrades, rollback policy, representative host composition, and compatibility across the declared Laravel/PHP/database matrix.
- Run the independent repository's Pest 5 suite through Composer scripts and the shared package testbench. Generate meaningful coverage, static-analysis, security, documentation/link, and performance evidence; coverage complements risk-based assertions and never replaces them.
- Release with Composer metadata, module manifest, service provider, changelog, migration notes, README, compatibility matrix, runbook, and safe install/enable/disable/upgrade/uninstall behavior. Disabling or removal never silently deletes user data.

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Detection** | Model `detection` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Packages** | Model `packages` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Services** | Model `services` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Firewall** | Model `firewall` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Users** | Model `users` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Filesystems** | Model `filesystems` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Repositories** | Model `repositories` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Support matrix** | Model `support matrix` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_110000_create_control_panel_os_adapters.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/database/migrations/2026_08_24_110000_create_control_panel_os_adapters.php) · [2026_08_24_110001_create_control_panel_os_resources.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/database/migrations/2026_08_24_110001_create_control_panel_os_resources.php).

| Observed core query | Public method signatures |
| --- | --- |
| [InstallationCommandReport.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/InstallationCommandReport.php) | `public function __construct(private readonly ServiceStatusReport $serviceStatusReport)`<br>`public function execute(string\|int $teamId): array` |
| [ListOsAdapters.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ListOsAdapters.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ServiceStatusReport.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ServiceStatusReport.php) | `public function all(string\|int $teamId): Collection`<br>`public function missing(string\|int $teamId): Collection`<br>`public function stopped(string\|int $teamId): Collection`<br>`public function find(string\|int $teamId, string $name): ?OsService` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/CreateFirewallRule.php) | `public function execute(array $attributes): FirewallRule`<br>`public function validateSource(mixed $source): void` |
| [DeleteFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/DeleteFirewallRule.php) | `public function execute(FirewallRule $rule): void` |
| [RecordOsResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordOsResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [RecordSupportMatrix.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordSupportMatrix.php) | `public function execute(array $attributes): SupportMatrixEntry` |
| [RegisterOsAdapter.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RegisterOsAdapter.php) | `public function execute(array $attributes): OsAdapter` |
| [UpdateFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateFirewallRule.php) | `public function execute(FirewallRule $rule, array $attributes): FirewallRule` |
| [UpdateOsService.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateOsService.php) | `public function execute(OsService $service, array $attributes): OsService` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FilesystemMount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FilesystemMount.php) | `team_id`, `node_id`, `device`, `mount_path`, `filesystem`, `size_bytes`, `free_bytes`, `options`, `mounted` |
| [FirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FirewallRule.php) | `team_id`, `node_id`, `direction`, `action`, `protocol`, `port`, `source`, `comment`, `active` |
| [OsAdapter.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsAdapter.php) | `team_id`, `node_id`, `operating_system`, `version`, `capabilities`, `status`, `metadata` |
| [OsPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsPackage.php) | `team_id`, `node_id`, `name`, `version`, `architecture`, `status`, `metadata` |
| [OsService.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsService.php) | `team_id`, `node_id`, `name`, `version`, `status`, `enabled`, `metadata` |
| [OsUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsUser.php) | `team_id`, `node_id`, `username`, `uid`, `shell`, `home`, `sudo`, `status`, `metadata` |
| [PackageRepository.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/PackageRepository.php) | `team_id`, `node_id`, `name`, `url`, `distribution`, `enabled`, `trusted`, `metadata` |
| [SupportMatrixEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/SupportMatrixEntry.php) | `operating_system`, `version`, `capability`, `supported`, `minimum_adapter_version`, `notes` |

### Consuming adapter specifications

- [HTTP API contract](../api/control-panel-os-adapters.md) · [Filament 5](../filament/control-panel-os-adapters.md) · [Livewire 4](../livewire/control-panel-os-adapters.md) · [React + Inertia](../react/control-panel-os-adapters.md) · [Vue + Inertia](../vue/control-panel-os-adapters.md) · [Nuxt 4](../nuxt/control-panel-os-adapters.md) · [Next.js](../nextjs/control-panel-os-adapters.md) · [React Native](../react-native/control-panel-os-adapters.md) · [Flutter & Dart](../flutter/control-panel-os-adapters.md)
<!-- core-implementation-plan:end -->
