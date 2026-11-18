# CRM: Service Agent Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#service-agent). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-service-agent-nuxt`
**Matching domain module:** `crm-service-agent`
**Application:** CRM
**Source feature:** [Service Agent](../features/service-agent.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/service-agent.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-service-agent` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Case classification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Knowledge retrieval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Response drafts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Resolution plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tool use:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Escalation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quality review:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-service-agent-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `case-classification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `knowledge-retrieval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `response-drafts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `resolution-plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tool-use`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `escalation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quality-review`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-service-agent` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/service-agent.md)) |
| Capability Nuxt module skeleton | [`module-crm-service-agent-nuxt`](https://github.com/liberusoftware/module-crm-service-agent-nuxt) (`@liberusoftware/module-crm-service-agent-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Case classification** | Expose composable and Vue 3 component for `case classification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Knowledge retrieval** | Expose composable and Vue 3 component for `knowledge retrieval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Response drafts** | Expose composable and Vue 3 component for `response drafts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Resolution plans** | Expose composable and Vue 3 component for `resolution plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Tool use** | Expose composable and Vue 3 component for `tool use` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Confidence** | Expose composable and Vue 3 component for `confidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Escalation** | Expose composable and Vue 3 component for `escalation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Quality review** | Expose composable and Vue 3 component for `quality review` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Queries/AgentQuery.php) | `public function cases(int $teamId)`<br>`public function knowledge(int $teamId, string $search = '')`<br>`public function tools(int $teamId)`<br>`public function reviews(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ClassifyCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/ClassifyCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, array $data): AgentCase` |
| [CreateAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/CreateAgentCase.php) | `public function execute(int $teamId, int $actorId, array $data): AgentCase` |
| [EscalateAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/EscalateAgentCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, array $data = []): AgentCase` |
| [RetrieveKnowledge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/RetrieveKnowledge.php) | `public function execute(int $teamId, int $actorId, array $data)` |
| [ReviewAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/ReviewAgentCase.php) | `public function execute(int $teamId, int $actorId, array $data): AgentReview` |
| [RunAgentTool.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/RunAgentTool.php) | `public function execute(int $teamId, int $actorId, array $data): AgentToolRun` |
| [UpdateAgentOutput.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/UpdateAgentOutput.php) | `public function execute(int $teamId, int $actorId, int $caseId, string $type, array $data): AgentCase` |
| [AgentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Services/AgentAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [AgentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Services/AgentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentKnowledge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentKnowledge.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentToolRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentToolRun.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AgentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent-api/src/Http/Controllers/AgentController.php) | `public function cases(Request $r, AgentQuery $q)`<br>`public function storeCase(Request $r, CreateAgentCase $a)`<br>`public function classify(Request $r, int $case, ClassifyCase $a)`<br>`public function knowledge(Request $r, RetrieveKnowledge $a)`<br>`public function output(Request $r, int $case, string $type, UpdateAgentOutput $a)`<br>`public function tool(Request $r, RunAgentTool $a)`<br>`public function escalate(Request $r, int $case, EscalateAgentCase $a)`<br>`public function review(Request $r, ReviewAgentCase $a)` |

**Observed route declarations:**

[modules/crm-service-agent-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/service-agent')->group(function (): void {
Route::get('/cases', [AgentController::class, 'cases']);
Route::post('/cases', [AgentController::class, 'storeCase']);
Route::post('/cases/{case}/classify', [AgentController::class, 'classify']);
Route::post('/cases/{case}/output/{type}', [AgentController::class, 'output'])->whereIn('type', ['draft', 'plan']);
Route::post('/cases/{case}/escalate', [AgentController::class, 'escalate']);
Route::get('/knowledge', [AgentController::class, 'knowledge']);
Route::post('/tools', [AgentController::class, 'tool']);
Route::post('/reviews', [AgentController::class, 'review']);
```
<!-- layer-implementation-plan:end -->
