# liberusoftware/real-estate-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral real-estate agencies, branches, and operational numbering.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-core](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: real-estate-laravel, `real-estate-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-core` |
| Composer version field | `1.0.1` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-core` |
| Module version field | `1.0.1` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\Core\\RealEstateCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/composer.json) · [module.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/module.json).

**Declared capabilities:** real-estate.core

**Declared features:** Agencies, Branches, Teams, Territories, Terminology, Statuses, Numbering, Audit, Communications, Calendar

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/validation` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\Core\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/AgencyPolicy.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/AgencyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Agency $agency): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Agency $agency): bool`<br>`public function delete(AuthUser $authUser, Agency $agency): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Agency $agency): bool`<br>`public function forceDelete(AuthUser $authUser, Agency $agency): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Agency $agency): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [src/Policies/BranchPolicy.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/BranchPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Branch $branch): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Branch $branch): bool`<br>`public function delete(AuthUser $authUser, Branch $branch): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Branch $branch): bool`<br>`public function forceDelete(AuthUser $authUser, Branch $branch): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Branch $branch): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [src/Policies/StatusDefinitionPolicy.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/StatusDefinitionPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function delete(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function forceDelete(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [src/Policies/TerritoryPolicy.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/TerritoryPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Territory $territory): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Territory $territory): bool`<br>`public function delete(AuthUser $authUser, Territory $territory): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Territory $territory): bool`<br>`public function forceDelete(AuthUser $authUser, Territory $territory): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Territory $territory): bool`<br>`public function reorder(AuthUser $authUser): bool` |

Other non-legacy PHP sources: [src/Application/CreateAgency.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/CreateAgency.php) · [src/Application/CreateBranch.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/CreateBranch.php) · [src/Application/CreateCalendarEntry.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/CreateCalendarEntry.php) · [src/Application/CreateTerritory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/CreateTerritory.php) · [src/Application/DefineStatus.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/DefineStatus.php) · [src/Application/DeleteAgency.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/DeleteAgency.php) · [src/Application/DeleteBranch.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/DeleteBranch.php) · [src/Application/DeleteTerritory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/DeleteTerritory.php) · [src/Application/NextNumber.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/NextNumber.php) · [src/Application/RecordAuditEntry.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/RecordAuditEntry.php) · [src/Application/RecordCommunication.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/RecordCommunication.php) · [src/Application/SetTerminology.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/SetTerminology.php) · [src/Application/UpdateAgency.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/UpdateAgency.php) · [src/Application/UpdateBranch.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/UpdateBranch.php) · [src/Application/UpdateTerritory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Application/UpdateTerritory.php) · [src/Domain/CoreCapabilityDefinition.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Domain/CoreCapabilityDefinition.php) · [src/Models/Agency.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Agency.php) · [src/Models/AuditEntry.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/AuditEntry.php) · [src/Models/Branch.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Branch.php) · [src/Models/CalendarEntry.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/CalendarEntry.php) · [src/Models/Communication.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Communication.php) · [src/Models/NumberSequence.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/NumberSequence.php) · [src/Models/StatusDefinition.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/StatusDefinition.php) · [src/Models/Terminology.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Terminology.php) · [src/Models/Territory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Territory.php) · [src/RealEstateCoreServiceProvider.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/RealEstateCoreServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000003_create_real_estate_branches_table.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/database/migrations/2026_08_23_000003_create_real_estate_branches_table.php)
- [database/migrations/2026_08_24_000002_create_real_estate_agencies_and_territories.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/database/migrations/2026_08_24_000002_create_real_estate_agencies_and_territories.php)
- [database/migrations/2026_08_25_000001_create_real_estate_number_sequences_table.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/database/migrations/2026_08_25_000001_create_real_estate_number_sequences_table.php)
- [database/migrations/2026_08_25_000002_create_real_estate_configuration_tables.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/database/migrations/2026_08_25_000002_create_real_estate_configuration_tables.php)
- [database/migrations/2026_08_30_000013_create_real_estate_communications.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/database/migrations/2026_08_30_000013_create_real_estate_communications.php)
- [database/migrations/2026_08_30_000014_create_real_estate_calendar_entries.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/database/migrations/2026_08_30_000014_create_real_estate_calendar_entries.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
