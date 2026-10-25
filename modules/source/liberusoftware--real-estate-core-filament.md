# liberusoftware/real-estate-core-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for real-estate branches.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-core-filament](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: real-estate-laravel, `real-estate-core-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-core-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-core-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\CoreFilament\\RealEstateCoreFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/composer.json) · [module.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/module.json).

**Declared capabilities:** real-estate.core.filament

**Declared features:** Branch resource, Team-scoped branch administration

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/real-estate-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\CoreFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/real-estate-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/RealEstateCoreFilamentPlugin.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/RealEstateCoreFilamentPlugin.php) · [src/RealEstateCoreFilamentServiceProvider.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/RealEstateCoreFilamentServiceProvider.php) · [src/Resources/AgencyResource.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/AgencyResource.php) · [src/Resources/AgencyResource/Pages/CreateAgency.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/AgencyResource/Pages/CreateAgency.php) · [src/Resources/AgencyResource/Pages/EditAgency.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/AgencyResource/Pages/EditAgency.php) · [src/Resources/AgencyResource/Pages/ListAgencies.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/AgencyResource/Pages/ListAgencies.php) · [src/Resources/BranchResource.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/BranchResource.php) · [src/Resources/BranchResource/Pages/CreateBranch.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/BranchResource/Pages/CreateBranch.php) · [src/Resources/BranchResource/Pages/EditBranch.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/BranchResource/Pages/EditBranch.php) · [src/Resources/BranchResource/Pages/ListBranches.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/BranchResource/Pages/ListBranches.php) · [src/Resources/StatusDefinitionResource.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/StatusDefinitionResource.php) · [src/Resources/StatusDefinitionResource/Pages/CreateStatusDefinition.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/StatusDefinitionResource/Pages/CreateStatusDefinition.php) · [src/Resources/StatusDefinitionResource/Pages/EditStatusDefinition.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/StatusDefinitionResource/Pages/EditStatusDefinition.php) · [src/Resources/StatusDefinitionResource/Pages/ListStatusDefinitions.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/StatusDefinitionResource/Pages/ListStatusDefinitions.php) · [src/Resources/TerritoryResource.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/TerritoryResource.php) · [src/Resources/TerritoryResource/Pages/CreateTerritory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/TerritoryResource/Pages/CreateTerritory.php) · [src/Resources/TerritoryResource/Pages/EditTerritory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/TerritoryResource/Pages/EditTerritory.php) · [src/Resources/TerritoryResource/Pages/ListTerritories.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/TerritoryResource/Pages/ListTerritories.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
