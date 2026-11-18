# Marketing Agent React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing-agent). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-marketing-agent-react-native
**Matching core package:** module-crm-marketing-agent ([implementation](../core/marketing-agent.md))
**Matching API package:** module-crm-marketing-agent-api ([contract](../api/marketing-agent.md))

## Implementation plan

This adapter presents Marketing Agent for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Marketing Agent API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/marketing-agent.md), and [API module](../api/marketing-agent.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `marketing-agent`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/marketing-agent.md)) |
| Capability React Native module skeleton | [`module-crm-marketing-agent-react-native`](https://github.com/liberusoftware/module-crm-marketing-agent-react-native) (`@liberusoftware/module-crm-marketing-agent-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Audience/campaign/content assistance** | Progressive mobile list/detail/sheet flow for `audience/campaign/content assistance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Variations** | Progressive mobile list/detail/sheet flow for `variations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Journey recommendations** | Progressive mobile list/detail/sheet flow for `journey recommendations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Brand/consent checks** | Progressive mobile list/detail/sheet flow for `brand/consent checks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Experiments** | Progressive mobile list/detail/sheet flow for `experiments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval workflow** | Progressive mobile list/detail/sheet flow for `approval workflow` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Queries/AgentQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAgentRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Actions/CreateAgentRequest.php) | `public function __construct(private readonly MarketingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentRequest` |
| [CreateExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Actions/CreateExperiment.php) | `public function __construct(private readonly MarketingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AgentRequest $request, array $input): AgentExperiment` |
| [RecordAgentCheck.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Actions/RecordAgentCheck.php) | `public function __construct(private readonly MarketingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AgentRequest $request, array $input): AgentCheck` |
| [MarketingAgentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Services/MarketingAgentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgentCheck.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Models/AgentCheck.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Models/AgentExperiment.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent/src/Models/AgentRequest.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MarketingAgentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent-api/src/Http/Controllers/MarketingAgentController.php) | `public function index(Request $r, AgentQuery $q): JsonResponse`<br>`public function store(Request $r, CreateAgentRequest $a): JsonResponse`<br>`public function check(Request $r, AgentRequest $request, RecordAgentCheck $a): JsonResponse`<br>`public function experiment(Request $r, AgentRequest $request, CreateExperiment $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
