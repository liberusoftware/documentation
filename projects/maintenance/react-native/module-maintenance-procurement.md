# Module Maintenance Procurement React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-procurement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-module-maintenance-procurement-react-native
**Matching core package:** module-maintenance-module-maintenance-procurement ([implementation](../core/module-maintenance-procurement.md))
**Matching API package:** module-maintenance-module-maintenance-procurement-api ([contract](../api/module-maintenance-procurement.md))

## Implementation plan

This adapter presents Module Maintenance Procurement for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Maintenance Procurement API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-maintenance-procurement.md), and [API module](../api/module-maintenance-procurement.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-maintenance-procurement`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-maintenance-mobile-react`](https://github.com/liberusoftware/project-maintenance-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-maintenance-procurement.md)) |
| Capability React Native module skeleton | [`module-maintenance-procurement-react-native`](https://github.com/liberusoftware/module-maintenance-procurement-react-native) (`@liberusoftware/module-maintenance-procurement-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Suppliers** | Progressive mobile list/detail/sheet flow for `suppliers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Requests** | Progressive mobile list/detail/sheet flow for `requests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Purchase orders** | Progressive mobile list/detail/sheet flow for `purchase orders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Receipts** | Progressive mobile list/detail/sheet flow for `receipts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Returns** | Progressive mobile list/detail/sheet flow for `returns` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cost allocation** | Progressive mobile list/detail/sheet flow for `cost allocation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApprovePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/ApprovePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, int $approverId): PurchaseRequest` |
| [CreatePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreatePurchaseRequest.php) | `public function handle(int $teamId, array $attributes): PurchaseRequest` |
| [CreateVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreateVendorContract.php) | `public function handle(int $teamId, array $attributes): VendorContract` |
| [CreateVendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreateVendorPerformanceEvaluation.php) | `public function handle(int $teamId, array $attributes): VendorPerformanceEvaluation` |
| [DeletePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeletePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request): void` |
| [DeleteVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeleteVendorContract.php) | `public function handle(int $teamId, VendorContract $contract): void` |
| [DeleteVendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeleteVendorPerformanceEvaluation.php) | `public function handle(int $teamId, VendorPerformanceEvaluation $evaluation): void` |
| [RejectPurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/RejectPurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, int $approverId, ?string $reason = null): PurchaseRequest` |
| [TransitionPurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/TransitionPurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, string $status, ?int $actorId = null): PurchaseRequest` |
| [TransitionVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/TransitionVendorContract.php) | `public function handle(int $teamId, VendorContract $contract, string $status): VendorContract` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/PurchaseRequest.php) | `team_id`, `supplier_name`, `title`, `description`, `amount`, `currency`, `status`, `requested_by`, `approved_by`, `metadata` |
| [VendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorContract.php) | `team_id`, `vendor_name`, `contract_number`, `title`, `description`, `contract_type`, `start_date`, `end_date`, `contract_value`, `currency`, `status`, `auto_renewal`, `renewal_date`, `notes`, `metadata` |
| [VendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorPerformanceEvaluation.php) | `team_id`, `vendor_contract_id`, `vendor_name`, `evaluation_date`, `evaluated_by`, `quality_rating`, `timeliness_rating`, `communication_rating`, `cost_effectiveness_rating`, `professionalism_rating`, `overall_rating`, `strengths`, `areas_for_improvement`, `comments`, `would_recommend` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PurchaseRequestController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-api/src/Http/Controllers/PurchaseRequestController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreatePurchaseRequest $create): JsonResponse`<br>`public function show(Request $r, PurchaseRequest $purchaseRequest): JsonResponse`<br>`public function approve(Request $r, PurchaseRequest $purchaseRequest, ApprovePurchaseRequest $approve): JsonResponse`<br>`public function reject(Request $r, PurchaseRequest $purchaseRequest, RejectPurchaseRequest $reject): JsonResponse`<br>`public function transition(Request $r, PurchaseRequest $purchaseRequest, TransitionPurchaseRequest $transition): JsonResponse`<br>`public function update(Request $r, PurchaseRequest $purchaseRequest, UpdatePurchaseRequest $update): JsonResponse`<br>`public function destroy(Request $r, PurchaseRequest $purchaseRequest, DeletePurchaseRequest $delete): JsonResponse` |
| [VendorContractController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-api/src/Http/Controllers/VendorContractController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVendorContract $create): JsonResponse`<br>`public function show(Request $request, VendorContract $vendorContract): JsonResponse`<br>`public function transition(Request $request, VendorContract $vendorContract, TransitionVendorContract $transition): JsonResponse`<br>`public function update(Request $request, VendorContract $vendorContract, UpdateVendorContract $update): JsonResponse`<br>`public function destroy(Request $request, VendorContract $vendorContract, DeleteVendorContract $delete): JsonResponse` |
| [VendorPerformanceEvaluationController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-api/src/Http/Controllers/VendorPerformanceEvaluationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVendorPerformanceEvaluation $create): JsonResponse`<br>`public function show(Request $request, VendorPerformanceEvaluation $vendorPerformanceEvaluation): JsonResponse`<br>`public function update(Request $request, VendorPerformanceEvaluation $vendorPerformanceEvaluation, UpdateVendorPerformanceEvaluation $update): JsonResponse`<br>`public function destroy(Request $request, VendorPerformanceEvaluation $vendorPerformanceEvaluation, DeleteVendorPerformanceEvaluation $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-procurement-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/procurement')->group(function (): void {
Route::get('/contracts', [VendorContractController::class, 'index']);
Route::post('/contracts', [VendorContractController::class, 'store']);
Route::get('/contracts/{vendorContract}', [VendorContractController::class, 'show']);
Route::patch('/contracts/{vendorContract}', [VendorContractController::class, 'update']);
Route::post('/contracts/{vendorContract}/transition', [VendorContractController::class, 'transition']);
Route::delete('/contracts/{vendorContract}', [VendorContractController::class, 'destroy']);
Route::get('/evaluations', [VendorPerformanceEvaluationController::class, 'index']);
Route::post('/evaluations', [VendorPerformanceEvaluationController::class, 'store']);
Route::get('/evaluations/{vendorPerformanceEvaluation}', [VendorPerformanceEvaluationController::class, 'show']);
Route::patch('/evaluations/{vendorPerformanceEvaluation}', [VendorPerformanceEvaluationController::class, 'update']);
Route::delete('/evaluations/{vendorPerformanceEvaluation}', [VendorPerformanceEvaluationController::class, 'destroy']);
Route::get('/', [PurchaseRequestController::class, 'index']);
Route::post('/', [PurchaseRequestController::class, 'store']);
Route::get('/{purchaseRequest}', [PurchaseRequestController::class, 'show']);
Route::patch('/{purchaseRequest}', [PurchaseRequestController::class, 'update']);
Route::delete('/{purchaseRequest}', [PurchaseRequestController::class, 'destroy']);
Route::post('/{purchaseRequest}/approve', [PurchaseRequestController::class, 'approve']);
Route::post('/{purchaseRequest}/reject', [PurchaseRequestController::class, 'reject']);
Route::post('/{purchaseRequest}/transitions', [PurchaseRequestController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
