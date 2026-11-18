# Module Billing Isp React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-isp). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-module-billing-isp-react-native
**Matching core package:** module-billing-module-billing-isp ([implementation](../core/module-billing-isp.md))
**Matching API package:** module-billing-module-billing-isp-api ([contract](../api/module-billing-isp.md))

## Implementation plan

This adapter presents Module Billing Isp for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Billing Isp API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-billing-isp.md), and [API module](../api/module-billing-isp.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-billing-isp`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-isp.md)) |
| Capability React Native module skeleton | [`module-billing-isp-react-native`](https://github.com/liberusoftware/module-billing-isp-react-native) (`@liberusoftware/module-billing-isp-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Access services** | Progressive mobile list/detail/sheet flow for `access services` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Coverage** | Progressive mobile list/detail/sheet flow for `coverage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Installation** | Progressive mobile list/detail/sheet flow for `installation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **RADIUS/AAA** | Progressive mobile list/detail/sheet flow for `radius/aaa` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Usage** | Progressive mobile list/detail/sheet flow for `usage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Equipment** | Progressive mobile list/detail/sheet flow for `equipment` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Network adapters** | Progressive mobile list/detail/sheet flow for `network adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListIspRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Queries/ListIspRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/CreateAccessService.php) | `public function handle(int $teamId, array $attributes): AccessService` |
| [CreateIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/CreateIspCapability.php) | `public function handle(int $teamId, array $attributes): IspCapability` |
| [RecordRadiusAccounting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/RecordRadiusAccounting.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(AccessService $service, array $accounting): RadiusSession` |
| [ResetUsagePeriod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/ResetUsagePeriod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(AccessService $service): AccessService` |
| [SynchronizeAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/SynchronizeAccessService.php) | `public function __construct(private DatabaseManager $database, private NetworkAdapterRegistry $adapters)`<br>`public function execute(AccessService $service, string $adapter): AccessService` |
| [TransitionAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/TransitionAccessService.php) | `public function handle(AccessService $service, string $status): AccessService` |
| [TransitionIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/TransitionIspCapability.php) | `public function handle(IspCapability $capability, string $status): IspCapability` |
| [NetworkAdapter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Contracts/NetworkAdapter.php) | `public function key(): string`<br>`public function install(array $attributes): array`<br>`public function suspend(array $attributes): array`<br>`public function remove(array $attributes): array` |
| [AccessServicePolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Policies/AccessServicePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, AccessService $record): bool`<br>`public function update(?Authenticatable $user, AccessService $record): bool` |
| [IspCapabilityPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Policies/IspCapabilityPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/AccessService.php) | No literal fillable array detected; inspect the model and API schema. |
| [IspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/IspCapability.php) | No literal fillable array detected; inspect the model and API schema. |
| [RadiusSession.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/RadiusSession.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [IspCapabilityController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-api/src/Http/Controllers/IspCapabilityController.php) | `public function accounts(Request $request): JsonResponse`<br>`public function showAccount(Request $request, int $record): JsonResponse`<br>`public function storeAccessService(Request $request, CreateAccessService $create): JsonResponse`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateIspCapability $create): JsonResponse`<br>`public function transition(Request $request, int $capability, TransitionIspCapability $transition): JsonResponse`<br>`public function transitionAccessService(Request $request, int $service, TransitionAccessService $transition): JsonResponse`<br>`public function synchronizeAccessService(Request $request, int $service, SynchronizeAccessService $synchronize): JsonResponse`<br>`public function recordAccounting(Request $request, int $service, RecordRadiusAccounting $record): JsonResponse`<br>`public function resetUsage(Request $request, int $service, ResetUsagePeriod $reset): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-isp-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.read'])->prefix('api/v1/billing/isp/capabilities')->group(function (): void {
Route::get('/', [IspCapabilityController::class, 'index'])->name('billing.isp.capabilities.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.write', 'idempotency'])->prefix('api/v1/billing/isp/capabilities')->group(function (): void {
Route::post('/', [IspCapabilityController::class, 'store'])->name('billing.isp.capabilities.store');
Route::patch('/{capability}/lifecycle', [IspCapabilityController::class, 'transition'])->whereNumber('capability')->name('billing.isp.capabilities.lifecycle');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.write', 'idempotency'])->prefix('api/v1/billing/isp')->group(function (): void {
Route::post('/', [IspCapabilityController::class, 'storeAccessService'])->name('billing.isp.store');
Route::patch('/{service}/lifecycle', [IspCapabilityController::class, 'transitionAccessService'])->whereNumber('service')->name('billing.isp.services.lifecycle');
Route::post('/{service}/synchronize', [IspCapabilityController::class, 'synchronizeAccessService'])->whereNumber('service')->name('billing.isp.services.synchronize');
Route::post('/{service}/accounting', [IspCapabilityController::class, 'recordAccounting'])->whereNumber('service')->name('billing.isp.services.accounting');
Route::post('/{service}/usage/reset', [IspCapabilityController::class, 'resetUsage'])->whereNumber('service')->name('billing.isp.services.usage.reset');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.read'])->prefix('api/v1/billing/isp')->group(function (): void {
Route::get('/', [IspCapabilityController::class, 'accounts'])->name('billing.isp.services.index');
Route::get('/{record}', [IspCapabilityController::class, 'showAccount'])->whereNumber('record')->name('billing.isp.services.show');
```
<!-- layer-implementation-plan:end -->
