# liberusoftware/module-crm-projects: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-projects](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-projects`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-projects` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-projects` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\Projects\\ProjectsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\Projects\\ProjectsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/module.json).

**Declared capabilities:** crm.projects

**Declared features:** Projects, templates, milestones, tasks and dependencies, Owners, time, files, status, risks and client visibility, Opportunity handoff

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\Projects\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ChangeProjectStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/ChangeProjectStatus.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, string $status): Project` |
| [src/Actions/CreateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/CreateProject.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Project` |
| [src/Actions/CreateProjectTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/CreateProjectTask.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectTask` |
| [src/Actions/HandoffOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/HandoffOpportunity.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, int $opportunityId): Project` |
| [src/Actions/LogProjectTime.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/LogProjectTime.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectTime` |
| [src/Actions/RecordProjectRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/RecordProjectRisk.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectRisk` |
| [src/Actions/UpdateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/UpdateProject.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, array $input): Project` |
| [src/Queries/ProjectQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Queries/ProjectQuery.php) | `public function templates(int $teamId)`<br>`public function projects(int $teamId)`<br>`public function tasks(int $teamId)`<br>`public function risks(int $teamId)` |
| [src/Services/ProjectPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Services/ProjectPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/ProjectStatusChanged.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Events/ProjectStatusChanged.php) · [src/Models/Project.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/Project.php) · [src/Models/ProjectEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectEvent.php) · [src/Models/ProjectRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectRisk.php) · [src/Models/ProjectTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTask.php) · [src/Models/ProjectTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTemplate.php) · [src/Models/ProjectTime.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTime.php) · [src/ProjectsServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/ProjectsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_050000_create_crm_projects_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/database/migrations/2026_08_26_050000_create_crm_projects_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/Projects/ProjectsModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/tests/Feature/Projects/ProjectsModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
