# CRM: Marketing Development Funds Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing-development-funds). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-marketing-development-funds-nuxt`
**Matching domain module:** `crm-marketing-development-funds`
**Application:** CRM
**Source feature:** [Marketing Development Funds](../features/marketing-development-funds.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/marketing-development-funds.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-marketing-development-funds` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Budgets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Claims:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reimbursements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **ROI:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-marketing-development-funds-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `budgets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `claims`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reimbursements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `roi`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-marketing-development-funds` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/marketing-development-funds.md)) |
| Capability Nuxt module skeleton | [`module-crm-marketing-development-funds-nuxt`](https://github.com/liberusoftware/module-crm-marketing-development-funds-nuxt) (`@liberusoftware/module-crm-marketing-development-funds-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Requests** | Expose composable and Vue 3 component for `requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-development-funds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Budgets** | Expose composable and Vue 3 component for `budgets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-development-funds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Plans** | Expose composable and Vue 3 component for `plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-development-funds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-development-funds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-development-funds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Claims** | Expose composable and Vue 3 component for `claims` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-development-funds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reimbursements** | Expose composable and Vue 3 component for `reimbursements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-development-funds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **ROI** | Expose composable and Vue 3 component for `roi` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing-development-funds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MdfQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Queries/MdfQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFund.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/CreateFund.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MdfFund` |
| [CreateMdfRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/CreateMdfRequest.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MdfFund $fund, array $input): MdfRequest` |
| [RecordMdfEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/RecordMdfEvent.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MdfRequest $request, array $input): MdfRequestEvent` |
| [MdfPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Services/MdfPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MdfFund.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfFund.php) | No literal fillable array detected; inspect the model and API schema. |
| [MdfRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [MdfRequestEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfRequestEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MdfController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds-api/src/Http/Controllers/MdfController.php) | `public function index(Request $r, MdfQuery $q): JsonResponse`<br>`public function store(Request $r, CreateFund $a): JsonResponse`<br>`public function request(Request $r, MdfFund $fund, CreateMdfRequest $a): JsonResponse`<br>`public function event(Request $r, MdfRequest $request, RecordMdfEvent $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
