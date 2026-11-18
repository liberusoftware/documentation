# Accounting: Three-Way Matching Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#three-way-matching). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-three-way-matching-vue-inertia`
**Matching domain module:** `accounting-three-way-matching`
**Application:** Accounting
**Source feature:** [Three-Way Matching](../features/three-way-matching.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/three-way-matching.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **PO/receipt/bill matching:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Quantity/price/tax tolerances:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exceptions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Partial matching:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Evidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-three-way-matching-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `po-receipt-bill-matching`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `quantity-price-tax-tolerances`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `exceptions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `approval`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `partial-matching`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `evidence`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-three-way-matching` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-three-way-matching-vue-inertia`](https://github.com/liberusoftware/module-accounting-three-way-matching-vue-inertia) (`@liberusoftware/module-accounting-three-way-matching-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/three-way-matching.md) · [Core plan](../core/three-way-matching.md) · [API plan](../api/three-way-matching.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **PO/receipt/bill matching** | Render `po/receipt/bill matching` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Quantity/price/tax tolerances** | Render `quantity/price/tax tolerances` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Exceptions** | Render `exceptions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Approval** | Render `approval` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Partial matching** | Render `partial matching` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Evidence** | Render `evidence` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ExceptionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Queries/ExceptionQuery.php) | `public function open(?int $matchId = null): Collection` |
| [MatchQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Queries/MatchQuery.php) | `public function paginate(?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/ApproveMatch.php) | `public function handle(MatchRecord $match, int $actorId, ?string $overrideReason = null): MatchRecord` |
| [CaptureMatchEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/CaptureMatchEvidence.php) | `public function handle(MatchRecord $match, string $sourceType, string $sourceId, array $snapshot, ?int $actorId = null): MatchEvidence` |
| [EvaluateMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/EvaluateMatch.php) | `public function handle(array $attributes): MatchRecord` |
| [RejectMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/RejectMatch.php) | `public function handle(MatchRecord $match, string $reason): MatchRecord` |
| [ResolveMatchException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/ResolveMatchException.php) | `public function handle(MatchException $exception, int $actorId, string $resolution, bool $waive = false): MatchException` |
| [ThreeWayMatchingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-api/src/Policies/ThreeWayMatchingPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $match): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $match): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MatchEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchEvidence.php) | `match_id`, `source_type`, `source_id`, `snapshot_hash`, `snapshot`, `captured_by`, `metadata` |
| [MatchException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchException.php) | `match_id`, `kind`, `severity`, `status`, `expected_value`, `actual_value`, `tolerance`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [MatchRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchRecord.php) | `purchase_order_type`, `purchase_order_id`, `receipt_type`, `receipt_id`, `bill_type`, `bill_id`, `currency`, `ordered_quantity`, `received_quantity`, `billed_quantity`, `ordered_unit_price`, `billed_unit_price`, `expected_tax`, `billed_tax`, `quantity_tolerance`, `price_tolerance`, `tax_tolerance`, `status`, `approved_by`, `approved_at`, `rejected_reason`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MatchController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-api/src/Http/Controllers/MatchController.php) | `public function index(Request $request, MatchQuery $query): mixed`<br>`public function show(MatchRecord $match): MatchResource`<br>`public function evaluate(Request $request, EvaluateMatch $action): MatchResource`<br>`public function approve(Request $request, MatchRecord $match, ApproveMatch $action): MatchResource`<br>`public function reject(Request $request, MatchRecord $match, RejectMatch $action): MatchResource`<br>`public function resolveException(Request $request, MatchException $exception, ResolveMatchException $action): MatchResource`<br>`public function exceptions(Request $request, ExceptionQuery $query): JsonResponse`<br>`public function evidence(Request $request, MatchRecord $match, CaptureMatchEvidence $action): MatchResource` |

**Observed route declarations:**

[modules/accounting-three-way-matching-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/three-way-matching')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.three-way-matching.read')->group(function (): void {
Route::get('/', [MatchController::class, 'index']);
Route::get('/exceptions', [MatchController::class, 'exceptions']);
Route::get('/{match}', [MatchController::class, 'show']);
Route::middleware('ability:accounting.three-way-matching.write')->group(function (): void {
Route::post('/', [MatchController::class, 'evaluate']);
Route::post('/{match}/approve', [MatchController::class, 'approve']);
Route::post('/{match}/reject', [MatchController::class, 'reject']);
Route::post('/{match}/evidence', [MatchController::class, 'evidence']);
Route::post('/exceptions/{exception}/resolve', [MatchController::class, 'resolveException']);
```
<!-- layer-implementation-plan:end -->
