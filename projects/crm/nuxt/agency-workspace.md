# CRM: Agency Workspace Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#agency-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-agency-workspace-nuxt`
**Matching domain module:** `crm-agency-workspace`
**Application:** CRM
**Source feature:** [Agency Workspace](../features/agency-workspace.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/agency-workspace.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-agency-workspace` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agency/client hierarchy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sub-accounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delegated administration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Usage visibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Support access:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Branding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cross-account operations:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-agency-workspace-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `agency-client-hierarchy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sub-accounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delegated-administration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `usage-visibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `support-access`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `branding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cross-account-operations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-agency-workspace` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/agency-workspace.md)) |
| Capability Nuxt module skeleton | [`module-crm-agency-workspace-nuxt`](https://github.com/liberusoftware/module-crm-agency-workspace-nuxt) (`@liberusoftware/module-crm-agency-workspace-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Agency/client hierarchy** | Expose composable and Vue 3 component for `agency/client hierarchy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/agency-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Sub-accounts** | Expose composable and Vue 3 component for `sub-accounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/agency-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Delegated administration** | Expose composable and Vue 3 component for `delegated administration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/agency-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Usage visibility** | Expose composable and Vue 3 component for `usage visibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/agency-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Support access** | Expose composable and Vue 3 component for `support access` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/agency-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Branding** | Expose composable and Vue 3 component for `branding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/agency-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Cross-account operations** | Expose composable and Vue 3 component for `cross-account operations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/agency-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgencyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Queries/AgencyQuery.php) | `public function accounts(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/CreateAgencyAccount.php) | `public function execute(int $teamId, int $ownerId, array $input): AgencyAccount` |
| [GrantAgencyAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/GrantAgencyAccess.php) | `public function execute(int $teamId, int $actorId, AgencyAccount $account, array $input): AgencyAccess` |
| [UpdateAgencyUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/UpdateAgencyUsage.php) | `public function execute(int $teamId, int $actorId, AgencyAccount $account, array $input): AgencyAccount` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgencyAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAccess.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgencyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAudit.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AgencyWorkspaceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-api/src/Http/Controllers/AgencyWorkspaceController.php) | `public function __construct(private readonly AgencyQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAgencyAccount $action): JsonResponse`<br>`public function grantAccess(Request $request, AgencyAccount $account, GrantAgencyAccess $action): JsonResponse`<br>`public function usage(Request $request, AgencyAccount $account, UpdateAgencyUsage $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-agency-workspace-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/agency-workspace')->group(function (): void {
Route::get('accounts', [AgencyWorkspaceController::class, 'index']);
Route::post('accounts', [AgencyWorkspaceController::class, 'store']);
Route::post('accounts/{account}/access', [AgencyWorkspaceController::class, 'grantAccess']);
Route::post('accounts/{account}/usage', [AgencyWorkspaceController::class, 'usage']);
```
<!-- layer-implementation-plan:end -->
