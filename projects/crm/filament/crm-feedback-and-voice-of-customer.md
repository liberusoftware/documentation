# CRM: Crm Feedback And Voice Of Customer Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-feedback-and-voice-of-customer). Observed identity: [`liberusoftware/module-crm-feedback-and-voice-of-customer-filament`](../../../modules/source/liberusoftware--module-crm-feedback-and-voice-of-customer-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-feedback-and-voice-of-customer-filament`  
**Matching domain module:** `crm-feedback-and-voice-of-customer`  
**Application:** CRM  
**Source feature:** [Crm Feedback And Voice Of Customer](../features/crm-feedback-and-voice-of-customer.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-feedback-and-voice-of-customer` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **CSAT:** resource/table/form/action or page behavior for this module's authorized workflow.
- **NPS:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CES:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Custom surveys:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sampling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Responses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Text analysis:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alerts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Close-the-loop cases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trend reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-feedback-and-voice-of-customer-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `csat`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `nps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ces`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `custom-surveys`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sampling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `responses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `text-analysis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alerts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `close-the-loop-cases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trend-reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-feedback-and-voice-of-customer` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-feedback-and-voice-of-customer-filament`](https://github.com/liberusoftware/module-crm-feedback-and-voice-of-customer-filament) (`liberusoftware/crm-feedback-and-voice-of-customer-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-feedback-and-voice-of-customer.md) · [API plan](../api/crm-feedback-and-voice-of-customer.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **CSAT** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `csat`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **NPS** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `nps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **CES** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ces`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Custom surveys** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `custom surveys`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sampling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sampling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Delivery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `delivery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Responses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `responses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Text analysis** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `text analysis`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Alerts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `alerts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Close-the-loop cases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `close-the-loop cases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trend reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trend reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [FeedbackAndVoiceOfCustomerFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-filament/src/FeedbackAndVoiceOfCustomerFilamentServiceProvider.php) · [FeedbackSurveyResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-filament/src/Resources/FeedbackSurveyResource.php) · [CreateFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-filament/src/Resources/Pages/CreateFeedbackSurvey.php) · [EditFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-filament/src/Resources/Pages/EditFeedbackSurvey.php) · [ListFeedbackSurveys.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-filament/src/Resources/Pages/ListFeedbackSurveys.php).

| Observed core query | Public method signatures |
| --- | --- |
| [FeedbackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Queries/FeedbackQuery.php) | `public function surveys(int $teamId)`<br>`public function responses(int $teamId, int $surveyId)`<br>`public function trend(int $teamId, int $surveyId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/CreateFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): FeedbackSurvey` |
| [DeliverFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/DeliverFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackSurvey $survey, ?int $recipientId, string $channel = 'email'): FeedbackDelivery` |
| [OpenFeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/OpenFeedbackCase.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackResponse $response, ?int $ownerId = null): FeedbackCase` |
| [RecordFeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/RecordFeedbackResponse.php) | `public function execute(int $teamId, FeedbackDelivery $delivery, array $input): FeedbackResponse` |
| [ResolveFeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/ResolveFeedbackAlert.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackAlert $alert): FeedbackAlert` |
| [FeedbackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Services/FeedbackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackAlert.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackResponse.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackSurvey.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
