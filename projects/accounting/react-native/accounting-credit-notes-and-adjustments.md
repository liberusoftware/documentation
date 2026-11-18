# Accounting Credit Notes And Adjustments React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-credit-notes-and-adjustments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-credit-notes-and-adjustments-react-native
**Matching core package:** module-accounting-accounting-credit-notes-and-adjustments ([implementation](../core/accounting-credit-notes-and-adjustments.md))
**Matching API package:** module-accounting-accounting-credit-notes-and-adjustments-api ([contract](../api/accounting-credit-notes-and-adjustments.md))

## Implementation plan

This adapter presents Accounting Credit Notes And Adjustments for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Credit Notes And Adjustments API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-credit-notes-and-adjustments.md), and [API module](../api/accounting-credit-notes-and-adjustments.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-credit-notes-and-adjustments`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-credit-notes-and-adjustments.md)) |
| Capability React Native module skeleton | [`module-accounting-credit-notes-and-adjustments-react-native`](https://github.com/liberusoftware/module-accounting-credit-notes-and-adjustments-react-native) (`@liberusoftware/module-accounting-credit-notes-and-adjustments-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Full/partial credits** | Progressive mobile list/detail/sheet flow for `full/partial credits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reasons** | Progressive mobile list/detail/sheet flow for `reasons` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval** | Progressive mobile list/detail/sheet flow for `approval` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Invoice allocation** | Progressive mobile list/detail/sheet flow for `invoice allocation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Refund/store-credit references** | Progressive mobile list/detail/sheet flow for `refund/store-credit references` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax correction** | Progressive mobile list/detail/sheet flow for `tax correction` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Audit** | Progressive mobile list/detail/sheet flow for `audit` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
