# Accounting: Accounting Depreciation Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-depreciation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-depreciation-nuxt`
**Matching domain module:** `accounting-depreciation`
**Application:** Accounting
**Source feature:** [Accounting Depreciation](../features/accounting-depreciation.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-depreciation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-depreciation` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Methods:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conventions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Useful life:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Residual value:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Runs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Journals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax books:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Forecast:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-depreciation-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `methods`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conventions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `useful-life`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `residual-value`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `runs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `journals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax-books`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `forecast`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-depreciation` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-depreciation.md)) |
| Capability Nuxt module skeleton | [`module-accounting-depreciation-nuxt`](https://github.com/liberusoftware/module-accounting-depreciation-nuxt) (`@liberusoftware/module-accounting-depreciation-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Methods** | Expose composable and Vue 3 component for `methods` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Conventions** | Expose composable and Vue 3 component for `conventions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Useful life** | Expose composable and Vue 3 component for `useful life` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Residual value** | Expose composable and Vue 3 component for `residual value` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Schedules** | Expose composable and Vue 3 component for `schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Runs** | Expose composable and Vue 3 component for `runs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Journals** | Expose composable and Vue 3 component for `journals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax books** | Expose composable and Vue 3 component for `tax books` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Forecast** | Expose composable and Vue 3 component for `forecast` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-depreciation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DepreciationForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Queries/DepreciationForecast.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDepreciationSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Actions/CreateDepreciationSchedule.php) | `public function handle(array $attributes): DepreciationSchedule` |
| [PostDepreciationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Actions/PostDepreciationRun.php) | `public function handle(DepreciationRun $run, int $actorId, string $journalReference): DepreciationRun` |
| [RunDepreciation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Actions/RunDepreciation.php) | `public function handle(DepreciationSchedule $schedule, string $periodStart, string $periodEnd): DepreciationRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DepreciationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Models/DepreciationRun.php) | `schedule_id`, `team_id`, `period_start`, `period_end`, `amount`, `accumulated_amount`, `status`, `journal_ref`, `posted_by`, `posted_at`, `metadata` |
| [DepreciationSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Models/DepreciationSchedule.php) | `team_id`, `asset_ref`, `book_ref`, `method`, `convention`, `useful_life_months`, `cost`, `residual_value`, `start_date`, `end_date`, `currency`, `status`, `metadata` |
| [DepreciationTaxBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Models/DepreciationTaxBook.php) | `team_id`, `book_ref`, `name`, `jurisdiction`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DepreciationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation-api/src/Http/Controllers/DepreciationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateDepreciationSchedule $action): JsonResponse`<br>`public function run(Request $request, string $schedule, RunDepreciation $action): JsonResponse`<br>`public function post(Request $request, string $run, PostDepreciationRun $action): JsonResponse`<br>`public function forecast(DepreciationForecast $forecast): JsonResponse` |

**Observed route declarations:**

[modules/accounting-depreciation-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/depreciation')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.depreciation.read')->group(function (): void {
Route::get('/schedules', [DepreciationController::class, 'index']);
Route::get('/forecast', [DepreciationController::class, 'forecast']);
Route::middleware('ability:accounting.depreciation.write')->group(function (): void {
Route::post('/schedules', [DepreciationController::class, 'store']);
Route::post('/schedules/{schedule}/runs', [DepreciationController::class, 'run']);
Route::post('/runs/{run}/post', [DepreciationController::class, 'post']);
```
<!-- layer-implementation-plan:end -->
