# Real Estate: Marketing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing). Observed identity: [`liberusoftware/real-estate-marketing-filament`](../../../modules/source/liberusoftware--real-estate-marketing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-marketing-filament`  
**Matching domain module:** `real-estate-marketing`  
**Application:** Real Estate  
**Source feature:** [Marketing](../features/marketing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-marketing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Campaigns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Boards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Brochures:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Portals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Website:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Social/email:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attribution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-marketing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `campaigns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `boards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `brochures`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `portals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `website`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `social-email`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-marketing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-marketing-filament`](https://github.com/liberusoftware/module-real-estate-marketing-filament) (`liberusoftware/real-estate-marketing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/marketing.md) · [API plan](../api/marketing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Campaigns** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `campaigns`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Boards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `boards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Brochures** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `brochures`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Portals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `portals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Website** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `website`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Social/email** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `social/email`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Consent** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MarketingFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-filament/src/MarketingFilamentPlugin.php) · [MarketingFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-filament/src/MarketingFilamentServiceProvider.php) · [MarketingCampaignResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-filament/src/Resources/MarketingCampaignResource.php) · [CreateMarketingCampaign.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-filament/src/Resources/MarketingCampaignResource/Pages/CreateMarketingCampaign.php) · [EditMarketingCampaign.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-filament/src/Resources/MarketingCampaignResource/Pages/EditMarketingCampaign.php) · [ListMarketingCampaigns.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-filament/src/Resources/MarketingCampaignResource/Pages/ListMarketingCampaigns.php) · [NewsArticleResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-filament/src/Resources/NewsArticleResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MarketingCampaignPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Policies/MarketingCampaignPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function delete(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function forceDelete(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MarketingCampaign.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Models/MarketingCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [NewsArticle.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Models/NewsArticle.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
