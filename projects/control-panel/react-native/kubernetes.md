# Kubernetes React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#kubernetes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-kubernetes-react-native
**Matching core package:** module-control-panel-kubernetes ([implementation](../core/kubernetes.md))
**Matching API package:** module-control-panel-kubernetes-api ([contract](../api/kubernetes.md))

## Implementation plan

This adapter presents Kubernetes for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Kubernetes API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/kubernetes.md), and [API module](../api/kubernetes.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `kubernetes`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/kubernetes.md)) |
| Capability React Native module skeleton | [`module-control-panel-kubernetes-react-native`](https://github.com/liberusoftware/module-control-panel-kubernetes-react-native) (`@liberusoftware/module-control-panel-kubernetes-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Clusters** | Progressive mobile list/detail/sheet flow for `clusters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Nodes** | Progressive mobile list/detail/sheet flow for `nodes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Namespaces** | Progressive mobile list/detail/sheet flow for `namespaces` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **RBAC** | Progressive mobile list/detail/sheet flow for `rbac` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Workloads** | Progressive mobile list/detail/sheet flow for `workloads` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Ingress** | Progressive mobile list/detail/sheet flow for `ingress` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Helm** | Progressive mobile list/detail/sheet flow for `helm` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Storage** | Progressive mobile list/detail/sheet flow for `storage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Autoscaling** | Progressive mobile list/detail/sheet flow for `autoscaling` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Upgrades** | Progressive mobile list/detail/sheet flow for `upgrades` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Multi-cluster views** | Progressive mobile list/detail/sheet flow for `multi-cluster views` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
