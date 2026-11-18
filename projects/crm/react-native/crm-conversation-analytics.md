# Crm Conversation Analytics React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-conversation-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-conversation-analytics-react-native
**Matching core package:** module-crm-crm-conversation-analytics ([implementation](../core/crm-conversation-analytics.md))
**Matching API package:** module-crm-crm-conversation-analytics-api ([contract](../api/crm-conversation-analytics.md))

## Implementation plan

This adapter presents Crm Conversation Analytics for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Conversation Analytics API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-conversation-analytics.md), and [API module](../api/crm-conversation-analytics.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-conversation-analytics`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-conversation-analytics.md)) |
| Capability React Native module skeleton | [`module-crm-conversation-analytics-react-native`](https://github.com/liberusoftware/module-crm-conversation-analytics-react-native) (`@liberusoftware/module-crm-conversation-analytics-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Topics** | Progressive mobile list/detail/sheet flow for `topics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Objections** | Progressive mobile list/detail/sheet flow for `objections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Competitors** | Progressive mobile list/detail/sheet flow for `competitors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Talk ratios** | Progressive mobile list/detail/sheet flow for `talk ratios` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Questions** | Progressive mobile list/detail/sheet flow for `questions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Outcomes** | Progressive mobile list/detail/sheet flow for `outcomes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Coaching moments** | Progressive mobile list/detail/sheet flow for `coaching moments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quality scorecards** | Progressive mobile list/detail/sheet flow for `quality scorecards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Trend comparison** | Progressive mobile list/detail/sheet flow for `trend comparison` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationAnalyticsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Queries/ConversationAnalyticsQuery.php) | `public function analyses(int $teamId): Builder`<br>`public function trends(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordConversationAnalysis.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Actions/RecordConversationAnalysis.php) | `public function execute(int $teamId, int $analystId, string $conversationKey, array $input): ConversationAnalysis` |
| [ScoreConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Actions/ScoreConversation.php) | `public function execute(int $teamId, ConversationAnalysis $analysis, array $scores): ConversationAnalysis` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConversationAnalysis.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Models/ConversationAnalysis.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConversationAnalyticsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics-api/src/Http/Controllers/ConversationAnalyticsController.php) | `public function __construct(private readonly ConversationAnalyticsQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(string $conversationKey, RecordConversationAnalysis $a): JsonResponse`<br>`public function score(ConversationAnalysis $analysis, ScoreConversation $a): JsonResponse`<br>`public function trends(): JsonResponse` |

**Observed route declarations:**

[modules/crm-conversation-analytics-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/conversation-analytics')->group(function (): void {
Route::get('analyses', [ConversationAnalyticsController::class, 'index']);
Route::post('analyses/{conversationKey}', [ConversationAnalyticsController::class, 'store']);
Route::post('analyses/{analysis}/score', [ConversationAnalyticsController::class, 'score']);
Route::get('trends', [ConversationAnalyticsController::class, 'trends']);
```
<!-- layer-implementation-plan:end -->
