# Maintenance: Commercial Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#commercial). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-commercial-nuxt`
**Matching domain module:** `maintenance-commercial`
**Application:** Maintenance
**Source feature:** [Commercial](../features/commercial.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/commercial.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `maintenance-commercial` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Quotes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contracts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Covered assets/services:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Renewals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SLA:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Billable lines:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-commercial-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `quotes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contracts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `covered-assets-services`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `renewals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sla`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `billable-lines`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-commercial` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/commercial.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-commercial-nuxt`](https://github.com/liberusoftware/module-maintenance-commercial-nuxt) (`@liberusoftware/module-maintenance-commercial-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Quotes** | Expose composable and Vue 3 component for `quotes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commercial.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Contracts** | Expose composable and Vue 3 component for `contracts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commercial.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Covered assets/services** | Expose composable and Vue 3 component for `covered assets/services` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commercial.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Rates** | Expose composable and Vue 3 component for `rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commercial.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Renewals** | Expose composable and Vue 3 component for `renewals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commercial.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **SLA** | Expose composable and Vue 3 component for `sla` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commercial.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Billable lines** | Expose composable and Vue 3 component for `billable lines` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commercial.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

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
