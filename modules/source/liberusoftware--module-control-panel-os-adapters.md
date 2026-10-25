# liberusoftware/module-control-panel-os-adapters: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral operating system adapter inventory and capabilities.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-os-adapters](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-os-adapters`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-os-adapters` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-os-adapters` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\OsAdapters\\OsAdaptersServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/module.json).

**Declared capabilities:** control-panel.os-adapters

**Declared features:** Detection, Packages, Services, Service installation suggestions, Firewall, Users, Filesystems, Repositories, Support matrix

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\OsAdapters\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateFirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/CreateFirewallRule.php) | `public function execute(array $attributes): FirewallRule`<br>`public function validateSource(mixed $source): void` |
| [src/Actions/DeleteFirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/DeleteFirewallRule.php) | `public function execute(FirewallRule $rule): void` |
| [src/Actions/RecordOsResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordOsResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [src/Actions/RecordSupportMatrix.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordSupportMatrix.php) | `public function execute(array $attributes): SupportMatrixEntry` |
| [src/Actions/RegisterOsAdapter.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RegisterOsAdapter.php) | `public function execute(array $attributes): OsAdapter` |
| [src/Actions/UpdateFirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateFirewallRule.php) | `public function execute(FirewallRule $rule, array $attributes): FirewallRule` |
| [src/Actions/UpdateOsService.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateOsService.php) | `public function execute(OsService $service, array $attributes): OsService` |
| [src/Queries/InstallationCommandReport.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/InstallationCommandReport.php) | `public function __construct(private readonly ServiceStatusReport $serviceStatusReport)`<br>`public function execute(string\|int $teamId): array` |
| [src/Queries/ListOsAdapters.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ListOsAdapters.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Queries/ServiceStatusReport.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ServiceStatusReport.php) | `public function all(string\|int $teamId): Collection`<br>`public function missing(string\|int $teamId): Collection`<br>`public function stopped(string\|int $teamId): Collection`<br>`public function find(string\|int $teamId, string $name): ?OsService` |

Other non-legacy PHP sources: [src/Models/FilesystemMount.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FilesystemMount.php) · [src/Models/FirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FirewallRule.php) · [src/Models/OsAdapter.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsAdapter.php) · [src/Models/OsPackage.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsPackage.php) · [src/Models/OsService.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsService.php) · [src/Models/OsUser.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsUser.php) · [src/Models/PackageRepository.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/PackageRepository.php) · [src/Models/SupportMatrixEntry.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/SupportMatrixEntry.php) · [src/OsAdaptersServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/OsAdaptersServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_110000_create_control_panel_os_adapters.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/database/migrations/2026_08_24_110000_create_control_panel_os_adapters.php)
- [database/migrations/2026_08_24_110001_create_control_panel_os_resources.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/database/migrations/2026_08_24_110001_create_control_panel_os_resources.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
