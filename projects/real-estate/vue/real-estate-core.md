# Real Estate: Real Estate Core Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-real-estate-core-vue-inertia`
**Matching domain module:** `real-estate-core`
**Application:** Real Estate
**Source feature:** [Real Estate Core](../features/real-estate-core.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Agencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Branches:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Teams:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Territories:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Terminology:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Statuses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Numbering:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Audit:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-real-estate-core-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `agencies`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `branches`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `teams`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `territories`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `terminology`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `statuses`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `numbering`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `audit`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-core` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-real-estate-laravel-inertia-vue`](https://github.com/liberusoftware/project-real-estate-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-real-estate-core-vue-inertia`](https://github.com/liberusoftware/module-real-estate-core-vue-inertia) (`@liberusoftware/module-real-estate-core-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/real-estate-core.md) · [Core plan](../core/real-estate-core.md) · [API plan](../api/real-estate-core.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Agencies** | Render `agencies` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Branches** | Render `branches` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Teams** | Render `teams` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Territories** | Render `territories` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Terminology** | Render `terminology` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Statuses** | Render `statuses` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Numbering** | Render `numbering` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Audit** | Render `audit` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AgencyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/AgencyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Agency $agency): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Agency $agency): bool`<br>`public function delete(AuthUser $authUser, Agency $agency): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Agency $agency): bool`<br>`public function forceDelete(AuthUser $authUser, Agency $agency): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Agency $agency): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [BranchPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/BranchPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Branch $branch): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Branch $branch): bool`<br>`public function delete(AuthUser $authUser, Branch $branch): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Branch $branch): bool`<br>`public function forceDelete(AuthUser $authUser, Branch $branch): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Branch $branch): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [StatusDefinitionPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/StatusDefinitionPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function delete(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function forceDelete(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [TerritoryPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/TerritoryPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Territory $territory): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Territory $territory): bool`<br>`public function delete(AuthUser $authUser, Territory $territory): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Territory $territory): bool`<br>`public function forceDelete(AuthUser $authUser, Territory $territory): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Territory $territory): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Agency.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Agency.php) | No literal fillable array detected; inspect the model and API schema. |
| [AuditEntry.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/AuditEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [Branch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Branch.php) | No literal fillable array detected; inspect the model and API schema. |
| [CalendarEntry.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/CalendarEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [Communication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Communication.php) | No literal fillable array detected; inspect the model and API schema. |
| [NumberSequence.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/NumberSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [StatusDefinition.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/StatusDefinition.php) | No literal fillable array detected; inspect the model and API schema. |
| [Terminology.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Terminology.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AgencyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/AgencyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAgency $create): JsonResponse`<br>`public function show(Request $request, Agency $agency): JsonResponse`<br>`public function update(Request $request, Agency $agency, UpdateAgency $update): JsonResponse`<br>`public function destroy(Request $request, Agency $agency, DeleteAgency $delete): Response` |
| [BranchController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/BranchController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateBranch $create): JsonResponse`<br>`public function show(Request $request, Branch $branch): JsonResponse`<br>`public function update(Request $request, Branch $branch, UpdateBranch $update): JsonResponse`<br>`public function destroy(Request $request, Branch $branch, DeleteBranch $delete): Response` |
| [CalendarEntryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CalendarEntryController.php) | `public function store(Request $request, CreateCalendarEntry $create): JsonResponse`<br>`public function update(Request $request, CalendarEntry $calendarEntry): JsonResponse`<br>`public function destroy(Request $request, CalendarEntry $calendarEntry): Response` |
| [CommunicationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CommunicationController.php) | `public function store(Request $request, RecordCommunication $record): JsonResponse`<br>`public function update(Request $request, Communication $communication): JsonResponse`<br>`public function destroy(Request $request, Communication $communication): Response` |
| [CoreConfigurationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CoreConfigurationController.php) | `public function terminology(Request $request, string $key, SetTerminology $set): JsonResponse`<br>`public function status(Request $request, DefineStatus $define): JsonResponse`<br>`public function audit(Request $request, RecordAuditEntry $record): JsonResponse`<br>`public function list(Request $request, string $kind): JsonResponse` |
| [NumberingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/NumberingController.php) | `public function next(Request $request, string $key, NextNumber $nextNumber): JsonResponse` |
| [PublicTerritoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/PublicTerritoryController.php) | `public function index(): JsonResponse` |
| [TerritoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/TerritoryController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateTerritory $create): JsonResponse`<br>`public function show(Request $request, Territory $territory): JsonResponse`<br>`public function update(Request $request, Territory $territory, UpdateTerritory $update): JsonResponse`<br>`public function destroy(Request $request, Territory $territory, DeleteTerritory $delete): Response` |

**Observed route declarations:**

[modules/real-estate-core-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/routes/api.php)

```php
Route::get('api/v1/public/territories', [PublicTerritoryController::class, 'index'])
Route::prefix('api/v1/real-estate/calendar-entries')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [CalendarEntryController::class, 'store']);
Route::delete('/{calendarEntry}', [CalendarEntryController::class, 'destroy']);
Route::prefix('api/v1/real-estate/communications')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [CommunicationController::class, 'store']);
Route::delete('/{communication}', [CommunicationController::class, 'destroy']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('api/v1/real-estate/core/{kind}', [CoreConfigurationController::class, 'list'])->whereIn('kind', ['terminology', 'statuses', 'audit']);
Route::put('api/v1/real-estate/core/terminology/{key}', [CoreConfigurationController::class, 'terminology']);
Route::post('api/v1/real-estate/core/statuses', [CoreConfigurationController::class, 'status']);
Route::post('api/v1/real-estate/core/audit', [CoreConfigurationController::class, 'audit']);
Route::post('api/v1/real-estate/numbering/{key}/next', [NumberingController::class, 'next'])
Route::prefix('api/v1/real-estate/branches')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [BranchController::class, 'index'])->name('real-estate.branches.index');
Route::post('/', [BranchController::class, 'store'])->name('real-estate.branches.store');
Route::get('/{branch}', [BranchController::class, 'show'])->name('real-estate.branches.show');
Route::delete('/{branch}', [BranchController::class, 'destroy'])->name('real-estate.branches.destroy');
Route::prefix('api/v1/real-estate/agencies')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [AgencyController::class, 'index']);
Route::post('/', [AgencyController::class, 'store']);
Route::get('/{agency}', [AgencyController::class, 'show']);
Route::delete('/{agency}', [AgencyController::class, 'destroy']);
Route::prefix('api/v1/real-estate/territories')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [TerritoryController::class, 'index']);
Route::post('/', [TerritoryController::class, 'store']);
Route::get('/{territory}', [TerritoryController::class, 'show']);
Route::delete('/{territory}', [TerritoryController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
