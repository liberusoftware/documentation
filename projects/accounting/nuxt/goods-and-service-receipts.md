# Accounting: Goods and Service Receipts Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#goods-and-service-receipts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-goods-and-service-receipts-nuxt`
**Matching domain module:** `accounting-goods-and-service-receipts`
**Application:** Accounting
**Source feature:** [Goods and Service Receipts](../features/goods-and-service-receipts.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/goods-and-service-receipts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-goods-and-service-receipts` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Receipts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Service confirmation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quantities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Variance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Returns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attachments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inventory/project references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accrual events:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-goods-and-service-receipts-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `receipts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `service-confirmation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quantities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `variance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `returns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attachments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inventory-project-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accrual-events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-goods-and-service-receipts` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/goods-and-service-receipts.md)) |
| Capability Nuxt module skeleton | [`module-accounting-goods-and-service-receipts-nuxt`](https://github.com/liberusoftware/module-accounting-goods-and-service-receipts-nuxt) (`@liberusoftware/module-accounting-goods-and-service-receipts-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Receipts** | Expose composable and Vue 3 component for `receipts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goods-and-service-receipts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Service confirmation** | Expose composable and Vue 3 component for `service confirmation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goods-and-service-receipts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Quantities** | Expose composable and Vue 3 component for `quantities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goods-and-service-receipts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Variance** | Expose composable and Vue 3 component for `variance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goods-and-service-receipts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Returns** | Expose composable and Vue 3 component for `returns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goods-and-service-receipts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Attachments** | Expose composable and Vue 3 component for `attachments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goods-and-service-receipts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Inventory/project references** | Expose composable and Vue 3 component for `inventory/project references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goods-and-service-receipts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Accrual events** | Expose composable and Vue 3 component for `accrual events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goods-and-service-receipts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReceiptQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Queries/ReceiptQuery.php) | `public function paginate(?int $teamId = null, ?ReceiptStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Receipt $receipt): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddReceiptAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/AddReceiptAttachment.php) | `public function handle(Receipt $receipt, array $a): ReceiptAttachment` |
| [AddReceiptLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/AddReceiptLine.php) | `public function handle(Receipt $receipt, array $a): ReceiptLine` |
| [ConfirmService.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/ConfirmService.php) | `public function handle(Receipt $receipt, array $a): ServiceConfirmation` |
| [CreateReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/CreateReceipt.php) | `public function handle(array $a): Receipt` |
| [PostAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/PostAccrual.php) | `public function handle(Receipt $receipt, array $a): ReceiptAccrual` |
| [ReturnReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/ReturnReceipt.php) | `public function handle(Receipt $receipt, array $a): ReceiptReturn` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Receipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/Receipt.php) | `team_id`, `receipt_ref`, `receipt_type`, `supplier_ref`, `purchase_order_ref`, `currency`, `status`, `received_at`, `inventory_ref`, `project_ref`, `total_value`, `metadata` |
| [ReceiptAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptAccrual.php) | `receipt_id`, `accrual_ref`, `amount`, `currency`, `period_ref`, `status`, `posted_at`, `source_ref`, `metadata` |
| [ReceiptAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptAttachment.php) | `receipt_id`, `attachment_ref`, `kind`, `file_ref`, `description`, `checksum`, `attached_by`, `attached_at`, `metadata` |
| [ReceiptLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptLine.php) | `receipt_id`, `line_ref`, `item_ref`, `description`, `ordered_quantity`, `received_quantity`, `returned_quantity`, `unit_price`, `line_value`, `variance_quantity`, `variance_value`, `inventory_ref`, `project_ref`, `metadata` |
| [ReceiptReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptReturn.php) | `receipt_id`, `return_ref`, `line_ref`, `quantity`, `value`, `reason`, `source_ref`, `returned_at`, `metadata` |
| [ServiceConfirmation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ServiceConfirmation.php) | `receipt_id`, `confirmation_ref`, `service_period`, `quantity`, `value`, `confirmed_by`, `confirmed_at`, `comment`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReceiptsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts-api/src/Http/Controllers/ReceiptsController.php) | `public function __construct(private readonly ReceiptQuery $query)`<br>`public function index(Request $r): ReceiptResource`<br>`public function store(Request $r, CreateReceipt $a): ReceiptResource`<br>`public function show(Receipt $receipt): ReceiptResource`<br>`public function line(Request $r, Receipt $receipt, AddReceiptLine $a): ReceiptResource`<br>`public function confirmService(Request $r, Receipt $receipt, ConfirmService $a): ReceiptResource`<br>`public function return(Request $r, Receipt $receipt, ReturnReceipt $a): ReceiptResource`<br>`public function attachment(Request $r, Receipt $receipt, AddReceiptAttachment $a): ReceiptResource`<br>`public function accrual(Request $r, Receipt $receipt, PostAccrual $a): ReceiptResource`<br>`public function variance(Receipt $receipt, ReceiptQuery $q): JsonResponse` |

**Observed route declarations:**

[modules/accounting-goods-and-service-receipts-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/goods-and-service-receipts')->group(function (): void {
Route::get('/', [ReceiptsController::class, 'index'])->name('accounting.receipts.list');
Route::post('/', [ReceiptsController::class, 'store'])->name('accounting.receipts.create');
Route::get('/{receipt}', [ReceiptsController::class, 'show'])->name('accounting.receipts.show');
Route::post('/{receipt}/lines', [ReceiptsController::class, 'line'])->name('accounting.receipts.line');
Route::post('/{receipt}/service-confirmation', [ReceiptsController::class, 'confirmService'])->name('accounting.receipts.confirm-service');
Route::post('/{receipt}/returns', [ReceiptsController::class, 'return'])->name('accounting.receipts.return');
Route::post('/{receipt}/attachments', [ReceiptsController::class, 'attachment'])->name('accounting.receipts.attachment');
Route::post('/{receipt}/accruals', [ReceiptsController::class, 'accrual'])->name('accounting.receipts.accrual');
Route::get('/{receipt}/variance', [ReceiptsController::class, 'variance'])->name('accounting.receipts.variance');
```
<!-- layer-implementation-plan:end -->
