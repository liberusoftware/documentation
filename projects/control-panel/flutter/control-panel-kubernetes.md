# Control Panel Kubernetes Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-kubernetes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-kubernetes-flutter
**Matching core package:** module-control-panel-control-panel-kubernetes ([implementation](../core/control-panel-kubernetes.md))
**Matching API package:** module-control-panel-control-panel-kubernetes-api ([contract](../api/control-panel-kubernetes.md))

## Implementation plan

This adapter presents Control Panel Kubernetes for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Kubernetes API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/control-panel-kubernetes.md), and [API module](../api/control-panel-kubernetes.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `control-panel-kubernetes`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-kubernetes-flutter`](https://github.com/liberusoftware/module-control-panel-kubernetes-flutter) (`module_control_panel_kubernetes_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-kubernetes-dart-mobile`](https://github.com/liberusoftware/module-control-panel-kubernetes-dart-mobile) (`module_control_panel_kubernetes_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-kubernetes-dart-desktop`](https://github.com/liberusoftware/module-control-panel-kubernetes-dart-desktop) (`module_control_panel_kubernetes_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/control-panel-kubernetes.md) · [Core plan](../core/control-panel-kubernetes.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Clusters** | Adaptive mobile cards/sheets for `clusters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `clusters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Nodes** | Adaptive mobile cards/sheets for `nodes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `nodes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Namespaces** | Adaptive mobile cards/sheets for `namespaces` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `namespaces` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **RBAC** | Adaptive mobile cards/sheets for `rbac` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rbac` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Workloads** | Adaptive mobile cards/sheets for `workloads` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `workloads` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Ingress** | Adaptive mobile cards/sheets for `ingress` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `ingress` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Helm** | Adaptive mobile cards/sheets for `helm` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `helm` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Storage** | Adaptive mobile cards/sheets for `storage` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `storage` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Autoscaling** | Adaptive mobile cards/sheets for `autoscaling` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `autoscaling` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Upgrades** | Adaptive mobile cards/sheets for `upgrades` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `upgrades` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Multi-cluster views** | Adaptive mobile cards/sheets for `multi-cluster views` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `multi-cluster views` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [ClusterController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-api/src/Http/Controllers/ClusterController.php) | `public function index(Request $request, ListClusters $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function assets(Request $request): JsonResponse`<br>`public function store(Request $request, RegisterCluster $register): JsonResponse`<br>`public function suspend(Request $request, Cluster $cluster, SuspendCluster $suspend): JsonResponse`<br>`public function archive(Request $request, Cluster $cluster, ArchiveCluster $archive): JsonResponse`<br>`public function resourceRecord(Request $request, RecordKubernetesResource $record): JsonResponse`<br>`public function asset(Request $request, RegisterKubernetesAsset $register): JsonResponse` |
| [NodeController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-kubernetes-api/src/Http/Controllers/NodeController.php) | `public function cordon(Request $request, string $node, CordonNode $cordon): JsonResponse`<br>`public function uncordon(Request $request, string $node, UncordonNode $uncordon): JsonResponse`<br>`public function drain(Request $request, string $node, DrainNode $drain): JsonResponse`<br>`public function label(Request $request, string $node, LabelNode $label): JsonResponse`<br>`public function unlabel(Request $request, string $node, UnlabelNode $unlabel): JsonResponse` |

**Observed route declarations:**

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
<!-- layer-implementation-plan:end -->
