# liberusoftware/module-crm-advertising: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-advertising](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-advertising`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-advertising` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-advertising` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\Advertising\\AdvertisingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\Advertising\\AdvertisingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/module.json).

**Declared capabilities:** crm.advertising

**Declared features:** Ad accounts, campaigns, lead ads, audiences, conversions, performance sync and attribution

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\Advertising\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/TransitionRecord.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AdvertisingRecord` |
| [src/Actions/UpsertRecord.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AdvertisingRecord` |
| [src/Queries/AdvertisingQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Queries/AdvertisingQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

Other non-legacy PHP sources: [src/AdvertisingServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/AdvertisingServiceProvider.php) · [src/Models/AdvertisingRecord.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Models/AdvertisingRecord.php).

**Legacy review:** 30 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2023_05_20_000000_create_social_media_posts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2023_05_20_000000_create_social_media_posts_table.php)
- [database/migrations/2023_05_20_000001_create_marketing_campaigns_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2023_05_20_000001_create_marketing_campaigns_table.php)
- [database/migrations/2023_05_20_000002_create_campaign_recipients_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2023_05_20_000002_create_campaign_recipients_table.php)
- [database/migrations/2024_10_22_000000_create_advertising_accounts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2024_10_22_000000_create_advertising_accounts_table.php)
- [database/migrations/2024_10_22_100000_add_last_sync_and_metadata_to_advertising_accounts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2024_10_22_100000_add_last_sync_and_metadata_to_advertising_accounts_table.php)
- [database/migrations/2024_10_22_110000_create_campaigns_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2024_10_22_110000_create_campaigns_table.php)
- [database/migrations/2024_10_22_120000_create_ad_sets_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2024_10_22_120000_create_ad_sets_table.php)
- [database/migrations/2024_10_22_130000_create_ads_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2024_10_22_130000_create_ads_table.php)
- [database/migrations/2024_11_20_000000_add_media_fields_to_social_media_posts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2024_11_20_000000_add_media_fields_to_social_media_posts_table.php)
- [database/migrations/2026_03_03_000000_add_media_fields_to_social_media_posts_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2026_03_03_000000_add_media_fields_to_social_media_posts_table.php)
- [database/migrations/2026_03_08_000004_create_mailchimp_campaigns_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2026_03_08_000004_create_mailchimp_campaigns_table.php)
- [database/migrations/2026_08_25_112000_create_crm_advertising_records_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/database/migrations/2026_08_25_112000_create_crm_advertising_records_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/Advertising/AdvertisingModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/tests/Feature/Advertising/AdvertisingModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
