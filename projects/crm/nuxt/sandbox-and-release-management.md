# CRM: Sandbox and Release Management Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sandbox-and-release-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-sandbox-and-release-management-nuxt`
**Matching domain module:** `crm-sandbox-and-release-management`
**Application:** CRM
**Source feature:** [Sandbox and Release Management](../features/sandbox-and-release-management.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/sandbox-and-release-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-sandbox-and-release-management` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Configuration snapshots:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Test data policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Change sets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dependency analysis:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Promotion:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rollback:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Environment comparison:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-sandbox-and-release-management-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `configuration-snapshots`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `test-data-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `change-sets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dependency-analysis`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `promotion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rollback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `environment-comparison`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-sandbox-and-release-management` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/sandbox-and-release-management.md)) |
| Capability Nuxt module skeleton | [`module-crm-sandbox-and-release-management-nuxt`](https://github.com/liberusoftware/module-crm-sandbox-and-release-management-nuxt) (`@liberusoftware/module-crm-sandbox-and-release-management-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Configuration snapshots** | Expose composable and Vue 3 component for `configuration snapshots` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sandbox-and-release-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Test data policy** | Expose composable and Vue 3 component for `test data policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sandbox-and-release-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Change sets** | Expose composable and Vue 3 component for `change sets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sandbox-and-release-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sandbox-and-release-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Dependency analysis** | Expose composable and Vue 3 component for `dependency analysis` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sandbox-and-release-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Promotion** | Expose composable and Vue 3 component for `promotion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sandbox-and-release-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Rollback** | Expose composable and Vue 3 component for `rollback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sandbox-and-release-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Environment comparison** | Expose composable and Vue 3 component for `environment comparison` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sandbox-and-release-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReleaseQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Queries/ReleaseQuery.php) | `public function snapshots(int $teamId)`<br>`public function changesets(int $teamId)`<br>`public function deployments(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateChangeset.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseChangeset` |
| [CreateSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateSnapshot.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseSnapshot` |
| [PromoteChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/PromoteChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [RollbackChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/RollbackChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [ValidateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/ValidateChangeset.php) | `public function execute(int $teamId, int $actorId, int $id): ReleaseChangeset` |
| [ReleaseAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleaseAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [ReleasePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleasePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReleaseChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseChangeset.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReleaseDeployment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseDeployment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReleaseSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReleaseController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-api/src/Http/Controllers/ReleaseController.php) | `public function snapshots(Request $r, ReleaseQuery $q)`<br>`public function snapshot(Request $r, CreateSnapshot $a)`<br>`public function changesets(Request $r, ReleaseQuery $q)`<br>`public function changeset(Request $r, CreateChangeset $a)`<br>`public function validateSet(Request $r, int $set, ValidateChangeset $a)`<br>`public function promote(Request $r, int $set, PromoteChangeset $a)`<br>`public function rollback(Request $r, int $set, RollbackChangeset $a)` |

**Observed route declarations:**

[modules/crm-sandbox-and-release-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sandbox-and-release-management')->group(function (): void {
Route::get('/snapshots', [ReleaseController::class, 'snapshots']);
Route::post('/snapshots', [ReleaseController::class, 'snapshot']);
Route::get('/changesets', [ReleaseController::class, 'changesets']);
Route::post('/changesets', [ReleaseController::class, 'changeset']);
Route::post('/changesets/{set}/validate', [ReleaseController::class, 'validateSet']);
Route::post('/changesets/{set}/promote', [ReleaseController::class, 'promote']);
Route::post('/changesets/{set}/rollback', [ReleaseController::class, 'rollback']);
```
<!-- layer-implementation-plan:end -->
