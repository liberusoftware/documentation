# liberusoftware/real-estate-property-management-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for real-estate property management.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-property-management-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-property-management-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-property-management-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-property-management-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\PropertyManagementFilament\\PropertyManagementFilamentServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\RealEstate\\PropertyManagementFilament\\PropertyManagementFilamentServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/module.json).

**Declared capabilities:** real-estate.property-management.filament

**Declared features:** Management capability forms, Team-scoped resource table, Lifecycle status controls, Inspection resource, Maintenance request resource, Vendor quote resource, Work-order resource

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/real-estate-property-management` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\PropertyManagementFilament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/real-estate-property-management": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/PropertyManagementFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/PropertyManagementFilamentPlugin.php) · [src/PropertyManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/PropertyManagementFilamentServiceProvider.php) · [src/Resources/InspectionResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/InspectionResource.php) · [src/Resources/InspectionResource/Pages/CreateInspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/InspectionResource/Pages/CreateInspection.php) · [src/Resources/InspectionResource/Pages/EditInspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/InspectionResource/Pages/EditInspection.php) · [src/Resources/InspectionResource/Pages/ListInspections.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/InspectionResource/Pages/ListInspections.php) · [src/Resources/MaintenanceRequestResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/MaintenanceRequestResource.php) · [src/Resources/MaintenanceRequestResource/Pages/CreateMaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/MaintenanceRequestResource/Pages/CreateMaintenanceRequest.php) · [src/Resources/MaintenanceRequestResource/Pages/EditMaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/MaintenanceRequestResource/Pages/EditMaintenanceRequest.php) · [src/Resources/MaintenanceRequestResource/Pages/ListMaintenanceRequests.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/MaintenanceRequestResource/Pages/ListMaintenanceRequests.php) · [src/Resources/ManagementRecordResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/ManagementRecordResource.php) · [src/Resources/ManagementRecordResource/Pages/CreateManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/ManagementRecordResource/Pages/CreateManagementRecord.php) · [src/Resources/ManagementRecordResource/Pages/EditManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/ManagementRecordResource/Pages/EditManagementRecord.php) · [src/Resources/ManagementRecordResource/Pages/ListManagementRecords.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/ManagementRecordResource/Pages/ListManagementRecords.php) · [src/Resources/VendorQuoteResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/VendorQuoteResource.php) · [src/Resources/VendorQuoteResource/Pages/CreateVendorQuote.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/VendorQuoteResource/Pages/CreateVendorQuote.php) · [src/Resources/VendorQuoteResource/Pages/EditVendorQuote.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/VendorQuoteResource/Pages/EditVendorQuote.php) · [src/Resources/VendorQuoteResource/Pages/ListVendorQuotes.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/VendorQuoteResource/Pages/ListVendorQuotes.php) · [src/Resources/WorkOrderResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/WorkOrderResource.php) · [src/Resources/WorkOrderResource/Pages/CreateWorkOrder.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/WorkOrderResource/Pages/CreateWorkOrder.php) · [src/Resources/WorkOrderResource/Pages/EditWorkOrder.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/WorkOrderResource/Pages/EditWorkOrder.php) · [src/Resources/WorkOrderResource/Pages/ListWorkOrders.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/WorkOrderResource/Pages/ListWorkOrders.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
