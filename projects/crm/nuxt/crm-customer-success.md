# CRM: Crm Customer Success Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-customer-success). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-customer-success-nuxt`
**Matching domain module:** `crm-customer-success`
**Application:** CRM
**Source feature:** [Crm Customer Success](../features/crm-customer-success.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-customer-success.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-customer-success` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer segments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Onboarding plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Success plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Objectives:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Health scores:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Product/usage signals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Risks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Playbooks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Touchpoints:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Renewals:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-customer-success-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `customer-segments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `onboarding-plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `success-plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `objectives`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `health-scores`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `product-usage-signals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `risks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `playbooks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `touchpoints`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `renewals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-customer-success` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-customer-success.md)) |
| Capability Nuxt module skeleton | [`module-crm-customer-success-nuxt`](https://github.com/liberusoftware/module-crm-customer-success-nuxt) (`@liberusoftware/module-crm-customer-success-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Customer segments** | Expose composable and Vue 3 component for `customer segments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Lifecycle** | Expose composable and Vue 3 component for `lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Onboarding plans** | Expose composable and Vue 3 component for `onboarding plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Success plans** | Expose composable and Vue 3 component for `success plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Objectives** | Expose composable and Vue 3 component for `objectives` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Health scores** | Expose composable and Vue 3 component for `health scores` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Product/usage signals** | Expose composable and Vue 3 component for `product/usage signals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Risks** | Expose composable and Vue 3 component for `risks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Playbooks** | Expose composable and Vue 3 component for `playbooks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Touchpoints** | Expose composable and Vue 3 component for `touchpoints` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Renewals** | Expose composable and Vue 3 component for `renewals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-success.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CustomerSuccessQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Queries/CustomerSuccessQuery.php) | `public function customers(int $teamId)`<br>`public function risks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OpenSuccessRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/OpenSuccessRisk.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessRisk` |
| [PlanRenewal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/PlanRenewal.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessRenewal` |
| [RecordHealthSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/RecordHealthSignal.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessSignal` |
| [UpsertSuccessCustomer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/UpsertSuccessCustomer.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SuccessCustomer` |
| [CustomerSuccessPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Services/CustomerSuccessPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SuccessCustomer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessCustomer.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessRenewal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessRenewal.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessRisk.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessSignal.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CustomerSuccessController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-api/src/Http/Controllers/CustomerSuccessController.php) | `public function __construct(private readonly CustomerSuccessQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(UpsertSuccessCustomer $action): JsonResponse`<br>`public function signal(SuccessCustomer $customer, RecordHealthSignal $action): JsonResponse`<br>`public function risk(SuccessCustomer $customer, OpenSuccessRisk $action): JsonResponse`<br>`public function renewal(SuccessCustomer $customer, PlanRenewal $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-customer-success-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/customer-success')->group(function (): void {
Route::get('customers', [CustomerSuccessController::class, 'index']);
Route::post('customers', [CustomerSuccessController::class, 'store']);
Route::post('customers/{customer}/signals', [CustomerSuccessController::class, 'signal']);
Route::post('customers/{customer}/risks', [CustomerSuccessController::class, 'risk']);
Route::post('customers/{customer}/renewals', [CustomerSuccessController::class, 'renewal']);
```
<!-- layer-implementation-plan:end -->
