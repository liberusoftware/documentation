# Activity Comments React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#activity-comments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-boilerplate-activity-comments-react-native
**Matching core package:** module-boilerplate-activity-comments ([implementation](../core/activity-comments.md))
**Matching API package:** module-boilerplate-activity-comments-api ([contract](../api/activity-comments.md))

## Implementation plan

This adapter presents Activity Comments for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Activity Comments API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/activity-comments.md), and [API module](../api/activity-comments.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `activity-comments`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/activity-comments.md)) |
| Capability React Native module skeleton | [`module-activity-comments-react-native`](https://github.com/liberusoftware/module-activity-comments-react-native) (`@liberusoftware/module-activity-comments-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Activity timelines** | Progressive mobile list/detail/sheet flow for `activity timelines` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Mentions** | Progressive mobile list/detail/sheet flow for `mentions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Subscriptions** | Progressive mobile list/detail/sheet flow for `subscriptions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Internal comments** | Progressive mobile list/detail/sheet flow for `internal comments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attachments** | Progressive mobile list/detail/sheet flow for `attachments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Visibility** | Progressive mobile list/detail/sheet flow for `visibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivityAuthorizer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/activity-comments/src/Contracts/ActivityAuthorizer.php) | `public function allowed(string\|int $actorId, string $subjectType, string\|int $subjectId, string $operation): bool` |

**Observed route declarations:**

[modules/activity-comments-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/activity-comments-api/routes/api.php)

```php
Route::prefix('api/v1/activity-comments')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('activity-comments-api.status');
```
<!-- layer-implementation-plan:end -->
