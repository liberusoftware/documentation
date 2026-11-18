# Crm Goals And Performance React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-goals-and-performance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-goals-and-performance-react-native
**Matching core package:** module-crm-crm-goals-and-performance ([implementation](../core/crm-goals-and-performance.md))
**Matching API package:** module-crm-crm-goals-and-performance-api ([contract](../api/crm-goals-and-performance.md))

## Implementation plan

This adapter presents Crm Goals And Performance for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Goals And Performance API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-goals-and-performance.md), and [API module](../api/crm-goals-and-performance.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-goals-and-performance`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-goals-and-performance.md)) |
| Capability React Native module skeleton | [`module-crm-goals-and-performance-react-native`](https://github.com/liberusoftware/module-crm-goals-and-performance-react-native) (`@liberusoftware/module-crm-goals-and-performance-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Individual/team/company goals** | Progressive mobile list/detail/sheet flow for `individual/team/company goals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Activity/outcome targets** | Progressive mobile list/detail/sheet flow for `activity/outcome targets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Scorecards** | Progressive mobile list/detail/sheet flow for `scorecards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Leaderboards** | Progressive mobile list/detail/sheet flow for `leaderboards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reviews** | Progressive mobile list/detail/sheet flow for `reviews` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Coaching plans** | Progressive mobile list/detail/sheet flow for `coaching plans` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Performance history** | Progressive mobile list/detail/sheet flow for `performance history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PerformanceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Queries/PerformanceQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/CreateGoal.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PerformanceGoal` |
| [RecordReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/RecordReview.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PerformanceReview` |
| [UpdateGoalActual.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/UpdateGoalActual.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, PerformanceGoal $goal, array $input): PerformanceEvent` |
| [PerformancePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Services/PerformancePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PerformanceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [PerformanceGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceGoal.php) | No literal fillable array detected; inspect the model and API schema. |
| [PerformanceReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceReview.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PerformanceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance-api/src/Http/Controllers/PerformanceController.php) | `public function index(Request $r, PerformanceQuery $q): JsonResponse`<br>`public function store(Request $r, CreateGoal $a): JsonResponse`<br>`public function event(Request $r, PerformanceGoal $goal, UpdateGoalActual $a): JsonResponse`<br>`public function review(Request $r, RecordReview $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
