# Billing: Application Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#application). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-application-filament`  
**Matching domain module:** `application`  
**Application:** Billing  
**Source feature:** [Application](../features/application.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `application` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Environment validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Application metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health/readiness:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Maintenance mode:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identifiers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Clocks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shared service contracts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-application-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `environment-validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `application-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health-readiness`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `maintenance-mode`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identifiers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `clocks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shared-service-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `application` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-application-filament`](https://github.com/liberusoftware/module-application-filament) (`liberusoftware/application-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/application.md) · [API plan](../api/application.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Environment validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `environment validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Application metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `application metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health/readiness** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health/readiness`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Maintenance mode** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `maintenance mode`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Identifiers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `identifiers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Clocks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `clocks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shared service contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shared service contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [Clock.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Contracts/Clock.php) | `public function now(): \DateTimeImmutable` |
| [IdentifierFactory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Contracts/IdentifierFactory.php) | `public function make(): string` |
<!-- layer-implementation-plan:end -->
