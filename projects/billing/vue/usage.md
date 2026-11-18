# Billing: Usage Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#usage). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-billing-usage-vue-inertia`
**Matching domain module:** `billing-usage`
**Application:** Billing
**Source feature:** [Usage](../features/usage.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/usage.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Meter definitions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Ingestion:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deduplication:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Aggregation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rating:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Corrections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Thresholds:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-billing-usage-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `meter-definitions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `ingestion`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `deduplication`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `aggregation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rating`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `corrections`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `thresholds`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `billing-usage` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-billing-usage-vue-inertia`](https://github.com/liberusoftware/module-billing-usage-vue-inertia) (`@liberusoftware/module-billing-usage-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/usage.md) · [Core plan](../core/usage.md) · [API plan](../api/usage.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Meter definitions** | Render `meter definitions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Ingestion** | Render `ingestion` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Deduplication** | Render `deduplication` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Aggregation** | Render `aggregation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rating** | Render `rating` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Corrections** | Render `corrections` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Thresholds** | Render `thresholds` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
