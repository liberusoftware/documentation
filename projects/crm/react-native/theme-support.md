# Theme Support React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#theme-support). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-theme-support-react-native
**Matching core package:** module-crm-theme-support ([implementation](../core/theme-support.md))
**Matching API package:** module-crm-theme-support-api ([contract](../api/theme-support.md))

## Implementation plan

This adapter presents Theme Support for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Theme Support API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/theme-support.md), and [API module](../api/theme-support.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `theme-support`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/theme-support.md)) |
| Capability React Native module skeleton | [`module-theme-support-react-native`](https://github.com/liberusoftware/module-theme-support-react-native) (`@liberusoftware/module-theme-support-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Theme discovery** | Progressive mobile list/detail/sheet flow for `theme discovery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **View overrides** | Progressive mobile list/detail/sheet flow for `view overrides` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Safe asset directives** | Progressive mobile list/detail/sheet flow for `safe asset directives` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Preferences** | Progressive mobile list/detail/sheet flow for `preferences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Panel palettes** | Progressive mobile list/detail/sheet flow for `panel palettes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeManager.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Services/ThemeManager.php) | `public function __construct(?string $themesPath = null)`<br>`public function setTheme(string $theme): void`<br>`public function persistTheme(string $theme): void`<br>`public function selectForSurface(string $surface, ?string $site = null, ?string $tenant = null): string`<br>`public function getActiveTheme(): string`<br>`public function getSiteTheme(): string`<br>`public function getThemes(): array`<br>`public function providers(): array`<br>`public function themeExists(string $theme): bool`<br>`public function themeIsCompatible(string $theme): bool`<br>`public function getThemePath(?string $theme = null): string`<br>`public function getThemeViewsPath(?string $theme = null): string`<br>`public function getThemeAssetPath(string $type, ?string $theme = null): ?string`<br>`public function inheritanceChain(?string $theme = null): array`<br>`public function registerThemePaths(): void`<br>`public function getThemeCss(?string $theme = null): ?string`<br>`public function getThemeJs(?string $theme = null): ?string`<br>`public function activeEntries(): array`<br>`public function assetUrl(string $path, ?string $theme = null): string`<br>`public function activeCssEntry(): string`<br>`public function viteHasAsset(string $path): bool`<br>`public function getThemeConfig(?string $theme = null): array`<br>`public function primaryColor(?string $theme = null): string`<br>`public function clearCache(): void`<br>`public function hasCustomLayout(string $layout, ?string $theme = null): bool`<br>`public function getLayout(string $layout, ?string $theme = null): string` |
<!-- layer-implementation-plan:end -->
