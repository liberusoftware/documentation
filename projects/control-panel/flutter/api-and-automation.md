# Api And Automation Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#api-and-automation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-api-and-automation-flutter
**Matching core package:** module-control-panel-api-and-automation ([implementation](../core/api-and-automation.md))
**Matching API package:** module-control-panel-api-and-automation-api ([contract](../api/api-and-automation.md))

## Implementation plan

This adapter presents Api And Automation for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Api And Automation API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/api-and-automation.md), and [API module](../api/api-and-automation.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `api-and-automation`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-api-and-automation-flutter`](https://github.com/liberusoftware/module-control-panel-api-and-automation-flutter) (`module_control_panel_api_and_automation_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-api-and-automation-dart-mobile`](https://github.com/liberusoftware/module-control-panel-api-and-automation-dart-mobile) (`module_control_panel_api_and_automation_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-api-and-automation-dart-desktop`](https://github.com/liberusoftware/module-control-panel-api-and-automation-dart-desktop) (`module_control_panel_api_and_automation_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/api-and-automation.md) · [Core plan](../core/api-and-automation.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Scoped API** | Adaptive mobile cards/sheets for `scoped api` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `scoped api` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Webhooks** | Adaptive mobile cards/sheets for `webhooks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `webhooks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **CLI** | Adaptive mobile cards/sheets for `cli` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cli` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Templates** | Adaptive mobile cards/sheets for `templates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `templates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Schedules** | Adaptive mobile cards/sheets for `schedules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `schedules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Orchestration** | Adaptive mobile cards/sheets for `orchestration` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `orchestration` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Billing/provisioning events** | Adaptive mobile cards/sheets for `billing/provisioning events` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `billing/provisioning events` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListAutomations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Queries/ListAutomations.php) | `public function execute(int\|string\|null $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListWebhooks.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Queries/ListWebhooks.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAutomationSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/CreateAutomationSchedule.php) | `public function execute(array $attributes): AutomationSchedule` |
| [CreateAutomationTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/CreateAutomationTemplate.php) | `public function execute(array $attributes): AutomationTemplate` |
| [PauseWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/PauseWebhook.php) | `public function execute(WebhookEndpoint $webhook): WebhookEndpoint` |
| [RecordBillingProvisioningEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RecordBillingProvisioningEvent.php) | `public function execute(array $attributes): BillingProvisioningEvent` |
| [RegisterApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterApiCredential.php) | `public function execute(array $attributes): ApiCredential` |
| [RegisterAutomation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterAutomation.php) | `public function execute(array $attributes): AutomationDefinition` |
| [RegisterAutomationCommand.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterAutomationCommand.php) | `public function execute(array $attributes): AutomationCommand` |
| [RegisterWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterWebhook.php) | `public function execute(array $attributes): WebhookEndpoint` |
| [ResumeWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/ResumeWebhook.php) | `public function execute(WebhookEndpoint $webhook): WebhookEndpoint` |
| [RevokeApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RevokeApiCredential.php) | `public function execute(ApiCredential $credential): ApiCredential` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/ApiCredential.php) | `team_id`, `name`, `scopes`, `secret`, `status`, `expires_at`, `last_used_at` |
| [AutomationCommand.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationCommand.php) | `team_id`, `name`, `description`, `command`, `arguments`, `enabled`, `last_run_at` |
| [AutomationDefinition.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationDefinition.php) | `team_id`, `name`, `kind`, `status`, `schedule`, `definition`, `credentials` |
| [AutomationSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationSchedule.php) | `team_id`, `name`, `cron`, `timezone`, `template_id`, `status`, `next_run_at`, `last_run_at` |
| [AutomationTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationTemplate.php) | `team_id`, `name`, `version`, `description`, `inputs`, `steps`, `active` |
| [BillingProvisioningEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/BillingProvisioningEvent.php) | `team_id`, `external_id`, `event_type`, `payload`, `status`, `processed_at`, `error` |
| [OrchestrationRun.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/OrchestrationRun.php) | `team_id`, `template_id`, `schedule_id`, `status`, `input`, `output`, `error`, `started_at`, `finished_at`, `idempotency_key` |
| [WebhookEndpoint.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/WebhookEndpoint.php) | `team_id`, `name`, `url`, `events`, `secret`, `status`, `retry_limit`, `last_delivered_at`, `failure_count` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AutomationController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-api/src/Http/Controllers/AutomationController.php) | `public function index(Request $request, ListAutomations $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, RegisterAutomation $register): JsonResponse`<br>`public function credential(Request $request, RegisterApiCredential $register): JsonResponse`<br>`public function webhook(Request $request, RegisterWebhook $register): JsonResponse`<br>`public function revokeCredential(Request $request, string $credential, RevokeApiCredential $revoke): JsonResponse`<br>`public function updateCredential(Request $request, string $credential, UpdateApiCredential $update): JsonResponse`<br>`public function updateWebhook(Request $request, string $webhook, UpdateWebhook $update): JsonResponse`<br>`public function pauseWebhook(Request $request, string $webhook, PauseWebhook $pause): JsonResponse`<br>`public function resumeWebhook(Request $request, string $webhook, ResumeWebhook $resume): JsonResponse`<br>`public function run(Request $request, string $template, StartOrchestration $start): JsonResponse`<br>`public function template(Request $request, CreateAutomationTemplate $create): JsonResponse`<br>`public function schedule(Request $request, CreateAutomationSchedule $create): JsonResponse`<br>`public function command(Request $request, RegisterAutomationCommand $register): JsonResponse`<br>`public function billingEvent(Request $request, RecordBillingProvisioningEvent $record): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-api-and-automation-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/api-and-automation')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [AutomationController::class, 'index'])->name('control-panel.api-and-automation.index');
Route::post('/', [AutomationController::class, 'store'])->name('control-panel.api-and-automation.store');
Route::post('credentials', [AutomationController::class, 'credential'])->name('control-panel.api-and-automation.credentials.store');
Route::patch('credentials/{credential}', [AutomationController::class, 'updateCredential'])->name('control-panel.api-and-automation.credentials.update');
Route::post('credentials/{credential}/revoke', [AutomationController::class, 'revokeCredential'])->name('control-panel.api-and-automation.credentials.revoke');
Route::post('webhooks', [AutomationController::class, 'webhook'])->name('control-panel.api-and-automation.webhooks.store');
Route::patch('webhooks/{webhook}', [AutomationController::class, 'updateWebhook'])->name('control-panel.api-and-automation.webhooks.update');
Route::post('webhooks/{webhook}/pause', [AutomationController::class, 'pauseWebhook'])->name('control-panel.api-and-automation.webhooks.pause');
Route::post('webhooks/{webhook}/resume', [AutomationController::class, 'resumeWebhook'])->name('control-panel.api-and-automation.webhooks.resume');
Route::post('templates/{template}/runs', [AutomationController::class, 'run'])->name('control-panel.api-and-automation.runs.store');
Route::post('templates', [AutomationController::class, 'template'])->name('control-panel.api-and-automation.templates.store');
Route::post('schedules', [AutomationController::class, 'schedule'])->name('control-panel.api-and-automation.schedules.store');
Route::post('commands', [AutomationController::class, 'command'])->name('control-panel.api-and-automation.commands.store');
Route::post('billing-events', [AutomationController::class, 'billingEvent'])->name('control-panel.api-and-automation.billing-events.store');
Route::get('{automation}', [AutomationController::class, 'show'])->name('control-panel.api-and-automation.show');
```
<!-- layer-implementation-plan:end -->
