# liberusoftware/module-control-panel-control-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Control Panel nodes, capabilities, credentials, inventory and operation coordination.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-control-core](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-control-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-control-core` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-control-core` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\ControlCore\\ControlCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/module.json).

**Declared capabilities:** control-panel.control-core

**Declared features:** Node lifecycle, Capability inventory, Encrypted node credentials, SSH key deployment and connection-test operations, Task engine with cancellation, durable step logs, timeout handling, compensation, and retry recovery, Inventory records, Desired and observed state, Idempotent operation locks, Audit records

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `phpseclib/phpseclib` | `^3.0` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\ControlCore\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AcquireOperationLock.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/AcquireOperationLock.php) | `public function execute(string\|int $teamId, string $nodeId, string $operationKey, string $owner, int $ttlSeconds = 300): OperationLock` |
| [src/Actions/CancelOperationTask.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/CancelOperationTask.php) | `public function __construct(private TransitionOperationTask $transition)`<br>`public function execute(OperationTask $task): OperationTask` |
| [src/Actions/ChangeNodeStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/ChangeNodeStatus.php) | `public function execute(Node $node, NodeStatus $status): Node` |
| [src/Actions/CreateOperationTask.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/CreateOperationTask.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): OperationTask` |
| [src/Actions/DecommissionNode.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/DecommissionNode.php) | `public function execute(Node $node): Node` |
| [src/Actions/ExpireNodeCredential.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/ExpireNodeCredential.php) | `public function execute(NodeCredential $credential): NodeCredential` |
| [src/Actions/GenerateSshKeyPair.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/GenerateSshKeyPair.php) | `public function execute(?string $passphrase = null, int $bits = 4096, ?string $comment = null): array` |
| [src/Actions/RecordInventory.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RecordInventory.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): InventoryRecord` |
| [src/Actions/RecordOperationTaskCompensation.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RecordOperationTaskCompensation.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(OperationTask $task, CompensationStatus $status, ?array $result = null, ?string $error = null): OperationTask` |
| [src/Actions/RecordOperationTaskStep.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RecordOperationTaskStep.php) | `public function execute(OperationTask $task, array $attributes): OperationTaskStep` |
| [src/Actions/RegisterNode.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RegisterNode.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Node` |
| [src/Actions/RegisterNodeCredential.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RegisterNodeCredential.php) | `public function execute(array $attributes): NodeCredential` |
| [src/Actions/ReleaseOperationLock.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/ReleaseOperationLock.php) | `public function execute(OperationLock $lock, string $owner): void` |
| [src/Actions/RequestSshOperation.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RequestSshOperation.php) | `public function __construct(private CreateOperationTask $createTask)`<br>`public function execute(string $teamId, string $nodeId, string $operation, string $idempotencyKey, array $payload = []): OperationTask` |
| [src/Actions/RetryOperationTask.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RetryOperationTask.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(OperationTask $task): OperationTask` |
| [src/Actions/RevokeNodeCredential.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/RevokeNodeCredential.php) | `public function execute(NodeCredential $credential): NodeCredential` |
| [src/Actions/SyncNodeCapabilities.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/SyncNodeCapabilities.php) | `public function execute(Node $node, array $capabilities): Node` |
| [src/Actions/TimeoutOperationTask.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/TimeoutOperationTask.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(OperationTask $task): OperationTask` |
| [src/Actions/TransitionOperationTask.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/TransitionOperationTask.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(OperationTask $task, TaskStatus $status, ?array $result = null, ?string $error = null): OperationTask` |
| [src/Actions/UpdateDesiredState.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/UpdateDesiredState.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(Node $node, array $state): Node` |
| [src/Actions/UpdateNodeCredential.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/UpdateNodeCredential.php) | `public function execute(NodeCredential $credential, array $attributes): NodeCredential` |
| [src/Actions/WriteAuditEntry.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Actions/WriteAuditEntry.php) | `public function execute(string $event, ?string $teamId, ?string $actorId, string $subjectType, string $subjectId, array $context = []): AuditEntry` |
| [src/Queries/ListAuditEntries.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Queries/ListAuditEntries.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Queries/ListInventory.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Queries/ListInventory.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Queries/ListNodes.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Queries/ListNodes.php) | `public function execute(?string $teamId = null, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [src/Queries/ListOperationTasks.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Queries/ListOperationTasks.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/ControlCoreServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/ControlCoreServiceProvider.php) · [src/Enums/CompensationStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/CompensationStatus.php) · [src/Enums/CredentialStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/CredentialStatus.php) · [src/Enums/NodeStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/NodeStatus.php) · [src/Enums/TaskStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/TaskStatus.php) · [src/Enums/TaskStepStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/TaskStepStatus.php) · [src/Events/DesiredStateUpdated.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Events/DesiredStateUpdated.php) · [src/Events/InventoryRecorded.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Events/InventoryRecorded.php) · [src/Events/NodeRegistered.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Events/NodeRegistered.php) · [src/Events/OperationTaskCompensationTransitioned.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Events/OperationTaskCompensationTransitioned.php) · [src/Events/OperationTaskCreated.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Events/OperationTaskCreated.php) · [src/Events/OperationTaskTransitioned.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Events/OperationTaskTransitioned.php) · [src/Exceptions/IdempotencyConflict.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Exceptions/IdempotencyConflict.php) · [src/Models/AuditEntry.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/AuditEntry.php) · [src/Models/InventoryRecord.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/InventoryRecord.php) · [src/Models/Node.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/Node.php) · [src/Models/NodeCapability.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/NodeCapability.php) · [src/Models/NodeCredential.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/NodeCredential.php) · [src/Models/OperationLock.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/OperationLock.php) · [src/Models/OperationTask.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/OperationTask.php) · [src/Models/OperationTaskStep.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Models/OperationTaskStep.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000000_create_control_panel_control_core_tables.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/database/migrations/2026_08_23_000000_create_control_panel_control_core_tables.php)
- [database/migrations/2026_08_24_000001_create_control_panel_operation_tables.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/database/migrations/2026_08_24_000001_create_control_panel_operation_tables.php)
- [database/migrations/2026_08_24_000002_create_control_panel_audit_entries.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/database/migrations/2026_08_24_000002_create_control_panel_audit_entries.php)
- [database/migrations/2026_08_24_150001_create_control_panel_node_credentials.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/database/migrations/2026_08_24_150001_create_control_panel_node_credentials.php)
- [database/migrations/2026_08_30_000008_create_control_panel_operation_task_steps.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/database/migrations/2026_08_30_000008_create_control_panel_operation_task_steps.php)
- [database/migrations/2026_08_30_000009_add_timeout_to_control_panel_operation_tasks.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/database/migrations/2026_08_30_000009_add_timeout_to_control_panel_operation_tasks.php)
- [database/migrations/2026_08_30_000010_add_compensation_to_control_panel_operation_tasks.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/database/migrations/2026_08_30_000010_add_compensation_to_control_panel_operation_tasks.php)

[src/Enums/CompensationStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/CompensationStatus.php): `NotRequired = 'not_required'`, `Pending = 'pending'`, `Running = 'running'`, `Succeeded = 'succeeded'`, `Failed = 'failed'`.

[src/Enums/CredentialStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/CredentialStatus.php): `Active = 'active'`, `Revoked = 'revoked'`, `Expired = 'expired'`.

[src/Enums/NodeStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/NodeStatus.php): `Pending = 'pending'`, `Active = 'active'`, `Draining = 'draining'`, `Suspended = 'suspended'`, `Decommissioned = 'decommissioned'`.

[src/Enums/TaskStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/TaskStatus.php): `Pending = 'pending'`, `Running = 'running'`, `Succeeded = 'succeeded'`, `Failed = 'failed'`, `Cancelled = 'cancelled'`.

[src/Enums/TaskStepStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core/src/Enums/TaskStepStatus.php): `Pending = 'pending'`, `Running = 'running'`, `Succeeded = 'succeeded'`, `Failed = 'failed'`, `Cancelled = 'cancelled'`.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
