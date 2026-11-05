# liberusoftware/module-liberu-revenue-and-care-orchestration: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu liberu-revenue-and-care-orchestration module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 2 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-liberu-revenue-and-care-orchestration](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-revenue-and-care-orchestration/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 2 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 2 |

Physical source locations: **3**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-billing-laravel-filament, `liberu-revenue-and-care-orchestration`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-liberu-revenue-and-care-orchestration` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `liberu-revenue-and-care-orchestration` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Platform\\RevenueAndCareOrchestration\\RevenueAndCareOrchestrationServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/composer.json) · [module.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/module.json).

**Declared capabilities:** liberu.revenue-and-care-orchestration, liberu.revenue-and-care-orchestration.lifecycle

**Declared features:** liberu revenue and care orchestration, liberu revenue and care orchestration lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Platform\\RevenueAndCareOrchestration\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateCarePlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/src/Actions/CreateCarePlan.php) | `public function execute(array $attributes): CarePlan` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/src/Capability.php) · [src/Models/CarePlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/src/Models/CarePlan.php) · [src/RevenueAndCareOrchestrationServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/src/RevenueAndCareOrchestrationServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_liberu_care_plans_table.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/database/migrations/2026_08_24_010000_create_liberu_care_plans_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: project-genealogy-laravel-filament, `liberu-revenue-and-care-orchestration`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-liberu-revenue-and-care-orchestration` |
| Composer version field | `1.1.1` |
| Package type | `liberu-module` |
| Module manifest name | `liberu-revenue-and-care-orchestration` |
| Module version field | `1.1.1` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Platform\\RevenueAndCareOrchestration\\RevenueAndCareOrchestrationServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/composer.json) · [module.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/module.json).

**Declared capabilities:** liberu.revenue-and-care-orchestration, liberu.revenue-and-care-orchestration.lifecycle

**Declared features:** liberu revenue and care orchestration, liberu revenue and care orchestration lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Platform\\RevenueAndCareOrchestration\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateCarePlan.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/Actions/CreateCarePlan.php) | `public function execute(array $attributes): CarePlan` |
| [src/Actions/TransitionCarePlan.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/Actions/TransitionCarePlan.php) | `public function execute(CarePlan $record, LifecycleStatus $to): CarePlan` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/Capability.php) · [src/Enums/LifecycleStatus.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/Enums/LifecycleStatus.php) · [src/Events/CarePlanTransitioned.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/Events/CarePlanTransitioned.php) · [src/Exceptions/InvalidLifecycleTransition.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/Exceptions/InvalidLifecycleTransition.php) · [src/Models/CarePlan.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/Models/CarePlan.php) · [src/RevenueAndCareOrchestrationServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/RevenueAndCareOrchestrationServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_liberu_care_plans_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/database/migrations/2026_08_24_010000_create_liberu_care_plans_table.php)

[src/Enums/LifecycleStatus.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/src/Enums/LifecycleStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Completed = 'completed'`, `Archived = 'archived'`.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
