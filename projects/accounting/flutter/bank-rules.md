# Bank Rules Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bank-rules). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-bank-rules-flutter
**Matching core package:** module-accounting-bank-rules ([implementation](../core/bank-rules.md))
**Matching API package:** module-accounting-bank-rules-api ([contract](../api/bank-rules.md))

## Implementation plan

This adapter presents Bank Rules for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Bank Rules API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/bank-rules.md), and [API module](../api/bank-rules.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `bank-rules`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-bank-rules-flutter`](https://github.com/liberusoftware/module-accounting-bank-rules-flutter) (`module_accounting_bank_rules_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-bank-rules-dart-mobile`](https://github.com/liberusoftware/module-accounting-bank-rules-dart-mobile) (`module_accounting_bank_rules_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-bank-rules-dart-desktop`](https://github.com/liberusoftware/module-accounting-bank-rules-dart-desktop) (`module_accounting_bank_rules_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/bank-rules.md) · [Core plan](../core/bank-rules.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Payee/text/amount/account conditions** | Adaptive mobile cards/sheets for `payee/text/amount/account conditions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `payee/text/amount/account conditions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Split/category/tax/dimension actions** | Adaptive mobile cards/sheets for `split/category/tax/dimension actions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `split/category/tax/dimension actions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Priority** | Adaptive mobile cards/sheets for `priority` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `priority` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Suggestions/automation** | Adaptive mobile cards/sheets for `suggestions/automation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `suggestions/automation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Testing** | Adaptive mobile cards/sheets for `testing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `testing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **History** | Adaptive mobile cards/sheets for `history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BankRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Queries/BankRuleQuery.php) | `public function forTeam(int $teamId): Builder`<br>`public function matching(int $teamId, array $transaction): array`<br>`public function matches(array $conditions, array $transaction): bool` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordBankRuleDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/RecordBankRuleDecision.php) | `public function handle(BankRule $rule, string $transactionReference, bool $matched, string $outcome, array $actionsApplied = [], ?string $actorReference = null): BankRuleHistory` |
| [SaveBankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/SaveBankRule.php) | `public function handle(array $attributes, ?BankRule $rule = null): BankRule` |
| [TestBankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/TestBankRule.php) | `public function __construct(private readonly BankRuleQuery $query)`<br>`public function handle(BankRule $rule, array $transaction): array` |
| [BankRulesPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/src/Policies/BankRulesPolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, BankRule $rule): bool`<br>`public function create($user): bool`<br>`public function update($user, BankRule $rule): bool`<br>`public function delete($user, BankRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Models/BankRule.php) | `team_id`, `name`, `priority`, `enabled`, `conditions`, `actions`, `automation_mode`, `metadata` |
| [BankRuleHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Models/BankRuleHistory.php) | `team_id`, `rule_id`, `transaction_reference`, `outcome`, `matched`, `actions_applied`, `actor_reference`, `created_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BankRuleController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/src/Http/Controllers/BankRuleController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, SaveBankRule $action): BankRuleResource`<br>`public function show(string $rule): BankRuleResource`<br>`public function update(Request $request, string $rule, SaveBankRule $action): BankRuleResource`<br>`public function destroy(string $rule): mixed`<br>`public function test(Request $request, string $rule, TestBankRule $action): mixed`<br>`public function history(string $rule): mixed` |

**Observed route declarations:**

[modules/accounting-bank-rules-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/bank-rules')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BankRuleController::class, 'index'])->middleware('ability:accounting.bank-rules.read');
Route::post('/', [BankRuleController::class, 'store'])->middleware('ability:accounting.bank-rules.write');
Route::get('/{rule}', [BankRuleController::class, 'show'])->middleware('ability:accounting.bank-rules.read');
Route::patch('/{rule}', [BankRuleController::class, 'update'])->middleware('ability:accounting.bank-rules.write');
Route::delete('/{rule}', [BankRuleController::class, 'destroy'])->middleware('ability:accounting.bank-rules.write');
Route::post('/{rule}/test', [BankRuleController::class, 'test'])->middleware('ability:accounting.bank-rules.read');
Route::get('/{rule}/history', [BankRuleController::class, 'history'])->middleware('ability:accounting.bank-rules.read');
```
<!-- layer-implementation-plan:end -->
