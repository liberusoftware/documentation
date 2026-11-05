# liberusoftware/module-control-panel-databases: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral database lifecycle for the Liberu Control Panel.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-databases](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-databases`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-databases` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-databases` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\Databases\\DatabasesServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/module.json).

**Declared capabilities:** control-panel.databases

**Declared features:** Database engines, Database lifecycle, Users and privileges, Backups, Upgrades, Health checks, Remote access

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `illuminate/validation` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\Databases\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ActivateDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ActivateDatabase.php) | `public function execute(Database $database): Database` |
| [src/Actions/ArchiveDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ArchiveDatabase.php) | `public function execute(Database $database): Database` |
| [src/Actions/ConfigureRemoteAccess.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ConfigureRemoteAccess.php) | `public function execute(Database $database, array $attributes): DatabaseRemoteAccess` |
| [src/Actions/CreateDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabase.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Database` |
| [src/Actions/CreateDatabaseBackup.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabaseBackup.php) | `public function execute(Database $database, array $attributes): DatabaseBackup` |
| [src/Actions/CreateDatabaseUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabaseUser.php) | `public function execute(Database $database, array $attributes): DatabaseUser` |
| [src/Actions/DeleteDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/DeleteDatabase.php) | `public function execute(Database $database): void` |
| [src/Actions/GrantDatabasePrivilege.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/GrantDatabasePrivilege.php) | `public function execute(DatabaseUser $user, string $privilege, string $objectName = '*'): DatabasePrivilege` |
| [src/Actions/RecordDatabaseHealth.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/RecordDatabaseHealth.php) | `public function execute(Database $database, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): DatabaseHealthCheck` |
| [src/Actions/RequestDatabaseUpgrade.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/RequestDatabaseUpgrade.php) | `public function execute(Database $database, string $toVersion): DatabaseUpgrade` |
| [src/Actions/SuspendDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/SuspendDatabase.php) | `public function execute(Database $database): Database` |
| [src/Actions/UpdateDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/UpdateDatabase.php) | `public function execute(Database $database, array $attributes): Database` |
| [src/Queries/ListDatabaseBackups.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Queries/ListDatabaseBackups.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [src/Queries/ListDatabases.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Queries/ListDatabases.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/DatabasesServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/DatabasesServiceProvider.php) · [src/Enums/BackupStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Enums/BackupStatus.php) · [src/Enums/DatabaseStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Enums/DatabaseStatus.php) · [src/Enums/UpgradeStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Enums/UpgradeStatus.php) · [src/Events/DatabaseCreated.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Events/DatabaseCreated.php) · [src/Models/Database.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/Database.php) · [src/Models/DatabaseBackup.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseBackup.php) · [src/Models/DatabaseEngine.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseEngine.php) · [src/Models/DatabaseHealthCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseHealthCheck.php) · [src/Models/DatabasePrivilege.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabasePrivilege.php) · [src/Models/DatabaseRemoteAccess.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseRemoteAccess.php) · [src/Models/DatabaseUpgrade.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseUpgrade.php) · [src/Models/DatabaseUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseUser.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000000_create_control_panel_database_tables.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/database/migrations/2026_08_24_000000_create_control_panel_database_tables.php)
- [database/migrations/2026_08_24_000001_create_control_panel_database_access.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/database/migrations/2026_08_24_000001_create_control_panel_database_access.php)
- [database/migrations/2026_08_24_000002_create_control_panel_database_operations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/database/migrations/2026_08_24_000002_create_control_panel_database_operations.php)

[src/Enums/BackupStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Enums/BackupStatus.php): `Pending = 'pending'`, `Running = 'running'`, `Completed = 'completed'`, `Failed = 'failed'`.

[src/Enums/DatabaseStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Enums/DatabaseStatus.php): `Provisioning = 'provisioning'`, `Active = 'active'`, `Suspended = 'suspended'`, `Archived = 'archived'`.

[src/Enums/UpgradeStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Enums/UpgradeStatus.php): `Pending = 'pending'`, `Running = 'running'`, `Succeeded = 'succeeded'`, `Failed = 'failed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
