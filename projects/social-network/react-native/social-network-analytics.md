# Social Network Analytics React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-analytics-react-native
**Matching core package:** module-social-network-social-network-analytics ([implementation](../core/social-network-analytics.md))
**Matching API package:** module-social-network-social-network-analytics-api ([contract](../api/social-network-analytics.md))

## Implementation plan

This adapter presents Social Network Analytics for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Analytics API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-analytics.md), and [API module](../api/social-network-analytics.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-analytics`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-analytics.md)) |
| Capability React Native module skeleton | [`module-social-network-analytics-react-native`](https://github.com/liberusoftware/module-social-network-analytics-react-native) (`@liberusoftware/module-social-network-analytics-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Growth** | Progressive mobile list/detail/sheet flow for `growth` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Engagement** | Progressive mobile list/detail/sheet flow for `engagement` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Retention** | Progressive mobile list/detail/sheet flow for `retention` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Health** | Progressive mobile list/detail/sheet flow for `health` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Moderation** | Progressive mobile list/detail/sheet flow for `moderation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery** | Progressive mobile list/detail/sheet flow for `delivery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Privacy-governed insights** | Progressive mobile list/detail/sheet flow for `privacy-governed insights` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BuildSnapshot.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/BuildSnapshot.php) | `public function __construct( private AnalyticsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(object $actor, string $metric, string $periodStart, string $periodEnd, int $cohortSize, float $value, array $dimensions = []): MetricSnapshot` |
| [GetMetrics.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/GetMetrics.php) | `public function __construct(private AnalyticsAuthorizer $authorizer)`<br>`public function handle(object $actor, string $metric, int $limit = 30): Collection` |
| [RecordMetric.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/RecordMetric.php) | `public function __construct( private AnalyticsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(object $actor, string $name, array $dimensions = [], int $value = 1): AnalyticsEvent` |
| [AnalyticsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Contracts/AnalyticsAuthorizer.php) | `public function view(object $actor, string $metric): void`<br>`public function record(object $actor, string $metric): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Models/AnalyticsEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [MetricSnapshot.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Models/MetricSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AnalyticsController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/src/Http/Controllers/AnalyticsController.php) | `public function show(Request $request, string $metric, GetMetrics $metrics): JsonResponse` |

**Observed route declarations:**

[modules/social-network-analytics-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/analytics')
Route::get('/metrics/{metric}', [AnalyticsController::class, 'show'])->name('social-network.analytics.metrics');
```
<!-- layer-implementation-plan:end -->
