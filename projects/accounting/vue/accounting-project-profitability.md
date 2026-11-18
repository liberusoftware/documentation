# Accounting: Accounting Project Profitability Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-project-profitability). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-project-profitability-vue-inertia`
**Matching domain module:** `accounting-project-profitability`
**Application:** Accounting
**Source feature:** [Accounting Project Profitability](../features/accounting-project-profitability.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-project-profitability.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Revenue:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cost:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Margin:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Estimates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Committed/actual:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Unbilled WIP:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Realization:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dashboards:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Drill-through:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-project-profitability-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `revenue`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cost`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `margin`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `estimates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `committed-actual`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `unbilled-wip`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `realization`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `dashboards`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `drill-through`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-project-profitability` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-project-profitability-vue-inertia`](https://github.com/liberusoftware/module-accounting-project-profitability-vue-inertia) (`@liberusoftware/module-accounting-project-profitability-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-project-profitability.md) · [Core plan](../core/accounting-project-profitability.md) · [API plan](../api/accounting-project-profitability.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Revenue** | Render `revenue` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Cost** | Render `cost` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Margin** | Render `margin` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Estimates** | Render `estimates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Committed/actual** | Render `committed/actual` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Unbilled WIP** | Render `unbilled wip` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Realization** | Render `realization` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Dashboards** | Render `dashboards` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Drill-through** | Render `drill-through` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectProfitabilityDashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Queries/ProjectProfitabilityDashboard.php) | `public function forProject(int $projectJobId, ?int $teamId = null): array`<br>`public function summarize(Collection $rows): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FinalizeProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Actions/FinalizeProjectProfitability.php) | `public function handle(ProjectProfitability $record): ProjectProfitability` |
| [RecordProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Actions/RecordProjectProfitability.php) | `public function handle(array $attributes): ProjectProfitability` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Models/ProjectProfitability.php) | `team_id`, `project_job_id`, `period_start`, `period_end`, `currency`, `revenue_amount`, `cost_amount`, `estimate_amount`, `committed_amount`, `actual_amount`, `unbilled_wip_amount`, `billed_amount`, `status`, `dimensions`, `source_links`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProjectProfitabilityController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability-api/src/Http/Controllers/ProjectProfitabilityController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, RecordProjectProfitability $action): mixed`<br>`public function show(Request $request, ProjectProfitability $projectProfitability): ProjectProfitability`<br>`public function finalize(Request $request, ProjectProfitability $projectProfitability, FinalizeProjectProfitability $action): ProjectProfitability`<br>`public function dashboard(Request $request, int $projectJobId, ProjectProfitabilityDashboard $query): array` |

**Observed route declarations:**

[modules/accounting-project-profitability-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/project-profitability')->group(function (): void {
Route::middleware('ability:accounting.project-profitability.read')->group(function (): void {
Route::get('/', [ProjectProfitabilityController::class, 'index']);
Route::get('/{projectProfitability}', [ProjectProfitabilityController::class, 'show']);
Route::get('/project/{projectJobId}/dashboard', [ProjectProfitabilityController::class, 'dashboard']);
Route::middleware('ability:accounting.project-profitability.write')->group(function (): void {
Route::post('/', [ProjectProfitabilityController::class, 'store']);
Route::post('/{projectProfitability}/finalize', [ProjectProfitabilityController::class, 'finalize']);
```
<!-- layer-implementation-plan:end -->
