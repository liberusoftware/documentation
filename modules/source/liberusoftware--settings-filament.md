# liberusoftware/settings-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament administration adapter for Liberu Settings.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/composer.json) | `39a49babafc0` | [Variant 2](#variant-2) | 5 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/settings-filament/composer.json) | `68e5f07a6704` | [Variant 2](#variant-2) | 5 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings-filament/composer.json) | `4743bdfebd1c` | [Variant 2](#variant-2) | 5 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/settings-filament/composer.json) | `3ade34046c3d` | [Variant 2](#variant-2) | 5 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings-filament/composer.json) | `790fdffebd3a` | [Variant 2](#variant-2) | 5 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 5 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings-filament/composer.json) | `63aad94e94c0` | [Variant 2](#variant-2) | 5 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/settings-filament/composer.json) | `b12a8c841c6a` | [Variant 2](#variant-2) | 5 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/settings-filament/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 5 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/settings-filament/composer.json) | `c267d625e264` | [Variant 2](#variant-2) | 5 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings-filament/composer.json) | `178d8015b601` | [Variant 2](#variant-2) | 5 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/settings-filament/composer.json) | `08bbc484b50f` | [Variant 2](#variant-2) | 5 |

Physical source locations: **12**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `settings-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/settings-filament` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `settings-filament` |
| Module version field | `1.4.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\SettingsFilament\\SettingsFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/module.json).

**Declared capabilities:** foundation.settings.filament

**Declared features:** Optional Filament settings administration surface

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.1` |
| `filament/spatie-laravel-settings-plugin` | `^5.0` |
| `liberusoftware/settings` | `^1.0` |
| `liberusoftware/theme-support` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\SettingsFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/settings": "^1.0", "liberusoftware/theme-support": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/Pages/ManageSiteSettings.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/src/Pages/ManageSiteSettings.php) · [src/SettingsFilamentPlugin.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/src/SettingsFilamentPlugin.php) · [src/SettingsFilamentServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/src/SettingsFilamentServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/tests/.gitkeep)
- [tests/Feature/ManageSiteSettingsTest.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/tests/Feature/ManageSiteSettingsTest.php)
- [tests/Fixtures/TestPanelProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/tests/Fixtures/TestPanelProvider.php)
- [tests/Pest.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: accounting-erp-laravel, `settings-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/settings-filament` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `settings-filament` |
| Module version field | `1.4.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\SettingsFilament\\SettingsFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/module.json).

**Declared capabilities:** foundation.settings.filament

**Declared features:** Optional Filament settings administration surface

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.1` |
| `filament/spatie-laravel-settings-plugin` | `^5.0` |
| `liberusoftware/settings` | `^1.0` |
| `liberusoftware/theme-support` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\SettingsFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/settings": "^1.0", "liberusoftware/theme-support": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/Pages/ManageSiteSettings.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/src/Pages/ManageSiteSettings.php) · [src/SettingsFilamentPlugin.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/src/SettingsFilamentPlugin.php) · [src/SettingsFilamentServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/src/SettingsFilamentServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/tests/.gitkeep)
- [tests/Feature/ManageSiteSettingsTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/tests/Feature/ManageSiteSettingsTest.php)
- [tests/Fixtures/TestPanelProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/tests/Fixtures/TestPanelProvider.php)
- [tests/Pest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
