# liberusoftware/theme-support: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Theme discovery and host presentation support for Liberu applications.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/composer.json) | `39a49babafc0` | [Variant 5](#variant-5) | 5 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/composer.json) | `68e5f07a6704` | [Variant 2](#variant-2) | 5 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 5 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/theme-support/composer.json) | `3ade34046c3d` | [Variant 2](#variant-2) | 5 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/theme-support/composer.json) | `790fdffebd3a` | [Variant 2](#variant-2) | 5 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/theme-support/composer.json) | `1797f25d705f` | [Variant 2](#variant-2) | 5 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/composer.json) | `63aad94e94c0` | [Variant 4](#variant-4) | 5 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/theme-support/composer.json) | `b12a8c841c6a` | [Variant 2](#variant-2) | 5 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/theme-support/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 5 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/composer.json) | `c267d625e264` | [Variant 3](#variant-3) | 5 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/theme-support/composer.json) | `178d8015b601` | [Variant 2](#variant-2) | 5 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/theme-support/composer.json) | `08bbc484b50f` | [Variant 3](#variant-3) | 5 |

Physical source locations: **12**. Reference variants: **5**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `theme-support`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/theme-support` |
| Composer version field | `1.4.2` |
| Package type | `liberu-module` |
| Module manifest name | `theme-support` |
| Module version field | `1.4.2` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Theme\\Providers\\ThemeServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/module.json).

**Declared capabilities:** foundation.theme-support

**Declared features:** Theme discovery, View overrides, Safe asset directives, Preferences, Panel palettes

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/settings` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Theme\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/settings": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Services/ThemeManager.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Services/ThemeManager.php) | `public function __construct(?string $themesPath = null)`<br>`public function setTheme(string $theme): void`<br>`public function persistTheme(string $theme): void`<br>`public function selectForSurface(string $surface, ?string $site = null, ?string $tenant = null): string`<br>`public function getActiveTheme(): string`<br>`public function getSiteTheme(): string`<br>`public function getThemes(): array`<br>`public function providers(): array`<br>`public function themeExists(string $theme): bool`<br>`public function themeIsCompatible(string $theme): bool`<br>`public function getThemePath(?string $theme = null): string`<br>`public function getThemeViewsPath(?string $theme = null): string`<br>`public function getThemeAssetPath(string $type, ?string $theme = null): ?string`<br>`public function inheritanceChain(?string $theme = null): array`<br>`public function registerThemePaths(): void`<br>`public function getThemeCss(?string $theme = null): ?string`<br>`public function getThemeJs(?string $theme = null): ?string`<br>`public function activeEntries(): array`<br>`public function assetUrl(string $path, ?string $theme = null): string`<br>`public function activeCssEntry(): string`<br>`public function viteHasAsset(string $path): bool`<br>`public function getThemeConfig(?string $theme = null): array`<br>`public function primaryColor(?string $theme = null): string`<br>`public function clearCache(): void`<br>`public function hasCustomLayout(string $layout, ?string $theme = null): bool`<br>`public function getLayout(string $layout, ?string $theme = null): string` |
| [src/Support/theme_helpers.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Support/theme_helpers.php) | `function theme(): ThemeManager`<br>`function active_theme(): string`<br>`function theme_asset(string $path, ?string $theme = null): string`<br>`function theme_path(?string $theme = null): string`<br>`function theme_views_path(?string $theme = null): string`<br>`function set_theme(string $themeName): void`<br>`function theme_layout(string $layout): string` |

