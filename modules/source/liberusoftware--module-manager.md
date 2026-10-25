# liberusoftware/module-manager: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Deterministic manifest discovery and runtime enablement for Liberu modules.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/composer.json) | `39a49babafc0` | [Variant 2](#variant-2) | 4 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/composer.json) | `68e5f07a6704` | [Variant 4](#variant-4) | 4 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 4 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/module-manager/composer.json) | `3ade34046c3d` | [Variant 1](#variant-1) | 4 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/module-manager/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 4 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/module-manager/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 4 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/composer.json) | `63aad94e94c0` | [Variant 3](#variant-3) | 5 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/module-manager/composer.json) | `b12a8c841c6a` | [Variant 1](#variant-1) | 4 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/module-manager/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 4 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-manager/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 4 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/module-manager/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 4 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/module-manager/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 4 |

Physical source locations: **12**. Reference variants: **4**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-manager`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-manager` |
| Composer version field | `1.4.2` |
| Package type | `liberu-module` |
| Module manifest name | `module-manager` |
| Module version field | `1.4.2` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ModuleManager\\ModuleManagerServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/module.json).

**Declared capabilities:** foundation.modules

**Declared features:** Manifest discovery, Dependency resolution, Deployment enablement, Registry caching, Diagnostics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `composer/semver` | `^3.4` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ModuleManager\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": [], "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/Cache/RegistryCache.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Cache/RegistryCache.php) · [src/Console/CacheModulesCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Console/CacheModulesCommand.php) · [src/Console/ClearModulesCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Console/ClearModulesCommand.php) · [src/Console/ListFeaturesCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Console/ListFeaturesCommand.php) · [src/Console/ListModulesCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Console/ListModulesCommand.php) · [src/Console/ModuleStatusCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Console/ModuleStatusCommand.php) · [src/Console/ValidateModulesCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Console/ValidateModulesCommand.php) · [src/Exceptions/DependencyResolutionFailed.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Exceptions/DependencyResolutionFailed.php) · [src/Exceptions/InvalidManifest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Exceptions/InvalidManifest.php) · [src/Manifest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/Manifest.php) · [src/ModuleDiscovery.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/ModuleDiscovery.php) · [src/ModuleManagerServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/ModuleManagerServiceProvider.php) · [src/ModuleRegistry.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/ModuleRegistry.php) · [src/ModuleValidationGuard.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/ModuleValidationGuard.php) · [src/ModuleValidator.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/src/ModuleValidator.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **4**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/tests/.gitkeep)
- [tests/Pest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/tests/Pest.php)
- [tests/Unit/ManifestTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/tests/Unit/ManifestTest.php)
- [tests/Unit/ModuleRegistryCoverageTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager/tests/Unit/ModuleRegistryCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: accounting-erp-laravel, `module-manager`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-manager` |
| Composer version field | `1.4.2` |
| Package type | `liberu-module` |
| Module manifest name | `module-manager` |
| Module version field | `1.4.2` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ModuleManager\\ModuleManagerServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/module.json).

**Declared capabilities:** foundation.modules

**Declared features:** Manifest discovery, Dependency resolution, Deployment enablement, Registry caching, Diagnostics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `composer/semver` | `^3.4` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ModuleManager\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": [], "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/Cache/RegistryCache.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Cache/RegistryCache.php) · [src/Console/CacheModulesCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Console/CacheModulesCommand.php) · [src/Console/ClearModulesCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Console/ClearModulesCommand.php) · [src/Console/ListFeaturesCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Console/ListFeaturesCommand.php) · [src/Console/ListModulesCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Console/ListModulesCommand.php) · [src/Console/ModuleStatusCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Console/ModuleStatusCommand.php) · [src/Console/ValidateModulesCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Console/ValidateModulesCommand.php) · [src/Exceptions/DependencyResolutionFailed.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Exceptions/DependencyResolutionFailed.php) · [src/Exceptions/InvalidManifest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Exceptions/InvalidManifest.php) · [src/Manifest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/Manifest.php) · [src/ModuleDiscovery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/ModuleDiscovery.php) · [src/ModuleManagerServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/ModuleManagerServiceProvider.php) · [src/ModuleRegistry.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/ModuleRegistry.php) · [src/ModuleValidationGuard.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/ModuleValidationGuard.php) · [src/ModuleValidator.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/src/ModuleValidator.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **4**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/tests/.gitkeep)
- [tests/Pest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/tests/Pest.php)
- [tests/Unit/ManifestTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/tests/Unit/ManifestTest.php)
- [tests/Unit/ModuleRegistryCoverageTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager/tests/Unit/ModuleRegistryCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: crm-laravel, `module-manager`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-manager` |
| Composer version field | `1.4.2` |
| Package type | `liberu-module` |
| Module manifest name | `module-manager` |
| Module version field | `1.4.2` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ModuleManager\\ModuleManagerServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/module.json).

