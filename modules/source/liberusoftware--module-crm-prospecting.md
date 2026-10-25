# liberusoftware/module-crm-prospecting: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-prospecting](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-prospecting`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-prospecting` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-prospecting` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\Prospecting\\ProspectingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\Prospecting\\ProspectingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/module.json).

**Declared capabilities:** crm.prospecting

**Declared features:** Ideal-customer profiles and prospect searches, List building, research queues and contact reveal credits, Provider provenance and compliant export handoff

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\Prospecting\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateIdealCustomerProfile.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateIdealCustomerProfile.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): IdealCustomerProfile` |
| [src/Actions/CreateProspectSearch.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateProspectSearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectSearch` |
| [src/Actions/ImportProspect.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/ImportProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Prospect` |
| [src/Actions/QueueExport.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueExport.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectExport` |
| [src/Actions/QueueResearch.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueResearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectResearchItem` |
| [src/Actions/RevealContact.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/RevealContact.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectCredit` |
| [src/Actions/UpdateProspect.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/UpdateProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $prospectId, array $input): Prospect` |
| [src/Queries/ProspectingQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Queries/ProspectingQuery.php) | `public function profiles(int $teamId)`<br>`public function searches(int $teamId)`<br>`public function prospects(int $teamId)`<br>`public function queue(int $teamId)`<br>`public function exports(int $teamId)` |
| [src/Services/ProspectingPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Services/ProspectingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/ProspectRevealed.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Events/ProspectRevealed.php) · [src/Models/IdealCustomerProfile.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/IdealCustomerProfile.php) · [src/Models/Prospect.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/Prospect.php) · [src/Models/ProspectCredit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectCredit.php) · [src/Models/ProspectExport.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectExport.php) · [src/Models/ProspectResearchItem.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectResearchItem.php) · [src/Models/ProspectSearch.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectSearch.php) · [src/ProspectingServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/ProspectingServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_020000_create_crm_prospecting_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/database/migrations/2026_08_26_020000_create_crm_prospecting_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/Prospecting/ProspectingModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/tests/Feature/Prospecting/ProspectingModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
