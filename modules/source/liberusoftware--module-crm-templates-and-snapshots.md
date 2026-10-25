# liberusoftware/module-crm-templates-and-snapshots: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-templates-and-snapshots](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-templates-and-snapshots`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-templates-and-snapshots` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-templates-and-snapshots` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\TemplatesAndSnapshots\\TemplatesAndSnapshotsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\TemplatesAndSnapshots\\TemplatesAndSnapshotsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/module.json).

**Declared capabilities:** crm.templates-and-snapshots

**Declared features:** Versioned bundles, protected sharing, install, preview, update and rollback

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\TemplatesAndSnapshots\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateSnapshot.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/CreateSnapshot.php) | `public function execute(int $teamId, int $actorId, array $data): SnapshotBundle` |
| [src/Actions/InstallSnapshot.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/InstallSnapshot.php) | `public function execute(int $teamId, int $actorId, int $bundleId): SnapshotInstall` |
| [src/Actions/RollbackSnapshot.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/RollbackSnapshot.php) | `public function execute(int $teamId, int $actorId, int $bundleId, int $version): SnapshotInstall` |
| [src/Actions/ShareSnapshot.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/ShareSnapshot.php) | `public function execute(int $teamId, int $actorId, int $bundleId): string` |
| [src/Actions/UpdateSnapshot.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/UpdateSnapshot.php) | `public function execute(int $teamId, int $actorId, int $bundleId, array $data): SnapshotBundle` |
| [src/Queries/SnapshotQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Queries/SnapshotQuery.php) | `public function list(int $teamId)`<br>`public function find(int $teamId, int $id): SnapshotBundle`<br>`public function preview(int $teamId, int $id): array` |
| [src/Services/SnapshotAudit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Services/SnapshotAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [src/Services/SnapshotPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Services/SnapshotPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Models/SnapshotAudit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Models/SnapshotAudit.php) · [src/Models/SnapshotBundle.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Models/SnapshotBundle.php) · [src/Models/SnapshotInstall.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Models/SnapshotInstall.php) · [src/TemplatesAndSnapshotsServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/TemplatesAndSnapshotsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_070000_create_crm_template_snapshot_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/database/migrations/2026_08_25_070000_create_crm_template_snapshot_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
