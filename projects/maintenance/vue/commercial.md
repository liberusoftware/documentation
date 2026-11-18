# Maintenance: Commercial Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#commercial). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-maintenance-commercial-vue-inertia`
**Matching domain module:** `maintenance-commercial`
**Application:** Maintenance
**Source feature:** [Commercial](../features/commercial.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/commercial.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Quotes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Contracts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Covered assets/services:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Renewals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **SLA:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Billable lines:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-maintenance-commercial-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `quotes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `contracts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `covered-assets-services`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `renewals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `sla`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `billable-lines`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-commercial` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-maintenance-laravel-inertia-vue`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-maintenance-commercial-vue-inertia`](https://github.com/liberusoftware/module-maintenance-commercial-vue-inertia) (`@liberusoftware/module-maintenance-commercial-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/commercial.md) · [Core plan](../core/commercial.md) · [API plan](../api/commercial.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Quotes** | Render `quotes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Contracts** | Render `contracts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Covered assets/services** | Render `covered assets/services` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rates** | Render `rates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Renewals** | Render `renewals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **SLA** | Render `sla` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Billable lines** | Render `billable lines` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/CreateCommercialRecord.php) | `public function handle(int $teamId, array $attributes): CommercialRecord` |
| [DeleteCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/DeleteCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record): void` |
| [TransitionCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/TransitionCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record, string $status): CommercialRecord` |
| [UpdateCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/UpdateCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record, array $attributes): CommercialRecord` |
| [CommercialRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Policies/CommercialRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, CommercialRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, CommercialRecord $record): bool`<br>`public function delete(object $user, CommercialRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Models/CommercialRecord.php) | `kind`, `title`, `description`, `amount`, `currency`, `status`, `metadata`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommercialRecordController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial-api/src/Http/Controllers/CommercialRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateCommercialRecord $create): JsonResponse`<br>`public function show(Request $request, CommercialRecord $record): JsonResponse`<br>`public function update(Request $request, CommercialRecord $record, UpdateCommercialRecord $update): JsonResponse`<br>`public function destroy(Request $request, CommercialRecord $record, DeleteCommercialRecord $delete): JsonResponse`<br>`public function transition(Request $request, CommercialRecord $record, TransitionCommercialRecord $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-commercial-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/commercial')->group(function (): void {
Route::get('/', [CommercialRecordController::class, 'index']);
Route::post('/', [CommercialRecordController::class, 'store']);
Route::post('/{record}/transition', [CommercialRecordController::class, 'transition']);
Route::get('/{record}', [CommercialRecordController::class, 'show']);
Route::patch('/{record}', [CommercialRecordController::class, 'update']);
Route::delete('/{record}', [CommercialRecordController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
