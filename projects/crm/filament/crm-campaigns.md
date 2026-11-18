# CRM: Crm Campaigns Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-campaigns). Observed identity: [`liberusoftware/module-crm-campaigns-filament`](../../../modules/source/liberusoftware--module-crm-campaigns-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-campaigns-filament`  
**Matching domain module:** `crm-campaigns`  
**Application:** CRM  
**Source feature:** [Crm Campaigns](../features/crm-campaigns.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-campaigns` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Campaign hierarchy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Briefs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Objectives:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Budget:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audience:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Owners:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calendar:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tasks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Costs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Responses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Influence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **ROI:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-campaigns-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `campaign-hierarchy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `briefs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `objectives`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `budget`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audience`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `owners`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calendar`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tasks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `costs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `responses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `influence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `roi`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-campaigns` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-campaigns-filament`](https://github.com/liberusoftware/module-crm-campaigns-filament) (`liberusoftware/crm-campaigns-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-campaigns.md) · [API plan](../api/crm-campaigns.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Campaign hierarchy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `campaign hierarchy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Briefs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `briefs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Objectives** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `objectives`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Budget** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `budget`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channels** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channels`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audience** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audience`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Owners** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `owners`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Calendar** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calendar`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tasks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tasks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Costs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `costs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Responses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `responses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Influence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `influence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **ROI** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `roi`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CampaignsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-filament/src/CampaignsFilamentPlugin.php) · [CampaignsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-filament/src/CampaignsFilamentServiceProvider.php) · [CampaignResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-filament/src/Resources/CampaignResource.php) · [CreateCampaignPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-filament/src/Resources/CampaignResource/Pages/CreateCampaignPage.php) · [ListCampaigns.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-filament/src/Resources/CampaignResource/Pages/ListCampaigns.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CampaignQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Queries/CampaignQuery.php) | `public function campaigns(int $teamId): Builder`<br>`public function roi(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Actions/CreateCampaign.php) | `public function execute(int $teamId, int $ownerId, array $input): Campaign` |
| [RecordCampaignEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Actions/RecordCampaignEvent.php) | `public function execute(int $teamId, int $actorId, Campaign $campaign, string $type, float $value = 0, array $payload = []): CampaignEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Campaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Models/Campaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [CampaignEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Models/CampaignEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
