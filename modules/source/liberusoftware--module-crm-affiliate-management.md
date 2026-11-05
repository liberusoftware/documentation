# liberusoftware/module-crm-affiliate-management: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-affiliate-management](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-affiliate-management`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-affiliate-management` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-affiliate-management` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\AffiliateManagement\\AffiliateManagementServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\AffiliateManagement\\AffiliateManagementServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/module.json).

**Declared capabilities:** crm.affiliate-management

**Declared features:** Affiliates, applications, links, clicks, conversions, commission rules, payouts, disputes, assets and portal

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\AffiliateManagement\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ApplyAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApplyAffiliate.php) | `public function execute(int $teamId, array $input): Affiliate` |
| [src/Actions/ApproveAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliate.php) | `public function execute(int $teamId, Affiliate $affiliate): Affiliate` |
| [src/Actions/ApproveAffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliatePayout.php) | `public function execute(int $teamId, int $actorId, AffiliatePayout $payout): AffiliatePayout` |
| [src/Actions/CreateAffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/CreateAffiliateLink.php) | `public function execute(int $teamId, Affiliate $affiliate, array $input): AffiliateLink` |
| [src/Actions/RecordAffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/RecordAffiliateEvent.php) | `public function execute(int $teamId, AffiliateLink $link, array $input): AffiliateEvent` |
| [src/Queries/AffiliateQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Queries/AffiliateQuery.php) | `public function affiliates(int $teamId): Builder`<br>`public function events(int $teamId): Builder` |

Other non-legacy PHP sources: [src/AffiliateManagementServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/AffiliateManagementServiceProvider.php) · [src/Models/Affiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/Affiliate.php) · [src/Models/AffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateEvent.php) · [src/Models/AffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateLink.php) · [src/Models/AffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliatePayout.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_28_130000_create_crm_affiliate_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/database/migrations/2026_08_28_130000_create_crm_affiliate_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/AffiliateManagement/AffiliateManagementModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/tests/Feature/AffiliateManagement/AffiliateManagementModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
