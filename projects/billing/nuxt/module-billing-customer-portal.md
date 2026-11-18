# Billing: Module Billing Customer Portal Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-customer-portal). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-customer-portal-nuxt`
**Matching domain module:** `module-billing-customer-portal`
**Application:** Billing
**Source feature:** [Module Billing Customer Portal](../features/module-billing-customer-portal.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-customer-portal.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-customer-portal` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Profile:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Orders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Services:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Usage:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Invoices:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tickets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Changes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cancellation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-customer-portal-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `profile`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `orders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `services`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `usage`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `invoices`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tickets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `changes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cancellation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-customer-portal` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-customer-portal.md)) |
| Capability Nuxt module skeleton | [`module-billing-customer-portal-nuxt`](https://github.com/liberusoftware/module-billing-customer-portal-nuxt) (`@liberusoftware/module-billing-customer-portal-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Profile** | Expose composable and Vue 3 component for `profile` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Orders** | Expose composable and Vue 3 component for `orders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Services** | Expose composable and Vue 3 component for `services` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Usage** | Expose composable and Vue 3 component for `usage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Invoices** | Expose composable and Vue 3 component for `invoices` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Payments** | Expose composable and Vue 3 component for `payments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Tickets** | Expose composable and Vue 3 component for `tickets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Changes** | Expose composable and Vue 3 component for `changes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Cancellation** | Expose composable and Vue 3 component for `cancellation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

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
