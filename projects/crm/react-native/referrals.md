# Referrals React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#referrals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-referrals-react-native
**Matching core package:** module-crm-referrals ([implementation](../core/referrals.md))
**Matching API package:** module-crm-referrals-api ([contract](../api/referrals.md))

## Implementation plan

This adapter presents Referrals for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Referrals API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/referrals.md), and [API module](../api/referrals.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `referrals`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/referrals.md)) |
| Capability React Native module skeleton | [`module-crm-referrals-react-native`](https://github.com/liberusoftware/module-crm-referrals-react-native) (`@liberusoftware/module-crm-referrals-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Referral programs extending AffiliateProgramContract** | Progressive mobile list/detail/sheet flow for `referral programs extending affiliateprogramcontract` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Links/codes via ReferralAttributionContract** | Progressive mobile list/detail/sheet flow for `links/codes via referralattributioncontract` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Advocates and referred prospects** | Progressive mobile list/detail/sheet flow for `advocates and referred prospects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Qualification via ConversionRecorderContract** | Progressive mobile list/detail/sheet flow for `qualification via conversionrecordercontract` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rewards via RewardFulfillmentContract** | Progressive mobile list/detail/sheet flow for `rewards via rewardfulfillmentcontract` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fraud/duplicate controls via FraudAndSelfReferralPolicyContract** | Progressive mobile list/detail/sheet flow for `fraud/duplicate controls via fraudandselfreferralpolicycontract` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Status and multi-touch attribution** | Progressive mobile list/detail/sheet flow for `status and multi-touch attribution` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReferralQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Queries/ReferralQuery.php) | `public function programs(int $teamId)`<br>`public function referrals(int $teamId)`<br>`public function rewards(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/CreateProgram.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReferralProgram` |
| [CreateReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/CreateReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Referral` |
| [IssueReward.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/IssueReward.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReferralReward` |
| [QualifyReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/QualifyReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $referralId, string $status): Referral` |
| [UpdateReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/UpdateReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $referralId, array $input): Referral` |
| [ReferralPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Services/ReferralPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Referral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/Referral.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReferralProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/ReferralProgram.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReferralReward.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/ReferralReward.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReferralsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-api/src/Http/Controllers/ReferralsController.php) | `public function programs(Request $r, ReferralQuery $q)`<br>`public function program(Request $r, CreateProgram $a)`<br>`public function referrals(Request $r, ReferralQuery $q)`<br>`public function referral(Request $r, CreateReferral $a)`<br>`public function qualify(Request $r, int $referral, string $status, QualifyReferral $a)`<br>`public function reward(Request $r, IssueReward $a)`<br>`public function rewards(Request $r, ReferralQuery $q)` |

**Observed route declarations:**

[modules/crm-referrals-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/referrals')->group(function (): void {
Route::get('/programs', [ReferralsController::class, 'programs']);
Route::post('/programs', [ReferralsController::class, 'program']);
Route::get('/referrals', [ReferralsController::class, 'referrals']);
Route::post('/referrals', [ReferralsController::class, 'referral']);
Route::post('/referrals/{referral}/{status}', [ReferralsController::class, 'qualify'])->whereIn('status', ['qualified', 'rejected', 'converted']);
Route::get('/rewards', [ReferralsController::class, 'rewards']);
Route::post('/rewards', [ReferralsController::class, 'reward']);
```
<!-- layer-implementation-plan:end -->
