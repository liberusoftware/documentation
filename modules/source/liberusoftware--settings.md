# liberusoftware/settings: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Typed scoped settings foundation for Liberu applications.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/composer.json) | `39a49babafc0` | [Variant 3](#variant-3) | 6 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/settings/composer.json) | `68e5f07a6704` | [Variant 3](#variant-3) | 6 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/composer.json) | `4743bdfebd1c` | [Variant 4](#variant-4) | 6 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/settings/composer.json) | `3ade34046c3d` | [Variant 3](#variant-3) | 6 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/composer.json) | `790fdffebd3a` | [Variant 2](#variant-2) | 6 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings/composer.json) | `1797f25d705f` | [Variant 3](#variant-3) | 6 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 6 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/settings/composer.json) | `b12a8c841c6a` | [Variant 3](#variant-3) | 6 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/settings/composer.json) | `577e93db23cc` | [Variant 3](#variant-3) | 6 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/settings/composer.json) | `c267d625e264` | [Variant 3](#variant-3) | 6 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/composer.json) | `178d8015b601` | [Variant 5](#variant-5) | 6 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/settings/composer.json) | `08bbc484b50f` | [Variant 3](#variant-3) | 6 |

Physical source locations: **12**. Reference variants: **5**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `settings`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/settings` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `settings` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Settings\\SettingsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/module.json).

**Declared capabilities:** foundation.settings

**Declared features:** Typed application, Organization, Team/site, User settings with validation and deterministic cache invalidation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-settings` | `^3.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Settings\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/SettingDefinition.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/src/Contracts/SettingDefinition.php) | `public function key(): string`<br>`public function validate(mixed $value): bool`<br>`public function secret(): bool` |
| [src/Services/ScopedSettings.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/src/Services/ScopedSettings.php) | `public function put(SettingDefinition $definition, string $scopeType, string $scopeId, mixed $value): void`<br>`public function resolve(string $key, array $scopes, mixed $fallback = null): mixed` |

Other non-legacy PHP sources: [src/Settings/SiteSettings.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/src/Settings/SiteSettings.php) · [src/SettingsServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/src/SettingsServiceProvider.php).

**Legacy review:** 15 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2022_12_14_083707_create_settings_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/migrations/2022_12_14_083707_create_settings_table.php)
- [database/migrations/2023_05_15_000000_create_site_settings_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/migrations/2023_05_15_000000_create_site_settings_table.php)
- [database/migrations/2024_07_24_080000_create_menus_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/migrations/2024_07_24_080000_create_menus_table.php)
- [database/migrations/2026_08_01_063100_create_scoped_settings_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/migrations/2026_08_01_063100_create_scoped_settings_table.php)
- [database/settings/2024_01_01_000001_create_settings_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/settings/2024_01_01_000001_create_settings_table.php)
- [database/settings/2025_12_10_102854_create_site_settings.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/settings/2025_12_10_102854_create_site_settings.php)
- [database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **6**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/tests/.gitkeep)
- [tests/Feature/SiteSettingsActiveThemeTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/tests/Feature/SiteSettingsActiveThemeTest.php)
- [tests/Feature/SiteSettingsDefaultsTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/tests/Feature/SiteSettingsDefaultsTest.php)
- [tests/Feature/SiteSettingsTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/tests/Feature/SiteSettingsTest.php)
- [tests/Pest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: browser-game-laravel, `settings`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/settings` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `settings` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Settings\\SettingsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/composer.json) · [module.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/module.json).

**Declared capabilities:** foundation.settings

**Declared features:** Typed application, Organization, Team/site, User settings with validation and deterministic cache invalidation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-settings` | `^3.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Settings\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/SettingDefinition.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/src/Contracts/SettingDefinition.php) | `public function key(): string`<br>`public function validate(mixed $value): bool`<br>`public function secret(): bool` |
| [src/Services/ScopedSettings.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/src/Services/ScopedSettings.php) | `public function put(SettingDefinition $definition, string $scopeType, string $scopeId, mixed $value): void`<br>`public function resolve(string $key, array $scopes, mixed $fallback = null): mixed` |

