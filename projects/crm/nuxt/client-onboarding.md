# CRM: Client Onboarding Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#client-onboarding). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-client-onboarding-nuxt`
**Matching domain module:** `crm-client-onboarding`
**Application:** CRM
**Source feature:** [Client Onboarding](../features/client-onboarding.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/client-onboarding.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-client-onboarding` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Intake:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Domain/provider connections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Data import:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Snapshot application:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Verification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Launch checklist:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Training:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Handoff:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Health:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-client-onboarding-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `intake`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `domain-provider-connections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `data-import`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `snapshot-application`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `verification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `launch-checklist`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `training`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `health`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-client-onboarding` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/client-onboarding.md)) |
| Capability Nuxt module skeleton | [`module-crm-client-onboarding-nuxt`](https://github.com/liberusoftware/module-crm-client-onboarding-nuxt) (`@liberusoftware/module-crm-client-onboarding-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Intake** | Expose composable and Vue 3 component for `intake` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Domain/provider connections** | Expose composable and Vue 3 component for `domain/provider connections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Data import** | Expose composable and Vue 3 component for `data import` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Snapshot application** | Expose composable and Vue 3 component for `snapshot application` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Verification** | Expose composable and Vue 3 component for `verification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Launch checklist** | Expose composable and Vue 3 component for `launch checklist` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Training** | Expose composable and Vue 3 component for `training` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Handoff** | Expose composable and Vue 3 component for `handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Health** | Expose composable and Vue 3 component for `health` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-onboarding.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ClientOnboardingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Queries/ClientOnboardingQuery.php) | `public function onboardings(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteOnboardingStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Actions/CompleteOnboardingStep.php) | `public function execute(int $teamId, int $actorId, ClientOnboarding $onboarding, string $kind, string $label, array $evidence = []): ClientOnboardingStep` |
| [StartClientOnboarding.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Actions/StartClientOnboarding.php) | `public function execute(int $teamId, int $ownerId, string $clientKey, array $intake = []): ClientOnboarding` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ClientOnboarding.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Models/ClientOnboarding.php) | No literal fillable array detected; inspect the model and API schema. |
| [ClientOnboardingStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Models/ClientOnboardingStep.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ClientOnboardingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-api/src/Http/Controllers/ClientOnboardingController.php) | `public function __construct(private readonly ClientOnboardingQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(StartClientOnboarding $a): JsonResponse`<br>`public function step(ClientOnboarding $onboarding, CompleteOnboardingStep $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-client-onboarding-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/client-onboarding')->group(function (): void {
Route::get('/', [ClientOnboardingController::class, 'index']);
Route::post('/', [ClientOnboardingController::class, 'store']);
Route::post('{onboarding}/steps', [ClientOnboardingController::class, 'step']);
```
<!-- layer-implementation-plan:end -->
