# Localization Core React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#localization-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-localization-core-react-native
**Matching core package:** module-real-estate-localization-core ([implementation](../core/localization-core.md))
**Matching API package:** module-real-estate-localization-core-api ([contract](../api/localization-core.md))

## Implementation plan

This adapter presents Localization Core for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Localization Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/localization-core.md), and [API module](../api/localization-core.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `localization-core`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/localization-core.md)) |
| Capability React Native module skeleton | [`module-localization-core-react-native`](https://github.com/liberusoftware/module-localization-core-react-native) (`@liberusoftware/module-localization-core-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Locale negotiation** | Progressive mobile list/detail/sheet flow for `locale negotiation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Translations** | Progressive mobile list/detail/sheet flow for `translations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Pluralization** | Progressive mobile list/detail/sheet flow for `pluralization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **RTL direction** | Progressive mobile list/detail/sheet flow for `rtl direction` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Timezone** | Progressive mobile list/detail/sheet flow for `timezone` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Localized formatting** | Progressive mobile list/detail/sheet flow for `localized formatting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed API controller | Handler signatures |
| --- | --- |
| [StatusController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/localization-core-api/src/Http/Controllers/StatusController.php) | `public function __invoke(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/localization-core-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/localization-core-api/routes/api.php)

```php
Route::prefix('api/v1/localization-core')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('localization-core-api.status');
```
<!-- layer-implementation-plan:end -->
