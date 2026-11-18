# Module Billing Billing Core Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-billing-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-module-billing-billing-core-flutter
**Matching core package:** module-billing-module-billing-billing-core ([implementation](../core/module-billing-billing-core.md))
**Matching API package:** module-billing-module-billing-billing-core-api ([contract](../api/module-billing-billing-core.md))

## Implementation plan

This adapter presents Module Billing Billing Core for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Billing Billing Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/module-billing-billing-core.md), and [API module](../api/module-billing-billing-core.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `module-billing-billing-core`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) | [`module-billing-billing-core-flutter`](https://github.com/liberusoftware/module-billing-billing-core-flutter) (`module_billing_billing_core_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) | [`module-billing-billing-core-dart-mobile`](https://github.com/liberusoftware/module-billing-billing-core-dart-mobile) (`module_billing_billing_core_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) | [`module-billing-billing-core-dart-desktop`](https://github.com/liberusoftware/module-billing-billing-core-dart-desktop) (`module_billing_billing_core_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | [API plan](../api/module-billing-billing-core.md) · [Core plan](../core/module-billing-billing-core.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Accounts** | Adaptive mobile cards/sheets for `accounts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `accounts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Contacts** | Adaptive mobile cards/sheets for `contacts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `contacts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Currencies** | Adaptive mobile cards/sheets for `currencies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `currencies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tax profiles** | Adaptive mobile cards/sheets for `tax profiles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tax profiles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Sequences** | Adaptive mobile cards/sheets for `sequences` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sequences` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Terms** | Adaptive mobile cards/sheets for `terms` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `terms` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Billing settings** | Adaptive mobile cards/sheets for `billing settings` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `billing settings` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListBillingAccounts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingAccounts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListBillingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingRecords.php) | `public function execute(string $modelClass, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateTax.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CalculateTax.php) | `public function execute(int $teamId, float $amount, ?string $jurisdiction = null, ?int $customerId = null): array` |
| [ConvertCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/ConvertCurrency.php) | `public function execute(int $teamId, float $amount, string $from, string $to): array` |
| [CreateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): BillingAccount` |
| [CreateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $modelClass, array $attributes): Model` |
| [DeleteBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account): void` |
| [DeleteBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, string $recordType): void` |
| [TransitionBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/TransitionBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, BillingAccountStatus $status): BillingAccount` |
| [UpdateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, array $attributes): BillingAccount` |
| [UpdateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, array $attributes): Model` |
| [BillingAccountPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Policies/BillingAccountPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, BillingAccount $account): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, BillingAccount $account): bool`<br>`public function delete(object $user, BillingAccount $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingCurrency.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSequence.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSetting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSetting.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxExemption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxExemption.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxProfile.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTerm.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTerm.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [BillingAccountController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-api/src/Http/Controllers/BillingAccountController.php) | `public function index(Request $request, ListBillingAccounts $query): JsonResponse`<br>`public function store(Request $request, CreateBillingAccount $create): JsonResponse`<br>`public function update(Request $request, int $account, UpdateBillingAccount $update): JsonResponse`<br>`public function transition(Request $request, int $account, TransitionBillingAccount $transition): JsonResponse`<br>`public function destroy(Request $request, int $account, DeleteBillingAccount $delete): JsonResponse` |
| [BillingCoreRecordController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-api/src/Http/Controllers/BillingCoreRecordController.php) | `public function index(Request $request, string $type, ListBillingRecords $list): JsonResponse`<br>`public function store(Request $request, string $type, CreateBillingRecord $create): JsonResponse`<br>`public function convertCurrency(Request $request, ConvertCurrency $convert): JsonResponse`<br>`public function calculateTax(Request $request, CalculateTax $calculate): JsonResponse`<br>`public function update(Request $request, string $type, int $record, UpdateBillingRecord $update): JsonResponse`<br>`public function destroy(Request $request, string $type, int $record, DeleteBillingRecord $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-core-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.billing-core.read'])
Route::get('/', [BillingAccountController::class, 'index'])->name('accounts.index');
Route::post('/currencies/convert', [BillingCoreRecordController::class, 'convertCurrency'])->name('currencies.convert');
Route::post('/tax/calculate', [BillingCoreRecordController::class, 'calculateTax'])->name('tax.calculate');
Route::get('/{type}', [BillingCoreRecordController::class, 'index'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.billing-core.write', 'idempotency'])
Route::post('/', [BillingAccountController::class, 'store'])->name('accounts.store');
Route::patch('/{account}', [BillingAccountController::class, 'update'])->whereNumber('account')->name('accounts.update');
Route::delete('/{account}', [BillingAccountController::class, 'destroy'])->whereNumber('account')->name('accounts.destroy');
Route::patch('/{account}/status', [BillingAccountController::class, 'transition'])->whereNumber('account')->name('accounts.status');
Route::post('/{type}', [BillingCoreRecordController::class, 'store'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.store');
Route::patch('/{type}/{record}', [BillingCoreRecordController::class, 'update'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.update');
Route::delete('/{type}/{record}', [BillingCoreRecordController::class, 'destroy'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.destroy');
```
<!-- layer-implementation-plan:end -->
