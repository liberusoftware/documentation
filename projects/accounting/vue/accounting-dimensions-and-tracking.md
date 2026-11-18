# Accounting: Accounting Dimensions And Tracking Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-dimensions-and-tracking). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-dimensions-and-tracking-vue-inertia`
**Matching domain module:** `accounting-dimensions-and-tracking`
**Application:** Accounting
**Source feature:** [Accounting Dimensions And Tracking](../features/accounting-dimensions-and-tracking.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-dimensions-and-tracking.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Classes/categories:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Locations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Departments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cost/profit centers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Projects:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tags:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Validation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Allocations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dimensional balances:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-dimensions-and-tracking-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `classes-categories`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `locations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `departments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cost-profit-centers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `projects`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tags`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `validation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `allocations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `dimensional-balances`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-dimensions-and-tracking` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-dimensions-and-tracking-vue-inertia`](https://github.com/liberusoftware/module-accounting-dimensions-and-tracking-vue-inertia) (`@liberusoftware/module-accounting-dimensions-and-tracking-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-dimensions-and-tracking.md) · [Core plan](../core/accounting-dimensions-and-tracking.md) · [API plan](../api/accounting-dimensions-and-tracking.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Classes/categories** | Render `classes/categories` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Locations** | Render `locations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Departments** | Render `departments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Cost/profit centers** | Render `cost/profit centers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Projects** | Render `projects` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tags** | Render `tags` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Validation** | Render `validation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Allocations** | Render `allocations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Dimensional balances** | Render `dimensional balances` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
