# Ai Gateway React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#ai-gateway). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-automation-ai-gateway-react-native
**Matching core package:** module-automation-ai-gateway ([implementation](../core/ai-gateway.md))
**Matching API package:** module-automation-ai-gateway-api ([contract](../api/ai-gateway.md))

## Implementation plan

This adapter presents Ai Gateway for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Ai Gateway API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/ai-gateway.md), and [API module](../api/ai-gateway.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `ai-gateway`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-automation-mobile-react`](https://github.com/liberusoftware/project-automation-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/ai-gateway.md)) |
| Capability React Native module skeleton | [`module-automation-ai-gateway-react-native`](https://github.com/liberusoftware/module-automation-ai-gateway-react-native) (`@liberusoftware/module-automation-ai-gateway-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Provider contracts** | Progressive mobile list/detail/sheet flow for `provider contracts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Model catalog** | Progressive mobile list/detail/sheet flow for `model catalog` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Routing** | Progressive mobile list/detail/sheet flow for `routing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fallback** | Progressive mobile list/detail/sheet flow for `fallback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Structured output** | Progressive mobile list/detail/sheet flow for `structured output` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tool policy** | Progressive mobile list/detail/sheet flow for `tool policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Usage metering** | Progressive mobile list/detail/sheet flow for `usage metering` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAiGatewayResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway/src/Actions/CreateAiGatewayResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): AiGatewayResource` |
| [TransitionAiGatewayResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway/src/Actions/TransitionAiGatewayResource.php) | `public function execute(AiGatewayResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): AiGatewayResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AiGatewayResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway/src/Models/AiGatewayResource.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AiGatewayResourceController.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway-api/src/Http/Controllers/AiGatewayResourceController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAiGatewayResource $create): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, string $id): JsonResponse`<br>`public function destroy(Request $request, string $id): JsonResponse`<br>`public function transition(Request $request, string $id, TransitionAiGatewayResource $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-automation-ai-gateway-api/routes/api.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:60,1'])->prefix('api/v1/automation/ai-gateway')->group(function (): void {
Route::get('/', [AiGatewayResourceController::class, 'index']);
Route::post('/', [AiGatewayResourceController::class, 'store']);
Route::get('/{id}', [AiGatewayResourceController::class, 'show']);
Route::patch('/{id}', [AiGatewayResourceController::class, 'update']);
Route::delete('/{id}', [AiGatewayResourceController::class, 'destroy']);
Route::post('/{id}/transition', [AiGatewayResourceController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
