# Crm Consent And Preferences React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-consent-and-preferences). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-consent-and-preferences-react-native
**Matching core package:** module-crm-crm-consent-and-preferences ([implementation](../core/crm-consent-and-preferences.md))
**Matching API package:** module-crm-crm-consent-and-preferences-api ([contract](../api/crm-consent-and-preferences.md))

## Implementation plan

This adapter presents Crm Consent And Preferences for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Consent And Preferences API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-consent-and-preferences.md), and [API module](../api/crm-consent-and-preferences.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-consent-and-preferences`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-consent-and-preferences.md)) |
| Capability React Native module skeleton | [`module-crm-consent-and-preferences-react-native`](https://github.com/liberusoftware/module-crm-consent-and-preferences-react-native) (`@liberusoftware/module-crm-consent-and-preferences-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Lawful basis** | Progressive mobile list/detail/sheet flow for `lawful basis` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Subscriptions** | Progressive mobile list/detail/sheet flow for `subscriptions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Channel/topic preferences** | Progressive mobile list/detail/sheet flow for `channel/topic preferences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Suppression** | Progressive mobile list/detail/sheet flow for `suppression` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quiet hours** | Progressive mobile list/detail/sheet flow for `quiet hours` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recording consent** | Progressive mobile list/detail/sheet flow for `recording consent` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Proof** | Progressive mobile list/detail/sheet flow for `proof` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Expiry** | Progressive mobile list/detail/sheet flow for `expiry` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Withdrawal** | Progressive mobile list/detail/sheet flow for `withdrawal` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Policy evaluation** | Progressive mobile list/detail/sheet flow for `policy evaluation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GrantConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/GrantConsent.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, array $attributes, ?int $actorId = null): ConsentRecord` |
| [SetPreference.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/SetPreference.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, string $channel, string $topic, array $values, ?int $actorId = null): PreferenceRecord` |
| [SuppressSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/SuppressSubject.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, array $attributes, ?int $actorId = null): SuppressionRecord` |
| [WithdrawConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/WithdrawConsent.php) | `public function execute(ConsentRecord $record): ConsentRecord` |
| [PolicyEvaluator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Services/PolicyEvaluator.php) | `public function evaluate(int $teamId, string $subjectType, int $subjectId, string $channel, string $topic = 'general', ?Carbon $at = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConsentRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/ConsentRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `lawful_basis`, `status`, `source`, `proof`, `consented_at`, `expires_at`, `withdrawn_at`, `actor_id` |
| [PolicyEvaluation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/PolicyEvaluation.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `allowed`, `reasons`, `evaluated_at` |
| [PreferenceRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/PreferenceRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `state`, `quiet_hours`, `timezone`, `actor_id` |
| [SuppressionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/SuppressionRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `reason`, `source`, `expires_at`, `withdrawn_at`, `actor_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConsentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-api/src/Http/Controllers/ConsentController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, GrantConsent $grant, SetPreference $preference): JsonResponse`<br>`public function show(Request $request, int $consent): JsonResponse`<br>`public function update(Request $request, int $consent): JsonResponse`<br>`public function withdraw(Request $request, int $consent, WithdrawConsent $withdraw): JsonResponse`<br>`public function evaluate(Request $request, PolicyEvaluator $evaluator): JsonResponse` |

**Observed route declarations:**

[modules/crm-consent-and-preferences-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/consent-and-preferences')->group(function (): void {
Route::get('/', [ConsentController::class, 'index']);
Route::post('/', [ConsentController::class, 'store']);
Route::get('/{consent}', [ConsentController::class, 'show']);
Route::patch('/{consent}', [ConsentController::class, 'update']);
Route::post('/{consent}/withdraw', [ConsentController::class, 'withdraw']);
Route::post('/evaluate', [ConsentController::class, 'evaluate']);
```
<!-- layer-implementation-plan:end -->
