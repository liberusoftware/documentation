# Accounting: Consolidation Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#consolidation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-consolidation-nuxt`
**Matching domain module:** `accounting-consolidation`
**Application:** Accounting
**Source feature:** [Consolidation](../features/consolidation.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/consolidation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-consolidation` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Group hierarchy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mappings:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Currency translation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Intercompany eliminations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ownership/minority interests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Adjustments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Group close:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-consolidation-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `group-hierarchy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mappings`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `currency-translation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `intercompany-eliminations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ownership-minority-interests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `adjustments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `group-close`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-consolidation` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/consolidation.md)) |
| Capability Nuxt module skeleton | [`module-accounting-consolidation-nuxt`](https://github.com/liberusoftware/module-accounting-consolidation-nuxt) (`@liberusoftware/module-accounting-consolidation-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Group hierarchy** | Expose composable and Vue 3 component for `group hierarchy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/consolidation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Mappings** | Expose composable and Vue 3 component for `mappings` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/consolidation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Currency translation** | Expose composable and Vue 3 component for `currency translation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/consolidation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Intercompany eliminations** | Expose composable and Vue 3 component for `intercompany eliminations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/consolidation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Ownership/minority interests** | Expose composable and Vue 3 component for `ownership/minority interests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/consolidation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Adjustments** | Expose composable and Vue 3 component for `adjustments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/consolidation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Group close** | Expose composable and Vue 3 component for `group close` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/consolidation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConsolidationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Queries/ConsolidationQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddConsolidationEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/AddConsolidationEntity.php) | `public function handle(ConsolidationGroup $group, array $entity): ConsolidationGroup` |
| [CreateConsolidationGroup.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/CreateConsolidationGroup.php) | `public function handle(array $attributes): ConsolidationGroup` |
| [PrepareConsolidatedReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/PrepareConsolidatedReport.php) | `public function handle(ConsolidationGroup $group, array $report): ConsolidationGroup` |
| [PublishConsolidatedReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/PublishConsolidatedReport.php) | `public function handle(ConsolidationGroup $group, array $translation = []): ConsolidationGroup` |
| [RecordEliminations.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/RecordEliminations.php) | `public function handle(ConsolidationGroup $group, array $elimination): ConsolidationGroup` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConsolidationGroup.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Models/ConsolidationGroup.php) | `team_id`, `group_ref`, `name`, `reporting_currency`, `status`, `entities`, `eliminations`, `translation`, `report` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConsolidationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation-api/src/Http/Controllers/ConsolidationController.php) | `public function index(ConsolidationQuery $query): JsonResponse`<br>`public function store(Request $request, CreateConsolidationGroup $action): JsonResponse`<br>`public function entity(Request $request, string $group, AddConsolidationEntity $action): JsonResponse`<br>`public function prepare(Request $request, string $group, PrepareConsolidatedReport $action): JsonResponse`<br>`public function publish(Request $request, string $group, PublishConsolidatedReport $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-consolidation-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/consolidation')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.consolidation.read')->get('/', [ConsolidationController::class, 'index']);
Route::middleware('ability:accounting.consolidation.write')->group(function (): void {
Route::post('/', [ConsolidationController::class, 'store']);
Route::post('/{group}/entities', [ConsolidationController::class, 'entity']);
Route::post('/{group}/prepare', [ConsolidationController::class, 'prepare']);
Route::post('/{group}/publish', [ConsolidationController::class, 'publish']);
```
<!-- layer-implementation-plan:end -->
