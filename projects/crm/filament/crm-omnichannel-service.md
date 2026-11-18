# CRM: Crm Omnichannel Service Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-omnichannel-service). Observed identity: [`liberusoftware/module-crm-omnichannel-service-filament`](../../../modules/source/liberusoftware--module-crm-omnichannel-service-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-omnichannel-service-filament`  
**Matching domain module:** `crm-omnichannel-service`  
**Application:** CRM  
**Source feature:** [Crm Omnichannel Service](../features/crm-omnichannel-service.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-omnichannel-service` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Email/chat/social/phone intake:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Agent workspace:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Macros:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suggested replies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Swarming:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Collision control:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Complete interaction history:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-omnichannel-service-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `email-chat-social-phone-intake`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `agent-workspace`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `macros`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suggested-replies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `swarming`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `collision-control`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `complete-interaction-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-omnichannel-service` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-omnichannel-service-filament`](https://github.com/liberusoftware/module-crm-omnichannel-service-filament) (`liberusoftware/crm-omnichannel-service-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-omnichannel-service.md) · [API plan](../api/crm-omnichannel-service.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Email/chat/social/phone intake** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `email/chat/social/phone intake`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Agent workspace** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agent workspace`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Macros** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `macros`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suggested replies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suggested replies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Swarming** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `swarming`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Collision control** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `collision control`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Complete interaction history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `complete interaction history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OmnichannelServiceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service-filament/src/OmnichannelServiceFilamentServiceProvider.php) · [ConversationResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service-filament/src/Resources/ConversationResource.php) · [CreateConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service-filament/src/Resources/Pages/CreateConversation.php) · [EditConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service-filament/src/Resources/Pages/EditConversation.php) · [ListConversations.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service-filament/src/Resources/Pages/ListConversations.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Queries/ConversationQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/AssignConversation.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): Conversation` |
| [RecordInteraction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/RecordInteraction.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): Interaction` |
| [RecordWorkspaceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/RecordWorkspaceEvent.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): WorkspaceEvent` |
| [StartConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/StartConversation.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Conversation` |
| [OmnichannelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Services/OmnichannelPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Conversation.php) | No literal fillable array detected; inspect the model and API schema. |
| [Interaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Interaction.php) | No literal fillable array detected; inspect the model and API schema. |
| [Macro.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Macro.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/WorkspaceEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