**Declared capabilities:** foundation.modules

**Declared features:** Manifest discovery, Dependency resolution, Deployment enablement, Registry caching, Diagnostics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `composer/semver` | `^3.4` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ModuleManager\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": [], "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/Cache/RegistryCache.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Cache/RegistryCache.php) · [src/Console/CacheModulesCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Console/CacheModulesCommand.php) · [src/Console/ClearModulesCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Console/ClearModulesCommand.php) · [src/Console/ListFeaturesCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Console/ListFeaturesCommand.php) · [src/Console/ListModulesCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Console/ListModulesCommand.php) · [src/Console/ModuleStatusCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Console/ModuleStatusCommand.php) · [src/Console/ValidateModulesCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Console/ValidateModulesCommand.php) · [src/Exceptions/DependencyResolutionFailed.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Exceptions/DependencyResolutionFailed.php) · [src/Exceptions/InvalidManifest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Exceptions/InvalidManifest.php) · [src/Manifest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/Manifest.php) · [src/ModuleDiscovery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/ModuleDiscovery.php) · [src/ModuleManagerServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/ModuleManagerServiceProvider.php) · [src/ModuleRegistry.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/ModuleRegistry.php) · [src/ModuleValidationGuard.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/ModuleValidationGuard.php) · [src/ModuleValidator.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/src/ModuleValidator.php).

**Legacy review:** 5 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_06_02_000001_create_modules_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/database/migrations/2026_06_02_000001_create_modules_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/tests/.gitkeep)
- [tests/Feature/Modules/BaseModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/tests/Feature/Modules/BaseModuleTest.php)
- [tests/Pest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/tests/Pest.php)
- [tests/Unit/ManifestTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/tests/Unit/ManifestTest.php)
- [tests/Unit/ModuleRegistryCoverageTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager/tests/Unit/ModuleRegistryCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 4

Representative: automation-laravel, `module-manager`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-manager` |
| Composer version field | `1.4.2` |
| Package type | `liberu-module` |
| Module manifest name | `module-manager` |
| Module version field | `1.4.2` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ModuleManager\\ModuleManagerServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/composer.json) · [module.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/module.json).

**Declared capabilities:** foundation.modules

**Declared features:** Manifest discovery, Dependency resolution, Deployment enablement, Registry caching, Diagnostics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `composer/semver` | `^3.4` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ModuleManager\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": [], "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/Cache/RegistryCache.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Cache/RegistryCache.php) · [src/Console/CacheModulesCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Console/CacheModulesCommand.php) · [src/Console/ClearModulesCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Console/ClearModulesCommand.php) · [src/Console/ListFeaturesCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Console/ListFeaturesCommand.php) · [src/Console/ListModulesCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Console/ListModulesCommand.php) · [src/Console/ModuleStatusCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Console/ModuleStatusCommand.php) · [src/Console/ValidateModulesCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Console/ValidateModulesCommand.php) · [src/Exceptions/DependencyResolutionFailed.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Exceptions/DependencyResolutionFailed.php) · [src/Exceptions/InvalidManifest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Exceptions/InvalidManifest.php) · [src/Manifest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/Manifest.php) · [src/ModuleDiscovery.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/ModuleDiscovery.php) · [src/ModuleManagerServiceProvider.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/ModuleManagerServiceProvider.php) · [src/ModuleRegistry.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/ModuleRegistry.php) · [src/ModuleValidationGuard.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/ModuleValidationGuard.php) · [src/ModuleValidator.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/src/ModuleValidator.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **4**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/tests/.gitkeep)
- [tests/Pest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/tests/Pest.php)
- [tests/Unit/ManifestTest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/tests/Unit/ManifestTest.php)
- [tests/Unit/ModuleRegistryCoverageTest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager/tests/Unit/ModuleRegistryCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
