# liberusoftware/module-crm-scheduling: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-scheduling](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-scheduling`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-scheduling` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-scheduling` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\Scheduling\\SchedulingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\Scheduling\\SchedulingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/module.json).

**Declared capabilities:** crm.scheduling

**Declared features:** Personal, team and round-robin links, Availability, buffers and minimum notice, Questions, reminders, reschedule, cancel and no-show, Routing and calendar adapters

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\Scheduling\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ChangeBookingStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/ChangeBookingStatus.php) | `public function execute(int $teamId, int $actorId, int $bookingId, string $status, array $data = []): Booking` |
| [src/Actions/CreateBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/CreateBooking.php) | `public function execute(int $teamId, int $actorId, array $data): Booking` |
| [src/Actions/CreateSchedulingLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/CreateSchedulingLink.php) | `public function execute(int $teamId, int $actorId, array $data): SchedulingLink` |
| [src/Queries/SchedulingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Queries/SchedulingQuery.php) | `public function links(int $teamId)`<br>`public function bookings(int $teamId)` |
| [src/Services/SchedulingAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Services/SchedulingAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [src/Services/SchedulingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Services/SchedulingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/BookingChanged.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Events/BookingChanged.php) · [src/Models/Booking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/Booking.php) · [src/Models/SchedulingAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/SchedulingAudit.php) · [src/Models/SchedulingLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/SchedulingLink.php) · [src/SchedulingServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/SchedulingServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_130000_create_crm_scheduling_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/database/migrations/2026_08_25_130000_create_crm_scheduling_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/Scheduling/SchedulingModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/tests/Feature/Scheduling/SchedulingModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