Other non-legacy PHP sources: [src/Models/SiteSettings.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/src/Models/SiteSettings.php) · [src/Settings/SiteSettings.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/src/Settings/SiteSettings.php) · [src/SettingsServiceProvider.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/src/SettingsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2022_12_14_083707_create_settings_table.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/database/migrations/2022_12_14_083707_create_settings_table.php)
- [database/migrations/2026_08_01_063100_create_scoped_settings_table.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/database/migrations/2026_08_01_063100_create_scoped_settings_table.php)
- [database/settings/2025_12_10_102854_create_site_settings.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/database/settings/2025_12_10_102854_create_site_settings.php)
- [database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **6**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/tests/.gitkeep)
- [tests/Feature/SiteSettingsActiveThemeTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/tests/Feature/SiteSettingsActiveThemeTest.php)
- [tests/Feature/SiteSettingsDefaultsTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/tests/Feature/SiteSettingsDefaultsTest.php)
- [tests/Feature/SiteSettingsTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/tests/Feature/SiteSettingsTest.php)
- [tests/Pest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: accounting-erp-laravel, `settings`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/settings` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `settings` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Settings\\SettingsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/module.json).

**Declared capabilities:** foundation.settings

**Declared features:** Typed application, Organization, Team/site, User settings with validation and deterministic cache invalidation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-settings` | `^3.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Settings\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/SettingDefinition.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/src/Contracts/SettingDefinition.php) | `public function key(): string`<br>`public function validate(mixed $value): bool`<br>`public function secret(): bool` |
| [src/Services/ScopedSettings.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/src/Services/ScopedSettings.php) | `public function put(SettingDefinition $definition, string $scopeType, string $scopeId, mixed $value): void`<br>`public function resolve(string $key, array $scopes, mixed $fallback = null): mixed` |

Other non-legacy PHP sources: [src/Settings/SiteSettings.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/src/Settings/SiteSettings.php) · [src/SettingsServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/src/SettingsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2022_12_14_083707_create_settings_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/database/migrations/2022_12_14_083707_create_settings_table.php)
- [database/migrations/2026_08_01_063100_create_scoped_settings_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/database/migrations/2026_08_01_063100_create_scoped_settings_table.php)
- [database/settings/2025_12_10_102854_create_site_settings.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/database/settings/2025_12_10_102854_create_site_settings.php)
- [database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **6**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/tests/.gitkeep)
- [tests/Feature/SiteSettingsActiveThemeTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/tests/Feature/SiteSettingsActiveThemeTest.php)
- [tests/Feature/SiteSettingsDefaultsTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/tests/Feature/SiteSettingsDefaultsTest.php)
- [tests/Feature/SiteSettingsTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/tests/Feature/SiteSettingsTest.php)
- [tests/Pest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 4

Representative: billing-laravel, `settings`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/settings` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `settings` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Settings\\SettingsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/module.json).

**Declared capabilities:** foundation.settings

**Declared features:** Typed application, Organization, Team/site, User settings with validation and deterministic cache invalidation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-settings` | `^3.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Settings\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/SettingDefinition.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/src/Contracts/SettingDefinition.php) | `public function key(): string`<br>`public function validate(mixed $value): bool`<br>`public function secret(): bool` |
| [src/Services/ScopedSettings.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/src/Services/ScopedSettings.php) | `public function put(SettingDefinition $definition, string $scopeType, string $scopeId, mixed $value): void`<br>`public function resolve(string $key, array $scopes, mixed $fallback = null): mixed` |

Other non-legacy PHP sources: [src/Models/SiteSettings.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/src/Models/SiteSettings.php) · [src/Settings/SiteSettings.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/src/Settings/SiteSettings.php) · [src/SettingsServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/src/SettingsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2022_12_14_083707_create_settings_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/database/migrations/2022_12_14_083707_create_settings_table.php)
- [database/migrations/2026_08_01_063100_create_scoped_settings_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/database/migrations/2026_08_01_063100_create_scoped_settings_table.php)
- [database/settings/2025_12_10_102854_create_site_settings.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/database/settings/2025_12_10_102854_create_site_settings.php)
- [database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **6**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/tests/.gitkeep)
- [tests/Feature/SiteSettingsActiveThemeTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/tests/Feature/SiteSettingsActiveThemeTest.php)
- [tests/Feature/SiteSettingsDefaultsTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/tests/Feature/SiteSettingsDefaultsTest.php)
- [tests/Feature/SiteSettingsTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/tests/Feature/SiteSettingsTest.php)
- [tests/Pest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 5

Representative: real-estate-laravel, `settings`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/settings` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `settings` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Settings\\SettingsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/composer.json) · [module.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/module.json).

**Declared capabilities:** foundation.settings

**Declared features:** Typed application, Organization, Team/site, User settings with validation and deterministic cache invalidation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-settings` | `^3.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Settings\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/SettingDefinition.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/src/Contracts/SettingDefinition.php) | `public function key(): string`<br>`public function validate(mixed $value): bool`<br>`public function secret(): bool` |
| [src/Services/ScopedSettings.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/src/Services/ScopedSettings.php) | `public function put(SettingDefinition $definition, string $scopeType, string $scopeId, mixed $value): void`<br>`public function resolve(string $key, array $scopes, mixed $fallback = null): mixed` |

Other non-legacy PHP sources: [src/Settings/SiteSettings.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/src/Settings/SiteSettings.php) · [src/SettingsServiceProvider.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/src/SettingsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2022_12_14_083707_create_settings_table.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/database/migrations/2022_12_14_083707_create_settings_table.php)
- [database/migrations/2026_08_01_063100_create_scoped_settings_table.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/database/migrations/2026_08_01_063100_create_scoped_settings_table.php)
- [database/settings/2025_12_10_102854_create_site_settings.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/database/settings/2025_12_10_102854_create_site_settings.php)
- [database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/database/settings/2026_07_01_000000_add_active_theme_to_site_settings.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **6**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/tests/.gitkeep)
- [tests/Feature/SiteSettingsActiveThemeTest.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/tests/Feature/SiteSettingsActiveThemeTest.php)
- [tests/Feature/SiteSettingsDefaultsTest.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/tests/Feature/SiteSettingsDefaultsTest.php)
- [tests/Feature/SiteSettingsTest.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/tests/Feature/SiteSettingsTest.php)
- [tests/Pest.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
