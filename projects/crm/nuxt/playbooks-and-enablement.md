# CRM: Playbooks and Enablement Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#playbooks-and-enablement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-playbooks-and-enablement-nuxt`
**Matching domain module:** `crm-playbooks-and-enablement`
**Application:** CRM
**Source feature:** [Playbooks and Enablement](../features/playbooks-and-enablement.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/playbooks-and-enablement.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-playbooks-and-enablement` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Guided scripts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Qualification cards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Battlecards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Onboarding content:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Required evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Coaching checklists:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Document/content recommendations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Usage analytics:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-playbooks-and-enablement-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `guided-scripts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `qualification-cards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `battlecards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `onboarding-content`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `required-evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `coaching-checklists`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `document-content-recommendations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `usage-analytics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-playbooks-and-enablement` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/playbooks-and-enablement.md)) |
| Capability Nuxt module skeleton | [`module-crm-playbooks-and-enablement-nuxt`](https://github.com/liberusoftware/module-crm-playbooks-and-enablement-nuxt) (`@liberusoftware/module-crm-playbooks-and-enablement-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Guided scripts** | Expose composable and Vue 3 component for `guided scripts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/playbooks-and-enablement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Qualification cards** | Expose composable and Vue 3 component for `qualification cards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/playbooks-and-enablement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Battlecards** | Expose composable and Vue 3 component for `battlecards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/playbooks-and-enablement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Onboarding content** | Expose composable and Vue 3 component for `onboarding content` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/playbooks-and-enablement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Required evidence** | Expose composable and Vue 3 component for `required evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/playbooks-and-enablement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Coaching checklists** | Expose composable and Vue 3 component for `coaching checklists` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/playbooks-and-enablement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Document/content recommendations** | Expose composable and Vue 3 component for `document/content recommendations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/playbooks-and-enablement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Usage analytics** | Expose composable and Vue 3 component for `usage analytics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/playbooks-and-enablement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PlaybookQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Queries/PlaybookQuery.php) | `public function playbooks(int $teamId)`<br>`public function assignments(int $teamId)`<br>`public function recommendations(int $teamId)`<br>`public function usage(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/AssignPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookAssignment` |
| [CompletePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CompletePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assignmentId, array $input): PlaybookAssignment` |
| [CreatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CreatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Playbook` |
| [RecommendPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecommendPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookRecommendation` |
| [RecordPlaybookUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecordPlaybookUsage.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookUsage` |
| [UpdatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/UpdatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $playbookId, array $input): Playbook` |
| [PlaybookPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Services/PlaybookPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Playbook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/Playbook.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookAssignment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookAssignment.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookRecommendation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookRecommendation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookUsage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PlaybooksAndEnablementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-api/src/Http/Controllers/PlaybooksAndEnablementController.php) | `public function playbooks(Request $r, PlaybookQuery $q)`<br>`public function playbook(Request $r, CreatePlaybook $a)`<br>`public function assignment(Request $r, AssignPlaybook $a)`<br>`public function complete(Request $r, int $assignment, CompletePlaybook $a)`<br>`public function recommendation(Request $r, RecommendPlaybook $a)`<br>`public function usage(Request $r, RecordPlaybookUsage $a)` |

**Observed route declarations:**

[modules/crm-playbooks-and-enablement-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/playbooks-and-enablement')->group(function (): void {
Route::get('/playbooks', [PlaybooksAndEnablementController::class, 'playbooks']);
Route::post('/playbooks', [PlaybooksAndEnablementController::class, 'playbook']);
Route::post('/assignments', [PlaybooksAndEnablementController::class, 'assignment']);
Route::post('/assignments/{assignment}/complete', [PlaybooksAndEnablementController::class, 'complete']);
Route::post('/recommendations', [PlaybooksAndEnablementController::class, 'recommendation']);
Route::post('/usage', [PlaybooksAndEnablementController::class, 'usage']);
```
<!-- layer-implementation-plan:end -->
