# Billing: Module Billing Usage Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-usage). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-usage-nuxt`
**Matching domain module:** `module-billing-usage`
**Application:** Billing
**Source feature:** [Module Billing Usage](../features/module-billing-usage.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-usage.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-usage` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Meter definitions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ingestion:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deduplication:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Aggregation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rating:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Corrections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Thresholds:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-usage-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `meter-definitions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ingestion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deduplication`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `aggregation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rating`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `corrections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `thresholds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-usage` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-usage.md)) |
| Capability Nuxt module skeleton | [`module-billing-usage-nuxt`](https://github.com/liberusoftware/module-billing-usage-nuxt) (`@liberusoftware/module-billing-usage-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Meter definitions** | Expose composable and Vue 3 component for `meter definitions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-usage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Ingestion** | Expose composable and Vue 3 component for `ingestion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-usage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Deduplication** | Expose composable and Vue 3 component for `deduplication` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-usage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Aggregation** | Expose composable and Vue 3 component for `aggregation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-usage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Rating** | Expose composable and Vue 3 component for `rating` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-usage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Corrections** | Expose composable and Vue 3 component for `corrections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-usage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Thresholds** | Expose composable and Vue 3 component for `thresholds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-usage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AggregateUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Queries/AggregateUsage.php) | `public function execute(int $meterId, ?int $customerId = null): object` |
| [ListMeters.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Queries/ListMeters.php) | `public function execute(?int $teamId = null): Collection` |
| [ListUsageRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Queries/ListUsageRecords.php) | `public function execute(?int $teamId = null, ?int $meterId = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CheckUsageThreshold.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/CheckUsageThreshold.php) | `public function execute(Meter $meter, float $quantity): bool` |
| [CorrectUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/CorrectUsage.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(UsageRecord $record, float $quantity, string $eventKey): UsageRecord` |
| [DefineMeter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/DefineMeter.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Meter` |
| [IngestUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/IngestUsage.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Meter $meter, array $attributes): UsageRecord` |
| [RateUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/RateUsage.php) | `public function execute(Meter $meter, float $quantity): int` |
| [TransitionMeter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/TransitionMeter.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Meter $meter, bool $active): Meter` |
| [UsagePolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Policies/UsagePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, Meter $meter): bool`<br>`public function update(?Authenticatable $user, Meter $meter): bool` |
| [UsageRecordPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Policies/UsageRecordPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Meter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Models/Meter.php) | No literal fillable array detected; inspect the model and API schema. |
| [UsageRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Models/UsageRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [UsageController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-api/src/Http/Controllers/UsageController.php) | `public function meters(Request $request, ListMeters $meters): JsonResponse`<br>`public function storeMeter(Request $request, DefineMeter $define): JsonResponse`<br>`public function transitionMeter(Request $request, Meter $meter, TransitionMeter $transition): JsonResponse`<br>`public function defineMeter(Request $request, DefineMeter $define): JsonResponse`<br>`public function ingest(Request $request, Meter $meter, IngestUsage $ingest): JsonResponse`<br>`public function records(Request $request, ListUsageRecords $records): JsonResponse`<br>`public function aggregate(Request $request, AggregateUsage $aggregate): JsonResponse`<br>`public function aggregateForMeter(Request $request, Meter $meter, AggregateUsage $aggregate): JsonResponse`<br>`public function rate(Request $request, Meter $meter, RateUsage $rate, CheckUsageThreshold $threshold): JsonResponse`<br>`public function correct(Request $request, UsageRecord $record, CorrectUsage $correct): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-usage-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.usage.read'])->prefix('api/v1/billing/usage')->name('billing.usage.')->group(function (): void {
Route::get('/meters', [UsageController::class, 'meters'])->name('meters');
Route::get('/meters/{meter}/aggregate', [UsageController::class, 'aggregateForMeter'])->name('aggregate');
Route::post('/meters/{meter}/rate', [UsageController::class, 'rate'])->name('rate');
Route::get('/records', [UsageController::class, 'records'])->name('records.index');
Route::get('/aggregate', [UsageController::class, 'aggregate'])->name('records.aggregate');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.usage.write', 'idempotency'])->prefix('api/v1/billing/usage')->name('billing.usage.')->group(function (): void {
Route::post('/meters', [UsageController::class, 'storeMeter'])->name('meters.store');
Route::patch('/meters/{meter}/status', [UsageController::class, 'transitionMeter'])->whereNumber('meter')->name('meters.status');
Route::post('/meters/{meter}/records', [UsageController::class, 'ingest'])->name('records.store');
Route::post('/meters/{meter}/ingest', [UsageController::class, 'ingest'])->name('records.ingest');
Route::post('/records/{record}/correct', [UsageController::class, 'correct'])->name('records.correct');
Route::post('/records/{record}/corrections', [UsageController::class, 'correct'])->name('records.corrected');
```
<!-- layer-implementation-plan:end -->
