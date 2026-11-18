# Static Publishing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#static-publishing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-static-publishing-react-native
**Matching core package:** module-cms-static-publishing ([implementation](../core/static-publishing.md))
**Matching API package:** module-cms-static-publishing-api ([contract](../api/static-publishing.md))

## Implementation plan

This adapter presents Static Publishing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Static Publishing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/static-publishing.md), and [API module](../api/static-publishing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `static-publishing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/static-publishing.md)) |
| Capability React Native module skeleton | [`module-cms-static-publishing-react-native`](https://github.com/liberusoftware/module-cms-static-publishing-react-native) (`@liberusoftware/module-cms-static-publishing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Full/incremental builds** | Progressive mobile list/detail/sheet flow for `full/incremental builds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Route manifests** | Progressive mobile list/detail/sheet flow for `route manifests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cache invalidation** | Progressive mobile list/detail/sheet flow for `cache invalidation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deployment adapters** | Progressive mobile list/detail/sheet flow for `deployment adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Preview builds** | Progressive mobile list/detail/sheet flow for `preview builds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rollback** | Progressive mobile list/detail/sheet flow for `rollback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Build diagnostics** | Progressive mobile list/detail/sheet flow for `build diagnostics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [StaticPublishingQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Queries/StaticPublishingQuery.php) | `public function builds(int $perPage = 15): LengthAwarePaginator`<br>`public function build(int\|string $id): ?StaticBuild` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DeploymentAdapterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Contracts/DeploymentAdapterInterface.php) | `public function key(): string`<br>`public function deploy(StaticBuild $build): array` |
| [StaticPublishingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Services/StaticPublishingService.php) | `public function __construct(private DeploymentAdapterRegistry $deployments)`<br>`public function build(array $routes, ?string $siteKey = null, string $kind = 'full', string $deployment = 'local', ?StaticBuild $parent = null): StaticBuild`<br>`public function invalidate(StaticBuild $build, string $path, string $reason = 'content-changed'): StaticInvalidation`<br>`public function rollback(StaticBuild $build): StaticBuild`<br>`public function diagnostics(StaticBuild $build): array`<br>`public function deploy(StaticBuild $build, string $adapter): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [StaticBuild.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Models/StaticBuild.php) | `site_key`, `state`, `kind`, `deployment`, `manifest`, `diagnostics`, `parent_build_id`, `checksum`, `started_at`, `finished_at`, `team_id` |
| [StaticInvalidation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Models/StaticInvalidation.php) | `build_id`, `path`, `reason`, `created_at` |
<!-- layer-implementation-plan:end -->
