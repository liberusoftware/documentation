# Accounting: Revenue Recognition Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-recognition). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-revenue-recognition-vue-inertia`
**Matching domain module:** `accounting-revenue-recognition`
**Application:** Accounting
**Source feature:** [Revenue Recognition](../features/revenue-recognition.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/revenue-recognition.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Obligations/schedules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Allocation references:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deferred/accrued revenue:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recognition runs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Modifications:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation (optional):** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-revenue-recognition-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `obligations-schedules`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `allocation-references`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `deferred-accrued-revenue`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `recognition-runs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `modifications`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reconciliation-optional`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-revenue-recognition` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-revenue-recognition-vue-inertia`](https://github.com/liberusoftware/module-accounting-revenue-recognition-vue-inertia) (`@liberusoftware/module-accounting-revenue-recognition-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/revenue-recognition.md) · [Core plan](../core/revenue-recognition.md) · [API plan](../api/revenue-recognition.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Obligations/schedules** | Render `obligations/schedules` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Allocation references** | Render `allocation references` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Deferred/accrued revenue** | Render `deferred/accrued revenue` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Recognition runs** | Render `recognition runs` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Modifications** | Render `modifications` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reconciliation (optional)** | Render `reconciliation (optional)` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/CreateRevenueSchedule.php) | `public function handle(array $attributes): RevenueSchedule` |
| [ModifyRevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ModifyRevenueSchedule.php) | `public function handle(RevenueSchedule $schedule, array $attributes): RevenueModification` |
| [RecognizeDueRevenue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/RecognizeDueRevenue.php) | `public function handle(RevenueSchedule $schedule, string $asOfDate, ?int $teamId = null): RevenueRecognitionRun` |
| [ReconcileRevenueRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ReconcileRevenueRun.php) | `public function handle(RevenueRecognitionRun $run, array $references = []): RevenueRecognitionRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueAllocationReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueAllocationReference.php) | `team_id`, `reference_type`, `reference_id`, `allocation`, `status`, `metadata` |
| [RevenueModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueModification.php) | `schedule_id`, `effective_date`, `amount_delta`, `reason`, `status`, `metadata` |
| [RevenueObligation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueObligation.php) | `team_id`, `source_type`, `source_id`, `description`, `currency`, `total_amount`, `start_date`, `periods`, `status`, `metadata` |
| [RevenueRecognitionRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueRecognitionRun.php) | `team_id`, `as_of_date`, `status`, `processed_entries`, `failed_entries`, `errors`, `metadata`, `started_at`, `finished_at` |
| [RevenueReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueReconciliation.php) | `run_id`, `reference_type`, `reference_id`, `expected_amount`, `recognized_amount`, `variance`, `status`, `notes`, `metadata` |
| [RevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueSchedule.php) | `obligation_id`, `allocation_reference_id`, `total_amount`, `start_date`, `periods`, `deferred_account_ref`, `revenue_account_ref`, `status`, `funded`, `metadata` |
| [RevenueScheduleEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueScheduleEntry.php) | `schedule_id`, `period_number`, `recognition_date`, `amount`, `status`, `recognized_at`, `ledger_reference`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [RevenueRecognitionController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-api/src/Http/Controllers/RevenueRecognitionController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateRevenueSchedule $action): mixed`<br>`public function show(Request $request, RevenueSchedule $schedule): RevenueScheduleResource`<br>`public function recognize(Request $request, RevenueSchedule $schedule, RecognizeDueRevenue $action): mixed`<br>`public function modify(Request $request, RevenueSchedule $schedule, ModifyRevenueSchedule $action): mixed`<br>`public function reconcile(Request $request, RevenueRecognitionRun $run, ReconcileRevenueRun $action): mixed` |

**Observed route declarations:**

[modules/accounting-revenue-recognition-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/revenue-recognition')->group(function (): void {
Route::middleware('ability:accounting.revenue-recognition.read')->group(function (): void {
Route::get('/', [RevenueRecognitionController::class, 'index']);
Route::get('/{schedule}', [RevenueRecognitionController::class, 'show']);
Route::middleware('ability:accounting.revenue-recognition.write')->group(function (): void {
Route::post('/', [RevenueRecognitionController::class, 'store']);
Route::post('/{schedule}/recognize', [RevenueRecognitionController::class, 'recognize']);
Route::post('/{schedule}/modify', [RevenueRecognitionController::class, 'modify']);
Route::post('/runs/{run}/reconcile', [RevenueRecognitionController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
