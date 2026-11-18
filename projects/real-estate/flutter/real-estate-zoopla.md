# Real Estate Zoopla Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-zoopla). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-zoopla-flutter
**Matching core package:** module-real-estate-real-estate-zoopla ([implementation](../core/real-estate-zoopla.md))
**Matching API package:** module-real-estate-real-estate-zoopla-api ([contract](../api/real-estate-zoopla.md))

## Implementation plan

This adapter presents Real Estate Zoopla for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Zoopla API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/real-estate-zoopla.md), and [API module](../api/real-estate-zoopla.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `real-estate-zoopla`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-zoopla-flutter`](https://github.com/liberusoftware/module-real-estate-zoopla-flutter) (`module_real_estate_zoopla_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-zoopla-dart-mobile`](https://github.com/liberusoftware/module-real-estate-zoopla-dart-mobile) (`module_real_estate_zoopla_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-zoopla-dart-desktop`](https://github.com/liberusoftware/module-real-estate-zoopla-dart-desktop) (`module_real_estate_zoopla_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/real-estate-zoopla.md) · [Core plan](../core/real-estate-zoopla.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Zoopla sync state** | Adaptive mobile cards/sheets for `zoopla sync state` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `zoopla sync state` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Provider payload boundary** | Adaptive mobile cards/sheets for `provider payload boundary` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provider payload boundary` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Retry and error state** | Adaptive mobile cards/sheets for `retry and error state` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `retry and error state` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ZooplaTransport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla/src/Contracts/ZooplaTransport.php) | `public function sendProperty(string $reference, array $payload, array $credentials): array`<br>`public function removeProperty(string $reference, array $credentials): array`<br>`public function branchPropertyList(array $credentials): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ZooplaSync.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla/src/Models/ZooplaSync.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ZooplaSyncController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla-api/src/Http/Controllers/ZooplaSyncController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateZooplaSync $create): JsonResponse`<br>`public function show(Request $request, ZooplaSync $zooplaSync): JsonResponse`<br>`public function sync(Request $request, ZooplaSync $zooplaSync, SyncZooplaListing $sync): JsonResponse`<br>`public function update(Request $request, ZooplaSync $zooplaSync, UpdateZooplaSync $update): JsonResponse`<br>`public function destroy(Request $request, ZooplaSync $zooplaSync, DeleteZooplaSync $delete): Response` |

**Observed route declarations:**

[modules/real-estate-zoopla-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/integrations/zoopla/syncs')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [ZooplaSyncController::class, 'index']);
Route::post('/', [ZooplaSyncController::class, 'store']);
Route::post('/{zooplaSync}/sync', [ZooplaSyncController::class, 'sync']);
Route::get('/{zooplaSync}', [ZooplaSyncController::class, 'show']);
Route::delete('/{zooplaSync}', [ZooplaSyncController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
