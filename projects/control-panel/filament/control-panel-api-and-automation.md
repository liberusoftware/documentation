# Control Panel: Control Panel Api And Automation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-api-and-automation). Observed identity: [`liberusoftware/module-control-panel-api-and-automation-filament`](../../../modules/source/liberusoftware--module-control-panel-api-and-automation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-control-panel-control-panel-api-and-automation-filament`  
**Matching domain module:** `control-panel-api-and-automation`  
**Application:** Control Panel  
**Source feature:** [Control Panel Api And Automation](../features/control-panel-api-and-automation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `control-panel-api-and-automation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Scoped API:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Webhooks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CLI:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Orchestration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Billing/provisioning events:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-control-panel-control-panel-api-and-automation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `scoped-api`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `webhooks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cli`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `orchestration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `billing-provisioning-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `control-panel-api-and-automation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-control-panel-api-and-automation-filament`](https://github.com/liberusoftware/module-control-panel-api-and-automation-filament) (`liberusoftware/control-panel-api-and-automation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/control-panel-api-and-automation.md) · [API plan](../api/control-panel-api-and-automation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Scoped API** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scoped api`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Webhooks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `webhooks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **CLI** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cli`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Orchestration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `orchestration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Billing/provisioning events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `billing/provisioning events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ApiAutomationFilamentPlugin.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/ApiAutomationFilamentPlugin.php) · [ApiAutomationFilamentServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/ApiAutomationFilamentServiceProvider.php) · [ApiCredentialResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/ApiCredentialResource.php) · [CreateApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/ApiCredentialResource/Pages/CreateApiCredential.php) · [EditApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/ApiCredentialResource/Pages/EditApiCredential.php) · [ListApiCredentials.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/ApiCredentialResource/Pages/ListApiCredentials.php) · [AutomationCommandResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationCommandResource.php) · [CreateAutomationCommand.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationCommandResource/Pages/CreateAutomationCommand.php) · [EditAutomationCommand.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationCommandResource/Pages/EditAutomationCommand.php) · [ListAutomationCommands.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationCommandResource/Pages/ListAutomationCommands.php) · [AutomationDefinitionResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationDefinitionResource.php) · [CreateAutomationDefinition.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationDefinitionResource/Pages/CreateAutomationDefinition.php) · [EditAutomationDefinition.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationDefinitionResource/Pages/EditAutomationDefinition.php) · [ListAutomationDefinitions.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-filament/src/Resources/AutomationDefinitionResource/Pages/ListAutomationDefinitions.php).

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
<!-- layer-implementation-plan:end -->
