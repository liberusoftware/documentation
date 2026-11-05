# Kubernetes: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-kubernetes`.

**Proposed design identifier:** `module-control-panel-kubernetes-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/kubernetes.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-kubernetes](../../../modules/source/liberusoftware--module-control-panel-kubernetes.md) |
| API | [liberusoftware/module-control-panel-kubernetes-api](../../../modules/source/liberusoftware--module-control-panel-kubernetes-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Clusters | A focused authorized view or workflow section for clusters; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Nodes | A focused authorized view or workflow section for nodes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Namespaces | A focused authorized view or workflow section for namespaces; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| RBAC | A focused authorized view or workflow section for rbac; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Workloads | A focused authorized view or workflow section for workloads; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Ingress | A focused authorized view or workflow section for ingress; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Helm | A focused authorized view or workflow section for helm; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Storage | A focused authorized view or workflow section for storage; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Autoscaling | A focused authorized view or workflow section for autoscaling; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Upgrades | A focused authorized view or workflow section for upgrades; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Multi-cluster views | A focused authorized view or workflow section for multi-cluster views; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListClusters.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Queries/ListClusters.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
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
| [UnlabelNode.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/UnlabelNode.php) | `public function execute(KubernetesNode $node, string $key): KubernetesNode` |
| [UpdateHelmRelease.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Actions/UpdateHelmRelease.php) | `public function execute(HelmRelease $release, array $attributes): HelmRelease` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Cluster.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/Cluster.php) | `team_id`, `name`, `endpoint`, `status`, `configuration` |
| [HelmRelease.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/HelmRelease.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `chart`, `version`, `values`, `status` |
| [KubernetesAutoscaler.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesAutoscaler.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `target`, `min_replicas`, `max_replicas`, `metric`, `status` |
| [KubernetesClusterView.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesClusterView.php) | `id`, `team_id`, `name`, `cluster_ids`, `filters`, `status` |
| [KubernetesIngress.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesIngress.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `host`, `paths`, `tls`, `backend`, `status` |
| [KubernetesNamespace.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesNamespace.php) | `id`, `team_id`, `cluster_id`, `name`, `status`, `labels`, `quotas` |
| [KubernetesNode.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesNode.php) | `id`, `team_id`, `cluster_id`, `name`, `uid`, `kubernetes_version`, `container_runtime`, `os_image`, `kernel_version`, `architecture`, `status`, `status_message`, `schedulable`, `labels`, `annotations`, `taints`, `addresses`, `capacity`, `allocatable`, `conditions`, `last_heartbeat_at` |
| [KubernetesRbacBinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesRbacBinding.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `role`, `subjects`, `rules`, `active` |
| [KubernetesResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesResource.php) | `id`, `team_id`, `cluster_id`, `kind`, `name`, `namespace`, `status`, `spec` |
| [KubernetesStorageClaim.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesStorageClaim.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `storage_class`, `capacity_bytes`, `access_modes`, `status` |
| [KubernetesUpgrade.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesUpgrade.php) | `id`, `team_id`, `cluster_id`, `from_version`, `to_version`, `status`, `started_at`, `completed_at`, `details` |
| [KubernetesWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes/src/Models/KubernetesWorkload.php) | `id`, `team_id`, `cluster_id`, `namespace`, `name`, `kind`, `image`, `replicas`, `status`, `spec` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-kubernetes-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/kubernetes')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [ClusterController::class, 'index'])->name('control-panel.kubernetes.index');
Route::post('/', [ClusterController::class, 'store'])->name('control-panel.kubernetes.store');
Route::get('/assets', [ClusterController::class, 'assets'])->name('control-panel.kubernetes.assets.index');
Route::post('/resources', [ClusterController::class, 'resourceRecord'])->name('control-panel.kubernetes.resources.store');
Route::post('/assets', [ClusterController::class, 'asset'])->name('control-panel.kubernetes.assets.store');
Route::post('/nodes/{node}/cordon', [NodeController::class, 'cordon'])->name('control-panel.kubernetes.nodes.cordon');
Route::post('/nodes/{node}/uncordon', [NodeController::class, 'uncordon'])->name('control-panel.kubernetes.nodes.uncordon');
Route::post('/nodes/{node}/drain', [NodeController::class, 'drain'])->name('control-panel.kubernetes.nodes.drain');
Route::post('/nodes/{node}/label', [NodeController::class, 'label'])->name('control-panel.kubernetes.nodes.label');
Route::post('/nodes/{node}/unlabel', [NodeController::class, 'unlabel'])->name('control-panel.kubernetes.nodes.unlabel');
Route::post('{cluster}/suspend', [ClusterController::class, 'suspend'])->name('control-panel.kubernetes.suspend');
Route::post('{cluster}/archive', [ClusterController::class, 'archive'])->name('control-panel.kubernetes.archive');
Route::get('{cluster}', [ClusterController::class, 'show'])->name('control-panel.kubernetes.show');
```

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
