# liberusoftware/module-maintenance-inspections: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Inspections domain module for Liberu Maintenance

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [module-maintenance-inspections](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-maintenance-laravel-filament, `module-maintenance-inspections`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-maintenance-inspections` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-maintenance-inspections` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Modules\\Maintenance\\Inspections\\InspectionsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/composer.json) · [module.json](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/module.json).

**Declared capabilities:** maintenance.inspections

**Declared features:** Templates, Conditional checklists, Readings, Failures, Signatures, Certificates, Follow-up

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Maintenance\\Inspections\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CompleteInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/CompleteInspection.php) | `public function handle(int $teamId, Inspection $inspection, string $outcome): Inspection` |
| [src/Actions/CreateInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/CreateInspection.php) | `public function handle(int $teamId, array $attributes): Inspection` |
| [src/Actions/DeleteInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/DeleteInspection.php) | `public function handle(int $teamId, Inspection $inspection): void` |
| [src/Actions/UpdateInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/UpdateInspection.php) | `public function handle(int $teamId, Inspection $inspection, array $attributes): Inspection` |
| [src/Policies/InspectionPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Policies/InspectionPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Inspection $inspection): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Inspection $inspection): bool`<br>`public function delete(object $user, Inspection $inspection): bool` |

Other non-legacy PHP sources: [src/InspectionsServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/InspectionsServiceProvider.php) · [src/Models/Inspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Models/Inspection.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_060000_create_maintenance_inspections_table.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/database/migrations/2026_08_25_060000_create_maintenance_inspections_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
