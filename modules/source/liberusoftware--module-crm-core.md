# liberusoftware/module-crm-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

CRM Core customer records, relationships, notes, tags, favorites, attachments, and timeline.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-core](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-core` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `crm-core` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\Core\\CRMCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/module.json).

**Declared capabilities:** crm.core.records, crm.core.timeline

**Declared features:** Contacts, Organizations, Households, Relationships, Owners, Teams, Tags, Notes, Attachments, Favorites, Record lifecycle, Unified timeline

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\CRM\\Core\\": "src/"}`.

Module resolver requirements: `{"capabilities": {"foundation.teams": "^1.0"}, "laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddNote.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/AddNote.php) | `public function execute(Record $record, string $body, ?int $authorId = null): Note` |
| [src/Actions/ArchiveRecord.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/ArchiveRecord.php) | `public function execute(Record $record): Record` |
| [src/Actions/CreateRecord.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateRecord.php) | `public function execute(string $type, int $teamId, string $name, array $data = [], ?int $ownerId = null): Record` |
| [src/Actions/CreateRelationship.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateRelationship.php) | `public function execute(Record $from, Record $to, string $type, array $metadata = []): Relationship` |
| [src/Actions/CreateTag.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateTag.php) | `public function execute(int $teamId, string $name): Tag` |
| [src/Actions/TagRecord.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/TagRecord.php) | `public function execute(Record $record, Tag $tag): void` |
| [src/Actions/ToggleFavorite.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/ToggleFavorite.php) | `public function execute(Model $record, int $teamId, int $userId): bool` |
| [src/Actions/UpdateRecord.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/UpdateRecord.php) | `public function execute(Record $record, array $attributes): Record` |
| [src/Contracts/RecordRepository.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Contracts/RecordRepository.php) | `public function find(string $type, int\|string $id): ?Record`<br>`public function paginate(string $type, int $perPage = 25): LengthAwarePaginator` |
| [src/Services/EloquentRecordRepository.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Services/EloquentRecordRepository.php) | `public function find(string $type, int\|string $id): ?Record`<br>`public function paginate(string $type, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/CRMCoreServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/CRMCoreServiceProvider.php) · [src/Enums/RecordType.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Enums/RecordType.php) · [src/Models/Attachment.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Attachment.php) · [src/Models/Contact.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Contact.php) · [src/Models/Favorite.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Favorite.php) · [src/Models/Household.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Household.php) · [src/Models/Note.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Note.php) · [src/Models/Organization.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Organization.php) · [src/Models/Record.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Record.php) · [src/Models/Relationship.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Relationship.php) · [src/Models/Tag.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Tag.php) · [src/Models/TimelineEntry.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/TimelineEntry.php).

**Legacy review:** 66 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2020_06_30_135250_create_activations_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2020_06_30_135250_create_activations_table.php)
- [database/migrations/2022_10_30_150853_create_companies_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2022_10_30_150853_create_companies_table.php)
- [database/migrations/2023_01_20_000003_update_companies_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_01_20_000003_update_companies_table.php)
- [database/migrations/2023_01_31_124707_create_contacts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_01_31_124707_create_contacts_table.php)
- [database/migrations/2023_05_20_000000_enhance_crm_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_05_20_000000_enhance_crm_tables.php)
- [database/migrations/2023_05_24_create_lead_forms_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_05_24_create_lead_forms_table.php)
- [database/migrations/2023_05_25_000000_create_custom_fields_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_05_25_000000_create_custom_fields_table.php)
- [database/migrations/2023_05_25_000001_add_contacts_email_index.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_05_25_000001_add_contacts_email_index.php)
- [database/migrations/2023_05_25_000001_add_custom_fields_to_contacts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_05_25_000001_add_custom_fields_to_contacts_table.php)
- [database/migrations/2023_05_25_000002_add_custom_fields_to_leads_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_05_25_000002_add_custom_fields_to_leads_table.php)
- [database/migrations/2023_06_01_000000_create_leads_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_06_01_000000_create_leads_table.php)
- [database/migrations/2023_10_31_125000_create_opportunities_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_10_31_125000_create_opportunities_table.php)
- [database/migrations/2023_10_31_125013_create_notes_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2023_10_31_125013_create_notes_table.php)
- [database/migrations/2024_05_20_000001_update_contacts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2024_05_20_000001_update_contacts_table.php)
- [database/migrations/2024_10_20_000000_enhance_crm_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2024_10_20_000000_enhance_crm_tables.php)
- [database/migrations/2026_03_03_000000_add_company_id_and_custom_fields_to_contacts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_03_03_000000_add_company_id_and_custom_fields_to_contacts_table.php)
- [database/migrations/2026_03_07_000001_add_missing_columns_to_custom_fields_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_03_07_000001_add_missing_columns_to_custom_fields_table.php)
- [database/migrations/2026_03_07_000003_add_missing_columns_to_lead_forms_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_03_07_000003_add_missing_columns_to_lead_forms_table.php)
- [database/migrations/2026_03_07_000004_fix_nullable_columns.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_03_07_000004_fix_nullable_columns.php)
- [database/migrations/2026_03_08_000001_change_company_size_to_string_in_contacts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_03_08_000001_change_company_size_to_string_in_contacts_table.php)
- [database/migrations/2026_07_06_140000_create_tags_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_07_06_140000_create_tags_table.php)
- [database/migrations/2026_07_06_160000_add_annual_revenue_to_companies_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_07_06_160000_add_annual_revenue_to_companies_table.php)
- [database/migrations/2026_07_06_170000_add_notes_to_call_logs_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_07_06_170000_add_notes_to_call_logs_table.php)
- [database/migrations/2026_07_08_040000_add_territory_id_to_contacts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_07_08_040000_add_territory_id_to_contacts_table.php)
- [database/migrations/2026_07_10_040000_encrypt_contact_email.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_07_10_040000_encrypt_contact_email.php)
- [database/migrations/2026_07_10_050000_encrypt_phone_numbers.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_07_10_050000_encrypt_phone_numbers.php)
- [database/migrations/2026_08_24_010000_scope_contact_email_uniqueness_to_team.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_08_24_010000_scope_contact_email_uniqueness_to_team.php)
- [database/migrations/2026_08_24_020000_scope_company_domain_uniqueness_to_team.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_08_24_020000_scope_company_domain_uniqueness_to_team.php)
- [database/migrations/2026_08_24_060000_create_crm_core_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/database/migrations/2026_08_24_060000_create_crm_core_tables.php)

[src/Enums/RecordType.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Enums/RecordType.php): `Contact = 'contact'`, `Organization = 'organization'`, `Household = 'household'`.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/CRMCore/CRMCoreModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/tests/Feature/CRMCore/CRMCoreModuleTest.php)
- [tests/Feature/Tags/ContactTagTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/tests/Feature/Tags/ContactTagTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
