# liberusoftware/module-control-panel-kubernetes-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Control Panel Kubernetes.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-kubernetes-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-kubernetes-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-kubernetes-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-kubernetes-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\KubernetesFilament\\KubernetesFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/module.json).

**Declared capabilities:** control-panel.kubernetes.filament

**Declared features:** Clusters, Nodes, Namespaces, RBAC, Workloads, Ingress, Helm, Storage, Autoscaling, Upgrades, Multi-cluster views

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-kubernetes` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\KubernetesFilament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-control-panel-kubernetes": "^1.0"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/KubernetesFilamentPlugin.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/KubernetesFilamentPlugin.php) · [src/KubernetesFilamentServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/KubernetesFilamentServiceProvider.php) · [src/Resources/ClusterResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/ClusterResource.php) · [src/Resources/ClusterResource/Pages/CreateCluster.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/ClusterResource/Pages/CreateCluster.php) · [src/Resources/ClusterResource/Pages/EditCluster.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/ClusterResource/Pages/EditCluster.php) · [src/Resources/ClusterResource/Pages/ListClusters.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/ClusterResource/Pages/ListClusters.php) · [src/Resources/HelmReleaseResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/HelmReleaseResource.php) · [src/Resources/HelmReleaseResource/Pages/CreateHelmRelease.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/HelmReleaseResource/Pages/CreateHelmRelease.php) · [src/Resources/HelmReleaseResource/Pages/EditHelmRelease.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/HelmReleaseResource/Pages/EditHelmRelease.php) · [src/Resources/HelmReleaseResource/Pages/ListHelmReleases.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/HelmReleaseResource/Pages/ListHelmReleases.php) · [src/Resources/KubernetesAssetResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesAssetResource.php) · [src/Resources/KubernetesAutoscalerResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesAutoscalerResource.php) · [src/Resources/KubernetesAutoscalerResource/Pages/ListKubernetesAutoscalers.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesAutoscalerResource/Pages/ListKubernetesAutoscalers.php) · [src/Resources/KubernetesClusterViewResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesClusterViewResource.php) · [src/Resources/KubernetesClusterViewResource/Pages/ListKubernetesClusterViews.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesClusterViewResource/Pages/ListKubernetesClusterViews.php) · [src/Resources/KubernetesIngressResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesIngressResource.php) · [src/Resources/KubernetesIngressResource/Pages/ListKubernetesIngresses.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesIngressResource/Pages/ListKubernetesIngresses.php) · [src/Resources/KubernetesNamespaceResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesNamespaceResource.php) · [src/Resources/KubernetesNamespaceResource/Pages/ListKubernetesNamespaces.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesNamespaceResource/Pages/ListKubernetesNamespaces.php) · [src/Resources/KubernetesNodeResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesNodeResource.php) · [src/Resources/KubernetesNodeResource/Pages/CreateKubernetesNode.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesNodeResource/Pages/CreateKubernetesNode.php) · [src/Resources/KubernetesNodeResource/Pages/EditKubernetesNode.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesNodeResource/Pages/EditKubernetesNode.php) · [src/Resources/KubernetesNodeResource/Pages/ListKubernetesNodes.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesNodeResource/Pages/ListKubernetesNodes.php) · [src/Resources/KubernetesNodeResource/Pages/ViewKubernetesNode.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesNodeResource/Pages/ViewKubernetesNode.php) · [src/Resources/KubernetesRbacBindingResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesRbacBindingResource.php) · [src/Resources/KubernetesRbacBindingResource/Pages/ListKubernetesRbacBindings.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesRbacBindingResource/Pages/ListKubernetesRbacBindings.php) · [src/Resources/KubernetesStorageClaimResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesStorageClaimResource.php) · [src/Resources/KubernetesStorageClaimResource/Pages/ListKubernetesStorageClaims.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesStorageClaimResource/Pages/ListKubernetesStorageClaims.php) · [src/Resources/KubernetesUpgradeResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesUpgradeResource.php) · [src/Resources/KubernetesUpgradeResource/Pages/ListKubernetesUpgrades.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesUpgradeResource/Pages/ListKubernetesUpgrades.php) · [src/Resources/KubernetesWorkloadResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesWorkloadResource.php) · [src/Resources/KubernetesWorkloadResource/Pages/ListKubernetesWorkloads.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Resources/KubernetesWorkloadResource/Pages/ListKubernetesWorkloads.php) · [src/Widgets/HelmStatsWidget.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-filament/src/Widgets/HelmStatsWidget.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
