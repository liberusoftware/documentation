# CRM: Conversation Analytics Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#conversation-analytics). Observed identity: [`liberusoftware/module-crm-conversation-analytics-filament`](../../../modules/source/liberusoftware--module-crm-conversation-analytics-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-conversation-analytics-filament`  
**Matching domain module:** `crm-conversation-analytics`  
**Application:** CRM  
**Source feature:** [Conversation Analytics](../features/conversation-analytics.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-conversation-analytics` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Topics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Objections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Competitors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Talk ratios:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Questions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Outcomes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Coaching moments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quality scorecards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trend comparison:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-conversation-analytics-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `topics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `objections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `competitors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `talk-ratios`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `questions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `outcomes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `coaching-moments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quality-scorecards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trend-comparison`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-conversation-analytics` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-conversation-analytics-filament`](https://github.com/liberusoftware/module-crm-conversation-analytics-filament) (`liberusoftware/crm-conversation-analytics-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/conversation-analytics.md) · [API plan](../api/conversation-analytics.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Topics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `topics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Objections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `objections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Competitors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `competitors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Talk ratios** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `talk ratios`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Questions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `questions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Outcomes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `outcomes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Coaching moments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `coaching moments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quality scorecards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quality scorecards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trend comparison** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trend comparison`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ConversationAnalyticsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics-filament/src/ConversationAnalyticsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationAnalyticsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Queries/ConversationAnalyticsQuery.php) | `public function analyses(int $teamId): Builder`<br>`public function trends(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordConversationAnalysis.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Actions/RecordConversationAnalysis.php) | `public function execute(int $teamId, int $analystId, string $conversationKey, array $input): ConversationAnalysis` |
| [ScoreConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Actions/ScoreConversation.php) | `public function execute(int $teamId, ConversationAnalysis $analysis, array $scores): ConversationAnalysis` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConversationAnalysis.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Models/ConversationAnalysis.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
