# liberusoftware/module-billing-catalog-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for the Liberu Billing Catalog module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-catalog-filament](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-billing-laravel-filament, `module-billing-catalog-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-catalog-filament` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-catalog-filament` |
| Module version field | `0.1.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Billing\\Catalog\\Filament\\CatalogFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/module.json).

**Declared capabilities:** billing.catalog.filament

**Declared features:** Product resource, Lifecycle display, Price fields

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `~5.1` |
| `liberusoftware/module-billing-catalog` | `^0.1` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Catalog\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-billing-catalog": "^0.1", "liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/CatalogFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/CatalogFilamentPlugin.php) · [src/CatalogFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/CatalogFilamentServiceProvider.php) · [src/Concerns/ScopesCurrentTeam.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Concerns/ScopesCurrentTeam.php) · [src/Resources/AddonResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/AddonResource.php) · [src/Resources/AddonResource/Pages/CreateAddon.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/AddonResource/Pages/CreateAddon.php) · [src/Resources/AddonResource/Pages/ListAddons.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/AddonResource/Pages/ListAddons.php) · [src/Resources/BundleResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/BundleResource.php) · [src/Resources/BundleResource/Pages/CreateBundle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/BundleResource/Pages/CreateBundle.php) · [src/Resources/BundleResource/Pages/ListBundles.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/BundleResource/Pages/ListBundles.php) · [src/Resources/CatalogRecordResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/CatalogRecordResource.php) · [src/Resources/ChannelResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ChannelResource.php) · [src/Resources/ChannelResource/Pages/CreateChannel.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ChannelResource/Pages/CreateChannel.php) · [src/Resources/ChannelResource/Pages/ListChannels.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ChannelResource/Pages/ListChannels.php) · [src/Resources/ConfigurableOptionResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ConfigurableOptionResource.php) · [src/Resources/ConfigurableOptionResource/Pages/CreateConfigurableOption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ConfigurableOptionResource/Pages/CreateConfigurableOption.php) · [src/Resources/ConfigurableOptionResource/Pages/ListConfigurableOptions.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ConfigurableOptionResource/Pages/ListConfigurableOptions.php) · [src/Resources/EligibilityResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/EligibilityResource.php) · [src/Resources/EligibilityResource/Pages/CreateEligibility.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/EligibilityResource/Pages/CreateEligibility.php) · [src/Resources/EligibilityResource/Pages/ListEligibility.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/EligibilityResource/Pages/ListEligibility.php) · [src/Resources/PlanResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/PlanResource.php) · [src/Resources/PlanResource/Pages/CreatePlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/PlanResource/Pages/CreatePlan.php) · [src/Resources/PlanResource/Pages/ListPlans.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/PlanResource/Pages/ListPlans.php) · [src/Resources/ProductResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ProductResource.php) · [src/Resources/ProductResource/Pages/CreateProduct.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ProductResource/Pages/CreateProduct.php) · [src/Resources/ProductResource/Pages/ListProducts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ProductResource/Pages/ListProducts.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
