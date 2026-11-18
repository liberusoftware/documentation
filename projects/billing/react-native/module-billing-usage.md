# Module Billing Usage React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-usage). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-module-billing-usage-react-native
**Matching core package:** module-billing-module-billing-usage ([implementation](../core/module-billing-usage.md))
**Matching API package:** module-billing-module-billing-usage-api ([contract](../api/module-billing-usage.md))

## Implementation plan

This adapter presents Module Billing Usage for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Billing Usage API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-billing-usage.md), and [API module](../api/module-billing-usage.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-billing-usage`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-usage.md)) |
| Capability React Native module skeleton | [`module-billing-usage-react-native`](https://github.com/liberusoftware/module-billing-usage-react-native) (`@liberusoftware/module-billing-usage-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Meter definitions** | Progressive mobile list/detail/sheet flow for `meter definitions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Ingestion** | Progressive mobile list/detail/sheet flow for `ingestion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deduplication** | Progressive mobile list/detail/sheet flow for `deduplication` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Aggregation** | Progressive mobile list/detail/sheet flow for `aggregation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rating** | Progressive mobile list/detail/sheet flow for `rating` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Corrections** | Progressive mobile list/detail/sheet flow for `corrections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Thresholds** | Progressive mobile list/detail/sheet flow for `thresholds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
