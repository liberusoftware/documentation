# Real Estate Vr Design React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-vr-design). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-vr-design-react-native
**Matching core package:** module-real-estate-real-estate-vr-design ([implementation](../core/real-estate-vr-design.md))
**Matching API package:** module-real-estate-real-estate-vr-design-api ([contract](../api/real-estate-vr-design.md))

## Implementation plan

This adapter presents Real Estate Vr Design for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Vr Design API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/real-estate-vr-design.md), and [API module](../api/real-estate-vr-design.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `real-estate-vr-design`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-vr-design.md)) |
| Capability React Native module skeleton | [`module-real-estate-vr-design-react-native`](https://github.com/liberusoftware/module-real-estate-vr-design-react-native) (`@liberusoftware/module-real-estate-vr-design-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Design styles** | Progressive mobile list/detail/sheet flow for `design styles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Furniture placement** | Progressive mobile list/detail/sheet flow for `furniture placement` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Room layouts** | Progressive mobile list/detail/sheet flow for `room layouts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Materials and lighting** | Progressive mobile list/detail/sheet flow for `materials and lighting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Public templates** | Progressive mobile list/detail/sheet flow for `public templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Thumbnail uploads** | Progressive mobile list/detail/sheet flow for `thumbnail uploads` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **VR exports** | Progressive mobile list/detail/sheet flow for `vr exports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [VrDesign.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-vr-design/src/Models/VrDesign.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [VrDesignController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-vr-design-api/src/Http/Controllers/VrDesignController.php) | `public function styles(VrDesignService $service): JsonResponse`<br>`public function furnitureCategories(VrDesignService $service): JsonResponse`<br>`public function roomTypes(VrDesignService $service): JsonResponse`<br>`public function devices(VrDesignService $service): JsonResponse`<br>`public function templates(Request $request, VrDesignService $service): JsonResponse`<br>`public function indexForProperty(Request $request, VrDesignService $service, int\|string $propertyId): JsonResponse`<br>`public function store(Request $request, VrDesignService $service, int\|string $propertyId): JsonResponse`<br>`public function show(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function update(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function destroy(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function addFurniture(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function removeFurniture(Request $request, VrDesignService $service, int\|string $designId, string $furnitureId): JsonResponse`<br>`public function cloneDesign(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function uploadThumbnail(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function export(Request $request, VrDesignService $service, int\|string $designId): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-vr-design-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-vr-design-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/vr-design')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/styles', [VrDesignController::class, 'styles'])->name('real-estate.vr-design.styles');
Route::get('/furniture-categories', [VrDesignController::class, 'furnitureCategories'])->name('real-estate.vr-design.furniture-categories');
Route::get('/room-types', [VrDesignController::class, 'roomTypes'])->name('real-estate.vr-design.room-types');
Route::get('/devices', [VrDesignController::class, 'devices'])->name('real-estate.vr-design.devices');
Route::get('/templates', [VrDesignController::class, 'templates'])->name('real-estate.vr-design.templates');
Route::get('/properties/{propertyId}/designs', [VrDesignController::class, 'indexForProperty'])->name('real-estate.vr-design.property.index');
Route::post('/properties/{propertyId}/designs', [VrDesignController::class, 'store'])->name('real-estate.vr-design.property.store');
Route::get('/designs/{designId}', [VrDesignController::class, 'show'])->name('real-estate.vr-design.show');
Route::delete('/designs/{designId}', [VrDesignController::class, 'destroy'])->name('real-estate.vr-design.destroy');
Route::post('/designs/{designId}/furniture', [VrDesignController::class, 'addFurniture'])->name('real-estate.vr-design.furniture.add');
Route::delete('/designs/{designId}/furniture/{furnitureId}', [VrDesignController::class, 'removeFurniture'])->name('real-estate.vr-design.furniture.remove');
Route::post('/designs/{designId}/clone', [VrDesignController::class, 'cloneDesign'])->name('real-estate.vr-design.clone');
Route::post('/designs/{designId}/thumbnail', [VrDesignController::class, 'uploadThumbnail'])->name('real-estate.vr-design.thumbnail');
Route::get('/designs/{designId}/export', [VrDesignController::class, 'export'])->name('real-estate.vr-design.export');
```
<!-- layer-implementation-plan:end -->
