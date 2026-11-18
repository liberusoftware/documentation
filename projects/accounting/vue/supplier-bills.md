# Accounting: Supplier Bills Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#supplier-bills). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-supplier-bills-vue-inertia`
**Matching domain module:** `accounting-supplier-bills`
**Application:** Accounting
**Source feature:** [Supplier Bills](../features/supplier-bills.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/supplier-bills.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Draft/approved/posted bills:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Capture sources:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Line coding:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Due dates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Duplicate detection:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Matching:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Credits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Documents:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-supplier-bills-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `draft-approved-posted-bills`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `capture-sources`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `line-coding`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tax`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `due-dates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `duplicate-detection`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `matching`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `credits`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `documents`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-supplier-bills` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-supplier-bills-vue-inertia`](https://github.com/liberusoftware/module-accounting-supplier-bills-vue-inertia) (`@liberusoftware/module-accounting-supplier-bills-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/supplier-bills.md) · [Core plan](../core/supplier-bills.md) · [API plan](../api/supplier-bills.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Draft/approved/posted bills** | Render `draft/approved/posted bills` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Capture sources** | Render `capture sources` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Line coding** | Render `line coding` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tax** | Render `tax` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Due dates** | Render `due dates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Duplicate detection** | Render `duplicate detection` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Matching** | Render `matching` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Credits** | Render `credits` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Documents** | Render `documents` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
