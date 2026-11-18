# CMS: Cms Extension Manager Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-extension-manager). Observed identity: [`liberusoftware/module-cms-extension-manager-filament`](../../../modules/source/liberusoftware--module-cms-extension-manager-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-extension-manager-filament`  
**Matching domain module:** `cms-extension-manager`  
**Application:** CMS  
**Source feature:** [Cms Extension Manager](../features/cms-extension-manager.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-extension-manager` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Install/enable/disable/update/uninstall:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compatibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Permissions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Configuration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Migrations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rollback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-extension-manager-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `install-enable-disable-update-uninstall`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compatibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `permissions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `configuration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `migrations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rollback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-extension-manager` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-extension-manager-filament`](https://github.com/liberusoftware/module-cms-extension-manager-filament) (`liberusoftware/cms-extension-manager-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-extension-manager.md) · [API plan](../api/cms-extension-manager.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Install/enable/disable/update/uninstall** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `install/enable/disable/update/uninstall`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compatibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compatibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Permissions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permissions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Configuration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `configuration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Migrations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `migrations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rollback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rollback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ExtensionManagerFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-extension-manager-filament/src/ExtensionManagerFilamentServiceProvider.php) · [ExtensionManagerPage.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-extension-manager-filament/src/Pages/ExtensionManagerPage.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExtensionManagerService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-manager/src/Services/ExtensionManagerService.php) | `public function __construct(private ModuleRegistryInterface $registry, private ModuleManagerInterface $manager)`<br>`public function all(): array`<br>`public function enable(string $key): void`<br>`public function disable(string $key): void` |
<!-- layer-implementation-plan:end -->
