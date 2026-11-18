# CRM: Marketing Agent Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing-agent). Observed identity: [`liberusoftware/module-crm-marketing-agent-filament`](../../../modules/source/liberusoftware--module-crm-marketing-agent-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-marketing-agent-filament`  
**Matching domain module:** `crm-marketing-agent`  
**Application:** CRM  
**Source feature:** [Marketing Agent](../features/marketing-agent.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-marketing-agent` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Audience/campaign/content assistance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Variations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Journey recommendations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Brand/consent checks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Experiments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval workflow:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-marketing-agent-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `audience-campaign-content-assistance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `variations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `journey-recommendations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `brand-consent-checks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `experiments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval-workflow`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-marketing-agent` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-marketing-agent-filament`](https://github.com/liberusoftware/module-crm-marketing-agent-filament) (`liberusoftware/crm-marketing-agent-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/marketing-agent.md) · [API plan](../api/marketing-agent.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Audience/campaign/content assistance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audience/campaign/content assistance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Variations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `variations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Journey recommendations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `journey recommendations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Brand/consent checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `brand/consent checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Experiments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `experiments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval workflow** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval workflow`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MarketingAgentFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent-filament/src/MarketingAgentFilamentServiceProvider.php) · [AgentRequestResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent-filament/src/Resources/AgentRequestResource.php) · [CreateAgentRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent-filament/src/Resources/Pages/CreateAgentRequest.php) · [EditAgentRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent-filament/src/Resources/Pages/EditAgentRequest.php) · [ListAgentRequests.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-agent-filament/src/Resources/Pages/ListAgentRequests.php).

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
<!-- layer-implementation-plan:end -->
