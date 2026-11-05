# liberusoftware/module-crm-revenue-lifecycle: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-revenue-lifecycle](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-revenue-lifecycle`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-revenue-lifecycle` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-revenue-lifecycle` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\RevenueLifecycle\\RevenueLifecycleServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\RevenueLifecycle\\RevenueLifecycleServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/module.json).

**Declared capabilities:** crm.revenue-lifecycle

**Declared features:** Opportunity-to-order orchestration, Assets and installed products, Entitlements, renewals, upgrades and downgrades, Cancellation, usage signals and fallout queues

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\RevenueLifecycle\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/CreateOrder.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueOrder` |
| [src/Actions/ManageAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ManageAsset.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueAsset` |
| [src/Actions/RecordUsageSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/RecordUsageSignal.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assetId, array $input): RevenueAsset` |
| [src/Actions/ResolveFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ResolveFallout.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $falloutId, array $input): RevenueFallout` |
| [src/Queries/RevenueQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Queries/RevenueQuery.php) | `public function assets(int $teamId)`<br>`public function orders(int $teamId)`<br>`public function fallout(int $teamId)` |
| [src/Services/RevenuePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Services/RevenuePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/RevenueLifecycleChanged.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Events/RevenueLifecycleChanged.php) · [src/Models/RevenueAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueAsset.php) · [src/Models/RevenueFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueFallout.php) · [src/Models/RevenueOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueOrder.php) · [src/RevenueLifecycleServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/RevenueLifecycleServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_200000_create_crm_revenue_lifecycle_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/database/migrations/2026_08_25_200000_create_crm_revenue_lifecycle_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/RevenueLifecycle/RevenueLifecycleModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/tests/Feature/RevenueLifecycle/RevenueLifecycleModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
