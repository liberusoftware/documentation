# CMS: Module Cms Observability Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-observability). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-observability-filament`  
**Matching domain module:** `module-cms-observability`  
**Application:** CMS  
**Source feature:** [Module Cms Observability](../features/module-cms-observability.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-observability` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Structured logs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Correlation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Metrics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Traces:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exception reporting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health checks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Redaction:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SLO hooks:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-observability-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `structured-logs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `correlation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `metrics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `traces`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exception-reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health-checks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `redaction`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `slo-hooks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-observability` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-observability-filament`](https://github.com/liberusoftware/module-cms-observability-filament) (`liberusoftware/cms-observability-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-observability.md) · [API plan](../api/module-cms-observability.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Structured logs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `structured logs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Correlation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `correlation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Metrics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `metrics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Traces** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `traces`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exception reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exception reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redaction** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redaction`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SLO hooks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `slo hooks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence
<!-- layer-implementation-plan:end -->
