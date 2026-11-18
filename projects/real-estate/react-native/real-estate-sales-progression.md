# Real Estate Sales Progression React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-sales-progression). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-sales-progression-react-native
**Matching core package:** module-real-estate-real-estate-sales-progression ([implementation](../core/real-estate-sales-progression.md))
**Matching API package:** module-real-estate-real-estate-sales-progression-api ([contract](../api/real-estate-sales-progression.md))

## Implementation plan

This adapter presents Real Estate Sales Progression for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Sales Progression API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/real-estate-sales-progression.md), and [API module](../api/real-estate-sales-progression.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `real-estate-sales-progression`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-sales-progression.md)) |
| Capability React Native module skeleton | [`module-real-estate-sales-progression-react-native`](https://github.com/liberusoftware/module-real-estate-sales-progression-react-native) (`@liberusoftware/module-real-estate-sales-progression-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Chain** | Progressive mobile list/detail/sheet flow for `chain` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Milestones** | Progressive mobile list/detail/sheet flow for `milestones` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Memoranda** | Progressive mobile list/detail/sheet flow for `memoranda` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Legal/finance contacts** | Progressive mobile list/detail/sheet flow for `legal/finance contacts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dependencies** | Progressive mobile list/detail/sheet flow for `dependencies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Risks** | Progressive mobile list/detail/sheet flow for `risks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Completion** | Progressive mobile list/detail/sheet flow for `completion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SalesProgressionPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression/src/Policies/SalesProgressionPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function delete(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function forceDelete(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesProgression.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression/src/Models/SalesProgression.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SalesProgressionController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression-api/src/Http/Controllers/SalesProgressionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateSalesProgression $create): JsonResponse`<br>`public function show(Request $request, SalesProgression $salesProgression): JsonResponse`<br>`public function update(Request $request, SalesProgression $salesProgression, UpdateSalesProgression $update): JsonResponse`<br>`public function transition(Request $request, SalesProgression $salesProgression, string $status, TransitionSalesProgression $transition): JsonResponse`<br>`public function updateSection(Request $request, SalesProgression $salesProgression, string $section, UpdateSalesProgressionSection $update): JsonResponse`<br>`public function destroy(Request $request, SalesProgression $salesProgression, DeleteSalesProgression $delete): Response` |

**Observed route declarations:**

[modules/real-estate-sales-progression-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/sales-progression')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [SalesProgressionController::class, 'index']);
Route::post('/', [SalesProgressionController::class, 'store']);
Route::get('/{salesProgression}', [SalesProgressionController::class, 'show']);
Route::post('/{salesProgression}/transition/{status}', [SalesProgressionController::class, 'transition']);
Route::patch('/{salesProgression}/{section}', [SalesProgressionController::class, 'updateSection'])->whereIn('section', ['chain', 'milestones', 'professionals', 'completion_controls']);
Route::delete('/{salesProgression}', [SalesProgressionController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
