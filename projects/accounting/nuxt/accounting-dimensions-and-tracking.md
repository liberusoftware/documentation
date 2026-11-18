# Accounting: Accounting Dimensions And Tracking Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-dimensions-and-tracking). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-dimensions-and-tracking-nuxt`
**Matching domain module:** `accounting-dimensions-and-tracking`
**Application:** Accounting
**Source feature:** [Accounting Dimensions And Tracking](../features/accounting-dimensions-and-tracking.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-dimensions-and-tracking.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-dimensions-and-tracking` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Classes/categories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Locations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Departments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost/profit centers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Projects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tags:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Allocations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dimensional balances:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-dimensions-and-tracking-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `classes-categories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `locations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `departments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-profit-centers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `projects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tags`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `allocations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dimensional-balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-dimensions-and-tracking` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-dimensions-and-tracking.md)) |
| Capability Nuxt module skeleton | [`module-accounting-dimensions-and-tracking-nuxt`](https://github.com/liberusoftware/module-accounting-dimensions-and-tracking-nuxt) (`@liberusoftware/module-accounting-dimensions-and-tracking-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Classes/categories** | Expose composable and Vue 3 component for `classes/categories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Locations** | Expose composable and Vue 3 component for `locations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Departments** | Expose composable and Vue 3 component for `departments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cost/profit centers** | Expose composable and Vue 3 component for `cost/profit centers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Projects** | Expose composable and Vue 3 component for `projects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tags** | Expose composable and Vue 3 component for `tags` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Allocations** | Expose composable and Vue 3 component for `allocations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Dimensional balances** | Expose composable and Vue 3 component for `dimensional balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dimensions-and-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DimensionalBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Queries/DimensionalBalances.php) | `public function handle(?string $key = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateDimensions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Actions/AllocateDimensions.php) | `public function handle(string $key, string\|int\|float $amount, array $allocations, ?string $currency = null, ?string $actor = null): array` |
| [SaveDimension.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Actions/SaveDimension.php) | `public function handle(array $attributes, ?Dimension $dimension = null): Dimension` |
| [SaveDimensionValue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Actions/SaveDimensionValue.php) | `public function handle(Dimension $dimension, array $attributes, ?DimensionValue $value = null): DimensionValue` |
| [ValidateDimensions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Actions/ValidateDimensions.php) | `public function handle(array $values): array` |
| [DimensionsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/src/Policies/DimensionsPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, Dimension $d): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, Dimension $d): bool`<br>`public function delete(?Authenticatable $u, Dimension $d): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Dimension.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Models/Dimension.php) | `code`, `name`, `kind`, `description`, `is_required`, `is_active`, `metadata` |
| [DimensionAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Models/DimensionAllocation.php) | `allocation_key`, `amount`, `currency`, `percentage`, `dimensions`, `created_by` |
| [DimensionValue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Models/DimensionValue.php) | `dimension_id`, `code`, `name`, `parent_id`, `is_active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DimensionsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/src/Http/Controllers/DimensionsController.php) | `public function index(Request $request)`<br>`public function show(string $dimension): DimensionResource`<br>`public function store(Request $request, SaveDimension $save)`<br>`public function update(Request $request, string $dimension, SaveDimension $save): DimensionResource`<br>`public function values(Request $request, string $dimension, SaveDimensionValue $save)`<br>`public function validateValues(Request $request, ValidateDimensions $validate)`<br>`public function allocate(Request $request, AllocateDimensions $allocate)`<br>`public function balances(Request $request, DimensionalBalances $balances)`<br>`public function destroy(string $dimension): Response` |

**Observed route declarations:**

[modules/accounting-dimensions-and-tracking-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:60,1'])->prefix('api/v1/accounting/dimensions-and-tracking')->group(function (): void {
Route::get('/', [DimensionsController::class, 'index'])->middleware('ability:accounting.dimensions.read');
Route::post('/', [DimensionsController::class, 'store'])->middleware('ability:accounting.dimensions.write');
Route::get('/balances', [DimensionsController::class, 'balances'])->middleware('ability:accounting.dimensions.read');
Route::post('/validate', [DimensionsController::class, 'validateValues'])->middleware('ability:accounting.dimensions.read');
Route::post('/allocate', [DimensionsController::class, 'allocate'])->middleware('ability:accounting.dimensions.write');
Route::get('/{dimension}', [DimensionsController::class, 'show'])->middleware('ability:accounting.dimensions.read');
Route::patch('/{dimension}', [DimensionsController::class, 'update'])->middleware('ability:accounting.dimensions.write');
Route::post('/{dimension}/values', [DimensionsController::class, 'values'])->middleware('ability:accounting.dimensions.write');
Route::delete('/{dimension}', [DimensionsController::class, 'destroy'])->middleware('ability:accounting.dimensions.write');
```
<!-- layer-implementation-plan:end -->
