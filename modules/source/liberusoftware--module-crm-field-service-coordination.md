# liberusoftware/module-crm-field-service-coordination: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-field-service-coordination](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-field-service-coordination`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-field-service-coordination` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-field-service-coordination` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\FieldServiceCoordination\\FieldServiceCoordinationServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\FieldServiceCoordination\\FieldServiceCoordinationServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/module.json).

**Declared capabilities:** crm.field-service-coordination

**Declared features:** Work types, appointments, dispatch visibility, asset history and maintenance handoff

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\FieldServiceCoordination\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateWorkType.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/CreateWorkType.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): WorkType` |
| [src/Actions/HandOffMaintenance.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/HandOffMaintenance.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, ServiceAppointment $appointment, array $input): MaintenanceHandoff` |
| [src/Actions/RecordServiceHistory.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/RecordServiceHistory.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, ServiceAppointment $appointment, array $input): ServiceHistory` |
| [src/Actions/ScheduleAppointment.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/ScheduleAppointment.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ServiceAppointment` |
| [src/Queries/FieldServiceQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Queries/FieldServiceQuery.php) | `public function workTypes(int $teamId)`<br>`public function appointments(int $teamId)`<br>`public function assets(int $teamId)` |
| [src/Services/FieldServicePolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Services/FieldServicePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/FieldServiceCoordinationServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/FieldServiceCoordinationServiceProvider.php) · [src/Models/MaintenanceHandoff.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/MaintenanceHandoff.php) · [src/Models/ServiceAppointment.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceAppointment.php) · [src/Models/ServiceAsset.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceAsset.php) · [src/Models/ServiceHistory.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceHistory.php) · [src/Models/WorkType.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/WorkType.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_27_020000_create_crm_field_service_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/database/migrations/2026_08_27_020000_create_crm_field_service_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/FieldServiceCoordination/FieldServiceCoordinationModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/tests/Feature/FieldServiceCoordination/FieldServiceCoordinationModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
