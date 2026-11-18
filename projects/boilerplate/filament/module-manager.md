# Boilerplate: Module Manager Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-manager). Observed identity: [`liberusoftware/module-manager-filament`](../../../modules/source/liberusoftware--module-manager-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-module-manager-filament`
**Matching core package:** [`module-module-manager`](../core/module-manager.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Manifest discovery, dependency resolution, enablement, lifecycle, compatibility, registry caching, and diagnostics.

## Adapter implementation plan

This package presents the Module Manager core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Module Manager core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-manager-filament`](https://github.com/liberusoftware/module-manager-filament) (`liberusoftware/manager-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-manager.md) · [API plan](../api/module-manager.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Manifest discovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `manifest discovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependency resolution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependency resolution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Enablement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `enablement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compatibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compatibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Registry caching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registry caching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Diagnostics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `diagnostics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ModuleManagerFilamentPlugin.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager-filament/src/ModuleManagerFilamentPlugin.php) · [ModuleManagerFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager-filament/src/ModuleManagerFilamentServiceProvider.php) · [FoundationOperations.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager-filament/src/Pages/FoundationOperations.php).
<!-- layer-implementation-plan:end -->
