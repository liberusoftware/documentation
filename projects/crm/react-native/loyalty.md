# Loyalty React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#loyalty). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-loyalty-react-native
**Matching core package:** module-crm-loyalty ([implementation](../core/loyalty.md))
**Matching API package:** module-crm-loyalty-api ([contract](../api/loyalty.md))

## Implementation plan

This adapter presents Loyalty for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Loyalty API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/loyalty.md), and [API module](../api/loyalty.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `loyalty`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/loyalty.md)) |
| Capability React Native module skeleton | [`module-crm-loyalty-react-native`](https://github.com/liberusoftware/module-crm-loyalty-react-native) (`@liberusoftware/module-crm-loyalty-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Programs** | Progressive mobile list/detail/sheet flow for `programs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tiers** | Progressive mobile list/detail/sheet flow for `tiers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Points ledger** | Progressive mobile list/detail/sheet flow for `points ledger` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Earning/redemption rules** | Progressive mobile list/detail/sheet flow for `earning/redemption rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rewards** | Progressive mobile list/detail/sheet flow for `rewards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Expiry** | Progressive mobile list/detail/sheet flow for `expiry` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Partner activity** | Progressive mobile list/detail/sheet flow for `partner activity` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Liabilities export** | Progressive mobile list/detail/sheet flow for `liabilities export` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fraud controls** | Progressive mobile list/detail/sheet flow for `fraud controls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Member statements** | Progressive mobile list/detail/sheet flow for `member statements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LoyaltyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Queries/LoyaltyQuery.php) | `public function forTeam(int $teamId)`<br>`public function statement(int $teamId, int $memberId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Actions/CreateProgram.php) | `public function __construct(private readonly LoyaltyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): LoyaltyProgram` |
| [EnrollMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Actions/EnrollMember.php) | `public function __construct(private readonly LoyaltyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LoyaltyProgram $program, array $input): LoyaltyMember` |
| [RecordPoints.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Actions/RecordPoints.php) | `public function __construct(private readonly LoyaltyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LoyaltyMember $member, array $input): LoyaltyLedgerEntry` |
| [SetFraudControl.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Actions/SetFraudControl.php) | `public function __construct(private readonly LoyaltyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LoyaltyMember $member, array $input): LoyaltyControl` |
| [LoyaltyPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Services/LoyaltyPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LoyaltyControl.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyControl.php) | No literal fillable array detected; inspect the model and API schema. |
| [LoyaltyLedgerEntry.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyLedgerEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [LoyaltyMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyMember.php) | No literal fillable array detected; inspect the model and API schema. |
| [LoyaltyProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyProgram.php) | No literal fillable array detected; inspect the model and API schema. |
| [LoyaltyRuleReward.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyRuleReward.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [LoyaltyController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty-api/src/Http/Controllers/LoyaltyController.php) | `public function index(Request $r, LoyaltyQuery $q): JsonResponse`<br>`public function store(Request $r, CreateProgram $a): JsonResponse`<br>`public function enroll(Request $r, LoyaltyProgram $program, EnrollMember $a): JsonResponse`<br>`public function points(Request $r, LoyaltyMember $member, RecordPoints $a): JsonResponse`<br>`public function statement(Request $r, LoyaltyMember $member, LoyaltyQuery $q): JsonResponse` |
<!-- layer-implementation-plan:end -->
