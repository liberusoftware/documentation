# liberusoftware/module-crm-service-agent: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-service-agent](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-service-agent`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-service-agent` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-service-agent` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\ServiceAgent\\ServiceAgentServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\ServiceAgent\\ServiceAgentServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/module.json).

**Declared capabilities:** crm.service-agent

**Declared features:** Case classification and confidence, Knowledge retrieval and response drafts, Resolution plans and tool use, Escalation and quality review

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\ServiceAgent\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ClassifyCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/ClassifyCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, array $data): AgentCase` |
| [src/Actions/CreateAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/CreateAgentCase.php) | `public function execute(int $teamId, int $actorId, array $data): AgentCase` |
| [src/Actions/EscalateAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/EscalateAgentCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, array $data = []): AgentCase` |
| [src/Actions/RetrieveKnowledge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/RetrieveKnowledge.php) | `public function execute(int $teamId, int $actorId, array $data)` |
| [src/Actions/ReviewAgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/ReviewAgentCase.php) | `public function execute(int $teamId, int $actorId, array $data): AgentReview` |
| [src/Actions/RunAgentTool.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/RunAgentTool.php) | `public function execute(int $teamId, int $actorId, array $data): AgentToolRun` |
| [src/Actions/UpdateAgentOutput.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Actions/UpdateAgentOutput.php) | `public function execute(int $teamId, int $actorId, int $caseId, string $type, array $data): AgentCase` |
| [src/Queries/AgentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Queries/AgentQuery.php) | `public function cases(int $teamId)`<br>`public function knowledge(int $teamId, string $search = '')`<br>`public function tools(int $teamId)`<br>`public function reviews(int $teamId)` |
| [src/Services/AgentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Services/AgentAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [src/Services/AgentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Services/AgentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/AgentCaseUpdated.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Events/AgentCaseUpdated.php) · [src/Models/AgentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentAudit.php) · [src/Models/AgentCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentCase.php) · [src/Models/AgentKnowledge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentKnowledge.php) · [src/Models/AgentReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentReview.php) · [src/Models/AgentToolRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/Models/AgentToolRun.php) · [src/ServiceAgentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/src/ServiceAgentServiceProvider.php).

**Legacy review:** 14 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2024_10_22_000000_create_tickets_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/database/migrations/2024_10_22_000000_create_tickets_table.php)
- [database/migrations/2026_03_03_000001_add_source_fields_to_tickets_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/database/migrations/2026_03_03_000001_add_source_fields_to_tickets_table.php)
- [database/migrations/2026_07_07_130000_add_attachment_to_tickets_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/database/migrations/2026_07_07_130000_add_attachment_to_tickets_table.php)
- [database/migrations/2026_08_25_110000_create_crm_service_agent_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/database/migrations/2026_08_25_110000_create_crm_service_agent_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/ServiceAgent/ServiceAgentModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-agent/tests/Feature/ServiceAgent/ServiceAgentModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
