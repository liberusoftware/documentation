# Pricing Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#pricing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-pricing-flutter
**Matching core package:** module-billing-pricing ([implementation](../core/pricing.md))
**Matching API package:** module-billing-pricing-api ([contract](../api/pricing.md))

## Implementation plan

This adapter presents Pricing for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Pricing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/pricing.md), and [API module](../api/pricing.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `pricing`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) | [`module-billing-pricing-flutter`](https://github.com/liberusoftware/module-billing-pricing-flutter) (`module_billing_pricing_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) | [`module-billing-pricing-dart-mobile`](https://github.com/liberusoftware/module-billing-pricing-dart-mobile) (`module_billing_pricing_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) | [`module-billing-pricing-dart-desktop`](https://github.com/liberusoftware/module-billing-pricing-dart-desktop) (`module_billing_pricing_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | [API plan](../api/pricing.md) · [Core plan](../core/pricing.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Recurring/one-time/usage/tiered pricing** | Adaptive mobile cards/sheets for `recurring/one-time/usage/tiered pricing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recurring/one-time/usage/tiered pricing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Contracts** | Adaptive mobile cards/sheets for `contracts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `contracts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Discounts** | Adaptive mobile cards/sheets for `discounts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `discounts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Proration** | Adaptive mobile cards/sheets for `proration` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `proration` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Snapshots** | Adaptive mobile cards/sheets for `snapshots` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `snapshots` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
