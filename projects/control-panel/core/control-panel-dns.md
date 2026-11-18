# Control Panel: Control Panel Dns Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-dns). Observed identity: [`liberusoftware/module-control-panel-dns`](../../../modules/source/liberusoftware--module-control-panel-dns.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-control-panel-control-panel-dns`
**Domain specification:** [Control Panel Dns](../features/control-panel-dns.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Control Panel Dns. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Zones** | Model `zones` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Records** | Model `records` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Templates** | Model `templates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **DNSSEC** | Model `dnssec` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Validation** | Model `validation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Providers** | Model `providers` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Propagation checks** | Model `propagation checks` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_010000_create_control_panel_dns_tables.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/database/migrations/2026_08_24_010000_create_control_panel_dns_tables.php) · [2026_08_24_120002_create_control_panel_dns_operations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/database/migrations/2026_08_24_120002_create_control_panel_dns_operations.php) · [2026_08_24_140003_create_control_panel_dns_features.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/database/migrations/2026_08_24_140003_create_control_panel_dns_features.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListZones.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Queries/ListZones.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ActivateZone.php) | `public function execute(Zone $zone): Zone` |
| [ArchiveZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ArchiveZone.php) | `public function execute(Zone $zone): Zone` |
| [CheckDnsPropagation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CheckDnsPropagation.php) | `public function __construct(private readonly DnsResolver $resolver)`<br>`public function execute(array $attributes): array` |
| [CheckDnsResolution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CheckDnsResolution.php) | `public function __construct(private readonly DnsResolver $resolver)`<br>`public function execute(array $attributes): array` |
| [CreateRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CreateRecord.php) | `public function execute(array $a): Record` |
| [CreateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CreateZone.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Zone` |
| [DeleteRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/DeleteRecord.php) | `public function execute(Record $record): void` |
| [RecordDnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/RecordDnsCheck.php) | `public function execute(array $a): DnsCheck` |
| [RegisterDnsFeature.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/RegisterDnsFeature.php) | `public function execute(array $a): Model` |
| [SuspendZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/SuspendZone.php) | `public function execute(Zone $zone): Zone` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsCheck.php) | `id`, `team_id`, `zone_id`, `kind`, `status`, `result`, `checked_at` |
| [DnsProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsProvider.php) | `id`, `team_id`, `name`, `driver`, `endpoint`, `credentials`, `settings`, `active` |
| [DnsTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsTemplate.php) | `id`, `team_id`, `name`, `records`, `active` |
| [DnsValidation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsValidation.php) | `id`, `team_id`, `zone_id`, `record_id`, `status`, `resolver`, `expected`, `observed`, `checked_at`, `details` |
| [DnssecKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnssecKey.php) | `id`, `team_id`, `zone_id`, `key_tag`, `algorithm`, `digest_type`, `digest`, `public_key`, `private_key`, `active`, `rotated_at` |
| [PropagationCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/PropagationCheck.php) | `id`, `team_id`, `zone_id`, `record_id`, `status`, `nameservers`, `results`, `checked_at` |
| [Record.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/Record.php) | `zone_id`, `name`, `type`, `content`, `ttl`, `priority`, `metadata` |
| [Zone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/Zone.php) | `team_id`, `domain`, `status`, `provider`, `dnssec_enabled`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/control-panel-dns.md) · [Filament 5](../filament/control-panel-dns.md) · [Livewire 4](../livewire/control-panel-dns.md) · [React + Inertia](../react/control-panel-dns.md) · [Vue + Inertia](../vue/control-panel-dns.md) · [Nuxt 4](../nuxt/control-panel-dns.md) · [Next.js](../nextjs/control-panel-dns.md) · [React Native](../react-native/control-panel-dns.md) · [Flutter & Dart](../flutter/control-panel-dns.md)
<!-- core-implementation-plan:end -->
