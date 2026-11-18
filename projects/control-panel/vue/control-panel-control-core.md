# Control Panel: Control Panel Control Core Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-control-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-control-panel-control-panel-control-core-vue-inertia`
**Matching domain module:** `control-panel-control-core`
**Application:** Control Panel
**Source feature:** [Control Panel Control Core](../features/control-panel-control-core.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-control-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Nodes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Capabilities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Credentials:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Task engine:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Inventory:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Desired state:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Locks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Audit:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-control-panel-control-panel-control-core-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `nodes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `capabilities`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `credentials`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `task-engine`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `inventory`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `desired-state`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `locks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `audit`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-control-core` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-control-panel-laravel-inertia-vue`](https://github.com/liberusoftware/project-control-panel-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-control-panel-control-core-vue-inertia`](https://github.com/liberusoftware/module-control-panel-control-core-vue-inertia) (`@liberusoftware/module-control-panel-control-core-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/control-panel-control-core.md) · [Core plan](../core/control-panel-control-core.md) · [API plan](../api/control-panel-control-core.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Nodes** | Render `nodes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Capabilities** | Render `capabilities` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Credentials** | Render `credentials` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Task engine** | Render `task engine` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Inventory** | Render `inventory` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Desired state** | Render `desired state` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Locks** | Render `locks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Audit** | Render `audit` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
