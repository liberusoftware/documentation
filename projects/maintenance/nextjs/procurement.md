# Procurement: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-maintenance-procurement`.

**Proposed design identifier:** `module-maintenance-procurement-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/procurement.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-maintenance-procurement](../../../modules/source/liberusoftware--module-maintenance-procurement.md) |
| API | [liberusoftware/module-maintenance-procurement-api](../../../modules/source/liberusoftware--module-maintenance-procurement-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Suppliers | A focused authorized view or workflow section for suppliers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Requests | A focused authorized view or workflow section for requests; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approvals | A focused authorized view or workflow section for approvals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Purchase orders | A focused authorized view or workflow section for purchase orders; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Receipts | A focused authorized view or workflow section for receipts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Returns | A focused authorized view or workflow section for returns; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Cost allocation | A focused authorized view or workflow section for cost allocation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
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
| [UpdatePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/UpdatePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, array $attributes): PurchaseRequest` |
| [UpdateVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/UpdateVendorContract.php) | `public function handle(int $teamId, VendorContract $contract, array $attributes): VendorContract` |
| [UpdateVendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/UpdateVendorPerformanceEvaluation.php) | `public function handle(int $teamId, VendorPerformanceEvaluation $evaluation, array $attributes): VendorPerformanceEvaluation` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [PurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/PurchaseRequest.php) | `team_id`, `supplier_name`, `title`, `description`, `amount`, `currency`, `status`, `requested_by`, `approved_by`, `metadata` |
| [VendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorContract.php) | `team_id`, `vendor_name`, `contract_number`, `title`, `description`, `contract_type`, `start_date`, `end_date`, `contract_value`, `currency`, `status`, `auto_renewal`, `renewal_date`, `notes`, `metadata` |
| [VendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorPerformanceEvaluation.php) | `team_id`, `vendor_contract_id`, `vendor_name`, `evaluation_date`, `evaluated_by`, `quality_rating`, `timeliness_rating`, `communication_rating`, `cost_effectiveness_rating`, `professionalism_rating`, `overall_rating`, `strengths`, `areas_for_improvement`, `comments`, `would_recommend` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

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

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
