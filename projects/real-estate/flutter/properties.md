# Properties Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#properties). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-properties-flutter
**Matching core package:** module-real-estate-properties ([implementation](../core/properties.md))
**Matching API package:** module-real-estate-properties-api ([contract](../api/properties.md))

## Implementation plan

This adapter presents Properties for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Properties API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/properties.md), and [API module](../api/properties.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `properties`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-properties-flutter`](https://github.com/liberusoftware/module-real-estate-properties-flutter) (`module_real_estate_properties_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-properties-dart-mobile`](https://github.com/liberusoftware/module-real-estate-properties-dart-mobile) (`module_real_estate_properties_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-properties-dart-desktop`](https://github.com/liberusoftware/module-real-estate-properties-dart-desktop) (`module_real_estate_properties_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/properties.md) · [Core plan](../core/properties.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Address/location** | Adaptive mobile cards/sheets for `address/location` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `address/location` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Units** | Adaptive mobile cards/sheets for `units` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `units` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Characteristics** | Adaptive mobile cards/sheets for `characteristics` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `characteristics` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tenure** | Adaptive mobile cards/sheets for `tenure` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tenure` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Utilities** | Adaptive mobile cards/sheets for `utilities` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `utilities` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Features** | Adaptive mobile cards/sheets for `features` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `features` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Status** | Adaptive mobile cards/sheets for `status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **History** | Adaptive mobile cards/sheets for `history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Keys** | Adaptive mobile cards/sheets for `keys` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `keys` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PropertyCategoryPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyCategoryPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function delete(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function forceDelete(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [PropertyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Property $property): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Property $property): bool`<br>`public function delete(AuthUser $authUser, Property $property): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Property $property): bool`<br>`public function forceDelete(AuthUser $authUser, Property $property): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Property $property): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [PropertyTemplatePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyTemplatePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function delete(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function forceDelete(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommunityEvent.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/CommunityEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [Neighborhood.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/Neighborhood.php) | No literal fillable array detected; inspect the model and API schema. |
| [NeighborhoodReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/NeighborhoodReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [Property.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/Property.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyCategory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyCategory.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyFavorite.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyFavorite.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyHistory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyHistory.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyKey.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyKey.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommunityEventController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/CommunityEventController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, CommunityEvent $event): JsonResponse` |
| [PropertyArTourController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyArTourController.php) | `public function config(Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function availability(Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function enable(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function disable(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function updateSettings(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse` |
| [PropertyCategoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyCategoryController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, PropertyCategory $category): JsonResponse`<br>`public function destroy(Request $request, PropertyCategory $category): Response` |
| [PropertyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateProperty $create): JsonResponse`<br>`public function favorite(Request $request, Property $property, TogglePropertyFavorite $toggle): JsonResponse`<br>`public function favorites(Request $request): JsonResponse`<br>`public function removeFavorite(Request $request, Property $property, RemovePropertyFavorite $remove): JsonResponse`<br>`public function similar(Request $request, Property $property): JsonResponse`<br>`public function walkability(Request $request, Property $property, FetchWalkabilityScores $fetch, UpdateProperty $update): JsonResponse`<br>`public function qrCode(Request $request, Property $property, GeneratePropertyQrCode $generate): JsonResponse`<br>`public function share(Request $request, Property $property, SendPropertyToFriend $send): JsonResponse`<br>`public function compare(Request $request): JsonResponse`<br>`public function taxEstimate(Request $request, EstimatePropertyTax $estimate): JsonResponse`<br>`public function show(Request $request, Property $property): JsonResponse`<br>`public function history(Request $request, Property $property): JsonResponse`<br>`public function update(Request $request, Property $property, UpdateProperty $update): JsonResponse`<br>`public function transition(Request $request, Property $property, string $status, TransitionProperty $transition): JsonResponse`<br>`public function unit(Request $request, Property $property, UpsertPropertyUnit $upsert): JsonResponse`<br>`public function key(Request $request, Property $property, RecordPropertyKey $record): JsonResponse`<br>`public function destroy(Request $request, Property $property, DeleteProperty $delete): Response` |
| [PropertyPriceAlertController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyPriceAlertController.php) | `public function index(Request $request, int\|string $property): JsonResponse`<br>`public function store(Request $request, int\|string $property, CreatePriceAlert $create): JsonResponse`<br>`public function update(Request $request, int\|string $alert, UpdatePriceAlert $update): JsonResponse`<br>`public function destroy(Request $request, int\|string $alert, DeletePriceAlert $delete): JsonResponse` |
| [PropertySavedSearchController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertySavedSearchController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, SavePropertySearch $save): JsonResponse`<br>`public function destroy(Request $request, int $savedSearch, DeletePropertySearch $delete): JsonResponse` |
| [PropertyTemplateController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyTemplateController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, PropertyTemplate $template): JsonResponse`<br>`public function destroy(Request $request, PropertyTemplate $template): Response` |
| [PublicPropertyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PublicPropertyController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, Property $property): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-properties-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/routes/api.php)

