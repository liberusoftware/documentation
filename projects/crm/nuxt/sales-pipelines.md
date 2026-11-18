# CRM: Sales Pipelines Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-pipelines). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-sales-pipelines-nuxt`
**Matching domain module:** `crm-sales-pipelines`
**Application:** CRM
**Source feature:** [Sales Pipelines](../features/sales-pipelines.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/sales-pipelines.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-sales-pipelines` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Multiple pipelines:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stages:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Opportunities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Products:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Values:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Probabilities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Close dates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Competitors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dependencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stage history:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rotting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Loss reasons:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-sales-pipelines-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `multiple-pipelines`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stages`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `opportunities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `products`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `values`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `probabilities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `close-dates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `competitors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dependencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stage-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rotting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `loss-reasons`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-sales-pipelines` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/sales-pipelines.md)) |
| Capability Nuxt module skeleton | [`module-crm-sales-pipelines-nuxt`](https://github.com/liberusoftware/module-crm-sales-pipelines-nuxt) (`@liberusoftware/module-crm-sales-pipelines-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Multiple pipelines** | Expose composable and Vue 3 component for `multiple pipelines` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Stages** | Expose composable and Vue 3 component for `stages` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Opportunities** | Expose composable and Vue 3 component for `opportunities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Products** | Expose composable and Vue 3 component for `products` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Values** | Expose composable and Vue 3 component for `values` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Probabilities** | Expose composable and Vue 3 component for `probabilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Close dates** | Expose composable and Vue 3 component for `close dates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Competitors** | Expose composable and Vue 3 component for `competitors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Dependencies** | Expose composable and Vue 3 component for `dependencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Stage history** | Expose composable and Vue 3 component for `stage history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Rotting** | Expose composable and Vue 3 component for `rotting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Loss reasons** | Expose composable and Vue 3 component for `loss reasons` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-pipelines.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PipelineQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Queries/PipelineQuery.php) | `public function pipelines(int $teamId)`<br>`public function stages(int $teamId, int $pipelineId)`<br>`public function opportunities(int $teamId)`<br>`public function rottingOpportunities(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CloseOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CloseOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, string $status, ?string $reason = null): Opportunity` |
| [CreateOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateOpportunity.php) | `public function execute(int $teamId, int $actorId, array $data): Opportunity` |
| [CreatePipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreatePipeline.php) | `public function execute(int $teamId, int $actorId, array $data): SalesPipeline` |
| [CreateStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateStage.php) | `public function execute(int $teamId, int $actorId, array $data): SalesStage` |
| [MoveOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/MoveOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, array $data): Opportunity` |
| [PipelineAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelineAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [PipelinePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelinePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Opportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/Opportunity.php) | No literal fillable array detected; inspect the model and API schema. |
| [SalesPipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesPipeline.php) | No literal fillable array detected; inspect the model and API schema. |
| [SalesStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesStage.php) | No literal fillable array detected; inspect the model and API schema. |
| [StageHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/StageHistory.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PipelineController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-api/src/Http/Controllers/PipelineController.php) | `public function pipelines(Request $r, PipelineQuery $q)`<br>`public function pipeline(Request $r, CreatePipeline $a)`<br>`public function stage(Request $r, CreateStage $a)`<br>`public function opportunities(Request $r, PipelineQuery $q)`<br>`public function rottingOpportunities(Request $r, PipelineQuery $q)`<br>`public function opportunity(Request $r, CreateOpportunity $a)`<br>`public function move(Request $r, int $opportunity, MoveOpportunity $a)`<br>`public function close(Request $r, int $opportunity, string $status, CloseOpportunity $a)` |

**Observed route declarations:**

[modules/crm-sales-pipelines-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-pipelines')->group(function (): void {
Route::get('/pipelines', [PipelineController::class, 'pipelines']);
Route::post('/pipelines', [PipelineController::class, 'pipeline']);
Route::post('/stages', [PipelineController::class, 'stage']);
Route::get('/opportunities', [PipelineController::class, 'opportunities']);
Route::get('/opportunities/rotting', [PipelineController::class, 'rottingOpportunities']);
Route::post('/opportunities', [PipelineController::class, 'opportunity']);
Route::post('/opportunities/{opportunity}/move', [PipelineController::class, 'move']);
Route::post('/opportunities/{opportunity}/close/{status}', [PipelineController::class, 'close'])->whereIn('status', ['won', 'lost']);
```
<!-- layer-implementation-plan:end -->

Read the [source-backed sales-pipeline walkthrough](../guides/SALES-PIPELINES.md) for actual actions, routes, permissions, UI behavior and differences from the target design.
