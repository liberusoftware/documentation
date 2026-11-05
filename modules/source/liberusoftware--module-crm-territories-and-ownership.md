# liberusoftware/module-crm-territories-and-ownership: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-territories-and-ownership](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-territories-and-ownership`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-territories-and-ownership` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-territories-and-ownership` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\TerritoriesAndOwnership\\TerritoriesAndOwnershipServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\TerritoriesAndOwnership\\TerritoriesAndOwnershipServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/module.json).

**Declared capabilities:** crm.territories-and-ownership

**Declared features:** Territories, queues, routing, coverage and ownership history

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\TerritoriesAndOwnership\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AssignOwner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/AssignOwner.php) | `public function execute(int $teamId, int $actorId, string $subjectType, int $subjectId, ?int $previousOwnerId, int $ownerId, string $reason): OwnershipHistory` |
| [src/Actions/CreateCoverage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/CreateCoverage.php) | `public function execute(int $teamId, int $actorId, array $data): TerritoryCoverage` |
| [src/Actions/UpsertTerritoryRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/UpsertTerritoryRule.php) | `public function execute(int $teamId, int $actorId, array $data): TerritoryRule` |
| [src/Queries/TerritoryQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Queries/TerritoryQuery.php) | `public function rules(int $teamId): LengthAwarePaginator`<br>`public function history(int $teamId): LengthAwarePaginator` |
| [src/Services/TerritoryPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Services/TerritoryPolicy.php) | `public function canManage(int $teamId, int $userId): bool`<br>`public function isTeamMember(int $teamId, int $userId, array $roles = [], bool $includeOwner = false): bool` |

Other non-legacy PHP sources: [src/Models/OwnershipHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/OwnershipHistory.php) · [src/Models/TerritoryCoverage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/TerritoryCoverage.php) · [src/Models/TerritoryRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/TerritoryRule.php) · [src/TerritoriesAndOwnershipServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/TerritoriesAndOwnershipServiceProvider.php).

**Legacy review:** 1 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_060000_create_crm_territory_ownership_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/database/migrations/2026_08_25_060000_create_crm_territory_ownership_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
