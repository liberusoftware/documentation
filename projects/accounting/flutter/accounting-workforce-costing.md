# Accounting Workforce Costing Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-workforce-costing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-workforce-costing-flutter
**Matching core package:** module-accounting-accounting-workforce-costing ([implementation](../core/accounting-workforce-costing.md))
**Matching API package:** module-accounting-accounting-workforce-costing-api ([contract](../api/accounting-workforce-costing.md))

## Implementation plan

This adapter presents Accounting Workforce Costing for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Workforce Costing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-workforce-costing.md), and [API module](../api/accounting-workforce-costing.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-workforce-costing`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-workforce-costing-flutter`](https://github.com/liberusoftware/module-accounting-workforce-costing-flutter) (`module_accounting_workforce_costing_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-workforce-costing-dart-mobile`](https://github.com/liberusoftware/module-accounting-workforce-costing-dart-mobile) (`module_accounting_workforce_costing_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-workforce-costing-dart-desktop`](https://github.com/liberusoftware/module-accounting-workforce-costing-dart-desktop) (`module_accounting_workforce_costing_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-workforce-costing.md) · [Core plan](../core/accounting-workforce-costing.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Time/payroll cost allocation to project** | Adaptive mobile cards/sheets for `time/payroll cost allocation to project` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `time/payroll cost allocation to project` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Department** | Adaptive mobile cards/sheets for `department` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `department` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Class/location** | Adaptive mobile cards/sheets for `class/location` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `class/location` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Capitalization rules** | Adaptive mobile cards/sheets for `capitalization rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `capitalization rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Profitability reporting** | Adaptive mobile cards/sheets for `profitability reporting` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `profitability reporting` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WorkforceProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Queries/WorkforceProfitability.php) | `public function handle(int $teamId, ?string $from = null, ?string $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/AllocateWorkforceCost.php) | `public function handle(WorkforceCost $cost, string\|WorkforceAllocationType $allocationType, string $allocationRef): WorkforceCost` |
| [CapitalizeWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/CapitalizeWorkforceCost.php) | `public function handle(WorkforceCost $cost): WorkforceCost` |
| [CreateWorkforceCostingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/CreateWorkforceCostingRule.php) | `public function handle(array $attributes): WorkforceCostingRule` |
| [RecordWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/RecordWorkforceCost.php) | `public function handle(array $attributes): WorkforceCost` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Models/WorkforceCost.php) | `team_id`, `worker_ref`, `source_type`, `source_id`, `cost_date`, `hours`, `hourly_rate`, `amount`, `allocation_type`, `allocation_ref`, `capitalized`, `status`, `metadata` |
| [WorkforceCostingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Models/WorkforceCostingRule.php) | `team_id`, `name`, `allocation_type`, `allocation_ref`, `hourly_rate`, `capitalize`, `active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkforceCostingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-api/src/Http/Controllers/WorkforceCostingController.php) | `public function costs(Request $request): mixed`<br>`public function record(Request $request, RecordWorkforceCost $action): mixed`<br>`public function allocate(Request $request, string $cost, AllocateWorkforceCost $action): mixed`<br>`public function capitalize(Request $request, string $cost, CapitalizeWorkforceCost $action): mixed`<br>`public function rules(Request $request): mixed`<br>`public function createRule(Request $request, CreateWorkforceCostingRule $action): mixed`<br>`public function profitability(Request $request, WorkforceProfitability $query): mixed` |

**Observed route declarations:**

[modules/accounting-workforce-costing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/workforce-costing')->middleware('auth:sanctum')->group(function (): void {
Route::get('/costs', [WorkforceCostingController::class, 'costs'])->middleware('ability:accounting.workforce-costing.read');
Route::post('/costs', [WorkforceCostingController::class, 'record'])->middleware('ability:accounting.workforce-costing.write');
Route::post('/costs/{cost}/allocate', [WorkforceCostingController::class, 'allocate'])->middleware('ability:accounting.workforce-costing.write');
Route::post('/costs/{cost}/capitalize', [WorkforceCostingController::class, 'capitalize'])->middleware('ability:accounting.workforce-costing.write');
Route::get('/rules', [WorkforceCostingController::class, 'rules'])->middleware('ability:accounting.workforce-costing.read');
Route::post('/rules', [WorkforceCostingController::class, 'createRule'])->middleware('ability:accounting.workforce-costing.write');
Route::get('/profitability', [WorkforceCostingController::class, 'profitability'])->middleware('ability:accounting.workforce-costing.read');
```
<!-- layer-implementation-plan:end -->
