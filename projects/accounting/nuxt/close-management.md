# Accounting: Close Management Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#close-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-close-management-nuxt`
**Matching domain module:** `accounting-close-management`
**Application:** Accounting
**Source feature:** [Close Management](../features/close-management.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/close-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-close-management` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Checklist:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Owners:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dependencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Due dates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Adjustments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Review:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Certification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lock:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reopen:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-close-management-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `checklist`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `owners`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dependencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `due-dates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `adjustments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `review`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `certification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lock`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reopen`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-close-management` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/close-management.md)) |
| Capability Nuxt module skeleton | [`module-accounting-close-management-nuxt`](https://github.com/liberusoftware/module-accounting-close-management-nuxt) (`@liberusoftware/module-accounting-close-management-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Checklist** | Expose composable and Vue 3 component for `checklist` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Owners** | Expose composable and Vue 3 component for `owners` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Dependencies** | Expose composable and Vue 3 component for `dependencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Due dates** | Expose composable and Vue 3 component for `due dates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliations** | Expose composable and Vue 3 component for `reconciliations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Adjustments** | Expose composable and Vue 3 component for `adjustments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Review** | Expose composable and Vue 3 component for `review` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Certification** | Expose composable and Vue 3 component for `certification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Lock** | Expose composable and Vue 3 component for `lock` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reopen** | Expose composable and Vue 3 component for `reopen` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/close-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CloseCycleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Queries/CloseCycleQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CertifyCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/CertifyCloseCycle.php) | `public function handle(CloseCycle $cycle, array $certification): CloseCycle` |
| [CreateCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/CreateCloseCycle.php) | `public function handle(array $attributes): CloseCycle` |
| [LockCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/LockCloseCycle.php) | `public function handle(CloseCycle $cycle): CloseCycle` |
| [RecordCloseEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/RecordCloseEvidence.php) | `public function handle(CloseCycle $cycle, array $evidence): CloseCycle` |
| [ReopenCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/ReopenCloseCycle.php) | `public function handle(CloseCycle $cycle, string $reason): CloseCycle` |
| [UpdateCloseChecklist.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/UpdateCloseChecklist.php) | `public function handle(CloseCycle $cycle, array $checklist): CloseCycle` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Models/CloseCycle.php) | `team_id`, `cycle_ref`, `period`, `due_date`, `status`, `checklist`, `owners`, `dependencies`, `evidence`, `reconciliations`, `adjustments`, `review`, `certification` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CloseCyclesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management-api/src/Http/Controllers/CloseCyclesController.php) | `public function index(CloseCycleQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCloseCycle $action): JsonResponse`<br>`public function checklist(Request $request, string $cycle, UpdateCloseChecklist $action): JsonResponse`<br>`public function evidence(Request $request, string $cycle, RecordCloseEvidence $action): JsonResponse`<br>`public function certify(Request $request, string $cycle, CertifyCloseCycle $action): JsonResponse`<br>`public function lock(string $cycle, LockCloseCycle $action): JsonResponse`<br>`public function reopen(Request $request, string $cycle, ReopenCloseCycle $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-close-management-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/close-management')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.close-management.read')->get('/', [CloseCyclesController::class, 'index']);
Route::middleware('ability:accounting.close-management.write')->group(function (): void {
Route::post('/', [CloseCyclesController::class, 'store']);
Route::post('/{cycle}/checklist', [CloseCyclesController::class, 'checklist']);
Route::post('/{cycle}/evidence', [CloseCyclesController::class, 'evidence']);
Route::post('/{cycle}/certify', [CloseCyclesController::class, 'certify']);
Route::post('/{cycle}/lock', [CloseCyclesController::class, 'lock']);
Route::post('/{cycle}/reopen', [CloseCyclesController::class, 'reopen']);
```
<!-- layer-implementation-plan:end -->
