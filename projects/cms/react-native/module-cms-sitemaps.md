# Module Cms Sitemaps React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-sitemaps). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-module-cms-sitemaps-react-native
**Matching core package:** module-cms-module-cms-sitemaps ([implementation](../core/module-cms-sitemaps.md))
**Matching API package:** module-cms-module-cms-sitemaps-api ([contract](../api/module-cms-sitemaps.md))

## Implementation plan

This adapter presents Module Cms Sitemaps for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Cms Sitemaps API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-cms-sitemaps.md), and [API module](../api/module-cms-sitemaps.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-cms-sitemaps`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-sitemaps.md)) |
| Capability React Native module skeleton | [`module-cms-sitemaps-react-native`](https://github.com/liberusoftware/module-cms-sitemaps-react-native) (`@liberusoftware/module-cms-sitemaps-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Site/type/locale-aware indexes** | Progressive mobile list/detail/sheet flow for `site/type/locale-aware indexes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Exclusions** | Progressive mobile list/detail/sheet flow for `exclusions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Images/video/news extensions** | Progressive mobile list/detail/sheet flow for `images/video/news extensions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Chunking** | Progressive mobile list/detail/sheet flow for `chunking` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cache** | Progressive mobile list/detail/sheet flow for `cache` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Search-engine notification adapters** | Progressive mobile list/detail/sheet flow for `search-engine notification adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SitemapService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-sitemaps/src/Services/SitemapService.php) | `public function __construct(private readonly TenantContextInterface $tenant)`<br>`public function add(string $url, ?int $siteId = null, string $type = 'web', ?string $locale = null, float $priority = .5, array $extensions = [], ?int $teamId = null): SitemapEntry`<br>`public function exclude(string $url, ?int $siteId = null): int`<br>`public function update(SitemapEntry $entry, array $attributes): SitemapEntry`<br>`public function remove(SitemapEntry $entry): void`<br>`public function entries(?int $siteId = null, ?string $type = null, ?string $locale = null): array`<br>`public function chunks(?int $siteId = null, int $size = 50000, ?string $type = null, ?string $locale = null): array`<br>`public function notify(string $engine, ?int $siteId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SitemapEntry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-sitemaps/src/Models/SitemapEntry.php) | `site_id`, `type`, `locale`, `url`, `last_modified`, `priority`, `change_frequency`, `images`, `video`, `news`, `excluded`, `team_id` |
<!-- layer-implementation-plan:end -->
