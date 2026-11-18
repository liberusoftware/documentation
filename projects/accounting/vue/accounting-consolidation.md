# Accounting: Accounting Consolidation Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-consolidation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-consolidation-vue-inertia`
**Matching domain module:** `accounting-consolidation`
**Application:** Accounting
**Source feature:** [Accounting Consolidation](../features/accounting-consolidation.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-consolidation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Group hierarchy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Mappings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Currency translation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Intercompany eliminations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Ownership/minority interests:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Adjustments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Group close:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-consolidation-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `group-hierarchy`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `mappings`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `currency-translation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `intercompany-eliminations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `ownership-minority-interests`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `adjustments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `group-close`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-consolidation` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-consolidation-vue-inertia`](https://github.com/liberusoftware/module-accounting-consolidation-vue-inertia) (`@liberusoftware/module-accounting-consolidation-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-consolidation.md) · [Core plan](../core/accounting-consolidation.md) · [API plan](../api/accounting-consolidation.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Group hierarchy** | Render `group hierarchy` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Mappings** | Render `mappings` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Currency translation** | Render `currency translation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Intercompany eliminations** | Render `intercompany eliminations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Ownership/minority interests** | Render `ownership/minority interests` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Adjustments** | Render `adjustments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Group close** | Render `group close` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConsolidationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Queries/ConsolidationQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddConsolidationEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/AddConsolidationEntity.php) | `public function handle(ConsolidationGroup $group, array $entity): ConsolidationGroup` |
| [CreateConsolidationGroup.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/CreateConsolidationGroup.php) | `public function handle(array $attributes): ConsolidationGroup` |
| [PrepareConsolidatedReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/PrepareConsolidatedReport.php) | `public function handle(ConsolidationGroup $group, array $report): ConsolidationGroup` |
| [PublishConsolidatedReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/PublishConsolidatedReport.php) | `public function handle(ConsolidationGroup $group, array $translation = []): ConsolidationGroup` |
| [RecordEliminations.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Actions/RecordEliminations.php) | `public function handle(ConsolidationGroup $group, array $elimination): ConsolidationGroup` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConsolidationGroup.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation/src/Models/ConsolidationGroup.php) | `team_id`, `group_ref`, `name`, `reporting_currency`, `status`, `entities`, `eliminations`, `translation`, `report` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConsolidationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation-api/src/Http/Controllers/ConsolidationController.php) | `public function index(ConsolidationQuery $query): JsonResponse`<br>`public function store(Request $request, CreateConsolidationGroup $action): JsonResponse`<br>`public function entity(Request $request, string $group, AddConsolidationEntity $action): JsonResponse`<br>`public function prepare(Request $request, string $group, PrepareConsolidatedReport $action): JsonResponse`<br>`public function publish(Request $request, string $group, PublishConsolidatedReport $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-consolidation-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-consolidation-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/consolidation')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.consolidation.read')->get('/', [ConsolidationController::class, 'index']);
Route::middleware('ability:accounting.consolidation.write')->group(function (): void {
Route::post('/', [ConsolidationController::class, 'store']);
Route::post('/{group}/entities', [ConsolidationController::class, 'entity']);
Route::post('/{group}/prepare', [ConsolidationController::class, 'prepare']);
Route::post('/{group}/publish', [ConsolidationController::class, 'publish']);
```
<!-- layer-implementation-plan:end -->
