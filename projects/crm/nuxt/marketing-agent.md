# CRM: Marketing Agent Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing-agent). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-marketing-agent-nuxt`
**Matching domain module:** `crm-marketing-agent`
**Application:** CRM
**Source feature:** [Marketing Agent](../features/marketing-agent.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/marketing-agent.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-marketing-agent` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Audience/campaign/content assistance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Variations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Journey recommendations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Brand/consent checks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Experiments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval workflow:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-marketing-agent-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `audience-campaign-content-assistance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `variations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `journey-recommendations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `brand-consent-checks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `experiments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval-workflow`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-marketing-agent` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/marketing-agent.md)) |
| Capability Nuxt module skeleton | [`module-crm-marketing-agent-nuxt`](https://github.com/liberusoftware/module-crm-marketing-agent-nuxt) (`@liberusoftware/module-crm-marketing-agent-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Audience/campaign/content assistance** | Expose composable and Vue 3 component for `audience/campaign/content assistance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Variations** | Expose composable and Vue 3 component for `variations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Journey recommendations** | Expose composable and Vue 3 component for `journey recommendations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Brand/consent checks** | Expose composable and Vue 3 component for `brand/consent checks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Experiments** | Expose composable and Vue 3 component for `experiments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Approval workflow** | Expose composable and Vue 3 component for `approval workflow` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-agent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Queries/AgentQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAgentRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Actions/CreateAgentRequest.php) | `public function __construct(private readonly MarketingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentRequest` |
| [CreateExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Actions/CreateExperiment.php) | `public function __construct(private readonly MarketingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AgentRequest $request, array $input): AgentExperiment` |
| [RecordAgentCheck.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Actions/RecordAgentCheck.php) | `public function __construct(private readonly MarketingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AgentRequest $request, array $input): AgentCheck` |
| [MarketingAgentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Services/MarketingAgentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgentCheck.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Models/AgentCheck.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Models/AgentExperiment.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Models/AgentRequest.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MarketingAgentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent-api/src/Http/Controllers/MarketingAgentController.php) | `public function index(Request $r, AgentQuery $q): JsonResponse`<br>`public function store(Request $r, CreateAgentRequest $a): JsonResponse`<br>`public function check(Request $r, AgentRequest $request, RecordAgentCheck $a): JsonResponse`<br>`public function experiment(Request $r, AgentRequest $request, CreateExperiment $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
