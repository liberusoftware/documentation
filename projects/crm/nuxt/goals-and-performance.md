# CRM: Goals and Performance Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#goals-and-performance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-goals-and-performance-nuxt`
**Matching domain module:** `crm-goals-and-performance`
**Application:** CRM
**Source feature:** [Goals and Performance](../features/goals-and-performance.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/goals-and-performance.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-goals-and-performance` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Individual/team/company goals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Activity/outcome targets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scorecards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Leaderboards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reviews:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Coaching plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Performance history:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-goals-and-performance-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `individual-team-company-goals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `activity-outcome-targets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scorecards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `leaderboards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reviews`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `coaching-plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `performance-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-goals-and-performance` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/goals-and-performance.md)) |
| Capability Nuxt module skeleton | [`module-crm-goals-and-performance-nuxt`](https://github.com/liberusoftware/module-crm-goals-and-performance-nuxt) (`@liberusoftware/module-crm-goals-and-performance-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Individual/team/company goals** | Expose composable and Vue 3 component for `individual/team/company goals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goals-and-performance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Activity/outcome targets** | Expose composable and Vue 3 component for `activity/outcome targets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goals-and-performance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Scorecards** | Expose composable and Vue 3 component for `scorecards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goals-and-performance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Leaderboards** | Expose composable and Vue 3 component for `leaderboards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goals-and-performance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reviews** | Expose composable and Vue 3 component for `reviews` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goals-and-performance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Coaching plans** | Expose composable and Vue 3 component for `coaching plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goals-and-performance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Performance history** | Expose composable and Vue 3 component for `performance history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/goals-and-performance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PerformanceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Queries/PerformanceQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/CreateGoal.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PerformanceGoal` |
| [RecordReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/RecordReview.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PerformanceReview` |
| [UpdateGoalActual.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/UpdateGoalActual.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, PerformanceGoal $goal, array $input): PerformanceEvent` |
| [PerformancePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Services/PerformancePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PerformanceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [PerformanceGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceGoal.php) | No literal fillable array detected; inspect the model and API schema. |
| [PerformanceReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceReview.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PerformanceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance-api/src/Http/Controllers/PerformanceController.php) | `public function index(Request $r, PerformanceQuery $q): JsonResponse`<br>`public function store(Request $r, CreateGoal $a): JsonResponse`<br>`public function event(Request $r, PerformanceGoal $goal, UpdateGoalActual $a): JsonResponse`<br>`public function review(Request $r, RecordReview $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
