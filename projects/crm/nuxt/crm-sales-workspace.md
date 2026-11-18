# CRM: Crm Sales Workspace Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sales-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-sales-workspace-nuxt`
**Matching domain module:** `crm-sales-workspace`
**Application:** CRM
**Source feature:** [Crm Sales Workspace](../features/crm-sales-workspace.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-sales-workspace.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-sales-workspace` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Prioritized seller feed:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Leads/deals inbox:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Overdue/risk indicators:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Next best action:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Daily agenda:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quick updates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contextual customer history:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-sales-workspace-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `prioritized-seller-feed`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `leads-deals-inbox`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `overdue-risk-indicators`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `next-best-action`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `daily-agenda`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quick-updates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contextual-customer-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-sales-workspace` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-sales-workspace.md)) |
| Capability Nuxt module skeleton | [`module-crm-sales-workspace-nuxt`](https://github.com/liberusoftware/module-crm-sales-workspace-nuxt) (`@liberusoftware/module-crm-sales-workspace-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Prioritized seller feed** | Expose composable and Vue 3 component for `prioritized seller feed` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Leads/deals inbox** | Expose composable and Vue 3 component for `leads/deals inbox` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Overdue/risk indicators** | Expose composable and Vue 3 component for `overdue/risk indicators` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Next best action** | Expose composable and Vue 3 component for `next best action` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Daily agenda** | Expose composable and Vue 3 component for `daily agenda` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Quick updates** | Expose composable and Vue 3 component for `quick updates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Contextual customer history** | Expose composable and Vue 3 component for `contextual customer history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WorkspaceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Queries/WorkspaceQuery.php) | `public function feed(int $teamId)`<br>`public function overdue(int $teamId)`<br>`public function agenda(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateWorkspaceItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Actions/CreateWorkspaceItem.php) | `public function execute(int $teamId, int $actorId, array $data): WorkspaceItem` |
| [QuickUpdate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Actions/QuickUpdate.php) | `public function execute(int $teamId, int $actorId, int $id, array $data): WorkspaceUpdate` |
| [WorkspacePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Services/WorkspacePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkspaceItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Models/WorkspaceItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceUpdate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Models/WorkspaceUpdate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkspaceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace-api/src/Http/Controllers/WorkspaceController.php) | `public function feed(Request $r, WorkspaceQuery $q)`<br>`public function overdue(Request $r, WorkspaceQuery $q)`<br>`public function agenda(Request $r, WorkspaceQuery $q)`<br>`public function store(Request $r, CreateWorkspaceItem $a)`<br>`public function update(Request $r, int $item, QuickUpdate $a)` |

**Observed route declarations:**

[modules/crm-sales-workspace-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-workspace')->group(function (): void {
Route::get('/feed', [WorkspaceController::class, 'feed']);
Route::get('/overdue', [WorkspaceController::class, 'overdue']);
Route::get('/agenda', [WorkspaceController::class, 'agenda']);
Route::post('/items', [WorkspaceController::class, 'store']);
Route::patch('/items/{item}', [WorkspaceController::class, 'update']);
```
<!-- layer-implementation-plan:end -->
