# Crm Telephony React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-telephony). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-telephony-react-native
**Matching core package:** module-crm-crm-telephony ([implementation](../core/crm-telephony.md))
**Matching API package:** module-crm-crm-telephony-api ([contract](../api/crm-telephony.md))

## Implementation plan

This adapter presents Crm Telephony for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Telephony API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-telephony.md), and [API module](../api/crm-telephony.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-telephony`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-telephony.md)) |
| Capability React Native module skeleton | [`module-crm-telephony-react-native`](https://github.com/liberusoftware/module-crm-telephony-react-native) (`@liberusoftware/module-crm-telephony-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Numbers** | Progressive mobile list/detail/sheet flow for `numbers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Caller ID** | Progressive mobile list/detail/sheet flow for `caller id` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **IVR** | Progressive mobile list/detail/sheet flow for `ivr` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Queues** | Progressive mobile list/detail/sheet flow for `queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Business hours** | Progressive mobile list/detail/sheet flow for `business hours` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Skills** | Progressive mobile list/detail/sheet flow for `skills` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recording** | Progressive mobile list/detail/sheet flow for `recording` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Voicemail** | Progressive mobile list/detail/sheet flow for `voicemail` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transfers** | Progressive mobile list/detail/sheet flow for `transfers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dispositions** | Progressive mobile list/detail/sheet flow for `dispositions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Click-to-call** | Progressive mobile list/detail/sheet flow for `click-to-call` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Call logging** | Progressive mobile list/detail/sheet flow for `call logging` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provider adapters** | Progressive mobile list/detail/sheet flow for `provider adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TelephonyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Queries/TelephonyQuery.php) | `public function numbers(int $teamId)`<br>`public function queues(int $teamId)`<br>`public function calls(int $teamId)`<br>`public function settings(int $teamId): ?TelephonySettings` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureTelephony.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/ConfigureTelephony.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonySettings` |
| [CreateTelephonyQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/CreateTelephonyQueue.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonyQueue` |
| [LogTelephonyCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/LogTelephonyCall.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonyCall` |
| [UpdateCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/UpdateCall.php) | `public function execute(int $teamId, int $actorId, int $callId, array $data): TelephonyCall` |
| [UpsertTelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/UpsertTelephonyNumber.php) | `public function execute(int $teamId, int $actorId, array $data, ?int $id = null): TelephonyNumber` |
| [TelephonyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TelephonyAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [TelephonyPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TelephonyPolicy.php) | `public function canManage(int $teamId, int $userId): bool`<br>`public function isTeamMember(int $teamId, int $userId, array $roles = [], bool $includeOwner = false): bool` |
| [TenantTwilioService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TenantTwilioService.php) | `public function client(int $teamId): Client`<br>`public function sendMessage(int $teamId, string $to, string $body): object`<br>`public function usage(int $teamId, array $filters = []): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TelephonyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyCall.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyNumber.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyQueue.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonySettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonySettings.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [TelephonyController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-api/src/Http/Controllers/TelephonyController.php) | `public function numbers(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function queues(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function settings(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function configure(Request $r, ConfigureTelephony $a): JsonResponse`<br>`public function number(Request $r, UpsertTelephonyNumber $a): JsonResponse`<br>`public function queue(Request $r, CreateTelephonyQueue $a): JsonResponse`<br>`public function calls(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function logCall(Request $r, LogTelephonyCall $a): JsonResponse`<br>`public function updateCall(Request $r, int $call, UpdateCall $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-telephony-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/telephony')->group(function (): void {
Route::get('/numbers', [TelephonyController::class, 'numbers']);
Route::post('/numbers', [TelephonyController::class, 'number']);
Route::get('/queues', [TelephonyController::class, 'queues']);
Route::post('/queues', [TelephonyController::class, 'queue']);
Route::get('/settings', [TelephonyController::class, 'settings']);
Route::put('/settings', [TelephonyController::class, 'configure']);
Route::get('/calls', [TelephonyController::class, 'calls']);
Route::post('/calls', [TelephonyController::class, 'logCall']);
Route::patch('/calls/{call}', [TelephonyController::class, 'updateCall']);
```
<!-- layer-implementation-plan:end -->
