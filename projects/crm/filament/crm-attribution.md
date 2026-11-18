# CRM: Crm Attribution Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-attribution). Observed identity: [`liberusoftware/module-crm-attribution-filament`](../../../modules/source/liberusoftware--module-crm-attribution-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-attribution-filament`  
**Matching domain module:** `crm-attribution`  
**Application:** CRM  
**Source feature:** [Crm Attribution](../features/crm-attribution.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-attribution` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **First/last/multi-touch models:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Campaign members:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source normalization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **UTM/click IDs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Offline conversions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Influence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cost allocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Model comparison:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-attribution-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `first-last-multi-touch-models`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `campaign-members`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-normalization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `utm-click-ids`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `offline-conversions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `influence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cost-allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `model-comparison`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-attribution` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-attribution-filament`](https://github.com/liberusoftware/module-crm-attribution-filament) (`liberusoftware/crm-attribution-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-attribution.md) · [API plan](../api/crm-attribution.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **First/last/multi-touch models** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `first/last/multi-touch models`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Campaign members** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `campaign members`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source normalization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source normalization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **UTM/click IDs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `utm/click ids`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Offline conversions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `offline conversions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Influence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `influence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cost allocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cost allocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Model comparison** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `model comparison`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AttributionFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-filament/src/AttributionFilamentPlugin.php) · [AttributionFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-filament/src/AttributionFilamentServiceProvider.php) · [ConversionResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-filament/src/Resources/ConversionResource.php) · [ListConversions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-filament/src/Resources/ConversionResource/Pages/ListConversions.php) · [TouchpointResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-filament/src/Resources/TouchpointResource.php) · [CreateTouchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-filament/src/Resources/TouchpointResource/Pages/CreateTouchpoint.php) · [ListTouchpoints.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-filament/src/Resources/TouchpointResource/Pages/ListTouchpoints.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AttributionQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Queries/AttributionQuery.php) | `public function touchpoints(int $teamId): Builder`<br>`public function conversions(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Actions/RecordConversion.php) | `public function execute(int $teamId, array $input): Conversion` |
| [RecordTouchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Actions/RecordTouchpoint.php) | `public function execute(int $teamId, array $input): Touchpoint` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Models/Conversion.php) | No literal fillable array detected; inspect the model and API schema. |
| [Touchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Models/Touchpoint.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
