# Accounting: Accounting Budgets Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-budgets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-budgets-nuxt`
**Matching domain module:** `accounting-budgets`
**Application:** Accounting
**Source feature:** [Accounting Budgets](../features/accounting-budgets.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-budgets.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-budgets` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Annual/rolling budgets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accounts/dimensions/projects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Imports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Versions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Phasing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Actual comparison:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Revisions:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-budgets-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `annual-rolling-budgets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accounts-dimensions-projects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `imports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `versions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `phasing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `actual-comparison`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `revisions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-budgets` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-budgets.md)) |
| Capability Nuxt module skeleton | [`module-accounting-budgets-nuxt`](https://github.com/liberusoftware/module-accounting-budgets-nuxt) (`@liberusoftware/module-accounting-budgets-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Annual/rolling budgets** | Expose composable and Vue 3 component for `annual/rolling budgets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-budgets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Accounts/dimensions/projects** | Expose composable and Vue 3 component for `accounts/dimensions/projects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-budgets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Imports** | Expose composable and Vue 3 component for `imports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-budgets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Versions** | Expose composable and Vue 3 component for `versions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-budgets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-budgets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Phasing** | Expose composable and Vue 3 component for `phasing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-budgets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Actual comparison** | Expose composable and Vue 3 component for `actual comparison` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-budgets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Revisions** | Expose composable and Vue 3 component for `revisions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-budgets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BudgetQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Queries/BudgetQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddBudgetLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/AddBudgetLine.php) | `public function handle(Budget $budget, array $attributes): BudgetLine` |
| [ApproveBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/ApproveBudget.php) | `public function handle(Budget $budget, int $actorId): Budget` |
| [CreateBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/CreateBudget.php) | `public function handle(array $attributes): Budget` |
| [ReviseBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/ReviseBudget.php) | `public function handle(Budget $budget, array $attributes): Budget` |
| [SubmitBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/SubmitBudget.php) | `public function handle(Budget $budget, int $actorId): Budget` |
| [BudgetsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/src/Policies/BudgetsPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Budget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Models/Budget.php) | `team_id`, `name`, `period_start`, `period_end`, `currency`, `status`, `version`, `notes`, `metadata`, `submitted_by`, `approved_by`, `approved_at`, `rejected_at` |
| [BudgetLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Models/BudgetLine.php) | `budget_id`, `account_id`, `project_id`, `dimensions`, `planned_amount`, `phases`, `actual_amount`, `notes` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BudgetsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/src/Http/Controllers/BudgetsController.php) | `public function index(Request $request, BudgetQuery $query): mixed`<br>`public function store(Request $request, CreateBudget $action): BudgetResource`<br>`public function show(Request $request, Budget $budget): BudgetResource`<br>`public function addLine(Request $request, Budget $budget, AddBudgetLine $action): BudgetResource`<br>`public function submit(Request $request, Budget $budget, SubmitBudget $action): BudgetResource`<br>`public function approve(Request $request, Budget $budget, ApproveBudget $action): BudgetResource`<br>`public function revise(Request $request, Budget $budget, ReviseBudget $action): BudgetResource` |

**Observed route declarations:**

[modules/accounting-budgets-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/budgets')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BudgetsController::class, 'index'])->middleware('ability:accounting.budgets.read');
Route::post('/', [BudgetsController::class, 'store'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/submit', [BudgetsController::class, 'submit'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/lines', [BudgetsController::class, 'addLine'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/approve', [BudgetsController::class, 'approve'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/revise', [BudgetsController::class, 'revise'])->middleware('ability:accounting.budgets.write');
Route::get('/{budget}', [BudgetsController::class, 'show'])->middleware('ability:accounting.budgets.read');
```
<!-- layer-implementation-plan:end -->
