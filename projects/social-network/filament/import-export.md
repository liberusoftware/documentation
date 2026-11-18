# Social Network: Import Export Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#import-export). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-import-export-filament`  
**Matching domain module:** `import-export`  
**Application:** Social Network  
**Source feature:** [Import Export](../features/import-export.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `import-export` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Schemas:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mapping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dry runs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queued execution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Progress:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Errors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Authorization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retention:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-import-export-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `schemas`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mapping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dry-runs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queued-execution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `progress`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `errors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `authorization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `import-export` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-import-export-filament`](https://github.com/liberusoftware/module-import-export-filament) (`liberusoftware/import-export-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/import-export.md) · [API plan](../api/import-export.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Schemas** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schemas`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mapping** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mapping`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dry runs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dry runs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Queued execution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `queued execution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Progress** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `progress`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Errors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `errors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Authorization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `authorization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retention** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retention`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransferAuthorizer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/src/Contracts/TransferAuthorizer.php) | `public function allowed(string\|int $actorId, string $schema, string $direction): bool` |
<!-- layer-implementation-plan:end -->
