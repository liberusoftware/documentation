# Maintenance: Module Maintenance Inventory React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-inventory). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-maintenance-module-maintenance-inventory-react-inertia`
**Matching domain module:** `module-maintenance-inventory`
**Application:** Maintenance
**Source feature:** [Module Maintenance Inventory](../features/module-maintenance-inventory.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-maintenance-inventory.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Parts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Warehouses/vans:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Stock ledger:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reservations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Issues/returns:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transfers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reorder:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Counts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-maintenance-module-maintenance-inventory-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `parts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `warehouses-vans`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `stock-ledger`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reservations`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `issues-returns`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `transfers`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reorder`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `counts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `module-maintenance-inventory` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-maintenance-laravel-inertia-react`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-maintenance-inventory-react-inertia`](https://github.com/liberusoftware/module-maintenance-inventory-react-inertia) (`@liberusoftware/module-maintenance-inventory-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/module-maintenance-inventory.md) · [Core plan](../core/module-maintenance-inventory.md) · [API plan](../api/module-maintenance-inventory.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Parts** | Render `parts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Warehouses/vans** | Render `warehouses/vans` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Stock ledger** | Render `stock ledger` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reservations** | Render `reservations` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Issues/returns** | Render `issues/returns` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Transfers** | Render `transfers` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reorder** | Render `reorder` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Counts** | Render `counts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdjustStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/AdjustStock.php) | `public function handle(int $teamId, StockItem $item, int $delta, string $reason = 'adjustment', ?int $userId = null, ?string $notes = null): StockItem` |
| [CreateStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/CreateStockItem.php) | `public function handle(int $teamId, array $attributes): StockItem` |
| [DeleteStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/DeleteStockItem.php) | `public function handle(int $teamId, StockItem $item): void` |
| [IssueStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/IssueStock.php) | `public function __construct(private readonly AdjustStock $adjustStock)`<br>`public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [ReleaseReservedStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReleaseReservedStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [ReserveStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReserveStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [ReturnStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReturnStock.php) | `public function __construct(private readonly AdjustStock $adjustStock)`<br>`public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [UpdateStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/UpdateStockItem.php) | `public function handle(int $teamId, StockItem $item, array $attributes): StockItem` |
| [StockItemPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Policies/StockItemPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, StockItem $item): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, StockItem $item): bool`<br>`public function delete(object $user, StockItem $item): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [StockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockItem.php) | `team_id`, `part_number`, `name`, `description`, `category`, `location`, `supplier_name`, `lead_time_days`, `notes`, `quantity`, `reorder_level`, `reorder_quantity`, `unit`, `unit_cost` |
| [StockMovement.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockMovement.php) | `team_id`, `stock_item_id`, `user_id`, `delta`, `quantity_before`, `quantity_after`, `reason`, `notes` |

| Observed API controller | Handler signatures |
| --- | --- |
| [StockItemController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-api/src/Http/Controllers/StockItemController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateStockItem $create): JsonResponse`<br>`public function show(Request $r, StockItem $stockItem): JsonResponse`<br>`public function adjust(Request $r, StockItem $stockItem, AdjustStock $adjust): JsonResponse`<br>`public function reserve(Request $r, StockItem $stockItem, ReserveStock $reserve): JsonResponse`<br>`public function release(Request $r, StockItem $stockItem, ReleaseReservedStock $release): JsonResponse`<br>`public function issue(Request $r, StockItem $stockItem, IssueStock $issue): JsonResponse`<br>`public function return(Request $r, StockItem $stockItem, ReturnStock $returnStock): JsonResponse`<br>`public function update(Request $r, StockItem $stockItem, UpdateStockItem $update): JsonResponse`<br>`public function destroy(Request $r, StockItem $stockItem, DeleteStockItem $delete): JsonResponse`<br>`public function movements(Request $r, StockItem $stockItem): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-inventory-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/inventory')->group(function (): void {
Route::get('/', [StockItemController::class, 'index']);
Route::post('/', [StockItemController::class, 'store']);
Route::get('/{stockItem}', [StockItemController::class, 'show']);
Route::patch('/{stockItem}', [StockItemController::class, 'update']);
Route::delete('/{stockItem}', [StockItemController::class, 'destroy']);
Route::post('/{stockItem}/adjust', [StockItemController::class, 'adjust']);
Route::post('/{stockItem}/reserve', [StockItemController::class, 'reserve']);
Route::post('/{stockItem}/release', [StockItemController::class, 'release']);
Route::post('/{stockItem}/issue', [StockItemController::class, 'issue']);
Route::post('/{stockItem}/return', [StockItemController::class, 'return']);
Route::get('/{stockItem}/movements', [StockItemController::class, 'movements']);
```
<!-- layer-implementation-plan:end -->
