# liberusoftware/module-crm-sales-pipelines: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-sales-pipelines](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-sales-pipelines`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-sales-pipelines` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-sales-pipelines` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\SalesPipelines\\SalesPipelinesServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\SalesPipelines\\SalesPipelinesServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/module.json).

**Declared capabilities:** crm.sales-pipelines

**Declared features:** Multiple pipelines and stages, Opportunities, values, probabilities and close dates, Products, competitors and dependencies, Stage history, rotting and loss reasons

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\SalesPipelines\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CloseOpportunity.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CloseOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, string $status, ?string $reason = null): Opportunity` |
| [src/Actions/CreateOpportunity.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateOpportunity.php) | `public function execute(int $teamId, int $actorId, array $data): Opportunity` |
| [src/Actions/CreatePipeline.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreatePipeline.php) | `public function execute(int $teamId, int $actorId, array $data): SalesPipeline` |
| [src/Actions/CreateStage.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateStage.php) | `public function execute(int $teamId, int $actorId, array $data): SalesStage` |
| [src/Actions/MoveOpportunity.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/MoveOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, array $data): Opportunity` |
| [src/Queries/PipelineQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Queries/PipelineQuery.php) | `public function pipelines(int $teamId)`<br>`public function stages(int $teamId, int $pipelineId)`<br>`public function opportunities(int $teamId)`<br>`public function rottingOpportunities(int $teamId)` |
| [src/Services/PipelineAudit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelineAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [src/Services/PipelinePolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelinePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/OpportunityChanged.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Events/OpportunityChanged.php) · [src/Models/Opportunity.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/Opportunity.php) · [src/Models/SalesPipeline.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesPipeline.php) · [src/Models/SalesStage.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesStage.php) · [src/Models/StageHistory.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/StageHistory.php) · [src/SalesPipelinesServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/SalesPipelinesServiceProvider.php).

**Legacy review:** 3 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2023_05_20_000004_create_pipelines_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/database/migrations/2023_05_20_000004_create_pipelines_table.php)
- [database/migrations/2024_01_01_000000_create_deals_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/database/migrations/2024_01_01_000000_create_deals_table.php)
- [database/migrations/2024_01_02_000000_create_stages_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/database/migrations/2024_01_02_000000_create_stages_table.php)
- [database/migrations/2024_10_13_000000_add_pipeline_and_stage_to_deals_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/database/migrations/2024_10_13_000000_add_pipeline_and_stage_to_deals_table.php)
- [database/migrations/2026_05_26_161939_add_team_id_to_deals_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/database/migrations/2026_05_26_161939_add_team_id_to_deals_table.php)
- [database/migrations/2026_08_25_150000_create_crm_sales_pipeline_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/database/migrations/2026_08_25_150000_create_crm_sales_pipeline_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/SalesPipelines/SalesPipelinesModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/tests/Feature/SalesPipelines/SalesPipelinesModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
