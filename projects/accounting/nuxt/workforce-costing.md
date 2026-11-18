# Accounting: Workforce Costing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#workforce-costing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-workforce-costing-nuxt`
**Matching domain module:** `accounting-workforce-costing`
**Application:** Accounting
**Source feature:** [Workforce Costing](../features/workforce-costing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/workforce-costing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-workforce-costing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Time/payroll cost allocation to project:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Department:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Class/location:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Capitalization rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Profitability reporting:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-workforce-costing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `time-payroll-cost-allocation-to-project`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `department`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `class-location`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `capitalization-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `profitability-reporting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-workforce-costing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/workforce-costing.md)) |
| Capability Nuxt module skeleton | [`module-accounting-workforce-costing-nuxt`](https://github.com/liberusoftware/module-accounting-workforce-costing-nuxt) (`@liberusoftware/module-accounting-workforce-costing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Time/payroll cost allocation to project** | Expose composable and Vue 3 component for `time/payroll cost allocation to project` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workforce-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Department** | Expose composable and Vue 3 component for `department` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workforce-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Class/location** | Expose composable and Vue 3 component for `class/location` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workforce-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Capitalization rules** | Expose composable and Vue 3 component for `capitalization rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workforce-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Profitability reporting** | Expose composable and Vue 3 component for `profitability reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workforce-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WorkforceProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Queries/WorkforceProfitability.php) | `public function handle(int $teamId, ?string $from = null, ?string $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/AllocateWorkforceCost.php) | `public function handle(WorkforceCost $cost, string\|WorkforceAllocationType $allocationType, string $allocationRef): WorkforceCost` |
| [CapitalizeWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/CapitalizeWorkforceCost.php) | `public function handle(WorkforceCost $cost): WorkforceCost` |
| [CreateWorkforceCostingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/CreateWorkforceCostingRule.php) | `public function handle(array $attributes): WorkforceCostingRule` |
| [RecordWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/RecordWorkforceCost.php) | `public function handle(array $attributes): WorkforceCost` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Models/WorkforceCost.php) | `team_id`, `worker_ref`, `source_type`, `source_id`, `cost_date`, `hours`, `hourly_rate`, `amount`, `allocation_type`, `allocation_ref`, `capitalized`, `status`, `metadata` |
| [WorkforceCostingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Models/WorkforceCostingRule.php) | `team_id`, `name`, `allocation_type`, `allocation_ref`, `hourly_rate`, `capitalize`, `active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkforceCostingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-api/src/Http/Controllers/WorkforceCostingController.php) | `public function costs(Request $request): mixed`<br>`public function record(Request $request, RecordWorkforceCost $action): mixed`<br>`public function allocate(Request $request, string $cost, AllocateWorkforceCost $action): mixed`<br>`public function capitalize(Request $request, string $cost, CapitalizeWorkforceCost $action): mixed`<br>`public function rules(Request $request): mixed`<br>`public function createRule(Request $request, CreateWorkforceCostingRule $action): mixed`<br>`public function profitability(Request $request, WorkforceProfitability $query): mixed` |

**Observed route declarations:**

[modules/accounting-workforce-costing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/workforce-costing')->middleware('auth:sanctum')->group(function (): void {
Route::get('/costs', [WorkforceCostingController::class, 'costs'])->middleware('ability:accounting.workforce-costing.read');
Route::post('/costs', [WorkforceCostingController::class, 'record'])->middleware('ability:accounting.workforce-costing.write');
Route::post('/costs/{cost}/allocate', [WorkforceCostingController::class, 'allocate'])->middleware('ability:accounting.workforce-costing.write');
Route::post('/costs/{cost}/capitalize', [WorkforceCostingController::class, 'capitalize'])->middleware('ability:accounting.workforce-costing.write');
Route::get('/rules', [WorkforceCostingController::class, 'rules'])->middleware('ability:accounting.workforce-costing.read');
Route::post('/rules', [WorkforceCostingController::class, 'createRule'])->middleware('ability:accounting.workforce-costing.write');
Route::get('/profitability', [WorkforceCostingController::class, 'profitability'])->middleware('ability:accounting.workforce-costing.read');
```
<!-- layer-implementation-plan:end -->
