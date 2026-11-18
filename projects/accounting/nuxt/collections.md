# Accounting: Collections Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collections). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-collections-nuxt`
**Matching domain module:** `accounting-collections`
**Application:** Accounting
**Source feature:** [Collections](../features/collections.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/collections.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-collections` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reminder schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statement runs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Promise-to-pay:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Disputes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Late fees/interest policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Collection stages:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Write-offs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Agency adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-collections-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `reminder-schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statement-runs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `promise-to-pay`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `disputes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `late-fees-interest-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `collection-stages`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `write-offs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `agency-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-collections` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/collections.md)) |
| Capability Nuxt module skeleton | [`module-accounting-collections-nuxt`](https://github.com/liberusoftware/module-accounting-collections-nuxt) (`@liberusoftware/module-accounting-collections-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Reminder schedules** | Expose composable and Vue 3 component for `reminder schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Statement runs** | Expose composable and Vue 3 component for `statement runs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Promise-to-pay** | Expose composable and Vue 3 component for `promise-to-pay` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Disputes** | Expose composable and Vue 3 component for `disputes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Late fees/interest policy** | Expose composable and Vue 3 component for `late fees/interest policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Collection stages** | Expose composable and Vue 3 component for `collection stages` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Write-offs** | Expose composable and Vue 3 component for `write-offs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Agency adapters** | Expose composable and Vue 3 component for `agency adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

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
