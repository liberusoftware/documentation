# Accounting: Accounting Job Estimates Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-job-estimates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-job-estimates-nuxt`
**Matching domain module:** `accounting-job-estimates`
**Application:** Accounting
**Source feature:** [Accounting Job Estimates](../features/accounting-job-estimates.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-job-estimates.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-job-estimates` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Cost/revenue estimates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quantities/rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Versions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Actual comparison:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Estimate-at-completion:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-job-estimates-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `cost-revenue-estimates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quantities-rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `versions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `actual-comparison`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `estimate-at-completion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-job-estimates` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-job-estimates.md)) |
| Capability Nuxt module skeleton | [`module-accounting-job-estimates-nuxt`](https://github.com/liberusoftware/module-accounting-job-estimates-nuxt) (`@liberusoftware/module-accounting-job-estimates-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Cost/revenue estimates** | Expose composable and Vue 3 component for `cost/revenue estimates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-job-estimates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Quantities/rates** | Expose composable and Vue 3 component for `quantities/rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-job-estimates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Versions** | Expose composable and Vue 3 component for `versions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-job-estimates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-job-estimates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Actual comparison** | Expose composable and Vue 3 component for `actual comparison` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-job-estimates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Estimate-at-completion** | Expose composable and Vue 3 component for `estimate-at-completion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-job-estimates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [JobEstimateQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Queries/JobEstimateQuery.php) | `public function paginate(?int $teamId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function comparison(JobEstimate $estimate): array`<br>`public function estimateAtCompletion(JobEstimate $estimate): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEstimateLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/AddEstimateLine.php) | `public function handle(JobEstimate $estimate, array $attributes): EstimateLine` |
| [CreateEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/CreateEstimate.php) | `public function handle(array $attributes): JobEstimate` |
| [CreateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/CreateVersion.php) | `public function handle(JobEstimate $estimate, ?string $notes = null): EstimateVersion` |
| [DecideEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/DecideEstimate.php) | `public function handle(JobEstimate $estimate, string $actor, bool $approved, ?string $comment = null): JobEstimate` |
| [RecordActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/RecordActual.php) | `public function handle(JobEstimate $estimate, array $attributes): EstimateActual` |
| [SubmitEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/SubmitEstimate.php) | `public function handle(JobEstimate $estimate): JobEstimate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EstimateActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateActual.php) | `estimate_id`, `version_id`, `line_ref`, `category`, `amount`, `source_ref`, `occurred_at`, `metadata` |
| [EstimateApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateApproval.php) | `estimate_id`, `version_id`, `actor_ref`, `decision`, `comment`, `decided_at`, `metadata` |
| [EstimateLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateLine.php) | `estimate_id`, `version_id`, `line_ref`, `line_type`, `category`, `description`, `quantity`, `rate`, `amount`, `actual_amount`, `metadata` |
| [EstimateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateVersion.php) | `estimate_id`, `version_no`, `status`, `notes`, `total_cost`, `total_revenue`, `metadata` |
| [JobEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/JobEstimate.php) | `team_id`, `estimate_ref`, `project_ref`, `title`, `currency`, `status`, `version_no`, `total_cost`, `total_revenue`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [JobEstimatesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates-api/src/Http/Controllers/JobEstimatesController.php) | `public function __construct(private readonly JobEstimateQuery $query)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreateEstimate $action): JsonResponse`<br>`public function show(Request $request, JobEstimate $estimate): JobEstimateResource`<br>`public function line(Request $request, JobEstimate $estimate, AddEstimateLine $action): JobEstimateResource`<br>`public function submit(JobEstimate $estimate, SubmitEstimate $action): JobEstimateResource`<br>`public function decide(Request $request, JobEstimate $estimate, DecideEstimate $action): JobEstimateResource`<br>`public function version(Request $request, JobEstimate $estimate, CreateVersion $action): JobEstimateResource`<br>`public function actual(Request $request, JobEstimate $estimate, RecordActual $action): JobEstimateResource`<br>`public function comparison(JobEstimate $estimate, JobEstimateQuery $query): JsonResponse`<br>`public function eac(JobEstimate $estimate, JobEstimateQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/accounting-job-estimates-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/job-estimates')->group(function (): void {
Route::middleware('ability:accounting.job-estimates.read')->group(function (): void {
Route::get('/', [JobEstimatesController::class, 'index'])->name('accounting.job-estimates.list');
Route::get('/{estimate}/comparison', [JobEstimatesController::class, 'comparison'])->name('accounting.job-estimates.comparison');
Route::get('/{estimate}/eac', [JobEstimatesController::class, 'eac'])->name('accounting.job-estimates.eac');
Route::get('/{estimate}', [JobEstimatesController::class, 'show'])->name('accounting.job-estimates.show');
Route::middleware('ability:accounting.job-estimates.write')->group(function (): void {
Route::post('/', [JobEstimatesController::class, 'store'])->name('accounting.job-estimates.create');
Route::post('/{estimate}/lines', [JobEstimatesController::class, 'line'])->name('accounting.job-estimates.line');
Route::post('/{estimate}/submit', [JobEstimatesController::class, 'submit'])->name('accounting.job-estimates.submit');
Route::post('/{estimate}/decide', [JobEstimatesController::class, 'decide'])->name('accounting.job-estimates.decide');
Route::post('/{estimate}/versions', [JobEstimatesController::class, 'version'])->name('accounting.job-estimates.version');
Route::post('/{estimate}/actuals', [JobEstimatesController::class, 'actual'])->name('accounting.job-estimates.actual');
```
<!-- layer-implementation-plan:end -->
