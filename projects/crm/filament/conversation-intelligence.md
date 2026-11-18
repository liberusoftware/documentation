# CRM: Conversation Intelligence Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#conversation-intelligence). Observed identity: [`liberusoftware/module-crm-conversation-intelligence-filament`](../../../modules/source/liberusoftware--module-crm-conversation-intelligence-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-conversation-intelligence-filament`  
**Matching domain module:** `crm-conversation-intelligence`  
**Application:** CRM  
**Source feature:** [Conversation Intelligence](../features/conversation-intelligence.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-conversation-intelligence` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Call/meeting recording:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transcription:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Summaries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Topics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Questions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Objections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Competitors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sentiment policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Action items:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Highlights:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Searchable evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-conversation-intelligence-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `call-meeting-recording`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transcription`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `summaries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `topics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `questions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `objections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `competitors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sentiment-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `action-items`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `highlights`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `searchable-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-conversation-intelligence` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-conversation-intelligence-filament`](https://github.com/liberusoftware/module-crm-conversation-intelligence-filament) (`liberusoftware/crm-conversation-intelligence-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/conversation-intelligence.md) · [API plan](../api/conversation-intelligence.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Call/meeting recording** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `call/meeting recording`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transcription** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transcription`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Summaries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `summaries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Topics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `topics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Questions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `questions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Objections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `objections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Competitors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `competitors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sentiment policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sentiment policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Action items** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `action items`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Highlights** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `highlights`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Searchable evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `searchable evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ConversationIntelligenceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence-filament/src/ConversationIntelligenceFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Queries/ConversationQuery.php) | `public function conversations(int $teamId): Builder`<br>`public function evidence(int $teamId, string $search): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEvidence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/AddEvidence.php) | `public function execute(int $teamId, Conversation $conversation, string $kind, string $label, string $content, array $metadata = []): ConversationEvidence` |
| [AnalyzeConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/AnalyzeConversation.php) | `public function execute(int $teamId, Conversation $conversation, string $transcript, array $insights = []): Conversation` |
| [RecordConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/RecordConversation.php) | `public function execute(int $teamId, int $userId, array $input): Conversation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Models/Conversation.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConversationEvidence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Models/ConversationEvidence.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
