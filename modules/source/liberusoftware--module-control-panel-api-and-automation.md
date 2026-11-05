# liberusoftware/module-control-panel-api-and-automation: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Control Panel API credentials, webhooks, schedules and automation records.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-api-and-automation](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-api-and-automation`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-api-and-automation` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-api-and-automation` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\ApiAutomation\\ApiAutomationServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/module.json).

**Declared capabilities:** control-panel.api-automation

**Declared features:** Scoped API credentials, Webhooks, CLI commands, Templates, Schedules, Orchestration, Billing and provisioning events

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\ApiAutomation\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateAutomationSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/CreateAutomationSchedule.php) | `public function execute(array $attributes): AutomationSchedule` |
| [src/Actions/CreateAutomationTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/CreateAutomationTemplate.php) | `public function execute(array $attributes): AutomationTemplate` |
| [src/Actions/PauseWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/PauseWebhook.php) | `public function execute(WebhookEndpoint $webhook): WebhookEndpoint` |
| [src/Actions/RecordBillingProvisioningEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RecordBillingProvisioningEvent.php) | `public function execute(array $attributes): BillingProvisioningEvent` |
| [src/Actions/RegisterApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterApiCredential.php) | `public function execute(array $attributes): ApiCredential` |
| [src/Actions/RegisterAutomation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterAutomation.php) | `public function execute(array $attributes): AutomationDefinition` |
| [src/Actions/RegisterAutomationCommand.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterAutomationCommand.php) | `public function execute(array $attributes): AutomationCommand` |
| [src/Actions/RegisterWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterWebhook.php) | `public function execute(array $attributes): WebhookEndpoint` |
| [src/Actions/ResumeWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/ResumeWebhook.php) | `public function execute(WebhookEndpoint $webhook): WebhookEndpoint` |
| [src/Actions/RevokeApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RevokeApiCredential.php) | `public function execute(ApiCredential $credential): ApiCredential` |
| [src/Actions/StartOrchestration.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/StartOrchestration.php) | `public function execute(AutomationTemplate $template, array $input, ?string $teamId, ?string $idempotencyKey = null): OrchestrationRun` |
| [src/Actions/UpdateApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/UpdateApiCredential.php) | `public function execute(ApiCredential $credential, array $attributes): ApiCredential` |
| [src/Actions/UpdateWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/UpdateWebhook.php) | `public function execute(WebhookEndpoint $webhook, array $attributes): WebhookEndpoint` |
| [src/Queries/ListAutomations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Queries/ListAutomations.php) | `public function execute(int\|string\|null $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [src/Queries/ListWebhooks.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Queries/ListWebhooks.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/ApiAutomationServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/ApiAutomationServiceProvider.php) · [src/Enums/AutomationStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Enums/AutomationStatus.php) · [src/Exceptions/OrchestrationIdempotencyConflict.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Exceptions/OrchestrationIdempotencyConflict.php) · [src/Models/ApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/ApiCredential.php) · [src/Models/AutomationCommand.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationCommand.php) · [src/Models/AutomationDefinition.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationDefinition.php) · [src/Models/AutomationSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationSchedule.php) · [src/Models/AutomationTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationTemplate.php) · [src/Models/BillingProvisioningEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/BillingProvisioningEvent.php) · [src/Models/OrchestrationRun.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/OrchestrationRun.php) · [src/Models/WebhookEndpoint.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/WebhookEndpoint.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_110006_create_control_panel_automation_definitions.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/database/migrations/2026_08_24_110006_create_control_panel_automation_definitions.php)
- [database/migrations/2026_08_24_110007_create_control_panel_api_automation_operations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/database/migrations/2026_08_24_110007_create_control_panel_api_automation_operations.php)

[src/Enums/AutomationStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Enums/AutomationStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Paused = 'paused'`, `Failed = 'failed'`, `Completed = 'completed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
