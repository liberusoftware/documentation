# Profiles React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#profiles). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-profiles-react-native
**Matching core package:** module-social-network-profiles ([implementation](../core/profiles.md))
**Matching API package:** module-social-network-profiles-api ([contract](../api/profiles.md))

## Implementation plan

This adapter presents Profiles for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Profiles API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/profiles.md), and [API module](../api/profiles.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `profiles`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/profiles.md)) |
| Capability React Native module skeleton | [`module-profiles-react-native`](https://github.com/liberusoftware/module-profiles-react-native) (`@liberusoftware/module-profiles-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Handles** | Progressive mobile list/detail/sheet flow for `handles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bios** | Progressive mobile list/detail/sheet flow for `bios` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attributes** | Progressive mobile list/detail/sheet flow for `attributes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Avatars** | Progressive mobile list/detail/sheet flow for `avatars` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Verification** | Progressive mobile list/detail/sheet flow for `verification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Visibility** | Progressive mobile list/detail/sheet flow for `visibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Blocking** | Progressive mobile list/detail/sheet flow for `blocking` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Profile lifecycle** | Progressive mobile list/detail/sheet flow for `profile lifecycle` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [UpdateProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/profiles/src/Actions/UpdateProfile.php) | `public function handle(Model $profile, ProfileUpdate $update): Model` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProfilesController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles-api/src/Http/Controllers/ProfilesController.php) | `public function me(Request $request, GetProfile $get): JsonResponse`<br>`public function show(string $profile, GetProfile $get): JsonResponse`<br>`public function update(Request $request, GetProfile $get, UpdateProfile $update): JsonResponse`<br>`public function block(string $profile, Request $request, GetProfile $get, BlockProfile $block): JsonResponse`<br>`public function unblock(string $profile, Request $request, GetProfile $get, UnblockProfile $unblock): JsonResponse`<br>`public function lifecycle(Request $request, GetProfile $get, UpdateLifecycleState $update): JsonResponse`<br>`public function verification(string $profile, Request $request, GetProfile $get, UpdateVerificationStatus $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-profiles-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/profiles')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.profiles.api.')->group(function (): void {
Route::get('/me', [ProfilesController::class, 'me'])->name('me');
Route::patch('/me', [ProfilesController::class, 'update'])->name('update');
Route::post('/me/blocks/{profile}', [ProfilesController::class, 'block'])->name('block');
Route::delete('/me/blocks/{profile}', [ProfilesController::class, 'unblock'])->name('unblock');
Route::patch('/me/lifecycle', [ProfilesController::class, 'lifecycle'])->name('lifecycle');
Route::patch('/{profile}/verification', [ProfilesController::class, 'verification'])->name('verification');
Route::get('/{profile}', [ProfilesController::class, 'show'])->name('show');
```
<!-- layer-implementation-plan:end -->
