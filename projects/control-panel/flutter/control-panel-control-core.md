# Control Panel Control Core Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-control-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-control-core-flutter
**Matching core package:** module-control-panel-control-panel-control-core ([implementation](../core/control-panel-control-core.md))
**Matching API package:** module-control-panel-control-panel-control-core-api ([contract](../api/control-panel-control-core.md))

## Implementation plan

This adapter presents Control Panel Control Core for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Control Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/control-panel-control-core.md), and [API module](../api/control-panel-control-core.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `control-panel-control-core`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-control-core-flutter`](https://github.com/liberusoftware/module-control-panel-control-core-flutter) (`module_control_panel_control_core_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-control-core-dart-mobile`](https://github.com/liberusoftware/module-control-panel-control-core-dart-mobile) (`module_control_panel_control_core_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-control-core-dart-desktop`](https://github.com/liberusoftware/module-control-panel-control-core-dart-desktop) (`module_control_panel_control_core_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/control-panel-control-core.md) · [Core plan](../core/control-panel-control-core.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Nodes** | Adaptive mobile cards/sheets for `nodes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `nodes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Capabilities** | Adaptive mobile cards/sheets for `capabilities` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `capabilities` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Credentials** | Adaptive mobile cards/sheets for `credentials` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `credentials` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Task engine** | Adaptive mobile cards/sheets for `task engine` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `task engine` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Inventory** | Adaptive mobile cards/sheets for `inventory` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `inventory` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Desired state** | Adaptive mobile cards/sheets for `desired state` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `desired state` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Locks** | Adaptive mobile cards/sheets for `locks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `locks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Audit** | Adaptive mobile cards/sheets for `audit` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `audit` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListAuditEntries.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Queries/ListAuditEntries.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Queries/ListInventory.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListNodes.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Queries/ListNodes.php) | `public function execute(?string $teamId = null, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListOperationTasks.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Queries/ListOperationTasks.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcquireOperationLock.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/AcquireOperationLock.php) | `public function execute(string\|int $teamId, string $nodeId, string $operationKey, string $owner, int $ttlSeconds = 300): OperationLock` |
| [CancelOperationTask.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/CancelOperationTask.php) | `public function __construct(private TransitionOperationTask $transition)`<br>`public function execute(OperationTask $task): OperationTask` |
| [ChangeNodeStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/ChangeNodeStatus.php) | `public function execute(Node $node, NodeStatus $status): Node` |
| [CreateOperationTask.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/CreateOperationTask.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): OperationTask` |
| [DecommissionNode.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/DecommissionNode.php) | `public function execute(Node $node): Node` |
| [ExpireNodeCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/ExpireNodeCredential.php) | `public function execute(NodeCredential $credential): NodeCredential` |
| [GenerateSshKeyPair.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/GenerateSshKeyPair.php) | `public function execute(?string $passphrase = null, int $bits = 4096, ?string $comment = null): array` |
| [RecordInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RecordInventory.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): InventoryRecord` |
| [RecordOperationTaskCompensation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RecordOperationTaskCompensation.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(OperationTask $task, CompensationStatus $status, ?array $result = null, ?string $error = null): OperationTask` |
| [RecordOperationTaskStep.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RecordOperationTaskStep.php) | `public function execute(OperationTask $task, array $attributes): OperationTaskStep` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AuditEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/AuditEntry.php) | `team_id`, `actor_id`, `event`, `subject_type`, `subject_id`, `context` |
| [InventoryRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/InventoryRecord.php) | `team_id`, `node_id`, `kind`, `record_key`, `value`, `observed_at` |
| [Node.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/Node.php) | `team_id`, `name`, `hostname`, `platform`, `status`, `credentials`, `desired_state`, `observed_state`, `last_seen_at` |
| [NodeCapability.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/NodeCapability.php) | `node_id`, `name`, `version`, `metadata` |
| [NodeCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/NodeCredential.php) | `id`, `team_id`, `node_id`, `name`, `type`, `username`, `secret`, `public_key`, `status`, `expires_at`, `last_used_at`, `metadata` |
| [OperationLock.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/OperationLock.php) | `team_id`, `node_id`, `operation_key`, `owner`, `expires_at` |
| [OperationTask.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/OperationTask.php) | `team_id`, `node_id`, `operation`, `idempotency_key`, `status`, `payload`, `result`, `error`, `attempts`, `available_at`, `timeout_at`, `finished_at`, `compensation_status`, `compensation_result`, `compensation_error`, `compensation_started_at`, `compensation_finished_at` |
| [OperationTaskStep.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/OperationTaskStep.php) | `task_id`, `step_key`, `name`, `status`, `input`, `result`, `error`, `attempts`, `started_at`, `finished_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AuditController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/AuditController.php) | `public function index(Request $request, ListAuditEntries $entries): JsonResponse` |
| [InventoryController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/InventoryController.php) | `public function index(Request $request, ListInventory $inventory): JsonResponse`<br>`public function store(Request $request, RecordInventory $record): JsonResponse` |
| [NodeController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/NodeController.php) | `public function show(Request $request, string $node): JsonResponse`<br>`public function index(Request $request, ListNodes $nodes): JsonResponse`<br>`public function store(Request $request, RegisterNode $register): JsonResponse`<br>`public function updateDesiredState(Request $request, string $node, UpdateDesiredState $update): JsonResponse`<br>`public function updateStatus(Request $request, string $node, ChangeNodeStatus $change): JsonResponse`<br>`public function decommission(Request $request, string $node, DecommissionNode $decommission): JsonResponse`<br>`public function capabilities(Request $request, string $node, SyncNodeCapabilities $sync): JsonResponse`<br>`public function credential(Request $request, string $node, RegisterNodeCredential $register): JsonResponse`<br>`public function generateKeyPair(Request $request, GenerateSshKeyPair $generate): JsonResponse`<br>`public function deploySshKey(Request $request, string $node, RequestSshOperation $requestOperation): JsonResponse`<br>`public function testSshConnection(Request $request, string $node, RequestSshOperation $requestOperation): JsonResponse`<br>`public function revokeCredential(Request $request, string $credential, RevokeNodeCredential $revoke): JsonResponse`<br>`public function updateCredential(Request $request, string $credential, UpdateNodeCredential $update): JsonResponse`<br>`public function expireCredential(Request $request, string $credential, ExpireNodeCredential $expire): JsonResponse` |
| [OperationLockController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/OperationLockController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, AcquireOperationLock $acquire): JsonResponse`<br>`public function destroy(Request $request, string $lock, ReleaseOperationLock $release): JsonResponse` |
| [OperationTaskController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/OperationTaskController.php) | `public function index(Request $request, ListOperationTasks $tasks): JsonResponse`<br>`public function store(Request $request, CreateOperationTask $create): JsonResponse`<br>`public function transition(Request $request, string $task, TransitionOperationTask $transition): JsonResponse`<br>`public function retry(Request $request, string $task, RetryOperationTask $retry): JsonResponse`<br>`public function cancel(Request $request, string $task, CancelOperationTask $cancel): JsonResponse`<br>`public function timeout(Request $request, string $task, TimeoutOperationTask $timeout): JsonResponse`<br>`public function compensation(Request $request, string $task, RecordOperationTaskCompensation $record): JsonResponse`<br>`public function steps(Request $request, string $task): JsonResponse`<br>`public function recordStep(Request $request, string $task, RecordOperationTaskStep $record): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-control-core-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/control-core')
Route::get('nodes', [NodeController::class, 'index'])->name('control-panel.control-core.nodes.index');
Route::post('nodes', [NodeController::class, 'store'])->name('control-panel.control-core.nodes.store');
Route::get('nodes/{node}', [NodeController::class, 'show'])->name('control-panel.control-core.nodes.show');
Route::patch('nodes/{node}/desired-state', [NodeController::class, 'updateDesiredState'])->name('control-panel.control-core.nodes.desired-state');
Route::patch('nodes/{node}/status', [NodeController::class, 'updateStatus'])->name('control-panel.control-core.nodes.status');
Route::post('nodes/{node}/decommission', [NodeController::class, 'decommission'])->name('control-panel.control-core.nodes.decommission');
Route::put('nodes/{node}/capabilities', [NodeController::class, 'capabilities'])->name('control-panel.control-core.nodes.capabilities');
Route::post('nodes/{node}/credentials', [NodeController::class, 'credential'])->name('control-panel.control-core.nodes.credentials.store');
Route::post('nodes/{node}/ssh/deploy-key', [NodeController::class, 'deploySshKey'])->name('control-panel.control-core.nodes.ssh.deploy-key');
Route::post('nodes/{node}/ssh/test-connection', [NodeController::class, 'testSshConnection'])->name('control-panel.control-core.nodes.ssh.test-connection');
Route::post('credentials/generate-key-pair', [NodeController::class, 'generateKeyPair'])->name('control-panel.control-core.credentials.generate-key-pair');
Route::post('credentials/{credential}/revoke', [NodeController::class, 'revokeCredential'])->name('control-panel.control-core.credentials.revoke');
Route::patch('credentials/{credential}', [NodeController::class, 'updateCredential'])->name('control-panel.control-core.credentials.update');
Route::post('credentials/{credential}/expire', [NodeController::class, 'expireCredential'])->name('control-panel.control-core.credentials.expire');
Route::get('tasks', [OperationTaskController::class, 'index'])->name('control-panel.control-core.tasks.index');
Route::post('tasks', [OperationTaskController::class, 'store'])->name('control-panel.control-core.tasks.store');
Route::post('tasks/{task}/transition', [OperationTaskController::class, 'transition'])->name('control-panel.control-core.tasks.transition');
Route::post('tasks/{task}/cancel', [OperationTaskController::class, 'cancel'])->name('control-panel.control-core.tasks.cancel');
Route::post('tasks/{task}/timeout', [OperationTaskController::class, 'timeout'])->name('control-panel.control-core.tasks.timeout');
Route::post('tasks/{task}/compensation', [OperationTaskController::class, 'compensation'])->name('control-panel.control-core.tasks.compensation');
Route::get('tasks/{task}/steps', [OperationTaskController::class, 'steps'])->name('control-panel.control-core.tasks.steps.index');
Route::post('tasks/{task}/steps', [OperationTaskController::class, 'recordStep'])->name('control-panel.control-core.tasks.steps.store');
Route::post('tasks/{task}/retry', [OperationTaskController::class, 'retry'])->name('control-panel.control-core.tasks.retry');
Route::get('inventory', [InventoryController::class, 'index'])->name('control-panel.control-core.inventory.index');
Route::post('inventory', [InventoryController::class, 'store'])->name('control-panel.control-core.inventory.store');
Route::get('audit', [AuditController::class, 'index'])->name('control-panel.control-core.audit.index');
Route::get('locks', [OperationLockController::class, 'index'])->name('control-panel.control-core.locks.index');
Route::post('locks', [OperationLockController::class, 'store'])->name('control-panel.control-core.locks.store');
Route::delete('locks/{lock}', [OperationLockController::class, 'destroy'])->name('control-panel.control-core.locks.destroy');
```
<!-- layer-implementation-plan:end -->
