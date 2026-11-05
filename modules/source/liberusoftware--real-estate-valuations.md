# liberusoftware/real-estate-valuations: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral valuation records and lifecycle actions.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-valuations](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-valuations`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-valuations` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-valuations` |
| Module version field | `1.0.0` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\Valuations\\ValuationsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\RealEstate\\Valuations\\ValuationsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/module.json).

**Declared capabilities:** real-estate.valuations

**Declared features:** Appraisals, Comparables, Pricing, Fees, Recommendations, Follow-up, Conversion, Property valuation estimates, Mortgage estimates, Rental yield estimates

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/validation` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `liberusoftware/real-estate-properties` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\Valuations\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0", "liberusoftware/real-estate-properties": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/ValuationPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Policies/ValuationPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Valuation $valuation): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Valuation $valuation): bool`<br>`public function delete(AuthUser $authUser, Valuation $valuation): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Valuation $valuation): bool`<br>`public function forceDelete(AuthUser $authUser, Valuation $valuation): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Valuation $valuation): bool`<br>`public function reorder(AuthUser $authUser): bool` |

Other non-legacy PHP sources: [src/Application/AnalyzePropertyInvestment.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/AnalyzePropertyInvestment.php) · [src/Application/CalculateComparables.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/CalculateComparables.php) · [src/Application/CalculateCostOfMoving.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/CalculateCostOfMoving.php) · [src/Application/CalculateHomeValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/CalculateHomeValuation.php) · [src/Application/CalculateMortgage.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/CalculateMortgage.php) · [src/Application/CalculateRentalYield.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/CalculateRentalYield.php) · [src/Application/CalculateStampDuty.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/CalculateStampDuty.php) · [src/Application/CompleteValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/CompleteValuation.php) · [src/Application/ConvertValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/ConvertValuation.php) · [src/Application/CreateValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/CreateValuation.php) · [src/Application/DeleteValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/DeleteValuation.php) · [src/Application/GenerateNeuralPropertyValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/GenerateNeuralPropertyValuation.php) · [src/Application/GeneratePropertyValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/GeneratePropertyValuation.php) · [src/Application/ScheduleValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/ScheduleValuation.php) · [src/Application/UpdateValuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Application/UpdateValuation.php) · [src/Domain/ValuationStatus.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Domain/ValuationStatus.php) · [src/Domain/ValuationsCapabilityDefinition.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Domain/ValuationsCapabilityDefinition.php) · [src/Models/Valuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Models/Valuation.php) · [src/ValuationsServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/ValuationsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000005_create_real_estate_valuations_table.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/database/migrations/2026_08_23_000005_create_real_estate_valuations_table.php)
- [database/migrations/2026_08_24_000003_add_valuation_workflow_fields.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/database/migrations/2026_08_24_000003_add_valuation_workflow_fields.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
