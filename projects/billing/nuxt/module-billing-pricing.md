# Billing: Module Billing Pricing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-pricing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-pricing-nuxt`
**Matching domain module:** `module-billing-pricing`
**Application:** Billing
**Source feature:** [Module Billing Pricing](../features/module-billing-pricing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-pricing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-pricing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Recurring/one-time/usage/tiered pricing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contracts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Discounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Proration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Snapshots:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-pricing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `recurring-one-time-usage-tiered-pricing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contracts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `discounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `proration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `snapshots`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-pricing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-pricing.md)) |
| Capability Nuxt module skeleton | [`module-billing-pricing-nuxt`](https://github.com/liberusoftware/module-billing-pricing-nuxt) (`@liberusoftware/module-billing-pricing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Recurring/one-time/usage/tiered pricing** | Expose composable and Vue 3 component for `recurring/one-time/usage/tiered pricing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-pricing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Contracts** | Expose composable and Vue 3 component for `contracts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-pricing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Discounts** | Expose composable and Vue 3 component for `discounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-pricing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Proration** | Expose composable and Vue 3 component for `proration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-pricing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Snapshots** | Expose composable and Vue 3 component for `snapshots` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-pricing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListPricingPlans.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Queries/ListPricingPlans.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculatePricingPlanAmount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CalculatePricingPlanAmount.php) | `public function execute(PricingPlan $plan, array $options = []): int` |
| [CalculateProration.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CalculateProration.php) | `public function execute(int $amountMinor, int $remainingDays, int $periodDays): int` |
| [CalculateUsageBasedPrice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CalculateUsageBasedPrice.php) | `public function __construct(private readonly CalculatePricingPlanAmount $calculate)`<br>`public function execute( PricingPlan $plan, int $meterId, CarbonInterface $start, CarbonInterface $end, ?int $customerId = null, ): array` |
| [CapturePricingSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CapturePricingSnapshot.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PricingPlan $plan): PricingSnapshot` |
| [CreatePricingContract.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CreatePricingContract.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PricingContract` |
| [CreatePricingPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CreatePricingPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PricingPlan` |
| [RedeemPricingDiscount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/RedeemPricingDiscount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PricingDiscount $discount): PricingDiscount` |
| [PricingPlanPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Policies/PricingPlanPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, PricingPlan $plan): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, PricingPlan $plan): bool` |
| [PricingRecordPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Policies/PricingRecordPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PricingContract.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Models/PricingContract.php) | No literal fillable array detected; inspect the model and API schema. |
| [PricingDiscount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Models/PricingDiscount.php) | No literal fillable array detected; inspect the model and API schema. |
| [PricingPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Models/PricingPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [PricingSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Models/PricingSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PricingPlanController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing-api/src/Http/Controllers/PricingPlanController.php) | `public function index(Request $request, ListPricingPlans $query): JsonResponse`<br>`public function store(Request $request, CreatePricingPlan $create): JsonResponse` |
| [PricingSupportController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing-api/src/Http/Controllers/PricingSupportController.php) | `public function contracts(Request $request): JsonResponse`<br>`public function createContract(Request $request, CreatePricingContract $create): JsonResponse`<br>`public function discounts(Request $request): JsonResponse`<br>`public function snapshots(Request $request): JsonResponse`<br>`public function redeem(Request $request, PricingDiscount $discount, RedeemPricingDiscount $redeem): JsonResponse`<br>`public function snapshot(Request $request, PricingPlan $plan, CapturePricingSnapshot $capture): JsonResponse`<br>`public function proration(Request $request, CalculateProration $calculate): JsonResponse`<br>`public function usage(Request $request, PricingPlan $plan, CalculateUsageBasedPrice $calculate): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-pricing-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.pricing.read'])->prefix('api/v1/billing/pricing')->name('billing.pricing.')->group(function (): void {
Route::get('/contracts', [PricingSupportController::class, 'contracts'])->name('contracts.index');
Route::get('/discounts', [PricingSupportController::class, 'discounts'])->name('discounts.index');
Route::get('/snapshots', [PricingSupportController::class, 'snapshots'])->name('snapshots.index');
Route::post('/proration', [PricingSupportController::class, 'proration'])->name('proration');
Route::post('/plans/{plan}/usage', [PricingSupportController::class, 'usage'])->name('plans.usage');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.pricing.write', 'idempotency'])->prefix('api/v1/billing/pricing')->name('billing.pricing.')->group(function (): void {
Route::post('/contracts', [PricingSupportController::class, 'createContract'])->name('contracts.store');
Route::post('/discounts/{discount}/redeem', [PricingSupportController::class, 'redeem'])->name('discounts.redeem');
Route::post('/plans/{plan}/snapshot', [PricingSupportController::class, 'snapshot'])->name('plans.snapshot');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.pricing.read'])->prefix('api/v1/billing/pricing')->name('billing.pricing.')->group(fn () => Route::get('/', [PricingPlanController::class, 'index'])->name('plans.index'));
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.pricing.write', 'idempotency'])->prefix('api/v1/billing/pricing')->name('billing.pricing.')->group(fn () => Route::post('/', [PricingPlanController::class, 'store'])->name('plans.store'));
```
<!-- layer-implementation-plan:end -->