```php
Route::prefix('api/v1/public/properties')->middleware(['api', 'throttle:api'])->group(function (): void {
Route::get('/', [PublicPropertyController::class, 'index'])->name('public.properties.index');
Route::get('/{property}', [PublicPropertyController::class, 'show'])->name('public.properties.show');
Route::prefix('api/v1/real-estate/properties/{property}/ar-tour')->middleware(['api', 'throttle:api'])->group(function (): void {
Route::get('/config', [PropertyArTourController::class, 'config'])->name('real-estate.properties.ar-tour.config');
Route::get('/availability', [PropertyArTourController::class, 'availability'])->name('real-estate.properties.ar-tour.availability');
Route::prefix('api/v1/real-estate/properties/{property}/ar-tour')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/enable', [PropertyArTourController::class, 'enable'])->name('real-estate.properties.ar-tour.enable');
Route::post('/disable', [PropertyArTourController::class, 'disable'])->name('real-estate.properties.ar-tour.disable');
Route::prefix('api/v1/real-estate/property-saved-searches')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertySavedSearchController::class, 'index'])->name('real-estate.property-saved-searches.index');
Route::post('/', [PropertySavedSearchController::class, 'store'])->name('real-estate.property-saved-searches.store');
Route::delete('/{savedSearch}', [PropertySavedSearchController::class, 'destroy'])->name('real-estate.property-saved-searches.destroy');
Route::prefix('api/v1/real-estate/community-events')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CommunityEventController::class, 'index'])->name('real-estate.community-events.index');
Route::get('/{event}', [CommunityEventController::class, 'show'])->name('real-estate.community-events.show');
Route::prefix('api/v1/real-estate/properties')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertyController::class, 'index'])->name('real-estate.properties.index');
Route::post('/', [PropertyController::class, 'store'])->name('real-estate.properties.store');
Route::get('/compare', [PropertyController::class, 'compare'])->name('real-estate.properties.compare');
Route::post('/tax-estimate', [PropertyController::class, 'taxEstimate'])->name('real-estate.properties.tax-estimate');
Route::get('/favorites', [PropertyController::class, 'favorites'])->name('real-estate.properties.favorites');
Route::post('/{property}/transition/{status}', [PropertyController::class, 'transition'])->name('real-estate.properties.transition');
Route::post('/{property}/favorite', [PropertyController::class, 'favorite'])->name('real-estate.properties.favorite');
Route::delete('/favorites/{property}', [PropertyController::class, 'removeFavorite'])->name('real-estate.properties.favorite-remove');
Route::get('/{property}/similar', [PropertyController::class, 'similar'])->name('real-estate.properties.similar');
Route::post('/{property}/walkability', [PropertyController::class, 'walkability'])->name('real-estate.properties.walkability');
Route::get('/{property}/qr-code', [PropertyController::class, 'qrCode'])->name('real-estate.properties.qr-code');
Route::post('/{property}/share', [PropertyController::class, 'share'])->name('real-estate.properties.share');
Route::get('/{property}/history', [PropertyController::class, 'history'])->name('real-estate.properties.history');
Route::put('/{property}/units', [PropertyController::class, 'unit'])->name('real-estate.properties.units');
Route::post('/{property}/keys', [PropertyController::class, 'key'])->name('real-estate.properties.keys');
Route::get('/{property}', [PropertyController::class, 'show'])->name('real-estate.properties.show');
Route::delete('/{property}', [PropertyController::class, 'destroy'])->name('real-estate.properties.destroy');
Route::prefix('api/v1/real-estate/properties/{property}/price-alerts')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertyPriceAlertController::class, 'index'])->name('real-estate.properties.price-alerts.index');
Route::post('/', [PropertyPriceAlertController::class, 'store'])->name('real-estate.properties.price-alerts.store');
Route::prefix('api/v1/real-estate/price-alerts')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::delete('/{alert}', [PropertyPriceAlertController::class, 'destroy'])->name('real-estate.price-alerts.destroy');
Route::prefix('api/v1/real-estate/property-categories')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertyCategoryController::class, 'index'])->name('real-estate.property-categories.index');
Route::post('/', [PropertyCategoryController::class, 'store'])->name('real-estate.property-categories.store');
Route::delete('/{category}', [PropertyCategoryController::class, 'destroy'])->name('real-estate.property-categories.destroy');
Route::prefix('api/v1/real-estate/property-templates')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertyTemplateController::class, 'index'])->name('real-estate.property-templates.index');
Route::post('/', [PropertyTemplateController::class, 'store'])->name('real-estate.property-templates.store');
Route::delete('/{template}', [PropertyTemplateController::class, 'destroy'])->name('real-estate.property-templates.destroy');
```
<!-- layer-implementation-plan:end -->
