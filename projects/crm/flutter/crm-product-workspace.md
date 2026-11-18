# Crm Product Workspace Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-product-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-product-workspace-flutter
**Matching core package:** module-crm-crm-product-workspace ([implementation](../core/crm-product-workspace.md))
**Matching API package:** module-crm-crm-product-workspace-api ([contract](../api/crm-product-workspace.md))

## Implementation plan

This adapter presents Crm Product Workspace for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Product Workspace API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-product-workspace.md), and [API module](../api/crm-product-workspace.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-product-workspace`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-product-workspace-flutter`](https://github.com/liberusoftware/module-crm-product-workspace-flutter) (`module_crm_product_workspace_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-product-workspace-dart-mobile`](https://github.com/liberusoftware/module-crm-product-workspace-dart-mobile) (`module_crm_product_workspace_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-product-workspace-dart-desktop`](https://github.com/liberusoftware/module-crm-product-workspace-dart-desktop) (`module_crm_product_workspace_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-product-workspace.md) · [Core plan](../core/crm-product-workspace.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Sales-facing catalog projections** | Adaptive mobile cards/sheets for `sales-facing catalog projections` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sales-facing catalog projections` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Bundles** | Adaptive mobile cards/sheets for `bundles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `bundles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Entitlements** | Adaptive mobile cards/sheets for `entitlements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `entitlements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Price-book references** | Adaptive mobile cards/sheets for `price-book references` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `price-book references` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Product eligibility** | Adaptive mobile cards/sheets for `product eligibility` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `product eligibility` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Governed Billing/Ecommerce synchronization** | Adaptive mobile cards/sheets for `governed billing/ecommerce synchronization` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `governed billing/ecommerce synchronization` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProductWorkspaceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Queries/ProductWorkspaceQuery.php) | `public function products(int $teamId)`<br>`public function entitlements(int $teamId, int $customerId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GrantEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/GrantEntitlement.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProductEntitlement` |
| [RecordProductSync.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/RecordProductSync.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProductSync` |
| [UpsertWorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/UpsertWorkspaceProduct.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): WorkspaceProduct` |
| [ProductWorkspacePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Services/ProductWorkspacePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProductBundle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductBundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProductEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProductSync.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductSync.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/WorkspaceProduct.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProductWorkspaceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-api/src/Http/Controllers/ProductWorkspaceController.php) | `public function __construct(private readonly ProductWorkspaceQuery $query)`<br>`public function products(): JsonResponse`<br>`public function store(UpsertWorkspaceProduct $action): JsonResponse`<br>`public function entitlement(GrantEntitlement $action): JsonResponse`<br>`public function sync(RecordProductSync $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-product-workspace-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/crm-product-workspace')->group(function (): void {
Route::get('products', [ProductWorkspaceController::class, 'products']);
Route::post('products', [ProductWorkspaceController::class, 'store']);
Route::post('entitlements', [ProductWorkspaceController::class, 'entitlement']);
Route::post('syncs', [ProductWorkspaceController::class, 'sync']);
```
<!-- layer-implementation-plan:end -->
