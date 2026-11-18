# CRM: Channel Sales Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#channel-sales). Observed identity: [`liberusoftware/module-crm-channel-sales-filament`](../../../modules/source/liberusoftware--module-crm-channel-sales-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-channel-sales-filament`  
**Matching domain module:** `crm-channel-sales`  
**Application:** CRM  
**Source feature:** [Channel Sales](../features/channel-sales.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-channel-sales` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Partner opportunities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shared pipelines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Referrals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reseller pricing references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quotes/orders handoff:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Commissions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forecasts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Partner portal:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-channel-sales-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `partner-opportunities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shared-pipelines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `referrals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reseller-pricing-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quotes-orders-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `commissions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forecasts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `partner-portal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-channel-sales` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-channel-sales-filament`](https://github.com/liberusoftware/module-crm-channel-sales-filament) (`liberusoftware/crm-channel-sales-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/channel-sales.md) · [API plan](../api/channel-sales.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Partner opportunities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `partner opportunities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shared pipelines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shared pipelines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Referrals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `referrals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reseller pricing references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reseller pricing references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quotes/orders handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quotes/orders handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Commissions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `commissions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Forecasts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `forecasts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Partner portal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `partner portal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ChannelSalesFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-filament/src/ChannelSalesFilamentPlugin.php) · [ChannelSalesFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-filament/src/ChannelSalesFilamentServiceProvider.php) · [ChannelOpportunityResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-filament/src/Resources/ChannelOpportunityResource.php) · [CreateChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-filament/src/Resources/ChannelOpportunityResource/Pages/CreateChannelOpportunity.php) · [ListChannelOpportunities.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-filament/src/Resources/ChannelOpportunityResource/Pages/ListChannelOpportunities.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ChannelSalesQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Queries/ChannelSalesQuery.php) | `public function opportunities(int $teamId): Builder`<br>`public function forecast(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdvanceChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Actions/AdvanceChannelOpportunity.php) | `public function execute(int $teamId, int $actorId, ChannelOpportunity $opportunity, string $stage, string $handoffStatus = 'pending'): ChannelEvent` |
| [RegisterChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Actions/RegisterChannelOpportunity.php) | `public function execute(int $teamId, int $ownerId, string $partnerKey, string $opportunityKey, float $amount, float $commissionRate, array $pricingReference = []): ChannelOpportunity` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ChannelEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Models/ChannelEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Models/ChannelOpportunity.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
