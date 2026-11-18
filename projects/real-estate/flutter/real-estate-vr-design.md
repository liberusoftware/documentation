# Real Estate Vr Design Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-vr-design). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-vr-design-flutter
**Matching core package:** module-real-estate-real-estate-vr-design ([implementation](../core/real-estate-vr-design.md))
**Matching API package:** module-real-estate-real-estate-vr-design-api ([contract](../api/real-estate-vr-design.md))

## Implementation plan

This adapter presents Real Estate Vr Design for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Vr Design API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/real-estate-vr-design.md), and [API module](../api/real-estate-vr-design.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `real-estate-vr-design`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-vr-design-flutter`](https://github.com/liberusoftware/module-real-estate-vr-design-flutter) (`module_real_estate_vr_design_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-vr-design-dart-mobile`](https://github.com/liberusoftware/module-real-estate-vr-design-dart-mobile) (`module_real_estate_vr_design_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-vr-design-dart-desktop`](https://github.com/liberusoftware/module-real-estate-vr-design-dart-desktop) (`module_real_estate_vr_design_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/real-estate-vr-design.md) · [Core plan](../core/real-estate-vr-design.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Design styles** | Adaptive mobile cards/sheets for `design styles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `design styles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Furniture placement** | Adaptive mobile cards/sheets for `furniture placement` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `furniture placement` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Room layouts** | Adaptive mobile cards/sheets for `room layouts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `room layouts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Materials and lighting** | Adaptive mobile cards/sheets for `materials and lighting` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `materials and lighting` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Public templates** | Adaptive mobile cards/sheets for `public templates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `public templates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Thumbnail uploads** | Adaptive mobile cards/sheets for `thumbnail uploads` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `thumbnail uploads` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **VR exports** | Adaptive mobile cards/sheets for `vr exports` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `vr exports` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
