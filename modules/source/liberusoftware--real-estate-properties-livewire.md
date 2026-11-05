# liberusoftware/real-estate-properties-livewire: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Livewire 4 adapter for real-estate properties.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-properties-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-properties-livewire`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-properties-livewire` |
| Composer version field | `1.0.1` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-properties-livewire` |
| Module version field | `1.0.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\PropertiesLivewire\\PropertiesLivewireServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/module.json).

**Declared capabilities:** real-estate.properties.livewire

**Declared features:** Property search state, Category filtering, Template filtering, Advanced bounded filters, Validation and empty states, Property detail disclosures, Property gallery, Property comparison, Property tax estimates, Saved property wishlist, Property review form, Neighborhood review form, Price alert manager, Property submission form, Property preview, Live virtual tour scheduling, Property map

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/real-estate-media-and-documents` | `^1.0` |
| `liberusoftware/real-estate-properties` | `^1.0` |
| `liberusoftware/real-estate-viewings` | `^1.0` |
| `liberusoftware/real-estate-viewings-livewire` | `^1.0` |
| `livewire/livewire` | `^4.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\PropertiesLivewire\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/real-estate-media-and-documents": "^1.0", "liberusoftware/real-estate-properties": "^1.0", "liberusoftware/real-estate-viewings": "^1.0", "liberusoftware/real-estate-viewings-livewire": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/Components/AdvancedPropertySearch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/AdvancedPropertySearch.php) · [src/Components/NeighborhoodReviewForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/NeighborhoodReviewForm.php) · [src/Components/PriceAlertManager.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PriceAlertManager.php) · [src/Components/PropertyComparison.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PropertyComparison.php) · [src/Components/PropertyDetail.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PropertyDetail.php) · [src/Components/PropertyList.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PropertyList.php) · [src/Components/PropertyMap.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PropertyMap.php) · [src/Components/PropertyPreview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PropertyPreview.php) · [src/Components/PropertyReviewForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PropertyReviewForm.php) · [src/Components/PropertySubmissionForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PropertySubmissionForm.php) · [src/Components/PropertyTaxEstimator.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/PropertyTaxEstimator.php) · [src/Components/WishlistManager.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/Components/WishlistManager.php) · [src/PropertiesLivewireServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/src/PropertiesLivewireServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [routes/web.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-livewire/routes/web.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
