# CRM: Crm Prospecting Agent Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-prospecting-agent). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-prospecting-agent-nuxt`
**Matching domain module:** `crm-prospecting-agent`
**Application:** CRM
**Source feature:** [Crm Prospecting Agent](../features/crm-prospecting-agent.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-prospecting-agent.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-prospecting-agent` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Approved research:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Target selection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Personalization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sequence preparation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Engagement monitoring:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Policy-based review/dispatch:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-prospecting-agent-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `approved-research`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `target-selection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `personalization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sequence-preparation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `engagement-monitoring`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `policy-based-review-dispatch`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-prospecting-agent` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-prospecting-agent.md)) |
| Capability Nuxt module skeleton | [`module-crm-prospecting-agent-nuxt`](https://github.com/liberusoftware/module-crm-prospecting-agent-nuxt) (`@liberusoftware/module-crm-prospecting-agent-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Approved research** | Expose composable and Vue 3 component for `approved research` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-prospecting-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Target selection** | Expose composable and Vue 3 component for `target selection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-prospecting-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Personalization** | Expose composable and Vue 3 component for `personalization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-prospecting-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Sequence preparation** | Expose composable and Vue 3 component for `sequence preparation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-prospecting-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Engagement monitoring** | Expose composable and Vue 3 component for `engagement monitoring` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-prospecting-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Policy-based review/dispatch** | Expose composable and Vue 3 component for `policy-based review/dispatch` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-prospecting-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProspectingAgentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Queries/ProspectingAgentQuery.php) | `public function runs(int $teamId)`<br>`public function targets(int $teamId)`<br>`public function sequences(int $teamId)`<br>`public function engagements(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/ApproveAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $runId): AgentRun` |
| [CreateAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/CreateAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentRun` |
| [DispatchSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/DispatchSequence.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $sequenceId): AgentSequence` |
| [PrepareSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/PrepareSequence.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentSequence` |
| [RecordEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/RecordEngagement.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentEngagement` |
| [SelectTarget.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/SelectTarget.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentTarget` |
| [UpdateAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/UpdateAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $runId, array $input): AgentRun` |
| [ProspectingAgentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Services/ProspectingAgentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentEngagement.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentRun.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentTarget.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentTarget.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProspectingAgentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent-api/src/Http/Controllers/ProspectingAgentController.php) | `public function runs(Request $r, ProspectingAgentQuery $q)`<br>`public function run(Request $r, CreateAgentRun $a)`<br>`public function approve(Request $r, int $run, ApproveAgentRun $a)`<br>`public function target(Request $r, SelectTarget $a)`<br>`public function sequence(Request $r, PrepareSequence $a)`<br>`public function dispatch(Request $r, int $sequence, DispatchSequence $a)`<br>`public function engagement(Request $r, RecordEngagement $a)` |

**Observed route declarations:**

[modules/crm-prospecting-agent-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/prospecting-agent')->group(function (): void {
Route::get('/runs', [ProspectingAgentController::class, 'runs']);
Route::post('/runs', [ProspectingAgentController::class, 'run']);
Route::post('/runs/{run}/approve', [ProspectingAgentController::class, 'approve']);
Route::post('/targets', [ProspectingAgentController::class, 'target']);
Route::post('/sequences', [ProspectingAgentController::class, 'sequence']);
Route::post('/sequences/{sequence}/dispatch', [ProspectingAgentController::class, 'dispatch']);
Route::post('/engagements', [ProspectingAgentController::class, 'engagement']);
```
<!-- layer-implementation-plan:end -->
