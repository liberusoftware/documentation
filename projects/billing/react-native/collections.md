# Collections React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collections). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-collections-react-native
**Matching core package:** module-billing-collections ([implementation](../core/collections.md))
**Matching API package:** module-billing-collections-api ([contract](../api/collections.md))

## Implementation plan

This adapter presents Collections for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Collections API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/collections.md), and [API module](../api/collections.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `collections`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/collections.md)) |
| Capability React Native module skeleton | [`module-billing-collections-react-native`](https://github.com/liberusoftware/module-billing-collections-react-native) (`@liberusoftware/module-billing-collections-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Retries** | Progressive mobile list/detail/sheet flow for `retries` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dunning** | Progressive mobile list/detail/sheet flow for `dunning` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reminders** | Progressive mobile list/detail/sheet flow for `reminders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Promises** | Progressive mobile list/detail/sheet flow for `promises` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Credit control** | Progressive mobile list/detail/sheet flow for `credit control` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Suspension** | Progressive mobile list/detail/sheet flow for `suspension` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Write-off** | Progressive mobile list/detail/sheet flow for `write-off` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recovery** | Progressive mobile list/detail/sheet flow for `recovery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
