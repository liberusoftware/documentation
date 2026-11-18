# CRM: Crm Unified Conversations Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-unified-conversations). Observed identity: [`liberusoftware/module-crm-unified-conversations-filament`](../../../modules/source/liberusoftware--module-crm-unified-conversations-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-unified-conversations-filament`  
**Matching domain module:** `crm-unified-conversations`  
**Application:** CRM  
**Source feature:** [Crm Unified Conversations](../features/crm-unified-conversations.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-unified-conversations` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Omnichannel threads:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Participants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identity matching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assignments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Collision detection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drafts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Internal notes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attachments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery/read state:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Timeline:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-unified-conversations-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `omnichannel-threads`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `participants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identity-matching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assignments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `collision-detection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drafts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `internal-notes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attachments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery-read-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `timeline`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-unified-conversations` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-unified-conversations-filament`](https://github.com/liberusoftware/module-crm-unified-conversations-filament) (`liberusoftware/crm-unified-conversations-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-unified-conversations.md) · [API plan](../api/crm-unified-conversations.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Omnichannel threads** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `omnichannel threads`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Participants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `participants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Identity matching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `identity matching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assignments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assignments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Collision detection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `collision detection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drafts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drafts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Internal notes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `internal notes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attachments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attachments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Delivery/read state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `delivery/read state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Timeline** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `timeline`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ConversationResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations-filament/src/Resources/ConversationResource.php) · [ListConversations.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations-filament/src/Resources/ConversationResource/Pages/ListConversations.php) · [UnifiedConversationsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations-filament/src/UnifiedConversationsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Queries/ConversationQuery.php) | `public function list(int $teamId)`<br>`public function find(int $teamId, int $id): Conversation` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/AssignConversation.php) | `public function execute(int $teamId, int $actorId, int $conversationId, ?int $assignee): Conversation` |
| [OpenConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/OpenConversation.php) | `public function execute(int $teamId, int $actorId, array $data): Conversation` |
| [SendMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/SendMessage.php) | `public function execute(int $teamId, int $actorId, int $conversationId, array $data): ConversationMessage` |
| [SyncExternalConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/SyncExternalConversation.php) | `public function execute(int $teamId, array $data): Conversation` |
| [ConversationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Services/ConversationAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [ConversationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Services/ConversationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/Conversation.php) | `team_id`, `channel`, `external_id`, `subject`, `status`, `priority`, `assigned_to`, `last_message_at`, `metadata` |
| [ConversationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationAudit.php) | `team_id`, `actor_id`, `event`, `details` |
| [ConversationMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationMessage.php) | `team_id`, `conversation_id`, `external_id`, `sender_id`, `body`, `direction`, `metadata`, `internal`, `delivery_status`, `read_at`, `idempotency_key` |
| [ConversationParticipant.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationParticipant.php) | `team_id`, `conversation_id`, `identity`, `name`, `role` |
<!-- layer-implementation-plan:end -->
