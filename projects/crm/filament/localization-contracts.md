# CRM: Localization Contracts Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#localization-contracts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-localization-contracts-filament`  
**Matching domain module:** `localization-contracts`  
**Application:** CRM  
**Source feature:** [Localization Contracts](../features/localization-contracts.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `localization-contracts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Translation provider interface contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locale and language-pair value objects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Segment translation request and result DTOs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fallback and quota error contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Catalog synchronization metadata:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-localization-contracts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `translation-provider-interface-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locale-and-language-pair-value-objects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `segment-translation-request-and-result-dtos`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fallback-and-quota-error-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `catalog-synchronization-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `localization-contracts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-localization-contracts-filament`](https://github.com/liberusoftware/module-localization-contracts-filament) (`liberusoftware/localization-contracts-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/localization-contracts.md) · [API plan](../api/localization-contracts.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Translation provider interface contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `translation provider interface contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locale and language-pair value objects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locale and language-pair value objects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Segment translation request and result DTOs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `segment translation request and result dtos`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fallback and quota error contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fallback and quota error contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Catalog synchronization metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `catalog synchronization metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
