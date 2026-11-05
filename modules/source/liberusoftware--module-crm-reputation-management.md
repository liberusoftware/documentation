# liberusoftware/module-crm-reputation-management: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-reputation-management](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-reputation-management`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-reputation-management` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-reputation-management` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\ReputationManagement\\ReputationManagementServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\ReputationManagement\\ReputationManagementServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/module.json).

**Declared capabilities:** crm.reputation-management

**Declared features:** Review requests and site connections, Monitoring, response workflow, templates and escalation, Sentiment, location rollups and reputation reporting

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\ReputationManagement\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ConnectReviewSite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/ConnectReviewSite.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationConnection` |
| [src/Actions/CreateReviewRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/CreateReviewRequest.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationRequest` |
| [src/Actions/EscalateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/EscalateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId): ReputationReview` |
| [src/Actions/RecordReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RecordReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationReview` |
| [src/Actions/RespondToReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RespondToReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [src/Actions/SaveTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/SaveTemplate.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationTemplate` |
| [src/Actions/UpdateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/UpdateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [src/Queries/ReputationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Queries/ReputationQuery.php) | `public function connections(int $teamId)`<br>`public function requests(int $teamId)`<br>`public function reviews(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function rollups(int $teamId)` |
| [src/Services/ReputationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Services/ReputationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/ReputationReviewReceived.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Events/ReputationReviewReceived.php) · [src/Models/ReputationConnection.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationConnection.php) · [src/Models/ReputationRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRequest.php) · [src/Models/ReputationReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationReview.php) · [src/Models/ReputationRollup.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRollup.php) · [src/Models/ReputationTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationTemplate.php) · [src/ReputationManagementServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/ReputationManagementServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_230000_create_crm_reputation_management_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/database/migrations/2026_08_25_230000_create_crm_reputation_management_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/ReputationManagement/ReputationManagementModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/tests/Feature/ReputationManagement/ReputationManagementModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
