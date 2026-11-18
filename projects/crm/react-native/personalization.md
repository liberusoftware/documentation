# Personalization React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#personalization). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-personalization-react-native
**Matching core package:** module-crm-personalization ([implementation](../core/personalization.md))
**Matching API package:** module-crm-personalization-api ([contract](../api/personalization.md))

## Implementation plan

This adapter presents Personalization for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Personalization API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/personalization.md), and [API module](../api/personalization.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `personalization`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/personalization.md)) |
| Capability React Native module skeleton | [`module-crm-personalization-react-native`](https://github.com/liberusoftware/module-crm-personalization-react-native) (`@liberusoftware/module-crm-personalization-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Rules and decisioning for content** | Progressive mobile list/detail/sheet flow for `rules and decisioning for content` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Offer** | Progressive mobile list/detail/sheet flow for `offer` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Channel** | Progressive mobile list/detail/sheet flow for `channel` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Send time** | Progressive mobile list/detail/sheet flow for `send time` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Locale** | Progressive mobile list/detail/sheet flow for `locale` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lifecycle** | Progressive mobile list/detail/sheet flow for `lifecycle` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Customer attributes with holdouts and fallback** | Progressive mobile list/detail/sheet flow for `customer attributes with holdouts and fallback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PersonalizationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Queries/PersonalizationQuery.php) | `public function rules(int $teamId)`<br>`public function decisions(int $teamId)`<br>`public function outcomes(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/CreatePersonalizationRule.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationRule` |
| [DecidePersonalization.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/DecidePersonalization.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationDecision` |
| [RecordPersonalizationOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/RecordPersonalizationOutcome.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationOutcome` |
| [UpdatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/UpdatePersonalizationRule.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $ruleId, array $input): PersonalizationRule` |
| [PersonalizationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Services/PersonalizationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PersonalizationDecision.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationDecision.php) | No literal fillable array detected; inspect the model and API schema. |
| [PersonalizationOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationOutcome.php) | No literal fillable array detected; inspect the model and API schema. |
| [PersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationRule.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PersonalizationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-api/src/Http/Controllers/PersonalizationController.php) | `public function rules(Request $r, PersonalizationQuery $q)`<br>`public function rule(Request $r, CreatePersonalizationRule $a)`<br>`public function decision(Request $r, DecidePersonalization $a)`<br>`public function outcome(Request $r, RecordPersonalizationOutcome $a)` |

**Observed route declarations:**

[modules/crm-personalization-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/personalization')->group(function (): void {
Route::get('/rules', [PersonalizationController::class, 'rules']);
Route::post('/rules', [PersonalizationController::class, 'rule']);
Route::post('/decisions', [PersonalizationController::class, 'decision']);
Route::post('/outcomes', [PersonalizationController::class, 'outcome']);
```
<!-- layer-implementation-plan:end -->
