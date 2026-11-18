# Control Panel: Control Panel Containers Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-containers). Observed identity: [`liberusoftware/module-control-panel-containers-filament`](../../../modules/source/liberusoftware--module-control-panel-containers-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-control-panel-control-panel-containers-filament`  
**Matching domain module:** `control-panel-containers`  
**Application:** Control Panel  
**Source feature:** [Control Panel Containers](../features/control-panel-containers.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `control-panel-containers` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Images:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Registries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workloads:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Networks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Volumes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Secrets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Limits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-control-panel-control-panel-containers-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `images`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `registries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workloads`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `networks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `volumes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `secrets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `limits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `control-panel-containers` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-control-panel-containers-filament`](https://github.com/liberusoftware/module-control-panel-containers-filament) (`liberusoftware/control-panel-containers-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/control-panel-containers.md) · [API plan](../api/control-panel-containers.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Images** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `images`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Registries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Workloads** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workloads`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Networks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `networks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Volumes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `volumes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Secrets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `secrets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Limits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `limits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContainersFilamentPlugin.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/ContainersFilamentPlugin.php) · [ContainersFilamentServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/ContainersFilamentServiceProvider.php) · [ContainerAssetResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerAssetResource.php) · [ContainerImageResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerImageResource.php) · [CreateContainerImage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerImageResource/Pages/CreateContainerImage.php) · [EditContainerImage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerImageResource/Pages/EditContainerImage.php) · [ListContainerImages.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerImageResource/Pages/ListContainerImages.php) · [ContainerLifecycleResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerLifecycleResource.php) · [ListContainerLifecycles.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerLifecycleResource/Pages/ListContainerLifecycles.php) · [ContainerLimitResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerLimitResource.php) · [ListContainerLimits.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerLimitResource/Pages/ListContainerLimits.php) · [ContainerNetworkResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerNetworkResource.php) · [ListContainerNetworks.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerNetworkResource/Pages/ListContainerNetworks.php) · [ContainerRegistryResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerRegistryResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListWorkloads.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Queries/ListWorkloads.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DeleteWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/DeleteWorkload.php) | `public function execute(Workload $workload): void` |
| [RecordContainerResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RecordContainerResource.php) | `public function execute(array $a): ContainerResource` |
| [RegisterContainerAsset.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RegisterContainerAsset.php) | `public function execute(array $attributes): Model` |
| [RegisterWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RegisterWorkload.php) | `public function execute(array $attributes): Workload` |
| [StartWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/StartWorkload.php) | `public function execute(Workload $workload): Workload` |
| [StopWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/StopWorkload.php) | `public function execute(Workload $workload): Workload` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContainerImage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerImage.php) | `id`, `team_id`, `repository`, `tag`, `digest`, `size_bytes`, `architecture`, `status`, `metadata` |
| [ContainerLifecycle.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerLifecycle.php) | `id`, `team_id`, `workload_id`, `operation`, `status`, `idempotency_key`, `requested_at`, `completed_at`, `details` |
| [ContainerLimit.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerLimit.php) | `id`, `team_id`, `workload_id`, `cpu_millis`, `memory_bytes`, `pids`, `restart_policy` |
| [ContainerNetwork.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerNetwork.php) | `id`, `team_id`, `name`, `driver`, `subnet`, `gateway`, `options`, `status` |
| [ContainerRegistry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerRegistry.php) | `id`, `team_id`, `name`, `endpoint`, `username`, `credential`, `tls_verify`, `active` |
| [ContainerResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerResource.php) | `id`, `team_id`, `workload_id`, `kind`, `name`, `status`, `spec` |
| [ContainerSecret.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerSecret.php) | `id`, `team_id`, `name`, `value`, `metadata`, `active` |
| [ContainerVolume.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerVolume.php) | `id`, `team_id`, `name`, `driver`, `mount_path`, `size_bytes`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
