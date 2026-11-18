# Control Panel: Kubernetes Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#kubernetes). Observed identity: [`liberusoftware/module-control-panel-kubernetes-filament`](../../../modules/source/liberusoftware--module-control-panel-kubernetes-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-control-panel-kubernetes-filament`  
**Matching domain module:** `control-panel-kubernetes`  
**Application:** Control Panel  
**Source feature:** [Kubernetes](../features/kubernetes.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `control-panel-kubernetes` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Clusters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Nodes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Namespaces:** resource/table/form/action or page behavior for this module's authorized workflow.
- **RBAC:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workloads:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ingress:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Helm:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Storage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Autoscaling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Upgrades:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Multi-cluster views:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-control-panel-kubernetes-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `clusters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `nodes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `namespaces`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rbac`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workloads`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ingress`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `helm`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `storage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `autoscaling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `upgrades`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `multi-cluster-views`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `control-panel-kubernetes` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-control-panel-kubernetes-filament`](https://github.com/liberusoftware/module-control-panel-kubernetes-filament) (`liberusoftware/control-panel-kubernetes-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/kubernetes.md) · [API plan](../api/kubernetes.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Clusters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `clusters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Nodes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `nodes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Namespaces** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `namespaces`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **RBAC** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rbac`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Workloads** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workloads`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ingress** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ingress`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Helm** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `helm`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Storage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `storage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Autoscaling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `autoscaling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Upgrades** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `upgrades`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Multi-cluster views** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `multi-cluster views`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [KubernetesFilamentPlugin.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/KubernetesFilamentPlugin.php) · [KubernetesFilamentServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/KubernetesFilamentServiceProvider.php) · [ClusterResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/ClusterResource.php) · [CreateCluster.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/ClusterResource/Pages/CreateCluster.php) · [EditCluster.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/ClusterResource/Pages/EditCluster.php) · [ListClusters.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/ClusterResource/Pages/ListClusters.php) · [HelmReleaseResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/HelmReleaseResource.php) · [CreateHelmRelease.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/HelmReleaseResource/Pages/CreateHelmRelease.php) · [EditHelmRelease.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/HelmReleaseResource/Pages/EditHelmRelease.php) · [ListHelmReleases.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/HelmReleaseResource/Pages/ListHelmReleases.php) · [KubernetesAssetResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesAssetResource.php) · [KubernetesAutoscalerResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesAutoscalerResource.php) · [ListKubernetesAutoscalers.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesAutoscalerResource/Pages/ListKubernetesAutoscalers.php) · [KubernetesClusterViewResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesClusterViewResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListClusters.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Queries/ListClusters.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveCluster.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/ArchiveCluster.php) | `public function execute(Cluster $cluster): Cluster` |
| [CordonNode.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/CordonNode.php) | `public function execute(KubernetesNode $node): KubernetesNode` |
| [DeleteHelmRelease.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/DeleteHelmRelease.php) | `public function execute(HelmRelease $release): void` |
| [DrainNode.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/DrainNode.php) | `public function execute(KubernetesNode $node, array $options = []): KubernetesNode` |
| [LabelNode.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/LabelNode.php) | `public function execute(KubernetesNode $node, string $key, string $value): KubernetesNode` |
| [RecordKubernetesResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/RecordKubernetesResource.php) | `public function execute(array $a): KubernetesResource` |
| [RegisterCluster.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/RegisterCluster.php) | `public function execute(array $attributes): Cluster` |
| [RegisterKubernetesAsset.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/RegisterKubernetesAsset.php) | `public function execute(array $a): Model` |
| [SuspendCluster.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/SuspendCluster.php) | `public function execute(Cluster $cluster): Cluster` |
| [UncordonNode.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/UncordonNode.php) | `public function execute(KubernetesNode $node): KubernetesNode` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Cluster.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/Cluster.php) | `team_id`, `name`, `endpoint`, `status`, `configuration` |
| [HelmRelease.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/HelmRelease.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `chart`, `version`, `values`, `status` |
| [KubernetesAutoscaler.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesAutoscaler.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `target`, `min_replicas`, `max_replicas`, `metric`, `status` |
| [KubernetesClusterView.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesClusterView.php) | `id`, `team_id`, `name`, `cluster_ids`, `filters`, `status` |
| [KubernetesIngress.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesIngress.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `host`, `paths`, `tls`, `backend`, `status` |
| [KubernetesNamespace.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesNamespace.php) | `id`, `team_id`, `cluster_id`, `name`, `status`, `labels`, `quotas` |
| [KubernetesNode.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesNode.php) | `id`, `team_id`, `cluster_id`, `name`, `uid`, `kubernetes_version`, `container_runtime`, `os_image`, `kernel_version`, `architecture`, `status`, `status_message`, `schedulable`, `labels`, `annotations`, `taints`, `addresses`, `capacity`, `allocatable`, `conditions`, `last_heartbeat_at` |
| [KubernetesRbacBinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesRbacBinding.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `role`, `subjects`, `rules`, `active` |
<!-- layer-implementation-plan:end -->
