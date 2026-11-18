# CRM: Journey Orchestration Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#journey-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-journey-orchestration-nuxt`
**Matching domain module:** `crm-journey-orchestration`
**Application:** CRM
**Source feature:** [Journey Orchestration](../features/journey-orchestration.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/journey-orchestration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-journey-orchestration` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Triggered/scheduled journeys:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Branching:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Waits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Goals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Re-entry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Suppression:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Frequency caps:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Experiments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stop-on-response:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Versioned publication:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-journey-orchestration-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `triggered-scheduled-journeys`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `branching`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `waits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `goals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `re-entry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `suppression`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `frequency-caps`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `experiments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stop-on-response`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `versioned-publication`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-journey-orchestration` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/journey-orchestration.md)) |
| Capability Nuxt module skeleton | [`module-crm-journey-orchestration-nuxt`](https://github.com/liberusoftware/module-crm-journey-orchestration-nuxt) (`@liberusoftware/module-crm-journey-orchestration-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Triggered/scheduled journeys** | Expose composable and Vue 3 component for `triggered/scheduled journeys` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Branching** | Expose composable and Vue 3 component for `branching` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Waits** | Expose composable and Vue 3 component for `waits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Goals** | Expose composable and Vue 3 component for `goals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Re-entry** | Expose composable and Vue 3 component for `re-entry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Suppression** | Expose composable and Vue 3 component for `suppression` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Frequency caps** | Expose composable and Vue 3 component for `frequency caps` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Experiments** | Expose composable and Vue 3 component for `experiments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Stop-on-response** | Expose composable and Vue 3 component for `stop-on-response` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Versioned publication** | Expose composable and Vue 3 component for `versioned publication` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journey-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [JourneyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Queries/JourneyQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateJourney.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Actions/CreateJourney.php) | `public function __construct(private readonly JourneyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Journey` |
| [PublishJourney.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Actions/PublishJourney.php) | `public function __construct(private readonly JourneyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Journey $journey, array $input): Journey` |
| [StartJourneyRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Actions/StartJourneyRun.php) | `public function __construct(private readonly JourneyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Journey $journey, array $input): JourneyRun` |
| [StopJourneyRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Actions/StopJourneyRun.php) | `public function __construct(private readonly JourneyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, JourneyRun $run, array $input): JourneyEvent` |
| [JourneyPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Services/JourneyPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Journey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Models/Journey.php) | No literal fillable array detected; inspect the model and API schema. |
| [JourneyEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Models/JourneyEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [JourneyRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Models/JourneyRun.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [JourneyController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration-api/src/Http/Controllers/JourneyController.php) | `public function index(Request $r, JourneyQuery $q): JsonResponse`<br>`public function store(Request $r, CreateJourney $a): JsonResponse`<br>`public function publish(Request $r, Journey $journey, PublishJourney $a): JsonResponse`<br>`public function run(Request $r, Journey $journey, StartJourneyRun $a): JsonResponse`<br>`public function stop(Request $r, JourneyRun $run, StopJourneyRun $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
