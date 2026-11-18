# Accounting: Accounting Goods And Service Receipts Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-goods-and-service-receipts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-goods-and-service-receipts-vue-inertia`
**Matching domain module:** `accounting-goods-and-service-receipts`
**Application:** Accounting
**Source feature:** [Accounting Goods And Service Receipts](../features/accounting-goods-and-service-receipts.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-goods-and-service-receipts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Receipts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Service confirmation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Quantities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Variance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Returns:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Attachments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Inventory/project references:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Accrual events:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-goods-and-service-receipts-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `receipts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `service-confirmation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `quantities`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `variance`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `returns`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `attachments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `inventory-project-references`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `accrual-events`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-goods-and-service-receipts` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-goods-and-service-receipts-vue-inertia`](https://github.com/liberusoftware/module-accounting-goods-and-service-receipts-vue-inertia) (`@liberusoftware/module-accounting-goods-and-service-receipts-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-goods-and-service-receipts.md) · [Core plan](../core/accounting-goods-and-service-receipts.md) · [API plan](../api/accounting-goods-and-service-receipts.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Receipts** | Render `receipts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Service confirmation** | Render `service confirmation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Quantities** | Render `quantities` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Variance** | Render `variance` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Returns** | Render `returns` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Attachments** | Render `attachments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Inventory/project references** | Render `inventory/project references` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Accrual events** | Render `accrual events` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
