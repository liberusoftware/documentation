# Billing: Customer Portal Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-portal). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-billing-customer-portal-vue-inertia`
**Matching domain module:** `billing-customer-portal`
**Application:** Billing
**Source feature:** [Customer Portal](../features/customer-portal.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/customer-portal.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Profile:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Orders:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Services:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Usage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Invoices:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tickets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Changes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cancellation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-billing-customer-portal-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `profile`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `orders`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `services`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `usage`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `invoices`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tickets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `changes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cancellation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `billing-customer-portal` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-billing-customer-portal-vue-inertia`](https://github.com/liberusoftware/module-billing-customer-portal-vue-inertia) (`@liberusoftware/module-billing-customer-portal-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/customer-portal.md) · [Core plan](../core/customer-portal.md) · [API plan](../api/customer-portal.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Profile** | Render `profile` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Orders** | Render `orders` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Services** | Render `services` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Usage** | Render `usage` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Invoices** | Render `invoices` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Payments** | Render `payments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tickets** | Render `tickets` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Changes** | Render `changes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Cancellation** | Render `cancellation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [GetCustomerBillingSummary.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/GetCustomerBillingSummary.php) | `public function __construct(private DatabaseManager $database)`<br>`public function handle(int $teamId, int $customerId, ?CarbonInterface $startAt = null, ?CarbonInterface $endAt = null): array` |
| [ListCustomerPortalRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/ListCustomerPortalRecords.php) | `public function handle(int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListPortalItems.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/ListPortalItems.php) | `public function handle(int $teamId, ?string $type = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/CreatePortalItem.php) | `public function handle(int $teamId, array $attributes): PortalItem` |
| [CreatePortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/CreatePortalRequest.php) | `public function handle(int $teamId, array $attributes): PortalRequest` |
| [TransitionPortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/TransitionPortalItem.php) | `public function handle(PortalItem $item, string $status): PortalItem` |
| [TransitionPortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/TransitionPortalRequest.php) | `public function handle(PortalRequest $request, string $status): PortalRequest` |
| [PortalItemPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Policies/PortalItemPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $item): bool`<br>`public function view(?object $user, object $item): bool` |
| [PortalRequestPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Policies/PortalRequestPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, PortalRequest $record): bool`<br>`public function update(?Authenticatable $user, PortalRequest $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Models/PortalItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [PortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Models/PortalRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [Customer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Models/Customer.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CustomerBillingController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Http/Controllers/CustomerBillingController.php) | `public function show(Request $request, int $customer, GetCustomerBillingSummary $summary): JsonResponse` |
| [PortalItemController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Http/Controllers/PortalItemController.php) | `public function index(Request $request, ListPortalItems $list): JsonResponse`<br>`public function store(Request $request, CreatePortalItem $create): JsonResponse`<br>`public function transition(Request $request, int $item, TransitionPortalItem $transition): JsonResponse` |
| [PortalRequestController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Http/Controllers/PortalRequestController.php) | `public function index(Request $request, ListCustomerPortalRecords $list): JsonResponse`<br>`public function store(Request $request, CreatePortalRequest $create): JsonResponse`<br>`public function transition(Request $request, int $record, TransitionPortalRequest $transition): JsonResponse`<br>`public function show(Request $request, int $record): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-customer-portal-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.customer-portal.read'])->prefix('api/v1/billing/customer-portal/items')->group(function (): void {
Route::get('/', [PortalItemController::class, 'index'])->name('billing.customer-portal.items.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.customer-portal.write', 'idempotency'])->prefix('api/v1/billing/customer-portal/items')->group(function (): void {
Route::post('/', [PortalItemController::class, 'store'])->name('billing.customer-portal.items.store');
Route::patch('/{item}/status', [PortalItemController::class, 'transition'])->whereNumber('item')->name('billing.customer-portal.items.status');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.customer-portal.read'])->prefix('api/v1/billing/customer-portal')->group(function (): void {
Route::get('/billing/{customer}', [CustomerBillingController::class, 'show'])->whereNumber('customer')->name('billing.customer-portal.billing.show');
Route::get('/', [PortalRequestController::class, 'index'])->name('billing.customer-portal.requests.index');
Route::get('/{record}', [PortalRequestController::class, 'show'])->whereNumber('record')->name('billing.customer-portal.requests.show');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.customer-portal.write', 'idempotency'])->prefix('api/v1/billing/customer-portal')->group(function (): void {
Route::post('/', [PortalRequestController::class, 'store'])->name('billing.customer-portal.requests.store');
Route::patch('/{record}/status', [PortalRequestController::class, 'transition'])->whereNumber('record')->name('billing.customer-portal.requests.status');
```
<!-- layer-implementation-plan:end -->
