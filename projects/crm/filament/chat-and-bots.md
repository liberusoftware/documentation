# CRM: Chat and Bots Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#chat-and-bots). Observed identity: [`liberusoftware/module-crm-chat-and-bots-filament`](../../../modules/source/liberusoftware--module-crm-chat-and-bots-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-chat-and-bots-filament`  
**Matching domain module:** `crm-chat-and-bots`  
**Application:** CRM  
**Source feature:** [Chat and Bots](../features/chat-and-bots.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-chat-and-bots` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Web chat:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bot/playbook builder:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Qualification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Knowledge answers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Meeting booking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Live-agent handoff:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Office hours:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transcripts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channel identity:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-chat-and-bots-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `web-chat`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bot-playbook-builder`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `qualification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `knowledge-answers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `meeting-booking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `live-agent-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `office-hours`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transcripts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channel-identity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-chat-and-bots` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-chat-and-bots-filament`](https://github.com/liberusoftware/module-crm-chat-and-bots-filament) (`liberusoftware/crm-chat-and-bots-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/chat-and-bots.md) · [API plan](../api/chat-and-bots.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Web chat** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `web chat`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bot/playbook builder** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bot/playbook builder`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Qualification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `qualification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Knowledge answers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `knowledge answers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Meeting booking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `meeting booking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Live-agent handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `live-agent handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Office hours** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `office hours`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transcripts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transcripts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channel identity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channel identity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ChatAndBotsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots-filament/src/ChatAndBotsFilamentPlugin.php) · [ChatAndBotsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots-filament/src/ChatAndBotsFilamentServiceProvider.php) · [ChatBotResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots-filament/src/Resources/ChatBotResource.php) · [CreateChatBotPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots-filament/src/Resources/ChatBotResource/Pages/CreateChatBotPage.php) · [ListChatBots.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots-filament/src/Resources/ChatBotResource/Pages/ListChatBots.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ChatBotQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Queries/ChatBotQuery.php) | `public function bots(int $teamId): Builder`<br>`public function sessions(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateChatBot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Actions/CreateChatBot.php) | `public function execute(int $teamId, int $ownerId, string $name, array $playbook, array $channels = []): ChatBot` |
| [HandoffChatSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Actions/HandoffChatSession.php) | `public function execute(int $teamId, ChatSession $session, string $assignee): ChatSession` |
| [StartChatSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Actions/StartChatSession.php) | `public function execute(int $teamId, ChatBot $bot, string $visitorKey, string $channel = 'web'): ChatSession` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ChatBot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Models/ChatBot.php) | No literal fillable array detected; inspect the model and API schema. |
| [ChatSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Models/ChatSession.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
