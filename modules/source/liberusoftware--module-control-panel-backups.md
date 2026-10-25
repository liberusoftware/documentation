# liberusoftware/module-control-panel-backups: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral backup policies, snapshots, restore, and verification for Liberu Control Panel.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-backups](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-backups`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-backups` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-backups` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\Backups\\BackupsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/module.json).

**Declared capabilities:** control-panel.backups

**Declared features:** Policies, Snapshots, Application-consistent backup, Encryption, Off-site storage, Restore, Verification, Destination health, Retention, Schedules

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `illuminate/validation` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\Backups\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateDestination.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateDestination.php) | `public function execute(array $attributes): BackupDestination` |
| [src/Actions/CreatePolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreatePolicy.php) | `public function execute(array $attributes): BackupPolicy` |
| [src/Actions/CreateSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSchedule.php) | `public function execute(BackupPolicy $policy, string $cron, string $timezone = 'UTC'): BackupSchedule` |
| [src/Actions/CreateSnapshot.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSnapshot.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(BackupPolicy $policy, array $attributes = []): BackupSnapshot` |
| [src/Actions/DeleteDestination.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteDestination.php) | `public function execute(BackupDestination $destination): void` |
| [src/Actions/DeletePolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeletePolicy.php) | `public function execute(BackupPolicy $policy): void` |
| [src/Actions/DeleteSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSchedule.php) | `public function execute(BackupSchedule $schedule): void` |
| [src/Actions/DeleteSnapshot.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSnapshot.php) | `public function execute(BackupSnapshot $snapshot): void` |
| [src/Actions/RecordBackupFeature.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordBackupFeature.php) | `public function execute(array $a): Model` |
| [src/Actions/RecordDestinationHealth.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordDestinationHealth.php) | `public function execute(BackupDestination $destination, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): BackupDestination` |
| [src/Actions/RequestRestore.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RequestRestore.php) | `public function execute(BackupSnapshot $snapshot, string $teamId, string $target, array $options = []): BackupRestore` |
| [src/Actions/UpdateDestination.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdateDestination.php) | `public function execute(BackupDestination $destination, array $attributes): BackupDestination` |
| [src/Actions/UpdatePolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdatePolicy.php) | `public function execute(BackupPolicy $policy, array $attributes): BackupPolicy` |
| [src/Actions/UpdateSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdateSchedule.php) | `public function execute(BackupSchedule $schedule, array $attributes): BackupSchedule` |
| [src/Actions/VerifySnapshot.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/VerifySnapshot.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(BackupSnapshot $snapshot, string $checksum): BackupSnapshot` |
| [src/Queries/ListSnapshots.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Queries/ListSnapshots.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/BackupsServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/BackupsServiceProvider.php) · [src/Enums/RestoreStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Enums/RestoreStatus.php) · [src/Enums/SnapshotStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Enums/SnapshotStatus.php) · [src/Events/SnapshotCreated.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Events/SnapshotCreated.php) · [src/Events/SnapshotVerified.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Events/SnapshotVerified.php) · [src/Models/BackupDestination.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupDestination.php) · [src/Models/BackupEncryption.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupEncryption.php) · [src/Models/BackupExecution.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupExecution.php) · [src/Models/BackupPolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupPolicy.php) · [src/Models/BackupRestore.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupRestore.php) · [src/Models/BackupSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSchedule.php) · [src/Models/BackupSnapshot.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSnapshot.php) · [src/Models/OffsiteTransfer.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/OffsiteTransfer.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_030000_create_control_panel_backup_tables.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/database/migrations/2026_08_24_030000_create_control_panel_backup_tables.php)
- [database/migrations/2026_08_24_030001_create_control_panel_backup_operations.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/database/migrations/2026_08_24_030001_create_control_panel_backup_operations.php)
- [database/migrations/2026_08_24_140005_create_control_panel_backup_features.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/database/migrations/2026_08_24_140005_create_control_panel_backup_features.php)

[src/Enums/RestoreStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Enums/RestoreStatus.php): `Queued = 'queued'`, `Running = 'running'`, `Completed = 'completed'`, `Failed = 'failed'`.

[src/Enums/SnapshotStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Enums/SnapshotStatus.php): `Queued = 'queued'`, `Running = 'running'`, `Verified = 'verified'`, `Failed = 'failed'`, `Restored = 'restored'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
