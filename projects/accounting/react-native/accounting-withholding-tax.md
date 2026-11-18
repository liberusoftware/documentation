# Accounting Withholding Tax React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-withholding-tax). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-withholding-tax-react-native
**Matching core package:** module-accounting-accounting-withholding-tax ([implementation](../core/accounting-withholding-tax.md))
**Matching API package:** module-accounting-accounting-withholding-tax-api ([contract](../api/accounting-withholding-tax.md))

## Implementation plan

This adapter presents Accounting Withholding Tax for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Withholding Tax API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-withholding-tax.md), and [API module](../api/accounting-withholding-tax.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-withholding-tax`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-withholding-tax.md)) |
| Capability React Native module skeleton | [`module-accounting-withholding-tax-react-native`](https://github.com/liberusoftware/module-accounting-withholding-tax-react-native) (`@liberusoftware/module-accounting-withholding-tax-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Rules** | Progressive mobile list/detail/sheet flow for `rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Certificates** | Progressive mobile list/detail/sheet flow for `certificates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Supplier/customer deductions** | Progressive mobile list/detail/sheet flow for `supplier/customer deductions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Liabilities** | Progressive mobile list/detail/sheet flow for `liabilities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Remittance** | Progressive mobile list/detail/sheet flow for `remittance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Statements** | Progressive mobile list/detail/sheet flow for `statements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Regional filing adapters** | Progressive mobile list/detail/sheet flow for `regional filing adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateWithholdingTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CalculateWithholdingTax.php) | `public function handle(WithholdingTaxRule $rule, array $attributes): WithholdingTaxDeduction` |
| [CreateWithholdingTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CreateWithholdingTaxRule.php) | `public function handle(array $attributes): WithholdingTaxRule` |
| [RemitWithholdingTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/RemitWithholdingTax.php) | `public function handle(WithholdingTaxLiability $liability, array $attributes): WithholdingTaxRemittance` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WithholdingTaxCertificate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxCertificate.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `certificate_ref`, `valid_from`, `valid_until`, `status`, `metadata` |
| [WithholdingTaxDeduction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxDeduction.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `source_ref`, `currency`, `gross_amount`, `withheld_amount`, `status`, `metadata` |
| [WithholdingTaxFilingAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxFilingAdapter.php) | `team_id`, `jurisdiction`, `provider`, `status`, `configuration` |
| [WithholdingTaxLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxLiability.php) | `team_id`, `deduction_id`, `amount`, `due_on`, `status`, `metadata` |
| [WithholdingTaxRemittance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRemittance.php) | `team_id`, `liability_id`, `amount`, `remitted_on`, `reference`, `status`, `metadata` |
| [WithholdingTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRule.php) | `team_id`, `code`, `name`, `jurisdiction`, `rate`, `threshold`, `effective_from`, `effective_until`, `status`, `metadata` |
| [WithholdingTaxStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxStatement.php) | `team_id`, `jurisdiction`, `period_start`, `period_end`, `total_amount`, `status`, `payload` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WithholdingTaxController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-api/src/Http/Controllers/WithholdingTaxController.php) | `public function rules(Request $request): mixed`<br>`public function deductions(Request $request): mixed`<br>`public function createRule(Request $request, CreateWithholdingTaxRule $action): mixed`<br>`public function calculate(Request $request, WithholdingTaxRule $rule, CalculateWithholdingTax $action): mixed`<br>`public function remit(Request $request, WithholdingTaxLiability $liability, RemitWithholdingTax $action): mixed` |

**Observed route declarations:**

[modules/accounting-withholding-tax-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/withholding-tax')->group(function (): void {
Route::middleware('ability:accounting.withholding-tax.read')->group(function (): void {
Route::get('/rules', [WithholdingTaxController::class, 'rules']);
Route::get('/deductions', [WithholdingTaxController::class, 'deductions']);
Route::middleware('ability:accounting.withholding-tax.write')->group(function (): void {
Route::post('/rules', [WithholdingTaxController::class, 'createRule']);
Route::post('/rules/{rule}/deductions', [WithholdingTaxController::class, 'calculate']);
Route::post('/liabilities/{liability}/remit', [WithholdingTaxController::class, 'remit']);
```
<!-- layer-implementation-plan:end -->
