# Accounting Credit Notes And Adjustments Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-credit-notes-and-adjustments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-credit-notes-and-adjustments-flutter
**Matching core package:** module-accounting-accounting-credit-notes-and-adjustments ([implementation](../core/accounting-credit-notes-and-adjustments.md))
**Matching API package:** module-accounting-accounting-credit-notes-and-adjustments-api ([contract](../api/accounting-credit-notes-and-adjustments.md))

## Implementation plan

This adapter presents Accounting Credit Notes And Adjustments for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Credit Notes And Adjustments API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-credit-notes-and-adjustments.md), and [API module](../api/accounting-credit-notes-and-adjustments.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-credit-notes-and-adjustments`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-credit-notes-and-adjustments-flutter`](https://github.com/liberusoftware/module-accounting-credit-notes-and-adjustments-flutter) (`module_accounting_credit_notes_and_adjustments_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-credit-notes-and-adjustments-dart-mobile`](https://github.com/liberusoftware/module-accounting-credit-notes-and-adjustments-dart-mobile) (`module_accounting_credit_notes_and_adjustments_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-credit-notes-and-adjustments-dart-desktop`](https://github.com/liberusoftware/module-accounting-credit-notes-and-adjustments-dart-desktop) (`module_accounting_credit_notes_and_adjustments_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-credit-notes-and-adjustments.md) · [Core plan](../core/accounting-credit-notes-and-adjustments.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Full/partial credits** | Adaptive mobile cards/sheets for `full/partial credits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `full/partial credits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reasons** | Adaptive mobile cards/sheets for `reasons` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reasons` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approval** | Adaptive mobile cards/sheets for `approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Invoice allocation** | Adaptive mobile cards/sheets for `invoice allocation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `invoice allocation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Refund/store-credit references** | Adaptive mobile cards/sheets for `refund/store-credit references` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `refund/store-credit references` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tax correction** | Adaptive mobile cards/sheets for `tax correction` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tax correction` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Audit** | Adaptive mobile cards/sheets for `audit` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `audit` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CreditNoteQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Queries/CreditNoteQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/AllocateCreditNote.php) | `public function handle(CreditNote $note, string $invoiceRef, float $amount): CreditNoteAllocation` |
| [ApproveCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/ApproveCreditNote.php) | `public function handle(CreditNote $note, int $actor): CreditNote` |
| [CreateCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/CreateCreditNote.php) | `public function handle(array $attributes): CreditNote` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Models/CreditNote.php) | `team_id`, `customer_id`, `credit_ref`, `status`, `reason`, `currency`, `amount`, `allocated_amount`, `tax_amount`, `refund_reference`, `store_credit_reference`, `approved_by`, `approved_at`, `evidence`, `metadata` |
| [CreditNoteAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Models/CreditNoteAllocation.php) | `credit_note_id`, `team_id`, `invoice_ref`, `amount` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CreditNotesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments-api/src/Http/Controllers/CreditNotesController.php) | `public function index(CreditNoteQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCreditNote $action): JsonResponse`<br>`public function approve(Request $request, string $note, ApproveCreditNote $action): JsonResponse`<br>`public function allocate(Request $request, string $note, AllocateCreditNote $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-credit-notes-and-adjustments-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/credit-notes-and-adjustments')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.credit-notes-and-adjustments.read')->get('/', [CreditNotesController::class, 'index']);
Route::middleware('ability:accounting.credit-notes-and-adjustments.write')->group(function (): void {
Route::post('/', [CreditNotesController::class, 'store']);
Route::post('/{note}/approve', [CreditNotesController::class, 'approve']);
Route::post('/{note}/allocations', [CreditNotesController::class, 'allocate']);
```
<!-- layer-implementation-plan:end -->
