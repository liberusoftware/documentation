# Accounting: Accounting Purchase Orders React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-purchase-orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-accounting-purchase-orders-react-inertia`
**Matching domain module:** `accounting-purchase-orders`
**Application:** Accounting
**Source feature:** [Accounting Purchase Orders](../features/accounting-purchase-orders.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-purchase-orders.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Supplier items:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Prices:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Quantities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Delivery:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Issue:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Receipts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Partials:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Changes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Closure:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Commitments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-purchase-orders-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `supplier-items`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `prices`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `quantities`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `delivery`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `approval`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `issue`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `receipts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `partials`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `changes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `closure`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `commitments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-purchase-orders` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-purchase-orders-react-inertia`](https://github.com/liberusoftware/module-accounting-purchase-orders-react-inertia) (`@liberusoftware/module-accounting-purchase-orders-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounting-purchase-orders.md) · [Core plan](../core/accounting-purchase-orders.md) · [API plan](../api/accounting-purchase-orders.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Supplier items** | Render `supplier items` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Prices** | Render `prices` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Quantities** | Render `quantities` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Delivery** | Render `delivery` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Approval** | Render `approval` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Issue** | Render `issue` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Receipts** | Render `receipts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Partials** | Render `partials` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Changes** | Render `changes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Closure** | Render `closure` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Commitments** | Render `commitments` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/CreatePurchaseOrder.php) | `public function handle(array $attributes, array $lines): PurchaseOrder` |
| [RecordPurchaseOrderChange.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/RecordPurchaseOrderChange.php) | `public function handle(PurchaseOrder $order, array $attributes): PurchaseOrderChange` |
| [RecordPurchaseReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/RecordPurchaseReceipt.php) | `public function handle(PurchaseOrder $order, array $attributes): PurchaseReceipt` |
| [TransitionPurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/TransitionPurchaseOrder.php) | `public function handle(PurchaseOrder $order, PurchaseOrderStatus $status, array $attributes = []): PurchaseOrder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrder.php) | `team_id`, `supplier_ref`, `order_number`, `currency`, `order_date`, `expected_delivery_on`, `total_amount`, `status`, `commitment_ref`, `source_requisition_ref`, `notes`, `metadata` |
| [PurchaseOrderChange.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrderChange.php) | `order_id`, `version`, `changes`, `reason`, `actor_ref`, `approved_at`, `metadata` |
| [PurchaseOrderLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrderLine.php) | `order_id`, `item_ref`, `description`, `quantity`, `unit_price`, `received_quantity`, `delivery_metadata`, `metadata` |
| [PurchaseReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseReceipt.php) | `order_id`, `receipt_ref`, `received_on`, `lines`, `status`, `document_ref`, `metadata` |
| [PurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/src/Models/PurchaseOrder.php) | `supplier_id`, `po_number`, `order_date`, `expected_delivery_date`, `total_amount`, `status`, `notes`, `purchase_request_id`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PurchaseOrdersController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/src/Http/Controllers/PurchaseOrdersController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreatePurchaseOrder $action): JsonResponse`<br>`public function show(Request $request, PurchaseOrder $order): PurchaseOrderResource`<br>`public function transition(Request $request, PurchaseOrder $order, TransitionPurchaseOrder $action): PurchaseOrderResource`<br>`public function receipt(Request $request, PurchaseOrder $order, RecordPurchaseReceipt $action): JsonResponse`<br>`public function change(Request $request, PurchaseOrder $order, RecordPurchaseOrderChange $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-purchase-orders-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/purchase-orders')->group(function (): void {
Route::middleware('ability:accounting.purchase-orders.read')->group(function (): void {
Route::get('/', [PurchaseOrdersController::class, 'index']);
Route::get('/{order}', [PurchaseOrdersController::class, 'show']);
Route::middleware('ability:accounting.purchase-orders.write')->group(function (): void {
Route::post('/', [PurchaseOrdersController::class, 'store']);
Route::post('/{order}/transition', [PurchaseOrdersController::class, 'transition']);
Route::post('/{order}/receipts', [PurchaseOrdersController::class, 'receipt']);
Route::post('/{order}/changes', [PurchaseOrdersController::class, 'change']);
```
<!-- layer-implementation-plan:end -->
