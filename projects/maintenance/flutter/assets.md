# Assets Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#assets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-assets-flutter
**Matching core package:** module-maintenance-assets ([implementation](../core/assets.md))
**Matching API package:** module-maintenance-assets-api ([contract](../api/assets.md))

## Implementation plan

This adapter presents Assets for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Assets API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/assets.md), and [API module](../api/assets.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `assets`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-assets-flutter`](https://github.com/liberusoftware/module-maintenance-assets-flutter) (`module_maintenance_assets_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-assets-dart-mobile`](https://github.com/liberusoftware/module-maintenance-assets-dart-mobile) (`module_maintenance_assets_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-assets-dart-desktop`](https://github.com/liberusoftware/module-maintenance-assets-dart-desktop) (`module_maintenance_assets_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/assets.md) · [Core plan](../core/assets.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Hierarchies** | Adaptive mobile cards/sheets for `hierarchies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `hierarchies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Categories** | Adaptive mobile cards/sheets for `categories` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `categories` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Specifications** | Adaptive mobile cards/sheets for `specifications` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `specifications` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Meters** | Adaptive mobile cards/sheets for `meters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `meters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Warranties** | Adaptive mobile cards/sheets for `warranties` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `warranties` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Condition** | Adaptive mobile cards/sheets for `condition` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `condition` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **QR/barcodes** | Adaptive mobile cards/sheets for `qr/barcodes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `qr/barcodes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **History** | Adaptive mobile cards/sheets for `history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/CreateAsset.php) | `public function handle(int $teamId, array $attributes): Asset` |
| [DeleteAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/DeleteAsset.php) | `public function handle(int $teamId, Asset $asset): void` |
| [RecordAssetHistory.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/RecordAssetHistory.php) | `public function handle(int $teamId, Asset $asset, string $type, string $note, ?int $actorId = null): Asset` |
| [UpdateAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/UpdateAsset.php) | `public function handle(int $teamId, Asset $asset, array $attributes): Asset` |
| [AssetPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Policies/AssetPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Asset $asset): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Asset $asset): bool`<br>`public function delete(object $user, Asset $asset): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Asset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Models/Asset.php) | `team_id`, `name`, `description`, `code`, `category`, `serial_number`, `model`, `manufacturer`, `location`, `purchase_date`, `warranty_expiry`, `notes`, `condition`, `criticality`, `status`, `qr_code`, `barcode`, `sensor_enabled`, `sensor_type`, `sensor_id`, `sensor_config`, `last_sensor_reading_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AssetController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets-api/src/Http/Controllers/AssetController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAsset $create): JsonResponse`<br>`public function show(Request $request, Asset $asset): JsonResponse`<br>`public function history(Request $request, Asset $asset, RecordAssetHistory $recordHistory): JsonResponse`<br>`public function update(Request $request, Asset $asset, UpdateAsset $update): JsonResponse`<br>`public function destroy(Request $request, Asset $asset, DeleteAsset $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-assets-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/assets')->group(function (): void {
Route::get('/', [AssetController::class, 'index']);
Route::post('/', [AssetController::class, 'store']);
Route::post('/{asset}/history', [AssetController::class, 'history']);
Route::get('/{asset}', [AssetController::class, 'show']);
Route::patch('/{asset}', [AssetController::class, 'update']);
Route::delete('/{asset}', [AssetController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
