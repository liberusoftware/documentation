# Billing: Subscriptions Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#subscriptions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-subscriptions-nuxt`
**Matching domain module:** `billing-subscriptions`
**Application:** Billing
**Source feature:** [Subscriptions](../features/subscriptions.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/subscriptions.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `billing-subscriptions` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Activation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Renewal:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Trial:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Upgrade/downgrade:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pause:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cancellation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Entitlement state:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-subscriptions-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `activation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `renewal`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `trial`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `upgrade-downgrade`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pause`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cancellation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `entitlement-state`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `billing-subscriptions` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/subscriptions.md)) |
| Capability Nuxt module skeleton | [`module-billing-subscriptions-nuxt`](https://github.com/liberusoftware/module-billing-subscriptions-nuxt) (`@liberusoftware/module-billing-subscriptions-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Activation** | Expose composable and Vue 3 component for `activation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/subscriptions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Renewal** | Expose composable and Vue 3 component for `renewal` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/subscriptions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Trial** | Expose composable and Vue 3 component for `trial` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/subscriptions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Upgrade/downgrade** | Expose composable and Vue 3 component for `upgrade/downgrade` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/subscriptions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Pause** | Expose composable and Vue 3 component for `pause` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/subscriptions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Cancellation** | Expose composable and Vue 3 component for `cancellation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/subscriptions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Entitlement state** | Expose composable and Vue 3 component for `entitlement state` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/subscriptions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListSubscriptions.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Queries/ListSubscriptions.php) | `public function execute(?int $teamId, int $perPage = 25, ?int $customerId = null, ?SubscriptionStatus $status = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ActivateSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Subscription` |
| [CancelSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/CancelSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [ChangeSubscriptionPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ChangeSubscriptionPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, ?int $pricingPlanId): Subscription` |
| [ExpireSubscriptions.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ExpireSubscriptions.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(?int $teamId = null, ?CarbonInterface $asOf = null): int` |
| [PauseSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/PauseSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [RenewSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/RenewSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, ?int $periodDays = null): Subscription` |
| [ResumeSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ResumeSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [UpdateEntitlementState.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/UpdateEntitlementState.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, array $entitlements): Subscription` |
| [SubscriptionPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Policies/SubscriptionPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Subscription $subscription): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Subscription $subscription): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Subscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Models/Subscription.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SubscriptionController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-api/src/Http/Controllers/SubscriptionController.php) | `public function index(Request $request, ListSubscriptions $query): JsonResponse`<br>`public function show(Request $request, Subscription $subscription): JsonResponse`<br>`public function store(Request $request, ActivateSubscription $activate): JsonResponse`<br>`public function renew(Request $request, Subscription $subscription, RenewSubscription $renew): JsonResponse`<br>`public function pause(Request $request, Subscription $subscription, PauseSubscription $pause): JsonResponse`<br>`public function cancel(Request $request, Subscription $subscription, CancelSubscription $cancel): JsonResponse`<br>`public function resume(Request $request, Subscription $subscription, ResumeSubscription $resume): JsonResponse`<br>`public function changePlan(Request $request, Subscription $subscription, ChangeSubscriptionPlan $change): JsonResponse`<br>`public function entitlements(Request $request, Subscription $subscription, UpdateEntitlementState $update): JsonResponse`<br>`public function expire(Request $request, ExpireSubscriptions $expire): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-subscriptions-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.subscriptions.read'])
Route::get('/', [SubscriptionController::class, 'index'])->name('index');
Route::get('/{subscription}', [SubscriptionController::class, 'show'])->whereNumber('subscription')->name('show');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.subscriptions.write', 'idempotency'])
Route::post('/', [SubscriptionController::class, 'store'])->name('store');
Route::post('/{subscription}/renew', [SubscriptionController::class, 'renew'])->name('renew');
Route::post('/{subscription}/pause', [SubscriptionController::class, 'pause'])->name('pause');
Route::post('/{subscription}/resume', [SubscriptionController::class, 'resume'])->name('resume');
Route::post('/{subscription}/cancel', [SubscriptionController::class, 'cancel'])->name('cancel');
Route::patch('/{subscription}/plan', [SubscriptionController::class, 'changePlan'])->name('plan');
Route::patch('/{subscription}/entitlements', [SubscriptionController::class, 'entitlements'])->name('entitlements');
Route::post('/expire', [SubscriptionController::class, 'expire'])->name('expire');
```
<!-- layer-implementation-plan:end -->
