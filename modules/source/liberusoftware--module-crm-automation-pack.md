# liberusoftware/module-crm-automation-pack: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-automation-pack](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-automation-pack`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-automation-pack` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-automation-pack` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\AutomationPack\\AutomationPackServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\AutomationPack\\AutomationPackServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/module.json).

**Declared capabilities:** crm.automation-pack

**Declared features:** Triggers, actions, conditions, recipes, enrollment history, versioning, simulation, approval gates and adapters

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\AutomationPack\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ApproveAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/ApproveAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, string $decision, ?string $reason = null): AutomationApproval` |
| [src/Actions/CreateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/CreateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AutomationRecipe` |
| [src/Actions/EnrollSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/EnrollSubject.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationEnrollment` |
| [src/Actions/PublishAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/PublishAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe): AutomationRecipe` |
| [src/Actions/SimulateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/SimulateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationRun` |
| [src/Queries/AutomationPackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Queries/AutomationPackQuery.php) | `public function recipes(int $teamId)` |
| [src/Services/AutomationPackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Services/AutomationPackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/AutomationPackServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/AutomationPackServiceProvider.php) · [src/Models/AutomationApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationApproval.php) · [src/Models/AutomationEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationEnrollment.php) · [src/Models/AutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRecipe.php) · [src/Models/AutomationRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRun.php).

**Legacy review:** 12 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2023_06_02_000000_create_workflows_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/database/migrations/2023_06_02_000000_create_workflows_table.php)
- [database/migrations/2024_02_15_000002_create_workflow_automation_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/database/migrations/2024_02_15_000002_create_workflow_automation_tables.php)
- [database/migrations/2024_02_15_000006_enhance_workflows_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/database/migrations/2024_02_15_000006_enhance_workflows_table.php)
- [database/migrations/2026_08_27_170000_create_crm_automation_pack_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/database/migrations/2026_08_27_170000_create_crm_automation_pack_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/AutomationPack/AutomationPackModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/tests/Feature/AutomationPack/AutomationPackModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
