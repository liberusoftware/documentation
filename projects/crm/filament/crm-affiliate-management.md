# CRM: Crm Affiliate Management Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-affiliate-management). Observed identity: [`liberusoftware/module-crm-affiliate-management-filament`](../../../modules/source/liberusoftware--module-crm-affiliate-management-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-affiliate-management-filament`  
**Matching domain module:** `crm-affiliate-management`  
**Application:** CRM  
**Source feature:** [Crm Affiliate Management](../features/crm-affiliate-management.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-affiliate-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Affiliates and partner profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Applications and onboarding approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Links, campaigns, and clicks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conversions and commission rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payout approvals/exports, disputes, assets, and portal:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-affiliate-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `affiliates-and-partner-profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `applications-and-onboarding-approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `links-campaigns-and-clicks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conversions-and-commission-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payout-approvals-exports-disputes-assets-and-portal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-affiliate-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-affiliate-management-filament`](https://github.com/liberusoftware/module-crm-affiliate-management-filament) (`liberusoftware/crm-affiliate-management-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-affiliate-management.md) · [API plan](../api/crm-affiliate-management.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Affiliates and partner profiles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `affiliates and partner profiles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Applications and onboarding approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `applications and onboarding approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Links, campaigns, and clicks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `links, campaigns, and clicks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conversions and commission rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conversions and commission rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payout approvals/exports, disputes, assets, and portal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payout approvals/exports, disputes, assets, and portal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AffiliateManagementFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-filament/src/AffiliateManagementFilamentPlugin.php) · [AffiliateManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-filament/src/AffiliateManagementFilamentServiceProvider.php) · [AffiliateResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-filament/src/Resources/AffiliateResource.php) · [CreateAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-filament/src/Resources/AffiliateResource/Pages/CreateAffiliate.php) · [EditAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-filament/src/Resources/AffiliateResource/Pages/EditAffiliate.php) · [ListAffiliates.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-filament/src/Resources/AffiliateResource/Pages/ListAffiliates.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AffiliateQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Queries/AffiliateQuery.php) | `public function affiliates(int $teamId): Builder`<br>`public function events(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApplyAffiliate.php) | `public function execute(int $teamId, array $input): Affiliate` |
| [ApproveAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliate.php) | `public function execute(int $teamId, Affiliate $affiliate): Affiliate` |
| [ApproveAffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliatePayout.php) | `public function execute(int $teamId, int $actorId, AffiliatePayout $payout): AffiliatePayout` |
| [CreateAffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/CreateAffiliateLink.php) | `public function execute(int $teamId, Affiliate $affiliate, array $input): AffiliateLink` |
| [RecordAffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/RecordAffiliateEvent.php) | `public function execute(int $teamId, AffiliateLink $link, array $input): AffiliateEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Affiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/Affiliate.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateLink.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliatePayout.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
