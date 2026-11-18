# CRM: Service Agent Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#service-agent). Observed identity: [`liberusoftware/module-crm-service-agent-filament`](../../../modules/source/liberusoftware--module-crm-service-agent-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-service-agent-filament`  
**Matching domain module:** `crm-service-agent`  
**Application:** CRM  
**Source feature:** [Service Agent](../features/service-agent.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-service-agent` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Case classification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Knowledge retrieval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Response drafts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Resolution plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tool use:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Escalation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quality review:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-service-agent-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `case-classification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `knowledge-retrieval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `response-drafts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `resolution-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tool-use`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `escalation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quality-review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-service-agent` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-service-agent-filament`](https://github.com/liberusoftware/module-crm-service-agent-filament) (`liberusoftware/crm-service-agent-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/service-agent.md) · [API plan](../api/service-agent.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Case classification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `case classification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Knowledge retrieval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `knowledge retrieval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Response drafts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `response drafts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Resolution plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `resolution plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tool use** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tool use`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Escalation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `escalation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quality review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quality review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AgentCaseResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent-filament/src/Resources/AgentCaseResource.php) · [ListAgentCases.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent-filament/src/Resources/AgentCaseResource/Pages/ListAgentCases.php) · [ServiceAgentFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent-filament/src/ServiceAgentFilamentPlugin.php) · [ServiceAgentFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent-filament/src/ServiceAgentFilamentServiceProvider.php).

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
<!-- layer-implementation-plan:end -->
