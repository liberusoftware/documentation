# Module Automation Ai Gateway Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-automation-ai-gateway). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-automation-module-automation-ai-gateway-flutter
**Matching core package:** module-automation-module-automation-ai-gateway ([implementation](../core/module-automation-ai-gateway.md))
**Matching API package:** module-automation-module-automation-ai-gateway-api ([contract](../api/module-automation-ai-gateway.md))

## Implementation plan

This adapter presents Module Automation Ai Gateway for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Automation Ai Gateway API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/module-automation-ai-gateway.md), and [API module](../api/module-automation-ai-gateway.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `module-automation-ai-gateway`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-automation-mobile-flutter`](https://github.com/liberusoftware/project-automation-mobile-flutter) | [`module-automation-ai-gateway-flutter`](https://github.com/liberusoftware/module-automation-ai-gateway-flutter) (`module_automation_ai_gateway_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-automation-dart-mobile`](https://github.com/liberusoftware/project-automation-dart-mobile) | [`module-automation-ai-gateway-dart-mobile`](https://github.com/liberusoftware/module-automation-ai-gateway-dart-mobile) (`module_automation_ai_gateway_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-automation-dart-desktop`](https://github.com/liberusoftware/project-automation-dart-desktop) | [`module-automation-ai-gateway-dart-desktop`](https://github.com/liberusoftware/module-automation-ai-gateway-dart-desktop) (`module_automation_ai_gateway_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | [API plan](../api/module-automation-ai-gateway.md) · [Core plan](../core/module-automation-ai-gateway.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Provider contracts** | Adaptive mobile cards/sheets for `provider contracts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provider contracts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Model catalog** | Adaptive mobile cards/sheets for `model catalog` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `model catalog` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Routing** | Adaptive mobile cards/sheets for `routing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `routing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Fallback** | Adaptive mobile cards/sheets for `fallback` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `fallback` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Structured output** | Adaptive mobile cards/sheets for `structured output` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `structured output` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tool policy** | Adaptive mobile cards/sheets for `tool policy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tool policy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Usage metering** | Adaptive mobile cards/sheets for `usage metering` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `usage metering` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
