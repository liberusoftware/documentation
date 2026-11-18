# CRM: CRM Automation Pack Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-automation-pack). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-automation-pack-nuxt`
**Matching domain module:** `crm-automation-pack`
**Application:** CRM
**Source feature:** [CRM Automation Pack](../features/crm-automation-pack.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-automation-pack.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-automation-pack` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **CRM triggers/actions/conditions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recipes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Enrollment history:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Versioning:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Simulation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval gates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Generic Automation module adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-automation-pack-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `crm-triggers-actions-conditions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recipes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `enrollment-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `versioning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `simulation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval-gates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `generic-automation-module-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-automation-pack` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-automation-pack.md)) |
| Capability Nuxt module skeleton | [`module-crm-automation-pack-nuxt`](https://github.com/liberusoftware/module-crm-automation-pack-nuxt) (`@liberusoftware/module-crm-automation-pack-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **CRM triggers/actions/conditions** | Expose composable and Vue 3 component for `crm triggers/actions/conditions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-automation-pack.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Recipes** | Expose composable and Vue 3 component for `recipes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-automation-pack.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Enrollment history** | Expose composable and Vue 3 component for `enrollment history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-automation-pack.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Versioning** | Expose composable and Vue 3 component for `versioning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-automation-pack.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Simulation** | Expose composable and Vue 3 component for `simulation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-automation-pack.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Approval gates** | Expose composable and Vue 3 component for `approval gates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-automation-pack.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Generic Automation module adapters** | Expose composable and Vue 3 component for `generic automation module adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-automation-pack.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AutomationPackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Queries/AutomationPackQuery.php) | `public function recipes(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/ApproveAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, string $decision, ?string $reason = null): AutomationApproval` |
| [CreateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/CreateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AutomationRecipe` |
| [EnrollSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/EnrollSubject.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationEnrollment` |
| [PublishAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/PublishAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe): AutomationRecipe` |
| [SimulateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/SimulateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationRun` |
| [AutomationPackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Services/AutomationPackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AutomationApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationApproval.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationEnrollment.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRecipe.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRun.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AutomationPackController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-api/src/Http/Controllers/AutomationPackController.php) | `public function __construct(private readonly AutomationPackQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateAutomationRecipe $action): JsonResponse`<br>`public function publish(AutomationRecipe $recipe, PublishAutomationRecipe $action): JsonResponse`<br>`public function simulate(AutomationRecipe $recipe, SimulateAutomationRecipe $action): JsonResponse`<br>`public function approve(AutomationRecipe $recipe, ApproveAutomationRecipe $action): JsonResponse`<br>`public function enroll(AutomationRecipe $recipe, EnrollSubject $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-automation-pack-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/crm-automation-pack')->group(function (): void {
Route::get('recipes', [AutomationPackController::class, 'index']);
Route::post('recipes', [AutomationPackController::class, 'store']);
Route::post('recipes/{recipe}/publish', [AutomationPackController::class, 'publish']);
Route::post('recipes/{recipe}/simulate', [AutomationPackController::class, 'simulate']);
Route::post('recipes/{recipe}/approve', [AutomationPackController::class, 'approve']);
Route::post('recipes/{recipe}/enroll', [AutomationPackController::class, 'enroll']);
```
<!-- layer-implementation-plan:end -->
