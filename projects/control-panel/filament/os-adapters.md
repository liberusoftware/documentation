# Control Panel: OS Adapters Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#os-adapters). Observed identity: [`liberusoftware/module-control-panel-os-adapters-filament`](../../../modules/source/liberusoftware--module-control-panel-os-adapters-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-control-panel-os-adapters-filament`  
**Matching domain module:** `control-panel-os-adapters`  
**Application:** Control Panel  
**Source feature:** [OS Adapters](../features/os-adapters.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `control-panel-os-adapters` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Detection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Packages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Services:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Firewall:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Users:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Filesystems:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Repositories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Support matrix:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-control-panel-os-adapters-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `detection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `packages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `services`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `firewall`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `users`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `filesystems`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `repositories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `support-matrix`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `control-panel-os-adapters` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-control-panel-os-adapters-filament`](https://github.com/liberusoftware/module-control-panel-os-adapters-filament) (`liberusoftware/control-panel-os-adapters-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/os-adapters.md) · [API plan](../api/os-adapters.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Detection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `detection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Packages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `packages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Services** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `services`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Firewall** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `firewall`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Users** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `users`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Filesystems** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `filesystems`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Repositories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `repositories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Support matrix** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `support matrix`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OsAdaptersFilamentPlugin.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/OsAdaptersFilamentPlugin.php) · [OsAdaptersFilamentServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/OsAdaptersFilamentServiceProvider.php) · [FirewallRuleResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/FirewallRuleResource.php) · [CreateFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/FirewallRuleResource/Pages/CreateFirewallRule.php) · [EditFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/FirewallRuleResource/Pages/EditFirewallRule.php) · [ListFirewallRules.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/FirewallRuleResource/Pages/ListFirewallRules.php) · [OsAdapterResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsAdapterResource.php) · [CreateOsAdapter.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsAdapterResource/Pages/CreateOsAdapter.php) · [EditOsAdapter.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsAdapterResource/Pages/EditOsAdapter.php) · [ListOsAdapters.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsAdapterResource/Pages/ListOsAdapters.php) · [OsPackageResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsPackageResource.php) · [CreateOsPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsPackageResource/Pages/CreateOsPackage.php) · [EditOsPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsPackageResource/Pages/EditOsPackage.php) · [ListOsPackages.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsPackageResource/Pages/ListOsPackages.php).

| Observed core query | Public method signatures |
| --- | --- |
| [InstallationCommandReport.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/InstallationCommandReport.php) | `public function __construct(private readonly ServiceStatusReport $serviceStatusReport)`<br>`public function execute(string\|int $teamId): array` |
| [ListOsAdapters.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ListOsAdapters.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ServiceStatusReport.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ServiceStatusReport.php) | `public function all(string\|int $teamId): Collection`<br>`public function missing(string\|int $teamId): Collection`<br>`public function stopped(string\|int $teamId): Collection`<br>`public function find(string\|int $teamId, string $name): ?OsService` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/CreateFirewallRule.php) | `public function execute(array $attributes): FirewallRule`<br>`public function validateSource(mixed $source): void` |
| [DeleteFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/DeleteFirewallRule.php) | `public function execute(FirewallRule $rule): void` |
| [RecordOsResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordOsResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [RecordSupportMatrix.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordSupportMatrix.php) | `public function execute(array $attributes): SupportMatrixEntry` |
| [RegisterOsAdapter.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RegisterOsAdapter.php) | `public function execute(array $attributes): OsAdapter` |
| [UpdateFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateFirewallRule.php) | `public function execute(FirewallRule $rule, array $attributes): FirewallRule` |
| [UpdateOsService.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateOsService.php) | `public function execute(OsService $service, array $attributes): OsService` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FilesystemMount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FilesystemMount.php) | `team_id`, `node_id`, `device`, `mount_path`, `filesystem`, `size_bytes`, `free_bytes`, `options`, `mounted` |
| [FirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FirewallRule.php) | `team_id`, `node_id`, `direction`, `action`, `protocol`, `port`, `source`, `comment`, `active` |
| [OsAdapter.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsAdapter.php) | `team_id`, `node_id`, `operating_system`, `version`, `capabilities`, `status`, `metadata` |
| [OsPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsPackage.php) | `team_id`, `node_id`, `name`, `version`, `architecture`, `status`, `metadata` |
| [OsService.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsService.php) | `team_id`, `node_id`, `name`, `version`, `status`, `enabled`, `metadata` |
| [OsUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsUser.php) | `team_id`, `node_id`, `username`, `uid`, `shell`, `home`, `sudo`, `status`, `metadata` |
| [PackageRepository.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/PackageRepository.php) | `team_id`, `node_id`, `name`, `url`, `distribution`, `enabled`, `trusted`, `metadata` |
| [SupportMatrixEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/SupportMatrixEntry.php) | `operating_system`, `version`, `capability`, `supported`, `minimum_adapter_version`, `notes` |
<!-- layer-implementation-plan:end -->
