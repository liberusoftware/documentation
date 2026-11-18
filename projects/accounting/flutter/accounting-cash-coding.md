# Accounting Cash Coding Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-cash-coding). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-cash-coding-flutter
**Matching core package:** module-accounting-accounting-cash-coding ([implementation](../core/accounting-cash-coding.md))
**Matching API package:** module-accounting-accounting-cash-coding-api ([contract](../api/accounting-cash-coding.md))

## Implementation plan

This adapter presents Accounting Cash Coding for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Cash Coding API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-cash-coding.md), and [API module](../api/accounting-cash-coding.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-cash-coding`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-cash-coding-flutter`](https://github.com/liberusoftware/module-accounting-cash-coding-flutter) (`module_accounting_cash_coding_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-cash-coding-dart-mobile`](https://github.com/liberusoftware/module-accounting-cash-coding-dart-mobile) (`module_accounting_cash_coding_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-cash-coding-dart-desktop`](https://github.com/liberusoftware/module-accounting-cash-coding-dart-desktop) (`module_accounting_cash_coding_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-cash-coding.md) · [Core plan](../core/accounting-cash-coding.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **High-volume statement coding** | Adaptive mobile cards/sheets for `high-volume statement coding` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `high-volume statement coding` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Bulk rules** | Adaptive mobile cards/sheets for `bulk rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `bulk rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tax/dimensions** | Adaptive mobile cards/sheets for `tax/dimensions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tax/dimensions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Payee creation policy** | Adaptive mobile cards/sheets for `payee creation policy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `payee creation policy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Review** | Adaptive mobile cards/sheets for `review` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `review` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Posting** | Adaptive mobile cards/sheets for `posting` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `posting` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Undo constraints** | Adaptive mobile cards/sheets for `undo constraints` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `undo constraints` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CashCodingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Queries/CashCodingQuery.php) | `public function forTeam(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Actions/CreateCashCodingBatch.php) | `public function handle(array $attributes): CashCodingBatch` |
| [TransitionCashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Actions/TransitionCashCodingBatch.php) | `public function review(CashCodingBatch $batch, ?int $actor = null): CashCodingBatch`<br>`public function post(CashCodingBatch $batch, ?int $actor = null): CashCodingBatch`<br>`public function undo(CashCodingBatch $batch, string $reason): CashCodingBatch` |
| [CashCodingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/src/Policies/CashCodingPolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, CashCodingBatch $batch): bool`<br>`public function create($user): bool`<br>`public function update($user, CashCodingBatch $batch): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Models/CashCodingBatch.php) | `team_id`, `reference`, `status`, `lines`, `payee_creation_policy`, `total_amount`, `currency`, `created_by`, `reviewed_by`, `posted_by`, `undo_reason`, `posted_at`, `undone_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CashCodingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/src/Http/Controllers/CashCodingController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateCashCodingBatch $action): CashCodingResource`<br>`public function show(string $batch): CashCodingResource`<br>`public function review(string $batch, TransitionCashCodingBatch $action): CashCodingResource`<br>`public function post(string $batch, TransitionCashCodingBatch $action): CashCodingResource`<br>`public function undo(Request $request, string $batch, TransitionCashCodingBatch $action): CashCodingResource` |

**Observed route declarations:**

[modules/accounting-cash-coding-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/cash-coding')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [CashCodingController::class, 'index'])->middleware('ability:accounting.cash-coding.read');
Route::post('/', [CashCodingController::class, 'store'])->middleware('ability:accounting.cash-coding.write');
Route::get('/{batch}', [CashCodingController::class, 'show'])->middleware('ability:accounting.cash-coding.read');
Route::post('/{batch}/review', [CashCodingController::class, 'review'])->middleware('ability:accounting.cash-coding.write');
Route::post('/{batch}/post', [CashCodingController::class, 'post'])->middleware('ability:accounting.cash-coding.write');
Route::post('/{batch}/undo', [CashCodingController::class, 'undo'])->middleware('ability:accounting.cash-coding.write');
```
<!-- layer-implementation-plan:end -->
