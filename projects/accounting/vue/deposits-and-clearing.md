# Accounting: Deposits and Clearing Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#deposits-and-clearing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-deposits-and-clearing-vue-inertia`
**Matching domain module:** `accounting-deposits-and-clearing`
**Application:** Accounting
**Source feature:** [Deposits and Clearing](../features/deposits-and-clearing.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/deposits-and-clearing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Undeposited funds:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Grouped deposits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payment-provider clearing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Fees:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payouts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Timing differences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-deposits-and-clearing-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `undeposited-funds`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `grouped-deposits`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payment-provider-clearing`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `fees`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payouts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `timing-differences`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-deposits-and-clearing` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-deposits-and-clearing-vue-inertia`](https://github.com/liberusoftware/module-accounting-deposits-and-clearing-vue-inertia) (`@liberusoftware/module-accounting-deposits-and-clearing-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/deposits-and-clearing.md) · [Core plan](../core/deposits-and-clearing.md) · [API plan](../api/deposits-and-clearing.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Undeposited funds** | Render `undeposited funds` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Grouped deposits** | Render `grouped deposits` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Payment-provider clearing** | Render `payment-provider clearing` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Fees** | Render `fees` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Payouts** | Render `payouts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Timing differences** | Render `timing differences` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reconciliation** | Render `reconciliation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ClearingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Queries/ClearingQuery.php) | `public function undeposited(int $teamId): Collection`<br>`public function deposits(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGroupedDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/CreateGroupedDeposit.php) | `public function handle(array $attributes, array $fundIds): ClearingDeposit` |
| [ReconcileDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/ReconcileDeposit.php) | `public function handle(ClearingDeposit $deposit, float $payoutAmount, float $feeAmount = 0): ClearingDeposit` |
| [RecordUndepositedFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/RecordUndepositedFund.php) | `public function handle(array $attributes): ClearingFund` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ClearingDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingDeposit.php) | `team_id`, `deposit_ref`, `provider`, `account_ref`, `currency`, `gross_amount`, `fee_amount`, `payout_amount`, `deposit_date`, `status`, `metadata` |
| [ClearingFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingFund.php) | `team_id`, `deposit_id`, `source_type`, `source_id`, `amount`, `currency`, `received_on`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ClearingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-api/src/Http/Controllers/ClearingController.php) | `public function funds(ClearingQuery $query): JsonResponse`<br>`public function deposits(ClearingQuery $query): JsonResponse`<br>`public function recordFund(Request $request, RecordUndepositedFund $action): JsonResponse`<br>`public function createDeposit(Request $request, CreateGroupedDeposit $action): JsonResponse`<br>`public function reconcile(Request $request, string $deposit, ReconcileDeposit $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-deposits-and-clearing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/deposits-and-clearing')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.deposits-and-clearing.read')->group(function (): void {
Route::get('/funds', [ClearingController::class, 'funds']);
Route::get('/deposits', [ClearingController::class, 'deposits']);
Route::middleware('ability:accounting.deposits-and-clearing.write')->group(function (): void {
Route::post('/funds', [ClearingController::class, 'recordFund']);
Route::post('/deposits', [ClearingController::class, 'createDeposit']);
Route::post('/deposits/{deposit}/reconcile', [ClearingController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
