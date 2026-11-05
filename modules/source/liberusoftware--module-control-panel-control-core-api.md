# liberusoftware/module-control-panel-control-core-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Authenticated API adapter for Control Panel Control Core.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-control-core-api](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-control-core-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-control-core-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-control-core-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\ControlCoreApi\\ControlCoreApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/module.json).

**Declared capabilities:** control-panel.control-core.api

**Declared features:** Node lifecycle, Capability inventory, Credential lifecycle, SSH key deployment and connection-test operations, Task engine, Task cancellation, timeout handling, compensation, and idempotent retry recovery, Inventory records, Desired and observed state, Operation locks, Audit records

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-control-panel-control-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\ControlCoreApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-control-panel-control-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/AuditController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/AuditController.php) | `public function index(Request $request, ListAuditEntries $entries): JsonResponse` |
| [src/Http/Controllers/InventoryController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/InventoryController.php) | `public function index(Request $request, ListInventory $inventory): JsonResponse`<br>`public function store(Request $request, RecordInventory $record): JsonResponse` |
| [src/Http/Controllers/NodeController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/NodeController.php) | `public function show(Request $request, string $node): JsonResponse`<br>`public function index(Request $request, ListNodes $nodes): JsonResponse`<br>`public function store(Request $request, RegisterNode $register): JsonResponse`<br>`public function updateDesiredState(Request $request, string $node, UpdateDesiredState $update): JsonResponse`<br>`public function updateStatus(Request $request, string $node, ChangeNodeStatus $change): JsonResponse`<br>`public function decommission(Request $request, string $node, DecommissionNode $decommission): JsonResponse`<br>`public function capabilities(Request $request, string $node, SyncNodeCapabilities $sync): JsonResponse`<br>`public function credential(Request $request, string $node, RegisterNodeCredential $register): JsonResponse`<br>`public function generateKeyPair(Request $request, GenerateSshKeyPair $generate): JsonResponse`<br>`public function deploySshKey(Request $request, string $node, RequestSshOperation $requestOperation): JsonResponse`<br>`public function testSshConnection(Request $request, string $node, RequestSshOperation $requestOperation): JsonResponse`<br>`public function revokeCredential(Request $request, string $credential, RevokeNodeCredential $revoke): JsonResponse`<br>`public function updateCredential(Request $request, string $credential, UpdateNodeCredential $update): JsonResponse`<br>`public function expireCredential(Request $request, string $credential, ExpireNodeCredential $expire): JsonResponse` |
| [src/Http/Controllers/OperationLockController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/OperationLockController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, AcquireOperationLock $acquire): JsonResponse`<br>`public function destroy(Request $request, string $lock, ReleaseOperationLock $release): JsonResponse` |
| [src/Http/Controllers/OperationTaskController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/OperationTaskController.php) | `public function index(Request $request, ListOperationTasks $tasks): JsonResponse`<br>`public function store(Request $request, CreateOperationTask $create): JsonResponse`<br>`public function transition(Request $request, string $task, TransitionOperationTask $transition): JsonResponse`<br>`public function retry(Request $request, string $task, RetryOperationTask $retry): JsonResponse`<br>`public function cancel(Request $request, string $task, CancelOperationTask $cancel): JsonResponse`<br>`public function timeout(Request $request, string $task, TimeoutOperationTask $timeout): JsonResponse`<br>`public function compensation(Request $request, string $task, RecordOperationTaskCompensation $record): JsonResponse`<br>`public function steps(Request $request, string $task): JsonResponse`<br>`public function recordStep(Request $request, string $task, RecordOperationTaskStep $record): JsonResponse` |

Other non-legacy PHP sources: [src/ControlCoreApiServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/ControlCoreApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/control-panel-control-core.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/openapi/v1/control-panel-control-core.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
