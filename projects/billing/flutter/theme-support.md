# Theme Support Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#theme-support). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-theme-support-flutter
**Matching core package:** module-billing-theme-support ([implementation](../core/theme-support.md))
**Matching API package:** module-billing-theme-support-api ([contract](../api/theme-support.md))

## Implementation plan

This adapter presents Theme Support for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Theme Support API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/theme-support.md), and [API module](../api/theme-support.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `theme-support`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) | [`module-theme-support-flutter`](https://github.com/liberusoftware/module-theme-support-flutter) (`module_theme_support_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) | [`module-theme-support-dart-mobile`](https://github.com/liberusoftware/module-theme-support-dart-mobile) (`module_theme_support_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) | [`module-theme-support-dart-desktop`](https://github.com/liberusoftware/module-theme-support-dart-desktop) (`module_theme_support_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | [API plan](../api/theme-support.md) · [Core plan](../core/theme-support.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Theme discovery** | Adaptive mobile cards/sheets for `theme discovery` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `theme discovery` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **View overrides** | Adaptive mobile cards/sheets for `view overrides` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `view overrides` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Safe asset directives** | Adaptive mobile cards/sheets for `safe asset directives` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `safe asset directives` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Preferences** | Adaptive mobile cards/sheets for `preferences` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `preferences` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Panel palettes** | Adaptive mobile cards/sheets for `panel palettes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `panel palettes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeManager.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Services/ThemeManager.php) | `public function __construct(?string $themesPath = null)`<br>`public function setTheme(string $theme): void`<br>`public function persistTheme(string $theme): void`<br>`public function selectForSurface(string $surface, ?string $site = null, ?string $tenant = null): string`<br>`public function getActiveTheme(): string`<br>`public function getSiteTheme(): string`<br>`public function getThemes(): array`<br>`public function providers(): array`<br>`public function themeExists(string $theme): bool`<br>`public function themeIsCompatible(string $theme): bool`<br>`public function getThemePath(?string $theme = null): string`<br>`public function getThemeViewsPath(?string $theme = null): string`<br>`public function getThemeAssetPath(string $type, ?string $theme = null): ?string`<br>`public function inheritanceChain(?string $theme = null): array`<br>`public function registerThemePaths(): void`<br>`public function getThemeCss(?string $theme = null): ?string`<br>`public function getThemeJs(?string $theme = null): ?string`<br>`public function activeEntries(): array`<br>`public function assetUrl(string $path, ?string $theme = null): string`<br>`public function activeCssEntry(): string`<br>`public function viteHasAsset(string $path): bool`<br>`public function getThemeConfig(?string $theme = null): array`<br>`public function primaryColor(?string $theme = null): string`<br>`public function clearCache(): void`<br>`public function hasCustomLayout(string $layout, ?string $theme = null): bool`<br>`public function getLayout(string $layout, ?string $theme = null): string` |
<!-- layer-implementation-plan:end -->
