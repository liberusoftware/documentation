# CRM: Crm Business Process Management Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-business-process-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-business-process-management-nuxt`
**Matching domain module:** `crm-business-process-management`
**Application:** CRM
**Source feature:** [Crm Business Process Management](../features/crm-business-process-management.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-business-process-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-business-process-management` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Guided stages:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Required steps/data:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Service processes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exception routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Process versioning:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-business-process-management-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `guided-stages`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `required-steps-data`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `service-processes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exception-routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `process-versioning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-business-process-management` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-business-process-management.md)) |
| Capability Nuxt module skeleton | [`module-crm-business-process-management-nuxt`](https://github.com/liberusoftware/module-crm-business-process-management-nuxt) (`@liberusoftware/module-crm-business-process-management-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Guided stages** | Expose composable and Vue 3 component for `guided stages` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-business-process-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Required steps/data** | Expose composable and Vue 3 component for `required steps/data` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-business-process-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-business-process-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Validations** | Expose composable and Vue 3 component for `validations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-business-process-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Service processes** | Expose composable and Vue 3 component for `service processes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-business-process-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Exception routing** | Expose composable and Vue 3 component for `exception routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-business-process-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Process versioning** | Expose composable and Vue 3 component for `process versioning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-business-process-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProcessQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Queries/ProcessQuery.php) | `public function processes(int $teamId): Builder`<br>`public function runs(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdvanceProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/AdvanceProcess.php) | `public function execute(int $teamId, int $actorId, ProcessRun $run, array $context = []): ProcessRun` |
| [CreateProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/CreateProcess.php) | `public function execute(int $teamId, int $ownerId, array $input): Process` |
| [PublishProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/PublishProcess.php) | `public function execute(int $teamId, int $actorId, Process $process): Process` |
| [StartProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/StartProcess.php) | `public function execute(int $teamId, int $actorId, Process $process, array $context = []): ProcessRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Process.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/Process.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessRun.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [BusinessProcessesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-api/src/Http/Controllers/BusinessProcessesController.php) | `public function __construct(private readonly ProcessQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateProcess $action): JsonResponse`<br>`public function publish(Request $request, Process $process, PublishProcess $action): JsonResponse`<br>`public function start(Request $request, Process $process, StartProcess $action): JsonResponse`<br>`public function advance(Request $request, ProcessRun $run, AdvanceProcess $action): JsonResponse`<br>`public function runs(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/crm-business-process-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/business-process-management')->group(function (): void {
Route::get('/', [BusinessProcessesController::class, 'index']);
Route::post('/', [BusinessProcessesController::class, 'store']);
Route::post('{process}/publish', [BusinessProcessesController::class, 'publish']);
Route::post('{process}/runs', [BusinessProcessesController::class, 'start']);
Route::post('runs/{run}/advance', [BusinessProcessesController::class, 'advance']);
Route::get('runs', [BusinessProcessesController::class, 'runs']);
```
<!-- layer-implementation-plan:end -->
