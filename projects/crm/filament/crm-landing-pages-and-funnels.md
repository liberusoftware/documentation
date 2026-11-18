# CRM: Crm Landing Pages And Funnels Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-landing-pages-and-funnels). Observed identity: [`liberusoftware/module-crm-landing-pages-and-funnels-filament`](../../../modules/source/liberusoftware--module-crm-landing-pages-and-funnels-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-landing-pages-and-funnels-filament`  
**Matching domain module:** `crm-landing-pages-and-funnels`  
**Application:** CRM  
**Source feature:** [Crm Landing Pages And Funnels](../features/crm-landing-pages-and-funnels.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-landing-pages-and-funnels` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Multi-step funnels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Landing/thank-you pages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Domains:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SEO metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Personalization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Order links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preview:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Publish:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conversion tracking:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-landing-pages-and-funnels-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `multi-step-funnels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `landing-thank-you-pages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `domains`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `seo-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `personalization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `order-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preview`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `publish`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conversion-tracking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-landing-pages-and-funnels` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-landing-pages-and-funnels-filament`](https://github.com/liberusoftware/module-crm-landing-pages-and-funnels-filament) (`liberusoftware/crm-landing-pages-and-funnels-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-landing-pages-and-funnels.md) · [API plan](../api/crm-landing-pages-and-funnels.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Multi-step funnels** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `multi-step funnels`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Landing/thank-you pages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `landing/thank-you pages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Domains** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `domains`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SEO metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `seo metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Personalization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `personalization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Forms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `forms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Order links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `order links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preview** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preview`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Publish** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `publish`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conversion tracking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conversion tracking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [LandingPagesAndFunnelsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels-filament/src/LandingPagesAndFunnelsFilamentServiceProvider.php) · [FunnelResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels-filament/src/Resources/FunnelResource.php) · [CreateFunnel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels-filament/src/Resources/Pages/CreateFunnel.php) · [EditFunnel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels-filament/src/Resources/Pages/EditFunnel.php) · [ListFunnels.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels-filament/src/Resources/Pages/ListFunnels.php).

| Observed core query | Public method signatures |
| --- | --- |
| [FunnelQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Queries/FunnelQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddFunnelPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Actions/AddFunnelPage.php) | `public function __construct(private readonly FunnelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Funnel $funnel, array $input): FunnelPage` |
| [CreateFunnel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Actions/CreateFunnel.php) | `public function __construct(private readonly FunnelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Funnel` |
| [PublishFunnel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Actions/PublishFunnel.php) | `public function __construct(private readonly FunnelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Funnel $funnel, array $input): Funnel` |
| [RecordFunnelEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Actions/RecordFunnelEvent.php) | `public function __construct(private readonly FunnelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Funnel $funnel, array $input): FunnelEvent` |
| [FunnelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Services/FunnelPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Funnel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Models/Funnel.php) | No literal fillable array detected; inspect the model and API schema. |
| [FunnelEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Models/FunnelEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [FunnelPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Models/FunnelPage.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