Other non-legacy PHP sources: [src/Cache/ThemeCache.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Cache/ThemeCache.php) · [src/Console/ThemeCacheCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Console/ThemeCacheCommand.php) · [src/Console/ThemeClearCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Console/ThemeClearCommand.php) · [src/Console/ThemeValidateCommand.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Console/ThemeValidateCommand.php) · [src/Discovery/ThemeDiscovery.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Discovery/ThemeDiscovery.php) · [src/Exceptions/InvalidTheme.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Exceptions/InvalidTheme.php) · [src/Manifests/ThemeManifest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Manifests/ThemeManifest.php) · [src/Providers/ThemeServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Providers/ThemeServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/tests/.gitkeep)
- [tests/Helpers.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/tests/Helpers.php)
- [tests/Pest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/tests/Pest.php)
- [tests/Unit/ThemeManagerCoverageBranchesTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/tests/Unit/ThemeManagerCoverageBranchesTest.php)
- [tests/Unit/ThemeManifestCoverageTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/tests/Unit/ThemeManifestCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: automation-laravel, `theme-support`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/theme-support` |
| Composer version field | `1.4.2` |
| Package type | `liberu-module` |
| Module manifest name | `theme-support` |
| Module version field | `1.4.2` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Theme\\Providers\\ThemeServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/composer.json) · [module.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/module.json).

**Declared capabilities:** foundation.theme-support

**Declared features:** Theme discovery, View overrides, Safe asset directives, Preferences, Panel palettes

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/settings` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Theme\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/settings": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Services/ThemeManager.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Services/ThemeManager.php) | `public function __construct(?string $themesPath = null)`<br>`public function setTheme(string $theme): void`<br>`public function persistTheme(string $theme): void`<br>`public function selectForSurface(string $surface, ?string $site = null, ?string $tenant = null): string`<br>`public function getActiveTheme(): string`<br>`public function getSiteTheme(): string`<br>`public function getThemes(): array`<br>`public function providers(): array`<br>`public function themeExists(string $theme): bool`<br>`public function themeIsCompatible(string $theme): bool`<br>`public function getThemePath(?string $theme = null): string`<br>`public function getThemeViewsPath(?string $theme = null): string`<br>`public function getThemeAssetPath(string $type, ?string $theme = null): ?string`<br>`public function inheritanceChain(?string $theme = null): array`<br>`public function registerThemePaths(): void`<br>`public function getThemeCss(?string $theme = null): ?string`<br>`public function getThemeJs(?string $theme = null): ?string`<br>`public function activeEntries(): array`<br>`public function assetUrl(string $path, ?string $theme = null): string`<br>`public function activeCssEntry(): string`<br>`public function viteHasAsset(string $path): bool`<br>`public function getThemeConfig(?string $theme = null): array`<br>`public function primaryColor(?string $theme = null): string`<br>`public function clearCache(): void`<br>`public function hasCustomLayout(string $layout, ?string $theme = null): bool`<br>`public function getLayout(string $layout, ?string $theme = null): string` |
| [src/Support/theme_helpers.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Support/theme_helpers.php) | `function theme(): ThemeManager`<br>`function active_theme(): string`<br>`function theme_asset(string $path, ?string $theme = null): string`<br>`function theme_path(?string $theme = null): string`<br>`function theme_views_path(?string $theme = null): string`<br>`function set_theme(string $themeName): void`<br>`function theme_layout(string $layout): string` |

Other non-legacy PHP sources: [src/Cache/ThemeCache.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Cache/ThemeCache.php) · [src/Console/ThemeCacheCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Console/ThemeCacheCommand.php) · [src/Console/ThemeClearCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Console/ThemeClearCommand.php) · [src/Console/ThemeValidateCommand.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Console/ThemeValidateCommand.php) · [src/Discovery/ThemeDiscovery.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Discovery/ThemeDiscovery.php) · [src/Exceptions/InvalidTheme.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Exceptions/InvalidTheme.php) · [src/Manifests/ThemeManifest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Manifests/ThemeManifest.php) · [src/Providers/ThemeServiceProvider.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/src/Providers/ThemeServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/tests/.gitkeep)
- [tests/Helpers.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/tests/Helpers.php)
- [tests/Pest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/tests/Pest.php)
- [tests/Unit/ThemeManagerCoverageBranchesTest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/tests/Unit/ThemeManagerCoverageBranchesTest.php)
- [tests/Unit/ThemeManifestCoverageTest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support/tests/Unit/ThemeManifestCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: maintenance-laravel, `theme-support`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/theme-support` |
| Composer version field | `1.4.3` |
| Package type | `liberu-module` |
| Module manifest name | `theme-support` |
| Module version field | `1.4.3` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Theme\\Providers\\ThemeServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/composer.json) · [module.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/module.json).

**Declared capabilities:** foundation.theme-support

**Declared features:** Theme discovery, View overrides, Safe asset directives, Preferences, Panel palettes

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/settings` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Theme\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/settings": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Services/ThemeManager.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Services/ThemeManager.php) | `public function __construct(?string $themesPath = null)`<br>`public function setTheme(string $theme): void`<br>`public function persistTheme(string $theme): void`<br>`public function selectForSurface(string $surface, ?string $site = null, ?string $tenant = null): string`<br>`public function getActiveTheme(): string`<br>`public function getSiteTheme(): string`<br>`public function getThemes(): array`<br>`public function providers(): array`<br>`public function themeExists(string $theme): bool`<br>`public function themeIsCompatible(string $theme): bool`<br>`public function getThemePath(?string $theme = null): string`<br>`public function getThemeViewsPath(?string $theme = null): string`<br>`public function getThemeAssetPath(string $type, ?string $theme = null): ?string`<br>`public function inheritanceChain(?string $theme = null): array`<br>`public function registerThemePaths(): void`<br>`public function getThemeCss(?string $theme = null): ?string`<br>`public function getThemeJs(?string $theme = null): ?string`<br>`public function activeEntries(): array`<br>`public function assetUrl(string $path, ?string $theme = null): string`<br>`public function activeCssEntry(): string`<br>`public function viteHasAsset(string $path): bool`<br>`public function getThemeConfig(?string $theme = null): array`<br>`public function primaryColor(?string $theme = null): string`<br>`public function clearCache(): void`<br>`public function hasCustomLayout(string $layout, ?string $theme = null): bool`<br>`public function getLayout(string $layout, ?string $theme = null): string` |
| [src/Support/theme_helpers.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Support/theme_helpers.php) | `function theme(): ThemeManager`<br>`function active_theme(): string`<br>`function theme_asset(string $path, ?string $theme = null): string`<br>`function theme_path(?string $theme = null): string`<br>`function theme_views_path(?string $theme = null): string`<br>`function set_theme(string $themeName): void`<br>`function theme_layout(string $layout): string` |

Other non-legacy PHP sources: [src/Cache/ThemeCache.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Cache/ThemeCache.php) · [src/Console/ThemeCacheCommand.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Console/ThemeCacheCommand.php) · [src/Console/ThemeClearCommand.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Console/ThemeClearCommand.php) · [src/Console/ThemeValidateCommand.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Console/ThemeValidateCommand.php) · [src/Discovery/ThemeDiscovery.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Discovery/ThemeDiscovery.php) · [src/Exceptions/InvalidTheme.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Exceptions/InvalidTheme.php) · [src/Manifests/ThemeManifest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Manifests/ThemeManifest.php) · [src/Providers/ThemeServiceProvider.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/src/Providers/ThemeServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/tests/.gitkeep)
- [tests/Helpers.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/tests/Helpers.php)
- [tests/Pest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/tests/Pest.php)
- [tests/Unit/ThemeManagerCoverageBranchesTest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/tests/Unit/ThemeManagerCoverageBranchesTest.php)
- [tests/Unit/ThemeManifestCoverageTest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support/tests/Unit/ThemeManifestCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 4

Representative: crm-laravel, `theme-support`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/theme-support` |
| Composer version field | `1.5.0` |
| Package type | `liberu-module` |
| Module manifest name | `theme-support` |
| Module version field | `1.4.3` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Theme\\Providers\\ThemeServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/module.json).

**Declared capabilities:** foundation.theme-support

**Declared features:** Theme discovery, View overrides, Safe asset directives, Preferences, Panel palettes

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/settings` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Theme\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/settings": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Services/ThemeManager.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Services/ThemeManager.php) | `public function __construct(?string $themesPath = null)`<br>`public function setTheme(string $theme): void`<br>`public function persistTheme(string $theme): void`<br>`public function selectForSurface(string $surface, ?string $site = null, ?string $tenant = null): string`<br>`public function getActiveTheme(): string`<br>`public function getSiteTheme(): string`<br>`public function getThemes(): array`<br>`public function providers(): array`<br>`public function themeExists(string $theme): bool`<br>`public function themeIsCompatible(string $theme): bool`<br>`public function getThemePath(?string $theme = null): string`<br>`public function getThemeViewsPath(?string $theme = null): string`<br>`public function getThemeAssetPath(string $type, ?string $theme = null): ?string`<br>`public function inheritanceChain(?string $theme = null): array`<br>`public function registerThemePaths(): void`<br>`public function getThemeCss(?string $theme = null): ?string`<br>`public function getThemeJs(?string $theme = null): ?string`<br>`public function activeEntries(): array`<br>`public function assetUrl(string $path, ?string $theme = null): string`<br>`public function activeCssEntry(): string`<br>`public function viteHasAsset(string $path): bool`<br>`public function getThemeConfig(?string $theme = null): array`<br>`public function primaryColor(?string $theme = null): string`<br>`public function clearCache(): void`<br>`public function hasCustomLayout(string $layout, ?string $theme = null): bool`<br>`public function getLayout(string $layout, ?string $theme = null): string` |
| [src/Support/theme_helpers.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Support/theme_helpers.php) | `function theme(): ThemeManager`<br>`function active_theme(): string`<br>`function theme_asset(string $path, ?string $theme = null): string`<br>`function theme_path(?string $theme = null): string`<br>`function theme_views_path(?string $theme = null): string`<br>`function set_theme(string $themeName): void`<br>`function theme_layout(string $layout): string` |

Other non-legacy PHP sources: [src/Cache/ThemeCache.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Cache/ThemeCache.php) · [src/Console/ThemeCacheCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Console/ThemeCacheCommand.php) · [src/Console/ThemeClearCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Console/ThemeClearCommand.php) · [src/Console/ThemeValidateCommand.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Console/ThemeValidateCommand.php) · [src/Discovery/ThemeDiscovery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Discovery/ThemeDiscovery.php) · [src/Exceptions/InvalidTheme.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Exceptions/InvalidTheme.php) · [src/Manifests/ThemeManifest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Manifests/ThemeManifest.php) · [src/Providers/ThemeServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/src/Providers/ThemeServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/tests/.gitkeep)
- [tests/Helpers.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/tests/Helpers.php)
- [tests/Pest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/tests/Pest.php)
- [tests/Unit/ThemeManagerCoverageBranchesTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/tests/Unit/ThemeManagerCoverageBranchesTest.php)
- [tests/Unit/ThemeManifestCoverageTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support/tests/Unit/ThemeManifestCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 5

Representative: accounting-erp-laravel, `theme-support`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/theme-support` |
| Composer version field | `1.4.2` |
| Package type | `liberu-module` |
| Module manifest name | `theme-support` |
| Module version field | `1.4.3` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Theme\\Providers\\ThemeServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/module.json).

**Declared capabilities:** foundation.theme-support

**Declared features:** Theme discovery, View overrides, Safe asset directives, Preferences, Panel palettes

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/settings` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Theme\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/settings": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Services/ThemeManager.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Services/ThemeManager.php) | `public function __construct(?string $themesPath = null)`<br>`public function setTheme(string $theme): void`<br>`public function persistTheme(string $theme): void`<br>`public function selectForSurface(string $surface, ?string $site = null, ?string $tenant = null): string`<br>`public function getActiveTheme(): string`<br>`public function getSiteTheme(): string`<br>`public function getThemes(): array`<br>`public function providers(): array`<br>`public function themeExists(string $theme): bool`<br>`public function themeIsCompatible(string $theme): bool`<br>`public function getThemePath(?string $theme = null): string`<br>`public function getThemeViewsPath(?string $theme = null): string`<br>`public function getThemeAssetPath(string $type, ?string $theme = null): ?string`<br>`public function inheritanceChain(?string $theme = null): array`<br>`public function registerThemePaths(): void`<br>`public function getThemeCss(?string $theme = null): ?string`<br>`public function getThemeJs(?string $theme = null): ?string`<br>`public function activeEntries(): array`<br>`public function assetUrl(string $path, ?string $theme = null): string`<br>`public function activeCssEntry(): string`<br>`public function viteHasAsset(string $path): bool`<br>`public function getThemeConfig(?string $theme = null): array`<br>`public function primaryColor(?string $theme = null): string`<br>`public function clearCache(): void`<br>`public function hasCustomLayout(string $layout, ?string $theme = null): bool`<br>`public function getLayout(string $layout, ?string $theme = null): string` |
| [src/Support/theme_helpers.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Support/theme_helpers.php) | `function theme(): ThemeManager`<br>`function active_theme(): string`<br>`function theme_asset(string $path, ?string $theme = null): string`<br>`function theme_path(?string $theme = null): string`<br>`function theme_views_path(?string $theme = null): string`<br>`function set_theme(string $themeName): void`<br>`function theme_layout(string $layout): string` |

Other non-legacy PHP sources: [src/Cache/ThemeCache.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Cache/ThemeCache.php) · [src/Console/ThemeCacheCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Console/ThemeCacheCommand.php) · [src/Console/ThemeClearCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Console/ThemeClearCommand.php) · [src/Console/ThemeValidateCommand.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Console/ThemeValidateCommand.php) · [src/Discovery/ThemeDiscovery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Discovery/ThemeDiscovery.php) · [src/Exceptions/InvalidTheme.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Exceptions/InvalidTheme.php) · [src/Manifests/ThemeManifest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Manifests/ThemeManifest.php) · [src/Providers/ThemeServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/src/Providers/ThemeServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/tests/.gitkeep)
- [tests/Helpers.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/tests/Helpers.php)
- [tests/Pest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/tests/Pest.php)
- [tests/Unit/ThemeManagerCoverageBranchesTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/tests/Unit/ThemeManagerCoverageBranchesTest.php)
- [tests/Unit/ThemeManifestCoverageTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support/tests/Unit/ThemeManifestCoverageTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
