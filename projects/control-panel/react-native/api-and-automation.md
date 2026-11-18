# Api And Automation React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#api-and-automation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-api-and-automation-react-native
**Matching core package:** module-control-panel-api-and-automation ([implementation](../core/api-and-automation.md))
**Matching API package:** module-control-panel-api-and-automation-api ([contract](../api/api-and-automation.md))

## Implementation plan

This adapter presents Api And Automation for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Api And Automation API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/api-and-automation.md), and [API module](../api/api-and-automation.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `api-and-automation`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/api-and-automation.md)) |
| Capability React Native module skeleton | [`module-control-panel-api-and-automation-react-native`](https://github.com/liberusoftware/module-control-panel-api-and-automation-react-native) (`@liberusoftware/module-control-panel-api-and-automation-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Scoped API** | Progressive mobile list/detail/sheet flow for `scoped api` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Webhooks** | Progressive mobile list/detail/sheet flow for `webhooks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **CLI** | Progressive mobile list/detail/sheet flow for `cli` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Schedules** | Progressive mobile list/detail/sheet flow for `schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Orchestration** | Progressive mobile list/detail/sheet flow for `orchestration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Billing/provisioning events** | Progressive mobile list/detail/sheet flow for `billing/provisioning events` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
