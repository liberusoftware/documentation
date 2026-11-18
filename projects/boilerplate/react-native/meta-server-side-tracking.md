# Meta Server-Side Tracking domain packages React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#meta-server-side-tracking). No dedicated package name match was found for this layer in the scanned module manifests. This retained spelling maps to `analytics-meta`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-meta-server-side-tracking-react-native
**Matching core package:** module-meta-server-side-tracking ([implementation](../core/meta-server-side-tracking.md))
**Matching API package:** module-meta-server-side-tracking-api ([contract](../api/meta-server-side-tracking.md))

## Implementation plan

This adapter presents Meta Server-Side Tracking domain packages for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Meta Server-Side Tracking domain packages API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/meta-server-side-tracking.md), and [API module](../api/meta-server-side-tracking.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `analytics-meta`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/meta-server-side-tracking.md)) |
| Capability React Native module skeleton | [`module-analytics-meta-react-native`](https://github.com/liberusoftware/module-analytics-meta-react-native) (`@liberusoftware/module-analytics-meta-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Meta server-side event mapping** | Progressive mobile list/detail/sheet flow for `meta server-side event mapping` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deduplication** | Progressive mobile list/detail/sheet flow for `deduplication` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Consent** | Progressive mobile list/detail/sheet flow for `consent` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Hashing** | Progressive mobile list/detail/sheet flow for `hashing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery** | Progressive mobile list/detail/sheet flow for `delivery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Diagnostics** | Progressive mobile list/detail/sheet flow for `diagnostics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MetaTransport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-meta/src/Contracts/MetaTransport.php) | `public function send(array $payload): array` |

**Observed route declarations:**

[modules/analytics-meta-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-meta-api/routes/api.php)

```php
Route::prefix('api/v1/analytics-meta')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('analytics-meta-api.status');
```
<!-- layer-implementation-plan:end -->
