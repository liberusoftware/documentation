# CRM: Crm Email Marketing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-email-marketing). Observed identity: [`liberusoftware/module-crm-email-marketing-filament`](../../../modules/source/liberusoftware--module-crm-email-marketing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-email-marketing-filament`  
**Matching domain module:** `crm-email-marketing`  
**Application:** CRM  
**Source feature:** [Crm Email Marketing](../features/crm-email-marketing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-email-marketing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Drag-and-drop and code templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Personalization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dynamic content:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Test sends:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inbox previews:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deliverability controls:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scheduling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Throttling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Analytics:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-email-marketing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `drag-and-drop-and-code-templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `personalization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dynamic-content`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `test-sends`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inbox-previews`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deliverability-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scheduling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `throttling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `analytics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-email-marketing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-email-marketing-filament`](https://github.com/liberusoftware/module-crm-email-marketing-filament) (`liberusoftware/crm-email-marketing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-email-marketing.md) · [API plan](../api/crm-email-marketing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Drag-and-drop and code templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drag-and-drop and code templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Personalization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `personalization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dynamic content** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dynamic content`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Test sends** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `test sends`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Inbox previews** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inbox previews`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deliverability controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deliverability controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scheduling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scheduling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Throttling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `throttling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Analytics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `analytics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EmailMarketingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-filament/src/EmailMarketingFilamentServiceProvider.php) · [EmailCampaignResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-filament/src/Resources/EmailCampaignResource.php) · [CreateEmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-filament/src/Resources/Pages/CreateEmailCampaign.php) · [EditEmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-filament/src/Resources/Pages/EditEmailCampaign.php) · [ListEmailCampaigns.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-filament/src/Resources/Pages/ListEmailCampaigns.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EmailMarketingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Queries/EmailMarketingQuery.php) | `public function campaigns(int $teamId)`<br>`public function analytics(int $teamId, int $campaignId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/CreateEmailCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailCampaign` |
| [RecordMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/RecordMarketingEvent.php) | `public function execute(int $teamId, EmailCampaign $campaign, array $input): EmailMarketingEvent` |
| [ScheduleCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/ScheduleCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EmailCampaign $campaign, array $input): EmailCampaign` |
| [EmailMarketingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Services/EmailMarketingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailMarketingEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
