# Control Panel: Control Panel Files Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-files). Observed identity: [`liberusoftware/module-control-panel-files`](../../../modules/source/liberusoftware--module-control-panel-files.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-control-panel-control-panel-files`
**Domain specification:** [Control Panel Files](../features/control-panel-files.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Control Panel Files. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Home directories** | Model `home directories` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Permissions** | Model `permissions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **SFTP** | Model `sftp` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **File operations** | Model `file operations` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Quotas** | Model `quotas` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Scanning** | Model `scanning` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Retention** | Model `retention` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_040000_create_control_panel_files_table.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/database/migrations/2026_08_24_040000_create_control_panel_files_table.php) · [2026_08_24_120004_create_control_panel_file_operations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/database/migrations/2026_08_24_120004_create_control_panel_file_operations.php) · [2026_08_24_130001_create_control_panel_file_management.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/database/migrations/2026_08_24_130001_create_control_panel_file_management.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListFiles.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Queries/ListFiles.php) | `public function execute(string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateHomeDirectory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/CreateHomeDirectory.php) | `public function execute(array $attributes): HomeDirectory` |
| [CreateSftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/CreateSftpAccount.php) | `public function execute(array $attributes): SftpAccount` |
| [DeleteFile.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/DeleteFile.php) | `public function execute(FileEntry $file): FileEntry` |
| [DeleteSftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/DeleteSftpAccount.php) | `public function execute(SftpAccount $account): void` |
| [GrantFilePermission.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/GrantFilePermission.php) | `public function execute(array $attributes): FilePermission` |
| [MarkFileScanned.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/MarkFileScanned.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(FileEntry $file, bool $clean): FileEntry` |
| [RecordFileOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RecordFileOperation.php) | `public function execute(array $a): FileOperation` |
| [RegenerateSftpKeyPair.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RegenerateSftpKeyPair.php) | `public function execute(SftpAccount $account, ?int $bits = null): array` |
| [RegisterFile.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RegisterFile.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): FileEntry` |
| [SetFileQuota.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/SetFileQuota.php) | `public function execute(array $attributes): FileQuota` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FileEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileEntry.php) | `team_id`, `owner_id`, `path`, `disk`, `mime_type`, `size_bytes`, `checksum`, `status`, `scanned_at`, `retention_until`, `metadata` |
| [FileOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileOperation.php) | `id`, `team_id`, `file_id`, `operation`, `status`, `details` |
| [FilePermission.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FilePermission.php) | `id`, `team_id`, `file_id`, `home_directory_id`, `subject_id`, `subject_type`, `mode`, `recursive` |
| [FileQuota.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileQuota.php) | `id`, `team_id`, `owner_id`, `limit_bytes`, `used_bytes`, `files_count` |
| [FileRetention.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileRetention.php) | `id`, `team_id`, `file_id`, `retention_until`, `policy`, `active` |
| [HomeDirectory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/HomeDirectory.php) | `id`, `team_id`, `owner_id`, `path`, `disk`, `mode`, `status`, `metadata` |
| [SftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/SftpAccount.php) | `id`, `team_id`, `owner_id`, `username`, `password`, `home_directory`, `quota_mb`, `bandwidth_limit_mb`, `active`, `last_login_at`, `ssh_key_auth_enabled`, `ssh_public_key`, `ssh_private_key`, `ssh_key_type`, `ssh_key_bits` |

### Consuming adapter specifications

- [HTTP API contract](../api/control-panel-files.md) · [Filament 5](../filament/control-panel-files.md) · [Livewire 4](../livewire/control-panel-files.md) · [React + Inertia](../react/control-panel-files.md) · [Vue + Inertia](../vue/control-panel-files.md) · [Nuxt 4](../nuxt/control-panel-files.md) · [Next.js](../nextjs/control-panel-files.md) · [React Native](../react-native/control-panel-files.md) · [Flutter & Dart](../flutter/control-panel-files.md)
<!-- core-implementation-plan:end -->
