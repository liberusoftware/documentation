# Pricing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#pricing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-pricing-react-native
**Matching core package:** module-billing-pricing ([implementation](../core/pricing.md))
**Matching API package:** module-billing-pricing-api ([contract](../api/pricing.md))

## Implementation plan

This adapter presents Pricing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Pricing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/pricing.md), and [API module](../api/pricing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `pricing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/pricing.md)) |
| Capability React Native module skeleton | [`module-billing-pricing-react-native`](https://github.com/liberusoftware/module-billing-pricing-react-native) (`@liberusoftware/module-billing-pricing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Recurring/one-time/usage/tiered pricing** | Progressive mobile list/detail/sheet flow for `recurring/one-time/usage/tiered pricing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contracts** | Progressive mobile list/detail/sheet flow for `contracts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Discounts** | Progressive mobile list/detail/sheet flow for `discounts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Proration** | Progressive mobile list/detail/sheet flow for `proration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Snapshots** | Progressive mobile list/detail/sheet flow for `snapshots` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListPricingPlans.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Queries/ListPricingPlans.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculatePricingPlanAmount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CalculatePricingPlanAmount.php) | `public function execute(PricingPlan $plan, array $options = []): int` |
| [CalculateProration.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CalculateProration.php) | `public function execute(int $amountMinor, int $remainingDays, int $periodDays): int` |
| [CalculateUsageBasedPrice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CalculateUsageBasedPrice.php) | `public function __construct(private readonly CalculatePricingPlanAmount $calculate)`<br>`public function execute( PricingPlan $plan, int $meterId, CarbonInterface $start, CarbonInterface $end, ?int $customerId = null, ): array` |
| [CapturePricingSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CapturePricingSnapshot.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PricingPlan $plan): PricingSnapshot` |
| [CreatePricingContract.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CreatePricingContract.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PricingContract` |
| [CreatePricingPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/CreatePricingPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PricingPlan` |
| [RedeemPricingDiscount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Actions/RedeemPricingDiscount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PricingDiscount $discount): PricingDiscount` |
| [PricingPlanPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Policies/PricingPlanPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, PricingPlan $plan): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, PricingPlan $plan): bool` |
| [PricingRecordPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Policies/PricingRecordPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PricingContract.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Models/PricingContract.php) | No literal fillable array detected; inspect the model and API schema. |
| [PricingDiscount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Models/PricingDiscount.php) | No literal fillable array detected; inspect the model and API schema. |
| [PricingPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Models/PricingPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [PricingSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing/src/Models/PricingSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PricingPlanController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing-api/src/Http/Controllers/PricingPlanController.php) | `public function index(Request $request, ListPricingPlans $query): JsonResponse`<br>`public function store(Request $request, CreatePricingPlan $create): JsonResponse` |
| [PricingSupportController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing-api/src/Http/Controllers/PricingSupportController.php) | `public function contracts(Request $request): JsonResponse`<br>`public function createContract(Request $request, CreatePricingContract $create): JsonResponse`<br>`public function discounts(Request $request): JsonResponse`<br>`public function snapshots(Request $request): JsonResponse`<br>`public function redeem(Request $request, PricingDiscount $discount, RedeemPricingDiscount $redeem): JsonResponse`<br>`public function snapshot(Request $request, PricingPlan $plan, CapturePricingSnapshot $capture): JsonResponse`<br>`public function proration(Request $request, CalculateProration $calculate): JsonResponse`<br>`public function usage(Request $request, PricingPlan $plan, CalculateUsageBasedPrice $calculate): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-pricing-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-pricing-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.pricing.read'])->prefix('api/v1/billing/pricing')->name('billing.pricing.')->group(function (): void {
Route::get('/contracts', [PricingSupportController::class, 'contracts'])->name('contracts.index');
Route::get('/discounts', [PricingSupportController::class, 'discounts'])->name('discounts.index');
Route::get('/snapshots', [PricingSupportController::class, 'snapshots'])->name('snapshots.index');
Route::post('/proration', [PricingSupportController::class, 'proration'])->name('proration');
Route::post('/plans/{plan}/usage', [PricingSupportController::class, 'usage'])->name('plans.usage');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.pricing.write', 'idempotency'])->prefix('api/v1/billing/pricing')->name('billing.pricing.')->group(function (): void {
Route::post('/contracts', [PricingSupportController::class, 'createContract'])->name('contracts.store');
Route::post('/discounts/{discount}/redeem', [PricingSupportController::class, 'redeem'])->name('discounts.redeem');
Route::post('/plans/{plan}/snapshot', [PricingSupportController::class, 'snapshot'])->name('plans.snapshot');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.pricing.read'])->prefix('api/v1/billing/pricing')->name('billing.pricing.')->group(fn () => Route::get('/', [PricingPlanController::class, 'index'])->name('plans.index'));
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.pricing.write', 'idempotency'])->prefix('api/v1/billing/pricing')->name('billing.pricing.')->group(fn () => Route::post('/', [PricingPlanController::class, 'store'])->name('plans.store'));
```
<!-- layer-implementation-plan:end -->
