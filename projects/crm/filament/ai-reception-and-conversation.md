# CRM: AI Reception and Conversation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#ai-reception-and-conversation). Observed identity: [`liberusoftware/module-crm-ai-reception-and-conversation-filament`](../../../modules/source/liberusoftware--module-crm-ai-reception-and-conversation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-ai-reception-and-conversation-filament`  
**Matching domain module:** `crm-ai-reception-and-conversation`  
**Application:** CRM  
**Source feature:** [AI Reception and Conversation](../features/ai-reception-and-conversation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-ai-reception-and-conversation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Governed chat/voice agents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approved knowledge/tools:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Qualification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Booking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Summaries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Live handoff:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Testing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Human-approval policy:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-ai-reception-and-conversation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `governed-chat-voice-agents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approved-knowledge-tools`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `qualification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `booking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `summaries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `live-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `testing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `human-approval-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-ai-reception-and-conversation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-ai-reception-and-conversation-filament`](https://github.com/liberusoftware/module-crm-ai-reception-and-conversation-filament) (`liberusoftware/crm-ai-reception-and-conversation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/ai-reception-and-conversation.md) · [API plan](../api/ai-reception-and-conversation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Governed chat/voice agents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `governed chat/voice agents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approved knowledge/tools** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approved knowledge/tools`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Qualification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `qualification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Booking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `booking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Summaries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `summaries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Live handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `live handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Testing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `testing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Human-approval policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `human-approval policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AIReceptionAndConversationFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-filament/src/AIReceptionAndConversationFilamentPlugin.php) · [AIReceptionAndConversationFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-filament/src/AIReceptionAndConversationFilamentServiceProvider.php) · [ReceptionAgentResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-filament/src/Resources/ReceptionAgentResource.php) · [CreateReceptionAgentPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-filament/src/Resources/ReceptionAgentResource/Pages/CreateReceptionAgentPage.php) · [ListReceptionAgents.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-filament/src/Resources/ReceptionAgentResource/Pages/ListReceptionAgents.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/ActivateReceptionAgent.php) | `public function execute(int $teamId, ReceptionAgent $agent): ReceptionAgent` |
| [CreateReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/CreateReceptionAgent.php) | `public function execute(int $teamId, int $ownerId, array $input): ReceptionAgent` |
| [RecordReceptionTurn.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/RecordReceptionTurn.php) | `public function execute(int $teamId, int $actorId, ReceptionConversation $conversation, array $input): ReceptionConversation` |
| [RequestReceptionHandoff.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/RequestReceptionHandoff.php) | `public function execute(int $teamId, int $actorId, ReceptionConversation $conversation, string $reason): ReceptionConversation` |
| [StartReceptionConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/StartReceptionConversation.php) | `public function execute(int $teamId, ReceptionAgent $agent, array $input = []): ReceptionConversation` |
| [ReceptionResponder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Services/ReceptionResponder.php) | `public function respond(ReceptionAgent $agent, ReceptionConversation $conversation, string $input): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReceptionAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReceptionConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionConversation.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
