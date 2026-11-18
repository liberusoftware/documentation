# Control Panel: Control Panel Control Core Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-control-core). Observed identity: [`liberusoftware/module-control-panel-control-core-livewire`](../../../modules/source/liberusoftware--module-control-panel-control-core-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-control-panel-control-panel-control-core-livewire`  
**Matching domain module:** `control-panel-control-core`  
**Application:** Control Panel  
**Source feature:** [Control Panel Control Core](../features/control-panel-control-core.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Nodes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Capabilities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Credentials:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Task engine:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inventory:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Desired state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Locks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Audit:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-control-panel-control-panel-control-core-livewire` component namespace and service provider; use explicit aliases such as `<livewire:controlpanelControlPanelControlCore::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `nodes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `capabilities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `credentials`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `task-engine`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inventory`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `desired-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `locks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `audit`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `control-panel-control-core` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/control-panel-control-core.md) · [API plan](../api/control-panel-control-core.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Nodes** | Expose a focused Livewire 4 component and namespaced Blade default view for `nodes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Capabilities** | Expose a focused Livewire 4 component and namespaced Blade default view for `capabilities` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Credentials** | Expose a focused Livewire 4 component and namespaced Blade default view for `credentials` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Task engine** | Expose a focused Livewire 4 component and namespaced Blade default view for `task engine` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inventory** | Expose a focused Livewire 4 component and namespaced Blade default view for `inventory` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Desired state** | Expose a focused Livewire 4 component and namespaced Blade default view for `desired state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Locks** | Expose a focused Livewire 4 component and namespaced Blade default view for `locks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Audit** | Expose a focused Livewire 4 component and namespaced Blade default view for `audit` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CredentialInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-livewire/src/Components/CredentialInventory.php) · [NodeInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-livewire/src/Components/NodeInventory.php) · [OperationsInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-livewire/src/Components/OperationsInventory.php) · [ControlCoreLivewireServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-livewire/src/ControlCoreLivewireServiceProvider.php).

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
<!-- layer-implementation-plan:end -->
