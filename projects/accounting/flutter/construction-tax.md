# Construction Tax Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#construction-tax). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-construction-tax-flutter
**Matching core package:** module-accounting-construction-tax ([implementation](../core/construction-tax.md))
**Matching API package:** module-accounting-construction-tax-api ([contract](../api/construction-tax.md))

## Implementation plan

This adapter presents Construction Tax for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Construction Tax API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/construction-tax.md), and [API module](../api/construction-tax.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `construction-tax`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-construction-tax-flutter`](https://github.com/liberusoftware/module-accounting-construction-tax-flutter) (`module_accounting_construction_tax_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-construction-tax-dart-mobile`](https://github.com/liberusoftware/module-accounting-construction-tax-dart-mobile) (`module_accounting_construction_tax_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-construction-tax-dart-desktop`](https://github.com/liberusoftware/module-accounting-construction-tax-dart-desktop) (`module_accounting_construction_tax_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/construction-tax.md) · [Core plan](../core/construction-tax.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **CIS-style subcontractor verification** | Adaptive mobile cards/sheets for `cis-style subcontractor verification` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cis-style subcontractor verification` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Deduction rates** | Adaptive mobile cards/sheets for `deduction rates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `deduction rates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Statements** | Adaptive mobile cards/sheets for `statements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `statements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Monthly returns** | Adaptive mobile cards/sheets for `monthly returns` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `monthly returns` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Corrections** | Adaptive mobile cards/sheets for `corrections` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `corrections` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Filing adapters** | Adaptive mobile cards/sheets for `filing adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `filing adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConstructionTaxQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Queries/ConstructionTaxQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CorrectConstructionTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/CorrectConstructionTaxReturn.php) | `public function handle(ConstructionTaxRecord $record, array $correction): ConstructionTaxRecord` |
| [CreateConstructionTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/CreateConstructionTaxRecord.php) | `public function handle(array $attributes): ConstructionTaxRecord` |
| [IssueConstructionTaxStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/IssueConstructionTaxStatement.php) | `public function handle(ConstructionTaxRecord $record, array $statement): ConstructionTaxRecord` |
| [SubmitConstructionTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/SubmitConstructionTaxReturn.php) | `public function handle(ConstructionTaxRecord $record, string $adapter): ConstructionTaxRecord` |
| [VerifySubcontractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/VerifySubcontractor.php) | `public function handle(ConstructionTaxRecord $record, array $verification): ConstructionTaxRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConstructionTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Models/ConstructionTaxRecord.php) | `team_id`, `subcontractor_ref`, `verification_status`, `deduction_rate`, `tax_period`, `gross_amount`, `deduction_amount`, `return_status`, `filing_adapter`, `verification`, `statement`, `correction` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConstructionTaxController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax-api/src/Http/Controllers/ConstructionTaxController.php) | `public function index(ConstructionTaxQuery $query): JsonResponse`<br>`public function store(Request $request, CreateConstructionTaxRecord $action): JsonResponse`<br>`public function verify(Request $request, string $record, VerifySubcontractor $action): JsonResponse`<br>`public function submit(Request $request, string $record, SubmitConstructionTaxReturn $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-construction-tax-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/construction-tax')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.construction-tax.read')->get('/', [ConstructionTaxController::class, 'index']);
Route::middleware('ability:accounting.construction-tax.write')->group(function (): void {
Route::post('/', [ConstructionTaxController::class, 'store']);
Route::post('/{record}/verify', [ConstructionTaxController::class, 'verify']);
Route::post('/{record}/submit', [ConstructionTaxController::class, 'submit']);
```
<!-- layer-implementation-plan:end -->
