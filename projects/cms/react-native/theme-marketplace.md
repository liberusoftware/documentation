# Theme Marketplace React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#theme-marketplace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-theme-marketplace-react-native
**Matching core package:** module-cms-theme-marketplace ([implementation](../core/theme-marketplace.md))
**Matching API package:** module-cms-theme-marketplace-api ([contract](../api/theme-marketplace.md))

## Implementation plan

This adapter presents Theme Marketplace for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Theme Marketplace API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/theme-marketplace.md), and [API module](../api/theme-marketplace.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `theme-marketplace`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/theme-marketplace.md)) |
| Capability React Native module skeleton | [`module-cms-theme-marketplace-react-native`](https://github.com/liberusoftware/module-cms-theme-marketplace-react-native) (`@liberusoftware/module-cms-theme-marketplace-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Theme manifests** | Progressive mobile list/detail/sheet flow for `theme manifests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Compatibility** | Progressive mobile list/detail/sheet flow for `compatibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Previews** | Progressive mobile list/detail/sheet flow for `previews` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Licenses** | Progressive mobile list/detail/sheet flow for `licenses` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Child themes** | Progressive mobile list/detail/sheet flow for `child themes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Installation** | Progressive mobile list/detail/sheet flow for `installation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Updates** | Progressive mobile list/detail/sheet flow for `updates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Security review** | Progressive mobile list/detail/sheet flow for `security review` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Ratings** | Progressive mobile list/detail/sheet flow for `ratings` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ThemeMarketplaceQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Queries/ThemeMarketplaceQuery.php) | `public function catalog(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key, ?string $version = null): ?MarketplaceTheme`<br>`public function installation(string $siteKey, string $themeKey): ?ThemeInstallation` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeMarketplaceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Services/ThemeMarketplaceService.php) | `public function publish(array $manifest, ?int $teamId = null): MarketplaceTheme`<br>`public function reviewSecurity(MarketplaceTheme $theme, string $status): MarketplaceTheme`<br>`public function compatible(MarketplaceTheme $theme, string $cmsVersion, array $features = []): bool`<br>`public function install(MarketplaceTheme $theme, string $siteKey, string $cmsVersion, array $features = [], ?int $teamId = null): ThemeInstallation`<br>`public function update(ThemeInstallation $installation, MarketplaceTheme $theme, string $cmsVersion, array $features = []): ThemeInstallation`<br>`public function rate(MarketplaceTheme $theme, string $reviewerType, int\|string $reviewerId, int $rating, ?string $review = null, ?int $teamId = null): ThemeRating`<br>`public function ratingSummary(MarketplaceTheme $theme): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MarketplaceTheme.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/MarketplaceTheme.php) | `key`, `name`, `version`, `author`, `description`, `manifest`, `compatibility`, `preview_url`, `license`, `parent_key`, `status`, `security_status`, `team_id` |
| [ThemeInstallation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/ThemeInstallation.php) | `theme_id`, `site_key`, `installed_version`, `status`, `installed_at`, `updated_at_version`, `team_id` |
| [ThemeRating.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/ThemeRating.php) | `theme_id`, `reviewer_type`, `reviewer_id`, `rating`, `review`, `team_id` |
<!-- layer-implementation-plan:end -->
