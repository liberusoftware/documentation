# Maintenance: Integrations Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#integrations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-integrations-filament`  
**Matching domain module:** `integrations`  
**Application:** Maintenance  
**Source feature:** [Integrations](../features/integrations.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `integrations` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider credentials:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **OAuth callbacks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Secret rotation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Connection tests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sync:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-integrations-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `provider-credentials`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `oauth-callbacks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `secret-rotation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `connection-tests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sync`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `integrations` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-integrations-filament`](https://github.com/liberusoftware/module-integrations-filament) (`liberusoftware/integrations-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/integrations.md) · [API plan](../api/integrations.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Provider credentials** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider credentials`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capabilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capabilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **OAuth callbacks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `oauth callbacks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Secret rotation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `secret rotation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Connection tests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `connection tests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sync** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sync`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IntegrationAdapter.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/src/Contracts/IntegrationAdapter.php) | `public function name(): string`<br>`public function capabilities(): array`<br>`public function test(array $credentials): bool` |
<!-- layer-implementation-plan:end -->
