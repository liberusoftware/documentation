# Real Estate: Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-core-nuxt`
**Matching domain module:** `core`
**Application:** Real Estate
**Source feature:** [Core](../features/core.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `core` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Branches:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Teams:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Territories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Terminology:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statuses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Numbering:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audit:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `agencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `branches`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `teams`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `territories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `terminology`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statuses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `numbering`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audit`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `core` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/core.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-core-nuxt`](https://github.com/liberusoftware/module-real-estate-core-nuxt) (`@liberusoftware/module-real-estate-core-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Agencies** | Expose composable and Vue 3 component for `agencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Branches** | Expose composable and Vue 3 component for `branches` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Teams** | Expose composable and Vue 3 component for `teams` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Territories** | Expose composable and Vue 3 component for `territories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Terminology** | Expose composable and Vue 3 component for `terminology` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Statuses** | Expose composable and Vue 3 component for `statuses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Numbering** | Expose composable and Vue 3 component for `numbering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Audit** | Expose composable and Vue 3 component for `audit` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

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
