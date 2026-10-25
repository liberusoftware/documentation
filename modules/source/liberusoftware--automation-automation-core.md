# liberusoftware/automation-automation-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral automation-core domain module for Liberu Automation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [module-automation-automation-core](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: automation-laravel, `module-automation-automation-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/automation-automation-core` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `module-automation-automation-core` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Modules\\Automation\\AutomationCore\\AutomationCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/composer.json) · [module.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/module.json).

**Declared capabilities:** automation.automation-core.workflow-definitions, automation.automation-core.versions, automation.automation-core.triggers, automation.automation-core.state, automation.automation-core.runs, automation.automation-core.variables, automation.automation-core.schedules, automation.automation-core.retries, automation.automation-core.cancellation, automation.automation-core.compensation

**Declared features:** workflow definitions, versions, triggers, state, runs, variables, schedules, retries, cancellation, compensation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Automation\\AutomationCore\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CancelWorkflowRun.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/CancelWorkflowRun.php) | `public function execute(WorkflowRunRecord $run, string $teamId, ?string $actorId = null, ?string $correlationId = null): WorkflowRunRecord` |
| [src/Actions/CreateAutomationCoreResource.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/CreateAutomationCoreResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): AutomationCoreResource` |
| [src/Actions/PublishWorkflow.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/PublishWorkflow.php) | `public function execute(AutomationCoreResource $workflow, string $teamId, WorkflowDefinition $definition, ?string $actorId = null, ?string $correlationId = null): WorkflowVersion` |
| [src/Actions/StartWorkflowRun.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/StartWorkflowRun.php) | `public function execute(AutomationCoreResource $workflow, string $teamId, array $variables = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): WorkflowRunRecord` |
| [src/Actions/TransitionAutomationCoreResource.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/TransitionAutomationCoreResource.php) | `public function execute(AutomationCoreResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): AutomationCoreResource` |

Other non-legacy PHP sources: [src/AutomationCoreServiceProvider.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/AutomationCoreServiceProvider.php) · [src/Domain/RetryPolicy.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Domain/RetryPolicy.php) · [src/Domain/WorkflowDefinition.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Domain/WorkflowDefinition.php) · [src/Domain/WorkflowRun.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Domain/WorkflowRun.php) · [src/Domain/WorkflowSchedule.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Domain/WorkflowSchedule.php) · [src/Domain/WorkflowTrigger.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Domain/WorkflowTrigger.php) · [src/Domain/WorkflowVariables.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Domain/WorkflowVariables.php) · [src/Enums/WorkflowStatus.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Enums/WorkflowStatus.php) · [src/Events/ResourceTransitioned.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Events/ResourceTransitioned.php) · [src/Events/WorkflowPublished.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Events/WorkflowPublished.php) · [src/Models/AutomationCoreResource.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/AutomationCoreResource.php) · [src/Models/WorkflowRunRecord.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/WorkflowRunRecord.php) · [src/Models/WorkflowVersion.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/WorkflowVersion.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000000_create_automation_automation_core_resources_table.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/database/migrations/2026_08_23_000000_create_automation_automation_core_resources_table.php)
- [database/migrations/2026_08_23_000001_create_automation_workflow_lifecycle_tables.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/database/migrations/2026_08_23_000001_create_automation_workflow_lifecycle_tables.php)
- [database/migrations/2026_08_24_000002_add_idempotency_key_to_automation_workflow_runs.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/database/migrations/2026_08_24_000002_add_idempotency_key_to_automation_workflow_runs.php)
- [database/migrations/2026_08_30_000003_add_lifecycle_metadata_to_automation_automation_core_resources.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/database/migrations/2026_08_30_000003_add_lifecycle_metadata_to_automation_automation_core_resources.php)
- [database/migrations/2026_08_30_000004_add_execution_lifecycle_metadata.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/database/migrations/2026_08_30_000004_add_execution_lifecycle_metadata.php)

[src/Enums/WorkflowStatus.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Enums/WorkflowStatus.php): `Draft = 'draft'`, `Published = 'published'`, `Paused = 'paused'`, `Archived = 'archived'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/DomainTest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/tests/Unit/DomainTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
