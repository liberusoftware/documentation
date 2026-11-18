# Billing: Module Billing Collections Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-collections). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-collections-nuxt`
**Matching domain module:** `module-billing-collections`
**Application:** Billing
**Source feature:** [Module Billing Collections](../features/module-billing-collections.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-collections.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-collections` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Retries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dunning:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reminders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Promises:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Credit control:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Suspension:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Write-off:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recovery:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-collections-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `retries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dunning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reminders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `promises`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `credit-control`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `suspension`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `write-off`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recovery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-collections` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-collections.md)) |
| Capability Nuxt module skeleton | [`module-billing-collections-nuxt`](https://github.com/liberusoftware/module-billing-collections-nuxt) (`@liberusoftware/module-billing-collections-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Retries** | Expose composable and Vue 3 component for `retries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Dunning** | Expose composable and Vue 3 component for `dunning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Reminders** | Expose composable and Vue 3 component for `reminders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Promises** | Expose composable and Vue 3 component for `promises` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Credit control** | Expose composable and Vue 3 component for `credit control` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Suspension** | Expose composable and Vue 3 component for `suspension` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Write-off** | Expose composable and Vue 3 component for `write-off` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Recovery** | Expose composable and Vue 3 component for `recovery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListCollectionCases.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Queries/ListCollectionCases.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyCreditControl.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ApplyCreditControl.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $level, ?string $reason = null): CollectionCase` |
| [OpenCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/OpenCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): CollectionCase` |
| [PromisePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/PromisePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $dueAt): CollectionCase` |
| [RecoverCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/RecoverCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case): CollectionCase` |
| [RetryCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/RetryCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [ScheduleDunning.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ScheduleDunning.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [ScheduleReminder.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ScheduleReminder.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [SuspendCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/SuspendCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $reason): CollectionCase` |
| [WriteOffCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/WriteOffCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $reason): CollectionCase` |
| [CollectionCasePolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Policies/CollectionCasePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, CollectionCase $case): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Models/CollectionCase.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CollectionCaseController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-api/src/Http/Controllers/CollectionCaseController.php) | `public function index(Request $request, ListCollectionCases $query): JsonResponse`<br>`public function store(Request $request, OpenCollectionCase $open): JsonResponse`<br>`public function promise(Request $request, CollectionCase $case, PromisePayment $promise): JsonResponse`<br>`public function suspend(Request $request, CollectionCase $case, SuspendCollectionCase $suspend): JsonResponse`<br>`public function recover(Request $request, CollectionCase $case, RecoverCollectionCase $recover): JsonResponse`<br>`public function retry(Request $request, CollectionCase $case, RetryCollectionCase $retry): JsonResponse`<br>`public function writeOff(Request $request, CollectionCase $case, WriteOffCollectionCase $writeOff): JsonResponse`<br>`public function dunning(Request $request, CollectionCase $case, ScheduleDunning $schedule): JsonResponse`<br>`public function reminder(Request $request, CollectionCase $case, ScheduleReminder $schedule): JsonResponse`<br>`public function creditControl(Request $request, CollectionCase $case, ApplyCreditControl $apply): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-collections-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.collections.read'])->prefix('api/v1/billing/collections')->name('billing.collections.')->group(function (): void {
Route::get('/', [CollectionCaseController::class, 'index'])->name('index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.collections.write', 'idempotency'])->prefix('api/v1/billing/collections')->name('billing.collections.')->group(function (): void {
Route::post('/', [CollectionCaseController::class, 'store'])->name('store');
Route::post('/{case}/promise', [CollectionCaseController::class, 'promise'])->name('promise');
Route::post('/{case}/suspend', [CollectionCaseController::class, 'suspend'])->name('suspend');
Route::post('/{case}/recover', [CollectionCaseController::class, 'recover'])->name('recover');
Route::post('/{case}/retry', [CollectionCaseController::class, 'retry'])->name('retry');
Route::post('/{case}/write-off', [CollectionCaseController::class, 'writeOff'])->name('write-off');
Route::post('/{case}/dunning', [CollectionCaseController::class, 'dunning'])->name('dunning');
Route::post('/{case}/reminder', [CollectionCaseController::class, 'reminder'])->name('reminder');
Route::post('/{case}/credit-control', [CollectionCaseController::class, 'creditControl'])->name('credit-control');
```
<!-- layer-implementation-plan:end -->
