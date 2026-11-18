# Crm Service Agent Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-service-agent). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-service-agent-flutter
**Matching core package:** module-crm-crm-service-agent ([implementation](../core/crm-service-agent.md))
**Matching API package:** module-crm-crm-service-agent-api ([contract](../api/crm-service-agent.md))

## Implementation plan

This adapter presents Crm Service Agent for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Service Agent API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-service-agent.md), and [API module](../api/crm-service-agent.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-service-agent`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-service-agent-flutter`](https://github.com/liberusoftware/module-crm-service-agent-flutter) (`module_crm_service_agent_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-service-agent-dart-mobile`](https://github.com/liberusoftware/module-crm-service-agent-dart-mobile) (`module_crm_service_agent_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-service-agent-dart-desktop`](https://github.com/liberusoftware/module-crm-service-agent-dart-desktop) (`module_crm_service_agent_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-service-agent.md) · [Core plan](../core/crm-service-agent.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Case classification** | Adaptive mobile cards/sheets for `case classification` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `case classification` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Knowledge retrieval** | Adaptive mobile cards/sheets for `knowledge retrieval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `knowledge retrieval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Response drafts** | Adaptive mobile cards/sheets for `response drafts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `response drafts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Resolution plans** | Adaptive mobile cards/sheets for `resolution plans` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `resolution plans` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tool use** | Adaptive mobile cards/sheets for `tool use` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tool use` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Confidence** | Adaptive mobile cards/sheets for `confidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `confidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Escalation** | Adaptive mobile cards/sheets for `escalation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `escalation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Quality review** | Adaptive mobile cards/sheets for `quality review` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quality review` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Queries/AgentQuery.php) | `public function cases(int $teamId)`<br>`public function knowledge(int $teamId, string $search = '')`<br>`public function tools(int $teamId)`<br>`public function reviews(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ClassifyCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/ClassifyCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, array $data): AgentCase` |
| [CreateAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/CreateAgentCase.php) | `public function execute(int $teamId, int $actorId, array $data): AgentCase` |
| [EscalateAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/EscalateAgentCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, array $data = []): AgentCase` |
| [RetrieveKnowledge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/RetrieveKnowledge.php) | `public function execute(int $teamId, int $actorId, array $data)` |
| [ReviewAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/ReviewAgentCase.php) | `public function execute(int $teamId, int $actorId, array $data): AgentReview` |
| [RunAgentTool.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/RunAgentTool.php) | `public function execute(int $teamId, int $actorId, array $data): AgentToolRun` |
| [UpdateAgentOutput.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/UpdateAgentOutput.php) | `public function execute(int $teamId, int $actorId, int $caseId, string $type, array $data): AgentCase` |
| [AgentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Services/AgentAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [AgentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Services/AgentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentKnowledge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentKnowledge.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentToolRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentToolRun.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AgentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent-api/src/Http/Controllers/AgentController.php) | `public function cases(Request $r, AgentQuery $q)`<br>`public function storeCase(Request $r, CreateAgentCase $a)`<br>`public function classify(Request $r, int $case, ClassifyCase $a)`<br>`public function knowledge(Request $r, RetrieveKnowledge $a)`<br>`public function output(Request $r, int $case, string $type, UpdateAgentOutput $a)`<br>`public function tool(Request $r, RunAgentTool $a)`<br>`public function escalate(Request $r, int $case, EscalateAgentCase $a)`<br>`public function review(Request $r, ReviewAgentCase $a)` |

**Observed route declarations:**

[modules/crm-service-agent-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/service-agent')->group(function (): void {
Route::get('/cases', [AgentController::class, 'cases']);
Route::post('/cases', [AgentController::class, 'storeCase']);
Route::post('/cases/{case}/classify', [AgentController::class, 'classify']);
Route::post('/cases/{case}/output/{type}', [AgentController::class, 'output'])->whereIn('type', ['draft', 'plan']);
Route::post('/cases/{case}/escalate', [AgentController::class, 'escalate']);
Route::get('/knowledge', [AgentController::class, 'knowledge']);
Route::post('/tools', [AgentController::class, 'tool']);
Route::post('/reviews', [AgentController::class, 'review']);
```
<!-- layer-implementation-plan:end -->
