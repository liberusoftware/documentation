# liberusoftware/module-crm-resource-planning: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-resource-planning](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-resource-planning`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-resource-planning` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-resource-planning` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\ResourcePlanning\\ResourcePlanningServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\ResourcePlanning\\ResourcePlanningServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/module.json).

**Declared capabilities:** crm.resource-planning

**Declared features:** Skills and capacity, Allocation and utilization, Tentative and confirmed bookings, Conflicts, rates and staffing forecasts

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\ResourcePlanning\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateBooking.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/CreateBooking.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceBooking` |
| [src/Actions/RecordForecast.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/RecordForecast.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceForecast` |
| [src/Actions/SetCapacity.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/SetCapacity.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceCapacity` |
| [src/Actions/SetRate.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/SetRate.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceRate` |
| [src/Actions/UpsertSkill.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/UpsertSkill.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceSkill` |
| [src/Queries/ResourcePlanningQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Queries/ResourcePlanningQuery.php) | `public function skills(int $teamId)`<br>`public function capacity(int $teamId)`<br>`public function bookings(int $teamId)`<br>`public function forecasts(int $teamId)` |
| [src/Services/ResourcePlanningPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Services/ResourcePlanningPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/ResourceBookingChanged.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Events/ResourceBookingChanged.php) · [src/Models/ResourceBooking.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceBooking.php) · [src/Models/ResourceCapacity.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceCapacity.php) · [src/Models/ResourceForecast.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceForecast.php) · [src/Models/ResourceRate.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceRate.php) · [src/Models/ResourceSkill.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceSkill.php) · [src/ResourcePlanningServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/ResourcePlanningServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_220000_create_crm_resource_planning_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/database/migrations/2026_08_25_220000_create_crm_resource_planning_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/ResourcePlanning/ResourcePlanningModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/tests/Feature/ResourcePlanning/ResourcePlanningModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
