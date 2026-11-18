# Accounting: Supplier Bills Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#supplier-bills). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-supplier-bills-nuxt`
**Matching domain module:** `accounting-supplier-bills`
**Application:** Accounting
**Source feature:** [Supplier Bills](../features/supplier-bills.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/supplier-bills.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-supplier-bills` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Draft/approved/posted bills:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Capture sources:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Line coding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Due dates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Duplicate detection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Matching:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Credits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Documents:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-supplier-bills-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `draft-approved-posted-bills`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `capture-sources`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `line-coding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `due-dates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `duplicate-detection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `matching`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `credits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `documents`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-supplier-bills` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/supplier-bills.md)) |
| Capability Nuxt module skeleton | [`module-accounting-supplier-bills-nuxt`](https://github.com/liberusoftware/module-accounting-supplier-bills-nuxt) (`@liberusoftware/module-accounting-supplier-bills-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Draft/approved/posted bills** | Expose composable and Vue 3 component for `draft/approved/posted bills` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Capture sources** | Expose composable and Vue 3 component for `capture sources` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Line coding** | Expose composable and Vue 3 component for `line coding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax** | Expose composable and Vue 3 component for `tax` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Due dates** | Expose composable and Vue 3 component for `due dates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Duplicate detection** | Expose composable and Vue 3 component for `duplicate detection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Matching** | Expose composable and Vue 3 component for `matching` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Credits** | Expose composable and Vue 3 component for `credits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Documents** | Expose composable and Vue 3 component for `documents` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/supplier-bills.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DuplicateSupplierBillQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Queries/DuplicateSupplierBillQuery.php) | `public function handle(int $partyId, string $billNumber, ?int $exceptId = null): Collection` |
| [SupplierBillAgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Queries/SupplierBillAgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddSupplierBillCredit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/AddSupplierBillCredit.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBill` |
| [ApproveSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/ApproveSupplierBill.php) | `public function handle(SupplierBill $bill, ?int $actorId = null): SupplierBill` |
| [AttachSupplierBillDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/AttachSupplierBillDocument.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBillDocument` |
| [CreateSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/CreateSupplierBill.php) | `public function handle(array $attributes, array $lines): SupplierBill` |
| [MatchSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/MatchSupplierBill.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBill` |
| [PostSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/PostSupplierBill.php) | `public function __construct(private readonly CreateOpenItem $createOpenItem)`<br>`public function handle(SupplierBill $bill): SupplierBill` |
| [RejectSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/RejectSupplierBill.php) | `public function handle(SupplierBill $bill, string $reason): SupplierBill` |
| [UpdateSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/UpdateSupplierBill.php) | `public function handle(SupplierBill $bill, array $attributes, array $lines): SupplierBill` |
| [VoidSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/VoidSupplierBill.php) | `public function handle(SupplierBill $bill, string $reason): SupplierBill` |
| [SupplierBillsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-api/src/Policies/SupplierBillsPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $bill): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $bill): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBill.php) | `party_id`, `bill_number`, `bill_date`, `due_on`, `status`, `payment_status`, `subtotal`, `tax_total`, `total`, `amount_paid`, `currency`, `capture_source`, `purchase_order_reference`, `reference_number`, `notes`, `approval_status`, `approved_by`, `approved_at`, `rejection_reason`, `recurring`, `recurrence_frequency`, `recurrence_start`, `recurrence_end`, `last_generated`, `external_ids`, `metadata` |
| [SupplierBillCredit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillCredit.php) | `bill_id`, `amount`, `currency`, `reason`, `reference`, `metadata` |
| [SupplierBillDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillDocument.php) | `bill_id`, `path`, `original_name`, `mime_type`, `sha256`, `metadata` |
| [SupplierBillLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillLine.php) | `bill_id`, `account_code`, `description`, `quantity`, `unit_price`, `discount_rate`, `tax_rate`, `net_amount`, `tax_amount`, `metadata` |
| [SupplierBillMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillMatch.php) | `bill_id`, `match_type`, `matched_type`, `matched_id`, `quantity`, `amount`, `status`, `metadata` |
| [Supplier.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-api/src/Models/Supplier.php) | `payment_term_id`, `supplier_first_name`, `supplier_last_name`, `supplier_email`, `supplier_address`, `supplier_phone_number`, `supplier_limit_credit`, `supplier_tin` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SupplierBillController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-api/src/Http/Controllers/SupplierBillController.php) | `public function index(Request $request): mixed`<br>`public function show(string $supplierBill): SupplierBillResource`<br>`public function store(Request $request, CreateSupplierBill $action): SupplierBillResource`<br>`public function update(Request $request, string $supplierBill, UpdateSupplierBill $action): SupplierBillResource`<br>`public function approve(string $supplierBill, ApproveSupplierBill $action): SupplierBillResource`<br>`public function post(string $supplierBill, PostSupplierBill $action): SupplierBillResource`<br>`public function reject(Request $request, string $supplierBill, RejectSupplierBill $action): SupplierBillResource`<br>`public function void(Request $request, string $supplierBill, VoidSupplierBill $action): SupplierBillResource`<br>`public function credit(Request $request, string $supplierBill, AddSupplierBillCredit $action): SupplierBillResource`<br>`public function match(Request $request, string $supplierBill, MatchSupplierBill $action): SupplierBillResource`<br>`public function document(Request $request, string $supplierBill, AttachSupplierBillDocument $action): SupplierBillResource`<br>`public function duplicates(Request $request, DuplicateSupplierBillQuery $query): JsonResponse`<br>`public function aging(Request $request, SupplierBillAgingQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/accounting-supplier-bills-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/supplier-bills')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.supplier-bills.read')->group(function (): void {
Route::get('/', [SupplierBillController::class, 'index']);
Route::get('/duplicates', [SupplierBillController::class, 'duplicates']);
Route::get('/aging', [SupplierBillController::class, 'aging']);
Route::get('/{supplierBill}', [SupplierBillController::class, 'show']);
Route::middleware('ability:accounting.supplier-bills.write')->group(function (): void {
Route::post('/', [SupplierBillController::class, 'store']);
Route::patch('/{supplierBill}', [SupplierBillController::class, 'update']);
Route::post('/{supplierBill}/approve', [SupplierBillController::class, 'approve']);
Route::post('/{supplierBill}/post', [SupplierBillController::class, 'post']);
Route::post('/{supplierBill}/reject', [SupplierBillController::class, 'reject']);
Route::post('/{supplierBill}/void', [SupplierBillController::class, 'void']);
Route::post('/{supplierBill}/credits', [SupplierBillController::class, 'credit']);
Route::post('/{supplierBill}/matches', [SupplierBillController::class, 'match']);
Route::post('/{supplierBill}/documents', [SupplierBillController::class, 'document']);
```
<!-- layer-implementation-plan:end -->
