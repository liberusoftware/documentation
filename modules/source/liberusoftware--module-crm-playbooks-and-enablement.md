# liberusoftware/module-crm-playbooks-and-enablement: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-playbooks-and-enablement](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-playbooks-and-enablement`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-playbooks-and-enablement` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-playbooks-and-enablement` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\PlaybooksAndEnablement\\PlaybooksAndEnablementServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\PlaybooksAndEnablement\\PlaybooksAndEnablementServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/module.json).

**Declared capabilities:** crm.playbooks-and-enablement

**Declared features:** Guided scripts, qualification cards and battlecards, Onboarding content, evidence and coaching checklists, Recommendations and usage analytics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\PlaybooksAndEnablement\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AssignPlaybook.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/AssignPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookAssignment` |
| [src/Actions/CompletePlaybook.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CompletePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assignmentId, array $input): PlaybookAssignment` |
| [src/Actions/CreatePlaybook.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CreatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Playbook` |
| [src/Actions/RecommendPlaybook.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecommendPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookRecommendation` |
| [src/Actions/RecordPlaybookUsage.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecordPlaybookUsage.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookUsage` |
| [src/Actions/UpdatePlaybook.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/UpdatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $playbookId, array $input): Playbook` |
| [src/Queries/PlaybookQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Queries/PlaybookQuery.php) | `public function playbooks(int $teamId)`<br>`public function assignments(int $teamId)`<br>`public function recommendations(int $teamId)`<br>`public function usage(int $teamId)` |
| [src/Services/PlaybookPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Services/PlaybookPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/PlaybookCompleted.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Events/PlaybookCompleted.php) · [src/Models/Playbook.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/Playbook.php) · [src/Models/PlaybookAssignment.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookAssignment.php) · [src/Models/PlaybookRecommendation.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookRecommendation.php) · [src/Models/PlaybookUsage.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookUsage.php) · [src/PlaybooksAndEnablementServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/PlaybooksAndEnablementServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_070000_create_crm_playbooks_and_enablement_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/database/migrations/2026_08_26_070000_create_crm_playbooks_and_enablement_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/PlaybooksAndEnablement/PlaybooksAndEnablementModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/tests/Feature/PlaybooksAndEnablement/PlaybooksAndEnablementModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
