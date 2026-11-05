# liberusoftware/module-crm-work-management-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

CRM work management API presentation package

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-work-management-api](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-work-management-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-work-management-api` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-work-management-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\CRM\\WorkManagement\\Api\\WorkManagementApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\WorkManagement\\Api\\WorkManagementApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/module.json).

**Declared capabilities:** crm.work-management.api

**Declared features:** Work items, Queues, Checklists, Approvals, Dependencies, Workload, Personal and team views

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/api-access` | `^1.0` |
| `liberusoftware/module-crm-work-management` | `^1.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\CRM\\WorkManagement\\Api\\": "src/"}`.

Module resolver requirements: `{"capabilities": {"crm.work-management": "^1.0"}, "laravel": "^13.0", "packages": {"liberusoftware/api-access": "^1.0", "liberusoftware/module-crm-work-management": "^1.0", "liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/WorkManagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/src/Http/Controllers/WorkManagementController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateWorkItem $create, IdempotencyStore $idempotency): JsonResponse`<br>`public function show(Request $request, int $workItem): JsonResponse`<br>`public function update(Request $request, int $workItem, UpdateWorkItem $update): JsonResponse`<br>`public function complete(Request $request, int $workItem, CompleteWorkItem $complete, IdempotencyStore $idempotency): JsonResponse`<br>`public function checklist(Request $request, int $workItem, AddChecklistItem $add): JsonResponse`<br>`public function requestApproval(Request $request, int $workItem, ReviewApproval $approval, IdempotencyStore $idempotency): JsonResponse`<br>`public function dependency(Request $request, int $workItem, AddDependency $add): JsonResponse`<br>`public function queues(Request $request): JsonResponse`<br>`public function storeQueue(Request $request, CreateWorkQueue $create, IdempotencyStore $idempotency): JsonResponse`<br>`public function workload(Request $request, WorkloadQuery $workload): JsonResponse` |

Other non-legacy PHP sources: [src/WorkManagementApiServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/src/WorkManagementApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/crm-work-management.yaml](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/openapi/v1/crm-work-management.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
