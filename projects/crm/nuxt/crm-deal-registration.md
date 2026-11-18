# CRM: Crm Deal Registration Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-deal-registration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-deal-registration-nuxt`
**Matching domain module:** `crm-deal-registration`
**Application:** CRM
**Source feature:** [Crm Deal Registration](../features/crm-deal-registration.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-deal-registration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-deal-registration` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Partner-submitted leads/deals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Duplicate/conflict checks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Territory rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Protection windows:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Collaboration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attribution:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-deal-registration-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `partner-submitted-leads-deals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `duplicate-conflict-checks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `territory-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `protection-windows`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `collaboration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attribution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-deal-registration` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-deal-registration.md)) |
| Capability Nuxt module skeleton | [`module-crm-deal-registration-nuxt`](https://github.com/liberusoftware/module-crm-deal-registration-nuxt) (`@liberusoftware/module-crm-deal-registration-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Partner-submitted leads/deals** | Expose composable and Vue 3 component for `partner-submitted leads/deals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-deal-registration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Duplicate/conflict checks** | Expose composable and Vue 3 component for `duplicate/conflict checks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-deal-registration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Territory rules** | Expose composable and Vue 3 component for `territory rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-deal-registration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-deal-registration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Protection windows** | Expose composable and Vue 3 component for `protection windows` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-deal-registration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Collaboration** | Expose composable and Vue 3 component for `collaboration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-deal-registration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Attribution** | Expose composable and Vue 3 component for `attribution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-deal-registration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DealRegistrationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Queries/DealRegistrationQuery.php) | `public function deals(int $teamId)`<br>`public function protected(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/ApproveDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DealRegistration $deal, int $protectionDays = 90): DealRegistration` |
| [CollaborateOnDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/CollaborateOnDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DealRegistration $deal, array $input): DealRegistration` |
| [SubmitDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/SubmitDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): DealRegistration` |
| [DealRegistrationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Services/DealRegistrationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DealRegistration.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Models/DealRegistration.php) | No literal fillable array detected; inspect the model and API schema. |
| [DealRegistrationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Models/DealRegistrationEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [DealRegistrationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-api/src/Http/Controllers/DealRegistrationController.php) | `public function __construct(private readonly DealRegistrationQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(SubmitDeal $action): JsonResponse`<br>`public function approve(DealRegistration $deal, ApproveDeal $action): JsonResponse`<br>`public function collaborate(DealRegistration $deal, CollaborateOnDeal $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-deal-registration-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/deal-registration')->group(function (): void {
Route::get('deals', [DealRegistrationController::class, 'index']);
Route::post('deals', [DealRegistrationController::class, 'store']);
Route::post('deals/{deal}/approve', [DealRegistrationController::class, 'approve']);
Route::post('deals/{deal}/collaborators', [DealRegistrationController::class, 'collaborate']);
```
<!-- layer-implementation-plan:end -->
