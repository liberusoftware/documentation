# Control Panel: Control Panel Backups Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-backups). Observed identity: [`liberusoftware/module-control-panel-backups-livewire`](../../../modules/source/liberusoftware--module-control-panel-backups-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-control-panel-control-panel-backups-livewire`  
**Matching domain module:** `control-panel-backups`  
**Application:** Control Panel  
**Source feature:** [Control Panel Backups](../features/control-panel-backups.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Policies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Snapshots:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Application-consistent backup:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Encryption:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Off-site storage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Restore:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Verification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-control-panel-control-panel-backups-livewire` component namespace and service provider; use explicit aliases such as `<livewire:controlpanelControlPanelBackups::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `policies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `snapshots`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `application-consistent-backup`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `encryption`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `off-site-storage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `restore`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `verification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `control-panel-backups` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/control-panel-backups.md) · [API plan](../api/control-panel-backups.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Policies** | Expose a focused Livewire 4 component and namespaced Blade default view for `policies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Snapshots** | Expose a focused Livewire 4 component and namespaced Blade default view for `snapshots` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Application-consistent backup** | Expose a focused Livewire 4 component and namespaced Blade default view for `application-consistent backup` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Encryption** | Expose a focused Livewire 4 component and namespaced Blade default view for `encryption` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Off-site storage** | Expose a focused Livewire 4 component and namespaced Blade default view for `off-site storage` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Restore** | Expose a focused Livewire 4 component and namespaced Blade default view for `restore` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Verification** | Expose a focused Livewire 4 component and namespaced Blade default view for `verification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [BackupsLivewireServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-livewire/src/BackupsLivewireServiceProvider.php) · [BackupExecutionInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-livewire/src/Components/BackupExecutionInventory.php) · [BackupFeatureInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-livewire/src/Components/BackupFeatureInventory.php) · [DestinationInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-livewire/src/Components/DestinationInventory.php) · [PolicyInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-livewire/src/Components/PolicyInventory.php) · [ScheduleInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-livewire/src/Components/ScheduleInventory.php) · [SnapshotInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-livewire/src/Components/SnapshotInventory.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListSnapshots.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Queries/ListSnapshots.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateDestination.php) | `public function execute(array $attributes): BackupDestination` |
| [CreatePolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreatePolicy.php) | `public function execute(array $attributes): BackupPolicy` |
| [CreateSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSchedule.php) | `public function execute(BackupPolicy $policy, string $cron, string $timezone = 'UTC'): BackupSchedule` |
| [CreateSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSnapshot.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(BackupPolicy $policy, array $attributes = []): BackupSnapshot` |
| [DeleteDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteDestination.php) | `public function execute(BackupDestination $destination): void` |
| [DeletePolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeletePolicy.php) | `public function execute(BackupPolicy $policy): void` |
| [DeleteSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSchedule.php) | `public function execute(BackupSchedule $schedule): void` |
| [DeleteSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSnapshot.php) | `public function execute(BackupSnapshot $snapshot): void` |
| [RecordBackupFeature.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordBackupFeature.php) | `public function execute(array $a): Model` |
| [RecordDestinationHealth.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordDestinationHealth.php) | `public function execute(BackupDestination $destination, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): BackupDestination` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BackupDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupDestination.php) | `team_id`, `name`, `driver`, `config`, `retention_days`, `default`, `active`, `last_checked_at`, `health` |
| [BackupEncryption.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupEncryption.php) | `id`, `team_id`, `policy_id`, `algorithm`, `key_reference`, `active`, `rotated_at` |
| [BackupExecution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupExecution.php) | `id`, `team_id`, `policy_id`, `type`, `consistency`, `status`, `started_at`, `completed_at`, `error`, `metadata` |
| [BackupPolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupPolicy.php) | `team_id`, `name`, `schedule`, `retention_days`, `storage_driver`, `storage_config`, `encrypted`, `active` |
| [BackupRestore.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupRestore.php) | `team_id`, `snapshot_id`, `target`, `status`, `options`, `error`, `started_at`, `finished_at` |
| [BackupSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSchedule.php) | `team_id`, `policy_id`, `cron`, `timezone`, `active`, `next_run_at`, `last_run_at` |
| [BackupSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSnapshot.php) | `team_id`, `policy_id`, `location`, `status`, `size_bytes`, `checksum`, `verified_at`, `metadata` |
| [OffsiteTransfer.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/OffsiteTransfer.php) | `id`, `team_id`, `snapshot_id`, `destination_id`, `status`, `attempts`, `transferred_at`, `error`, `metadata` |
<!-- layer-implementation-plan:end -->
