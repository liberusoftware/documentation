# General Ledger Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#general-ledger). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-general-ledger-flutter
**Matching core package:** module-accounting-general-ledger ([implementation](../core/general-ledger.md))
**Matching API package:** module-accounting-general-ledger-api ([contract](../api/general-ledger.md))

## Implementation plan

This adapter presents General Ledger for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test General Ledger API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/general-ledger.md), and [API module](../api/general-ledger.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `general-ledger`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-general-ledger-flutter`](https://github.com/liberusoftware/module-accounting-general-ledger-flutter) (`module_accounting_general_ledger_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-general-ledger-dart-mobile`](https://github.com/liberusoftware/module-accounting-general-ledger-dart-mobile) (`module_accounting_general_ledger_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-general-ledger-dart-desktop`](https://github.com/liberusoftware/module-accounting-general-ledger-dart-desktop) (`module_accounting_general_ledger_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/general-ledger.md) · [Core plan](../core/general-ledger.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Journals** | Adaptive mobile cards/sheets for `journals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `journals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Balanced postings** | Adaptive mobile cards/sheets for `balanced postings` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `balanced postings` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Recurring journals** | Adaptive mobile cards/sheets for `recurring journals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recurring journals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reversals** | Adaptive mobile cards/sheets for `reversals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reversals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Corrections** | Adaptive mobile cards/sheets for `corrections` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `corrections` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Allocations** | Adaptive mobile cards/sheets for `allocations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `allocations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Accruals** | Adaptive mobile cards/sheets for `accruals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `accruals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Prepayments** | Adaptive mobile cards/sheets for `prepayments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `prepayments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Balances** | Adaptive mobile cards/sheets for `balances` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `balances` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AccountBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Queries/AccountBalances.php) | `public function handle(int $bookId, ?string $through = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateAccrual.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateAllocation.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateCorrection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateCorrection.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateJournal.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreatePrepayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreatePrepayment.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateTypedJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateTypedJournal.php) | `public function handle(JournalType $type, array $attributes, array $lines): JournalEntry` |
| [GenerateRecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/GenerateRecurringJournal.php) | `public function handle(RecurringJournal $template, ?string $actor = null): JournalEntry` |
| [PostJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/PostJournal.php) | `public function handle(JournalEntry $journal, ?string $actor = null): JournalEntry` |
| [ReverseJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/ReverseJournal.php) | `public function handle(JournalEntry $journal, array $attributes = [], ?string $actor = null): JournalEntry` |
| [SaveRecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/SaveRecurringJournal.php) | `public function handle(array $attributes, ?RecurringJournal $template = null): RecurringJournal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [JournalEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/JournalEntry.php) | `book_id`, `entry_number`, `entry_date`, `journal_type`, `status`, `description`, `source_type`, `source_id`, `reversal_of_id`, `posted_by`, `posted_at`, `metadata` |
| [JournalLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/JournalLine.php) | `journal_entry_id`, `account_id`, `debit`, `credit`, `description`, `dimensions` |
| [RecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/RecurringJournal.php) | `book_id`, `name`, `frequency`, `next_run_on`, `end_on`, `is_active`, `description`, `lines`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [GeneralLedgerController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-api/src/Http/Controllers/GeneralLedgerController.php) | `public function index(Request $request)`<br>`public function show(string $journal): JournalResource`<br>`public function store(Request $request, CreateJournal $create)`<br>`public function storeTyped(Request $request, string $type, CreateTypedJournal $create): JsonResource`<br>`public function post(Request $request, string $journal, PostJournal $post): JournalResource`<br>`public function reverse(Request $request, string $journal, ReverseJournal $reverse): JournalResource`<br>`public function balances(Request $request, AccountBalances $balances)`<br>`public function saveRecurring(Request $request, SaveRecurringJournal $save)`<br>`public function generateRecurring(Request $request, string $recurring, GenerateRecurringJournal $generate): JournalResource`<br>`public function destroy(string $journal): Response` |

**Observed route declarations:**

[modules/accounting-general-ledger-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/accounting/general-ledger')->group(function (): void {
Route::middleware('ability:accounting.general-ledger.read')->group(function (): void {
Route::get('/', [GeneralLedgerController::class, 'index']);
Route::get('/balances', [GeneralLedgerController::class, 'balances']);
Route::get('/{journal}', [GeneralLedgerController::class, 'show']);
Route::middleware('ability:accounting.general-ledger.write')->group(function (): void {
Route::post('/', [GeneralLedgerController::class, 'store']);
Route::post('/recurring', [GeneralLedgerController::class, 'saveRecurring']);
Route::post('/recurring/{recurring}/generate', [GeneralLedgerController::class, 'generateRecurring']);
Route::post('/'.$type, [GeneralLedgerController::class, 'storeTyped'])->defaults('type', $type);
}Route::post('/{journal}/post', [GeneralLedgerController::class, 'post']);
Route::post('/{journal}/reverse', [GeneralLedgerController::class, 'reverse']);
Route::delete('/{journal}', [GeneralLedgerController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
