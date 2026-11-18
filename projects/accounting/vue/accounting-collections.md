# Accounting: Accounting Collections Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-collections). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-collections-vue-inertia`
**Matching domain module:** `accounting-collections`
**Application:** Accounting
**Source feature:** [Accounting Collections](../features/accounting-collections.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-collections.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Reminder schedules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Statement runs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Promise-to-pay:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Disputes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Late fees/interest policy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Collection stages:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Write-offs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Agency adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-collections-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `reminder-schedules`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `statement-runs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `promise-to-pay`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `disputes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `late-fees-interest-policy`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `collection-stages`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `write-offs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `agency-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-collections` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-collections-vue-inertia`](https://github.com/liberusoftware/module-accounting-collections-vue-inertia) (`@liberusoftware/module-accounting-collections-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-collections.md) · [Core plan](../core/accounting-collections.md) · [API plan](../api/accounting-collections.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Reminder schedules** | Render `reminder schedules` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Statement runs** | Render `statement runs` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Promise-to-pay** | Render `promise-to-pay` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Disputes** | Render `disputes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Late fees/interest policy** | Render `late fees/interest policy` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Collection stages** | Render `collection stages` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Write-offs** | Render `write-offs` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Agency adapters** | Render `agency adapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CollectionCaseQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Queries/CollectionCaseQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/CreateCollectionCase.php) | `public function handle(array $attributes): CollectionCase` |
| [PrepareCollectionStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/PrepareCollectionStatement.php) | `public function handle(CollectionCase $case, array $statement): CollectionCase` |
| [RecordCollectionActivity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/RecordCollectionActivity.php) | `public function reminder(CollectionCase $case, array $reminder): CollectionCase`<br>`public function promise(CollectionCase $case, array $promise): CollectionCase`<br>`public function dispute(CollectionCase $case, array $dispute): CollectionCase` |
| [SendToCollectionAgency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/SendToCollectionAgency.php) | `public function handle(CollectionCase $case, string $agency): CollectionCase` |
| [WriteOffCollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/WriteOffCollectionCase.php) | `public function handle(CollectionCase $case, array $writeOff): CollectionCase` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Models/CollectionCase.php) | `team_id`, `case_ref`, `customer_ref`, `balance`, `stage`, `interest_rate`, `reminders`, `statement_run`, `promise_to_pay`, `disputes`, `write_off`, `agency` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CollectionsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections-api/src/Http/Controllers/CollectionsController.php) | `public function index(CollectionCaseQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCollectionCase $action): JsonResponse`<br>`public function reminder(Request $request, string $case, RecordCollectionActivity $action): JsonResponse`<br>`public function promise(Request $request, string $case, RecordCollectionActivity $action): JsonResponse`<br>`public function dispute(Request $request, string $case, RecordCollectionActivity $action): JsonResponse`<br>`public function writeOff(Request $request, string $case, WriteOffCollectionCase $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-collections-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/collections')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.collections.read')->get('/', [CollectionsController::class, 'index']);
Route::middleware('ability:accounting.collections.write')->group(function (): void {
Route::post('/', [CollectionsController::class, 'store']);
Route::post('/{case}/reminders', [CollectionsController::class, 'reminder']);
Route::post('/{case}/promises', [CollectionsController::class, 'promise']);
Route::post('/{case}/disputes', [CollectionsController::class, 'dispute']);
Route::post('/{case}/write-off', [CollectionsController::class, 'writeOff']);
```
<!-- layer-implementation-plan:end -->
