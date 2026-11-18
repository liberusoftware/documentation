# Module Billing Provisioning React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-provisioning). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-module-billing-provisioning-react-native
**Matching core package:** module-billing-module-billing-provisioning ([implementation](../core/module-billing-provisioning.md))
**Matching API package:** module-billing-module-billing-provisioning-api ([contract](../api/module-billing-provisioning.md))

## Implementation plan

This adapter presents Module Billing Provisioning for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Billing Provisioning API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-billing-provisioning.md), and [API module](../api/module-billing-provisioning.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-billing-provisioning`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-provisioning.md)) |
| Capability React Native module skeleton | [`module-billing-provisioning-react-native`](https://github.com/liberusoftware/module-billing-provisioning-react-native) (`@liberusoftware/module-billing-provisioning-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Service state machine** | Progressive mobile list/detail/sheet flow for `service state machine` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provider drivers** | Progressive mobile list/detail/sheet flow for `provider drivers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Queued operations** | Progressive mobile list/detail/sheet flow for `queued operations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rollback** | Progressive mobile list/detail/sheet flow for `rollback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Polling** | Progressive mobile list/detail/sheet flow for `polling` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListProvisionedServices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Queries/ListProvisionedServices.php) | `public function execute(?int $teamId = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/CreateProvisionedService.php) | `public function execute(array $attributes): ProvisionedService` |
| [QueueProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/QueueProvisioningOperation.php) | `public function execute(ProvisionedService $service, string $operation, array $payload = []): ProvisioningOperation` |
| [ReconcileProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/ReconcileProvisionedService.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(ProvisionedService $service): ProvisionedService` |
| [RunProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/RunProvisioningOperation.php) | `public function __construct(private DatabaseManager $database, private ProvisioningDriverRegistry $drivers)`<br>`public function execute(ProvisioningOperation $operation): ProvisioningOperation` |
| [TransitionProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/TransitionProvisionedService.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(ProvisionedService $service, ProvisioningState $state, ?string $error = null): ProvisionedService` |
| [ProvisioningDriver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Contracts/ProvisioningDriver.php) | `public function provision(ProvisionedService $service): string`<br>`public function deprovision(ProvisionedService $service): void`<br>`public function poll(ProvisionedService $service): array` |
| [ProvisioningPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Policies/ProvisioningPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |
| [ProvisioningDriverRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Services/ProvisioningDriverRegistry.php) | `public function register(string $provider, ProvisioningDriver $driver): void`<br>`public function resolve(string $provider): ProvisioningDriver` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Models/ProvisionedService.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Models/ProvisioningOperation.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProvisioningOperationController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-api/src/Http/Controllers/ProvisioningOperationController.php) | `public function services(Request $request): JsonResponse`<br>`public function showService(Request $request, int $provisionedService): JsonResponse`<br>`public function storeService(Request $request, CreateProvisionedService $create): JsonResponse`<br>`public function index(Request $request): JsonResponse`<br>`public function queue(Request $request, ProvisionedService $provisionedService, QueueProvisioningOperation $queue): JsonResponse`<br>`public function reconcile(Request $request, ProvisionedService $provisionedService, ReconcileProvisionedService $reconcile): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-provisioning-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.provisioning.read'])->prefix('api/v1/billing/provisioning/operations')->group(function (): void {
Route::get('/', [ProvisioningOperationController::class, 'index'])->name('billing.provisioning.operations.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.provisioning.write', 'idempotency'])->prefix('api/v1/billing/provisioning')->group(function (): void {
Route::post('/', [ProvisioningOperationController::class, 'storeService'])->name('billing.provisioning.store');
Route::post('/{provisionedService}/operations', [ProvisioningOperationController::class, 'queue'])->name('billing.provisioning.operations.store');
Route::post('/{provisionedService}/reconcile', [ProvisioningOperationController::class, 'reconcile'])->name('billing.provisioning.reconcile');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.provisioning.read'])->prefix('api/v1/billing/provisioning')->group(function (): void {
Route::get('/', [ProvisioningOperationController::class, 'services'])->name('billing.provisioning.services.index');
Route::get('/{provisionedService}', [ProvisioningOperationController::class, 'showService'])->whereNumber('provisionedService')->name('billing.provisioning.services.show');
```
<!-- layer-implementation-plan:end -->
