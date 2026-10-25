# liberusoftware/module-control-panel-containers-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Control Panel Containers.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-containers-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-containers-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-containers-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-containers-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\ContainersFilament\\ContainersFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/module.json).

**Declared capabilities:** control-panel.containers.filament

**Declared features:** Workload administration, Image inventory, Container asset state

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-containers` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\ContainersFilament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-control-panel-containers": "^1.0"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/ContainersFilamentPlugin.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/ContainersFilamentPlugin.php) · [src/ContainersFilamentServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/ContainersFilamentServiceProvider.php) · [src/Resources/ContainerAssetResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerAssetResource.php) · [src/Resources/ContainerImageResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerImageResource.php) · [src/Resources/ContainerImageResource/Pages/CreateContainerImage.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerImageResource/Pages/CreateContainerImage.php) · [src/Resources/ContainerImageResource/Pages/EditContainerImage.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerImageResource/Pages/EditContainerImage.php) · [src/Resources/ContainerImageResource/Pages/ListContainerImages.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerImageResource/Pages/ListContainerImages.php) · [src/Resources/ContainerLifecycleResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerLifecycleResource.php) · [src/Resources/ContainerLifecycleResource/Pages/ListContainerLifecycles.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerLifecycleResource/Pages/ListContainerLifecycles.php) · [src/Resources/ContainerLimitResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerLimitResource.php) · [src/Resources/ContainerLimitResource/Pages/ListContainerLimits.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerLimitResource/Pages/ListContainerLimits.php) · [src/Resources/ContainerNetworkResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerNetworkResource.php) · [src/Resources/ContainerNetworkResource/Pages/ListContainerNetworks.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerNetworkResource/Pages/ListContainerNetworks.php) · [src/Resources/ContainerRegistryResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerRegistryResource.php) · [src/Resources/ContainerRegistryResource/Pages/ListContainerRegistries.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerRegistryResource/Pages/ListContainerRegistries.php) · [src/Resources/ContainerSecretResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerSecretResource.php) · [src/Resources/ContainerSecretResource/Pages/ListContainerSecrets.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerSecretResource/Pages/ListContainerSecrets.php) · [src/Resources/ContainerVolumeResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerVolumeResource.php) · [src/Resources/ContainerVolumeResource/Pages/ListContainerVolumes.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/ContainerVolumeResource/Pages/ListContainerVolumes.php) · [src/Resources/WorkloadResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/WorkloadResource.php) · [src/Resources/WorkloadResource/Pages/CreateWorkload.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/WorkloadResource/Pages/CreateWorkload.php) · [src/Resources/WorkloadResource/Pages/EditWorkload.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/WorkloadResource/Pages/EditWorkload.php) · [src/Resources/WorkloadResource/Pages/ListWorkloads.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-filament/src/Resources/WorkloadResource/Pages/ListWorkloads.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
