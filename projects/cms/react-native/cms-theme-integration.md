# Cms Theme Integration React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-theme-integration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-theme-integration-react-native
**Matching core package:** module-cms-cms-theme-integration ([implementation](../core/cms-theme-integration.md))
**Matching API package:** module-cms-cms-theme-integration-api ([contract](../api/cms-theme-integration.md))

## Implementation plan

This adapter presents Cms Theme Integration for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Theme Integration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cms-theme-integration.md), and [API module](../api/cms-theme-integration.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cms-theme-integration`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-theme-integration.md)) |
| Capability React Native module skeleton | [`module-cms-theme-integration-react-native`](https://github.com/liberusoftware/module-cms-theme-integration-react-native) (`@liberusoftware/module-cms-theme-integration-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Theme selection by site/channel** | Progressive mobile list/detail/sheet flow for `theme selection by site/channel` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Regions** | Progressive mobile list/detail/sheet flow for `regions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **View contracts** | Progressive mobile list/detail/sheet flow for `view contracts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Component registry** | Progressive mobile list/detail/sheet flow for `component registry` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Inheritance** | Progressive mobile list/detail/sheet flow for `inheritance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Preview** | Progressive mobile list/detail/sheet flow for `preview` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Safe fallback** | Progressive mobile list/detail/sheet flow for `safe fallback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ThemeIntegrationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Queries/ThemeIntegrationQuery.php) | `public function __construct(private TenantContextInterface $tenant)`<br>`public function bindings(int $perPage = 15, ?int $teamId = null): LengthAwarePaginator`<br>`public function binding(string $siteKey, ?string $channelKey = null, ?int $teamId = null): ?ThemeBinding`<br>`public function bindingById(int\|string $id, ?int $teamId = null): ?ThemeBinding`<br>`public function components(string $themeKey, ?string $region = null, ?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeIntegrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Services/ThemeIntegrationService.php) | `public function __construct(private ThemeIntegrationQuery $query)`<br>`public function bind(string $siteKey, ?string $channelKey, string $themeKey, string $fallbackThemeKey = 'default', ?int $teamId = null): ThemeBinding`<br>`public function updateBinding(ThemeBinding $binding, array $attributes): ThemeBinding`<br>`public function removeBinding(ThemeBinding $binding): void`<br>`public function select(?string $siteKey, ?string $channelKey = null, ?int $teamId = null): ?ThemeBinding`<br>`public function effectiveTheme(?string $siteKey, ?string $channelKey = null, ?int $teamId = null): string`<br>`public function registerComponent(string $themeKey, string $region, string $componentKey, array $viewContract = [], array $configuration = [], ?int $teamId = null): ThemeComponent`<br>`public function components(string $themeKey, ?string $region = null, ?int $teamId = null): array`<br>`public function previewToken(ThemeBinding $binding): string`<br>`public function preview(ThemeBinding $binding, string $token): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ThemeBinding.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Models/ThemeBinding.php) | `site_key`, `channel_key`, `theme_key`, `fallback_theme_key`, `preview_token`, `preview_expires_at`, `active`, `team_id` |
| [ThemeComponent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Models/ThemeComponent.php) | `theme_key`, `region`, `component_key`, `view_contract`, `configuration`, `team_id` |
<!-- layer-implementation-plan:end -->
