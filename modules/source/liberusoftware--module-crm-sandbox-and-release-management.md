# liberusoftware/module-crm-sandbox-and-release-management: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-sandbox-and-release-management](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-sandbox-and-release-management`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-sandbox-and-release-management` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-sandbox-and-release-management` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\SandboxAndReleaseManagement\\SandboxAndReleaseManagementServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\SandboxAndReleaseManagement\\SandboxAndReleaseManagementServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/module.json).

**Declared capabilities:** crm.sandbox-and-release-management

**Declared features:** Configuration snapshots and test data policy, Change sets, validation and dependency analysis, Promotion, rollback and environment comparison

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\SandboxAndReleaseManagement\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateChangeset.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseChangeset` |
| [src/Actions/CreateSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateSnapshot.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseSnapshot` |
| [src/Actions/PromoteChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/PromoteChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [src/Actions/RollbackChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/RollbackChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [src/Actions/ValidateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/ValidateChangeset.php) | `public function execute(int $teamId, int $actorId, int $id): ReleaseChangeset` |
| [src/Queries/ReleaseQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Queries/ReleaseQuery.php) | `public function snapshots(int $teamId)`<br>`public function changesets(int $teamId)`<br>`public function deployments(int $teamId)` |
| [src/Services/ReleaseAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleaseAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [src/Services/ReleasePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleasePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/ReleasePromoted.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Events/ReleasePromoted.php) · [src/Models/ReleaseChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseChangeset.php) · [src/Models/ReleaseDeployment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseDeployment.php) · [src/Models/ReleaseSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseSnapshot.php) · [src/SandboxAndReleaseManagementServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/SandboxAndReleaseManagementServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_140000_create_crm_sandbox_release_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/database/migrations/2026_08_25_140000_create_crm_sandbox_release_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
