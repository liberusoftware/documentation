# Recurring Transactions Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#recurring-transactions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-recurring-transactions-flutter
**Matching core package:** module-accounting-recurring-transactions ([implementation](../core/recurring-transactions.md))
**Matching API package:** module-accounting-recurring-transactions-api ([contract](../api/recurring-transactions.md))

## Implementation plan

This adapter presents Recurring Transactions for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Recurring Transactions API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/recurring-transactions.md), and [API module](../api/recurring-transactions.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `recurring-transactions`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-recurring-transactions-flutter`](https://github.com/liberusoftware/module-accounting-recurring-transactions-flutter) (`module_accounting_recurring_transactions_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-recurring-transactions-dart-mobile`](https://github.com/liberusoftware/module-accounting-recurring-transactions-dart-mobile) (`module_accounting_recurring_transactions_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-recurring-transactions-dart-desktop`](https://github.com/liberusoftware/module-accounting-recurring-transactions-dart-desktop) (`module_accounting_recurring_transactions_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/recurring-transactions.md) · [Core plan](../core/recurring-transactions.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Templates** | Adaptive mobile cards/sheets for `templates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `templates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Schedules** | Adaptive mobile cards/sheets for `schedules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `schedules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Date/amount rules** | Adaptive mobile cards/sheets for `date/amount rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `date/amount rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approval** | Adaptive mobile cards/sheets for `approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Draft/automatic generation** | Adaptive mobile cards/sheets for `draft/automatic generation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `draft/automatic generation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Exceptions** | Adaptive mobile cards/sheets for `exceptions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `exceptions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Expiry** | Adaptive mobile cards/sheets for `expiry` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `expiry` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **History** | Adaptive mobile cards/sheets for `history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveRecurringTemplate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Actions/ApproveRecurringTemplate.php) | `public function handle(RecurringTemplate $template, ?int $actorId = null): RecurringTemplate` |
| [CreateRecurringTemplate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Actions/CreateRecurringTemplate.php) | `public function handle(array $attributes): RecurringTemplate` |
| [GenerateRecurringOccurrences.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Actions/GenerateRecurringOccurrences.php) | `public function handle(RecurringTemplate $template, string $throughDate, ?int $safetyCap = 120): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RecurringException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Models/RecurringException.php) | `template_id`, `occurrence_id`, `kind`, `message`, `status`, `resolved_at`, `metadata` |
| [RecurringOccurrence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Models/RecurringOccurrence.php) | `template_id`, `occurrence_on`, `idempotency_key`, `status`, `generated_payload`, `error_message`, `generated_at`, `metadata` |
| [RecurringTemplate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Models/RecurringTemplate.php) | `team_id`, `name`, `transaction_type`, `frequency`, `starts_on`, `next_run_on`, `ends_on`, `status`, `automatic`, `date_rules`, `amount_rules`, `payload`, `approved_by`, `approved_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [RecurringTransactionsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions-api/src/Http/Controllers/RecurringTransactionsController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateRecurringTemplate $action): mixed`<br>`public function show(Request $request, RecurringTemplate $template): RecurringTemplate`<br>`public function approve(Request $request, RecurringTemplate $template, ApproveRecurringTemplate $action): RecurringTemplate`<br>`public function generate(Request $request, RecurringTemplate $template, GenerateRecurringOccurrences $action): int` |

**Observed route declarations:**

[modules/accounting-recurring-transactions-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/recurring-transactions')->group(function (): void {
Route::middleware('ability:accounting.recurring-transactions.read')->group(function (): void {
Route::get('/', [RecurringTransactionsController::class, 'index']);
Route::get('/{template}', [RecurringTransactionsController::class, 'show']);
Route::middleware('ability:accounting.recurring-transactions.write')->group(function (): void {
Route::post('/', [RecurringTransactionsController::class, 'store']);
Route::post('/{template}/approve', [RecurringTransactionsController::class, 'approve']);
Route::post('/{template}/generate', [RecurringTransactionsController::class, 'generate']);
```
<!-- layer-implementation-plan:end -->
