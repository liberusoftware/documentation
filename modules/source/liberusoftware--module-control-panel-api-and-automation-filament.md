# liberusoftware/module-control-panel-api-and-automation-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Control Panel API and Automation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-api-and-automation-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-api-and-automation-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-api-and-automation-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-api-and-automation-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\ApiAutomationFilament\\ApiAutomationFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/module.json).

**Declared capabilities:** control-panel.api-and-automation.filament

**Declared features:** Scoped API credentials, Webhooks, CLI commands, Templates, Schedules, Orchestration, Billing and provisioning events

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-api-and-automation` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\ApiAutomationFilament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-control-panel-api-and-automation": "^1.0"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/ApiAutomationFilamentPlugin.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/ApiAutomationFilamentPlugin.php) · [src/ApiAutomationFilamentServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/ApiAutomationFilamentServiceProvider.php) · [src/Resources/ApiCredentialResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/ApiCredentialResource.php) · [src/Resources/ApiCredentialResource/Pages/CreateApiCredential.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/ApiCredentialResource/Pages/CreateApiCredential.php) · [src/Resources/ApiCredentialResource/Pages/EditApiCredential.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/ApiCredentialResource/Pages/EditApiCredential.php) · [src/Resources/ApiCredentialResource/Pages/ListApiCredentials.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/ApiCredentialResource/Pages/ListApiCredentials.php) · [src/Resources/AutomationCommandResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationCommandResource.php) · [src/Resources/AutomationCommandResource/Pages/CreateAutomationCommand.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationCommandResource/Pages/CreateAutomationCommand.php) · [src/Resources/AutomationCommandResource/Pages/EditAutomationCommand.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationCommandResource/Pages/EditAutomationCommand.php) · [src/Resources/AutomationCommandResource/Pages/ListAutomationCommands.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationCommandResource/Pages/ListAutomationCommands.php) · [src/Resources/AutomationDefinitionResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationDefinitionResource.php) · [src/Resources/AutomationDefinitionResource/Pages/CreateAutomationDefinition.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationDefinitionResource/Pages/CreateAutomationDefinition.php) · [src/Resources/AutomationDefinitionResource/Pages/EditAutomationDefinition.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationDefinitionResource/Pages/EditAutomationDefinition.php) · [src/Resources/AutomationDefinitionResource/Pages/ListAutomationDefinitions.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationDefinitionResource/Pages/ListAutomationDefinitions.php) · [src/Resources/AutomationScheduleResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationScheduleResource.php) · [src/Resources/AutomationScheduleResource/Pages/CreateAutomationSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationScheduleResource/Pages/CreateAutomationSchedule.php) · [src/Resources/AutomationScheduleResource/Pages/EditAutomationSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationScheduleResource/Pages/EditAutomationSchedule.php) · [src/Resources/AutomationScheduleResource/Pages/ListAutomationSchedules.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationScheduleResource/Pages/ListAutomationSchedules.php) · [src/Resources/AutomationTemplateResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationTemplateResource.php) · [src/Resources/AutomationTemplateResource/Pages/CreateAutomationTemplate.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationTemplateResource/Pages/CreateAutomationTemplate.php) · [src/Resources/AutomationTemplateResource/Pages/EditAutomationTemplate.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationTemplateResource/Pages/EditAutomationTemplate.php) · [src/Resources/AutomationTemplateResource/Pages/ListAutomationTemplates.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationTemplateResource/Pages/ListAutomationTemplates.php) · [src/Resources/BillingProvisioningEventResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/BillingProvisioningEventResource.php) · [src/Resources/BillingProvisioningEventResource/Pages/ListBillingProvisioningEvents.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/BillingProvisioningEventResource/Pages/ListBillingProvisioningEvents.php) · [src/Resources/OrchestrationRunResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/OrchestrationRunResource.php) · [src/Resources/OrchestrationRunResource/Pages/ListOrchestrationRuns.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/OrchestrationRunResource/Pages/ListOrchestrationRuns.php) · [src/Resources/WebhookEndpointResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/WebhookEndpointResource.php) · [src/Resources/WebhookEndpointResource/Pages/CreateWebhookEndpoint.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/WebhookEndpointResource/Pages/CreateWebhookEndpoint.php) · [src/Resources/WebhookEndpointResource/Pages/EditWebhookEndpoint.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/WebhookEndpointResource/Pages/EditWebhookEndpoint.php) · [src/Resources/WebhookEndpointResource/Pages/ListWebhookEndpoints.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/WebhookEndpointResource/Pages/ListWebhookEndpoints.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
