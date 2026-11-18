# Accounting: Accounting Cash Coding Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-cash-coding). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-cash-coding-vue-inertia`
**Matching domain module:** `accounting-cash-coding`
**Application:** Accounting
**Source feature:** [Accounting Cash Coding](../features/accounting-cash-coding.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-cash-coding.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **High-volume statement coding:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Bulk rules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax/dimensions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payee creation policy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Posting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Undo constraints:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-cash-coding-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `high-volume-statement-coding`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `bulk-rules`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tax-dimensions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payee-creation-policy`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `review`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `posting`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `undo-constraints`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-cash-coding` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-cash-coding-vue-inertia`](https://github.com/liberusoftware/module-accounting-cash-coding-vue-inertia) (`@liberusoftware/module-accounting-cash-coding-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-cash-coding.md) · [Core plan](../core/accounting-cash-coding.md) · [API plan](../api/accounting-cash-coding.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **High-volume statement coding** | Render `high-volume statement coding` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Bulk rules** | Render `bulk rules` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tax/dimensions** | Render `tax/dimensions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Payee creation policy** | Render `payee creation policy` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Review** | Render `review` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Posting** | Render `posting` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Undo constraints** | Render `undo constraints` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CashCodingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Queries/CashCodingQuery.php) | `public function forTeam(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Actions/CreateCashCodingBatch.php) | `public function handle(array $attributes): CashCodingBatch` |
| [TransitionCashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Actions/TransitionCashCodingBatch.php) | `public function review(CashCodingBatch $batch, ?int $actor = null): CashCodingBatch`<br>`public function post(CashCodingBatch $batch, ?int $actor = null): CashCodingBatch`<br>`public function undo(CashCodingBatch $batch, string $reason): CashCodingBatch` |
| [CashCodingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/src/Policies/CashCodingPolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, CashCodingBatch $batch): bool`<br>`public function create($user): bool`<br>`public function update($user, CashCodingBatch $batch): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Models/CashCodingBatch.php) | `team_id`, `reference`, `status`, `lines`, `payee_creation_policy`, `total_amount`, `currency`, `created_by`, `reviewed_by`, `posted_by`, `undo_reason`, `posted_at`, `undone_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CashCodingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/src/Http/Controllers/CashCodingController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateCashCodingBatch $action): CashCodingResource`<br>`public function show(string $batch): CashCodingResource`<br>`public function review(string $batch, TransitionCashCodingBatch $action): CashCodingResource`<br>`public function post(string $batch, TransitionCashCodingBatch $action): CashCodingResource`<br>`public function undo(Request $request, string $batch, TransitionCashCodingBatch $action): CashCodingResource` |

**Observed route declarations:**

[modules/accounting-cash-coding-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/cash-coding')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [CashCodingController::class, 'index'])->middleware('ability:accounting.cash-coding.read');
Route::post('/', [CashCodingController::class, 'store'])->middleware('ability:accounting.cash-coding.write');
Route::get('/{batch}', [CashCodingController::class, 'show'])->middleware('ability:accounting.cash-coding.read');
Route::post('/{batch}/review', [CashCodingController::class, 'review'])->middleware('ability:accounting.cash-coding.write');
Route::post('/{batch}/post', [CashCodingController::class, 'post'])->middleware('ability:accounting.cash-coding.write');
Route::post('/{batch}/undo', [CashCodingController::class, 'undo'])->middleware('ability:accounting.cash-coding.write');
```
<!-- layer-implementation-plan:end -->
