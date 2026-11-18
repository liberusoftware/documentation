# CRM: Crm Projects Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-projects). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-projects-nuxt`
**Matching domain module:** `crm-projects`
**Application:** CRM
**Source feature:** [Crm Projects](../features/crm-projects.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-projects.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-projects` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Post-sale projects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Milestones:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tasks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dependencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Owners:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Time:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Files:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Risks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Client visibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Opportunity handoff:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-projects-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `post-sale-projects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `milestones`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tasks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dependencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `owners`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `time`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `files`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `risks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `client-visibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `opportunity-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-projects` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-projects.md)) |
| Capability Nuxt module skeleton | [`module-crm-projects-nuxt`](https://github.com/liberusoftware/module-crm-projects-nuxt) (`@liberusoftware/module-crm-projects-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Post-sale projects** | Expose composable and Vue 3 component for `post-sale projects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Milestones** | Expose composable and Vue 3 component for `milestones` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Tasks** | Expose composable and Vue 3 component for `tasks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Dependencies** | Expose composable and Vue 3 component for `dependencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Owners** | Expose composable and Vue 3 component for `owners` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Time** | Expose composable and Vue 3 component for `time` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Files** | Expose composable and Vue 3 component for `files` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Status** | Expose composable and Vue 3 component for `status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Risks** | Expose composable and Vue 3 component for `risks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Client visibility** | Expose composable and Vue 3 component for `client visibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Opportunity handoff** | Expose composable and Vue 3 component for `opportunity handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-projects.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Queries/ProjectQuery.php) | `public function templates(int $teamId)`<br>`public function projects(int $teamId)`<br>`public function tasks(int $teamId)`<br>`public function risks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeProjectStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/ChangeProjectStatus.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, string $status): Project` |
| [CreateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/CreateProject.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Project` |
| [CreateProjectTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/CreateProjectTask.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectTask` |
| [HandoffOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/HandoffOpportunity.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, int $opportunityId): Project` |
| [LogProjectTime.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/LogProjectTime.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectTime` |
| [RecordProjectRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/RecordProjectRisk.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectRisk` |
| [UpdateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/UpdateProject.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, array $input): Project` |
| [ProjectPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Services/ProjectPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Project.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/Project.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectRisk.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTask.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTime.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTime.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProjectsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-api/src/Http/Controllers/ProjectsController.php) | `public function projects(Request $r, ProjectQuery $q)`<br>`public function project(Request $r, CreateProject $a)`<br>`public function task(Request $r, CreateProjectTask $a)`<br>`public function time(Request $r, LogProjectTime $a)`<br>`public function status(Request $r, int $project, string $status, ChangeProjectStatus $a)`<br>`public function risk(Request $r, RecordProjectRisk $a)`<br>`public function handoff(Request $r, int $project, HandoffOpportunity $a)` |

**Observed route declarations:**

[modules/crm-projects-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/projects')->group(function (): void {
Route::get('/', [ProjectsController::class, 'projects']);
Route::post('/', [ProjectsController::class, 'project']);
Route::post('/tasks', [ProjectsController::class, 'task']);
Route::post('/time', [ProjectsController::class, 'time']);
Route::post('/risks', [ProjectsController::class, 'risk']);
Route::post('/{project}/{status}', [ProjectsController::class, 'status'])->whereIn('status', ['planning', 'active', 'at_risk', 'on_hold', 'completed', 'cancelled']);
Route::post('/{project}/handoff', [ProjectsController::class, 'handoff']);
```
<!-- layer-implementation-plan:end -->
