# liberusoftware/real-estate-portals-reporting: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral, team-scoped portal publication and reporting records for real estate.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-portals-reporting](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-portals-reporting`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-portals-reporting` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-portals-reporting` |
| Module version field | `1.0.0` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\PortalsReporting\\PortalsReportingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\RealEstate\\PortalsReporting\\PortalsReportingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/module.json).

**Declared capabilities:** real-estate.portals-reporting

**Declared features:** Party self-service plus pipeline, Conversion, Source, Fee, Time-to-complete, Occupancy, Compliance metrics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/validation` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\PortalsReporting\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/PortalReportPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Policies/PortalReportPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function delete(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function forceDelete(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function reorder(AuthUser $authUser): bool` |

Other non-legacy PHP sources: [src/Application/CreatePortalReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Application/CreatePortalReport.php) · [src/Application/DeletePortalReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Application/DeletePortalReport.php) · [src/Application/RecordPortalMetric.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Application/RecordPortalMetric.php) · [src/Application/TransitionPortalReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Application/TransitionPortalReport.php) · [src/Application/UpdatePortalReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Application/UpdatePortalReport.php) · [src/Domain/PortalMetric.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Domain/PortalMetric.php) · [src/Domain/PortalReportStatus.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Domain/PortalReportStatus.php) · [src/Domain/PortalsReportingCapabilityDefinition.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Domain/PortalsReportingCapabilityDefinition.php) · [src/Models/DashboardLayout.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Models/DashboardLayout.php) · [src/Models/PortalReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Models/PortalReport.php) · [src/Models/SavedReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Models/SavedReport.php) · [src/PortalsReportingServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/PortalsReportingServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000013_create_real_estate_portal_reports_table.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/database/migrations/2026_08_23_000013_create_real_estate_portal_reports_table.php)
- [database/migrations/2026_08_30_000023_create_real_estate_saved_reports.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/database/migrations/2026_08_30_000023_create_real_estate_saved_reports.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
