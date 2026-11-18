# Accounting Cash Collection Assistant React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-cash-collection-assistant). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-cash-collection-assistant-react-native
**Matching core package:** module-accounting-accounting-cash-collection-assistant ([implementation](../core/accounting-cash-collection-assistant.md))
**Matching API package:** module-accounting-accounting-cash-collection-assistant-api ([contract](../api/accounting-cash-collection-assistant.md))

## Implementation plan

This adapter presents Accounting Cash Collection Assistant for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Cash Collection Assistant API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-cash-collection-assistant.md), and [API module](../api/accounting-cash-collection-assistant.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-cash-collection-assistant`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-cash-collection-assistant.md)) |
| Capability React Native module skeleton | [`module-accounting-cash-collection-assistant-react-native`](https://github.com/liberusoftware/module-accounting-cash-collection-assistant-react-native) (`@liberusoftware/module-accounting-cash-collection-assistant-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Invoice-risk prioritization** | Progressive mobile list/detail/sheet flow for `invoice-risk prioritization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reminder drafts/timing** | Progressive mobile list/detail/sheet flow for `reminder drafts/timing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Promise tracking** | Progressive mobile list/detail/sheet flow for `promise tracking` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Policy** | Progressive mobile list/detail/sheet flow for `policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval** | Progressive mobile list/detail/sheet flow for `approval` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Outcome feedback** | Progressive mobile list/detail/sheet flow for `outcome feedback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CashCollectionAssistantQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Queries/CashCollectionAssistantQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/CreateCashCollectionAssistant.php) | `public function handle(array $attributes): CashCollectionAssistant` |
| [RecordCollectionPromise.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/RecordCollectionPromise.php) | `public function handle(CashCollectionAssistant $assistant, string $date, string\|float $amount): CashCollectionAssistant` |
| [ScheduleCollectionReminder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/ScheduleCollectionReminder.php) | `public function handle(CashCollectionAssistant $assistant, string $at, ?string $draft = null): CashCollectionAssistant` |
| [SetCollectionDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/SetCollectionDecision.php) | `public function handle(CashCollectionAssistant $assistant, string $field, string $value): CashCollectionAssistant` |
| [UpdateCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/UpdateCashCollectionAssistant.php) | `public function handle(CashCollectionAssistant $assistant, array $attributes): CashCollectionAssistant` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Models/CashCollectionAssistant.php) | `team_id`, `invoice_ref`, `customer_ref`, `risk_score`, `risk_level`, `reminder_status`, `reminder_at`, `promised_amount`, `promised_date`, `promise_status`, `policy_ref`, `approval_status`, `outcome`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CashCollectionAssistantsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant-api/src/Http/Controllers/CashCollectionAssistantsController.php) | `public function index(CashCollectionAssistantQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCashCollectionAssistant $action): JsonResponse`<br>`public function update(Request $request, string $assistant, UpdateCashCollectionAssistant $action): JsonResponse`<br>`public function reminder(Request $request, string $assistant, ScheduleCollectionReminder $action): JsonResponse`<br>`public function promise(Request $request, string $assistant, RecordCollectionPromise $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-cash-collection-assistant-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/cash-collection-assistant')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.cash-collection-assistant.read')->get('/', [CashCollectionAssistantsController::class, 'index']);
Route::middleware('ability:accounting.cash-collection-assistant.write')->group(function (): void {
Route::post('/', [CashCollectionAssistantsController::class, 'store']);
Route::post('/{assistant}/reminder', [CashCollectionAssistantsController::class, 'reminder']);
Route::post('/{assistant}/promise', [CashCollectionAssistantsController::class, 'promise']);
Route::patch('/{assistant}', [CashCollectionAssistantsController::class, 'update']);
```
<!-- layer-implementation-plan:end -->
