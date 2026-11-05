# Sales pipelines: implementation and user workflow

**Source reviewed:** CRM application commit `63aad94e94c0f9a18038e301eb979138c657be64`. This walkthrough explains the inspected domain/API/Filament/Livewire implementations. It does not report a test run or certify the remaining target requirements. Start with the [CRM clone guide](../DEVELOPMENT.md).

## Packages and responsibilities

| Responsibility | Observed Composer identity | Reference |
| --- | --- | --- |
| Pipelines, stages, opportunities, moves and close rules | `liberusoftware/module-crm-sales-pipelines` | [Domain source](../../../modules/source/liberusoftware--module-crm-sales-pipelines.md) |
| HTTP transport | `liberusoftware/module-crm-sales-pipelines-api` | [API source](../../../modules/source/liberusoftware--module-crm-sales-pipelines-api.md) |
| Administrative resources | `liberusoftware/module-crm-sales-pipelines-filament` | [Filament source](../../../modules/source/liberusoftware--module-crm-sales-pipelines-filament.md) |
| Interactive board | `liberusoftware/module-crm-sales-pipelines-livewire` | [Livewire source](../../../modules/source/liberusoftware--module-crm-sales-pipelines-livewire.md) |

The existing `sales-pipelines` and `crm-sales-pipelines` design spellings refer to the same observed domain package in this source map. Keep one owner for pipeline records and transitions. Extra design prefixes are not instructions to publish a second implementation. See the [reconciliation map](../SOURCE-MAPPING.md#sales-pipelines).

## Configure and use a pipeline

1. Select an authenticated current team. Domain mutations call the package's `PipelinePolicy`, which allows the team owner or a member whose pivot role is `admin`, `manager` or `sales rep`. The host owns identity and current-team selection.
2. Create a pipeline with a name. The inspected action validates a nonempty string up to 255 characters and sets `active` to true.
3. Add stages to that pipeline. Each stage needs its pipeline ID, name and nonnegative integer position. Optional probability is between 0 and 100; optional `rotting_days` is an integer of at least one. The action rejects a pipeline outside the selected team.
4. Create an opportunity with a pipeline ID, a stage in that pipeline, and a name. Optional fields include nonnegative value, probability, close date, products, competitors and dependencies. The action sets status to `open`, records `last_stage_at`, writes an audit entry and dispatches `OpportunityChanged` with the `created` change.
5. Move an open opportunity to another stage of the same pipeline. The move action scopes the record to the team, locks it within a database transaction, updates probability from the target stage, updates `last_stage_at`, and adds a stage-history entry. Moving to the existing stage or moving a closed opportunity is rejected.
6. Close an open opportunity as `won` or `lost`. Losing requires a nonblank loss reason; closing again is rejected. A won opportunity clears the loss reason. The inspected close action writes its own audit entry; do not assume every transition dispatches the same event as creation/movement.

Source: [mutation policy](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelinePolicy.php), [pipeline creation](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreatePipeline.php), [stage creation](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateStage.php), [opportunity creation](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateOpportunity.php), [movement](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/MoveOpportunity.php), and [closing](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CloseOpportunity.php).

## Read queries and rotting opportunities

`PipelineQuery` returns team-scoped builders for pipelines and opportunities. Stage queries first verify that the pipeline belongs to the team; an invalid pipeline returns an empty builder. The rotting query selects open opportunities whose stage has a threshold and whose non-null `last_stage_at` is at or before that threshold. It excludes closed records and returns an empty builder if no scoped stages define a threshold.

Source: [modules/crm-sales-pipelines/src/Queries/PipelineQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Queries/PipelineQuery.php).

The query methods take a team ID rather than an actor. Their caller must establish authorized team context. A query's `where('team_id', ...)` condition is not an independent membership check. The inspected policy imports `App\Models\Team`, so the package currently has host coupling that must be resolved or explicitly supported before claiming arbitrary clean-host reuse.

## Observed HTTP operations

The route file declares `auth:sanctum` and prefix `/api/v1/crm/sales-pipelines`. The controller derives the team from the authenticated user's non-null `current_team_id`; it does not accept a browser-selected team ID as a command argument.

| Method | Path after the prefix | Behavior |
| --- | --- | --- |
| GET | `/pipelines` | Return current-team pipelines |
| POST | `/pipelines` | Create a pipeline |
| POST | `/stages` | Create a stage |
| GET | `/opportunities` | Paginated current-team opportunities |
| GET | `/opportunities/rotting` | Paginated rotting opportunities |
| POST | `/opportunities` | Create an opportunity |
| POST | `/opportunities/{opportunity}/move` | Move using a `stage_id` body field |
| POST | `/opportunities/{opportunity}/close/{status}` | Close as `won` or `lost`; `loss_reason` is required by the action for lost records |

The inspected controller returns a `data` envelope. Paginated opportunity results wrap the paginator under that key, so row data is nested at `data.data`; clients should use the actual schema/response instead of the generic examples in a target API template. Creation returns 201 in this controller. Error formatting depends on the host exception handling.

Source: [routes](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-api/routes/api.php) and [controller](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-api/src/Http/Controllers/PipelineController.php).

Illustrative create-stage body for an existing authorized pipeline:

```json
{
  "pipeline_id": 42,
  "name": "Proposal",
  "position": 2,
  "probability": 60,
  "rotting_days": 7
}
```

The ID is example data, not a seeded record. Get actual IDs from the current team's authorized records. No generic delete, arbitrary update, reopen, idempotency-key storage or ETag support is established by these routes. Implementations must be reviewed before a client relies on those planned capabilities.

## Filament and Livewire behavior

Filament exposes pipeline, stage and opportunity resources. `OpportunityResource` filters its base query by current team and offers pipeline/stage, name, value, probability, close-date and status fields. Pipeline choices are active pipelines in that team. The inspected opportunity create/edit page classes inherit ordinary Filament record pages and do not themselves call the domain create/move/close actions. Review host policies, model behavior and save hooks before claiming action-level invariant parity; a status select alone is not the close workflow described above.

There is also a concrete validation difference: the inspected Filament pipeline form limits the name to 160 characters, while `CreatePipeline` accepts 255. Document and reconcile such differences when extending the adapter rather than assuming all surfaces already behave identically.

Source: [opportunity resource](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/OpportunityResource.php), [create page](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/OpportunityResource/Pages/CreateOpportunity.php), [edit page](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/OpportunityResource/Pages/EditOpportunity.php), and [pipeline resource](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/PipelineResource.php).

Livewire's `PipelineBoard` reads at most 100 current-team opportunities and fetches only their stage IDs. Its `move` method resolves the authenticated user/current team and delegates to `MoveOpportunity`. Preserve these server checks when adding drag-and-drop. An empty board can mean no matching records; the implementation does not establish a complete all-record paginated board.

Source: [modules/crm-sales-pipelines-livewire/src/Components/PipelineBoard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-livewire/src/Components/PipelineBoard.php).

## React, Next.js, Vue, Nuxt and mobile design

The scanned module manifests do not establish dedicated React/Next.js/Vue/Nuxt/mobile package implementations for this capability. Their existing specifications remain target designs. Use the observed API for transport, keep domain mutations server-owned, and share framework-independent opportunity cards, stage labels and form primitives where useful.

For Next.js, the application can own a pipeline list/detail/board route and server API adapter. Authenticated reads start with explicit no-store behavior until tenant-aware caching is reviewed. On an uncertain move outcome, requery the current stage before retrying: the source rejects moving to the same stage, so blind retries cannot be described as idempotent success. Preserve field errors and current-team context across navigation.

For mobile/offline use, permit local draft capture only with a clear stale indicator; stage moves and close decisions need fresh server validation. A queued offline request must not display a won/lost state as confirmed until the server accepts it. Use the [Next.js standard](../../../standards/NEXTJS.md) and [mobile architecture](../../../architecture/MOBILE.md).

## Verification and known limits

The tracked [module test file](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/tests/Feature/SalesPipelines/SalesPipelinesModuleTest.php) uses the host `Tests\TestCase` and covers a creation/move/loss lifecycle, Filament page exposure, rotting queries/team scope, and a closed-opportunity movement rejection. Those are inspected assertions, not a reported test execution or proof of full permission/concurrency coverage.

Before adopting the package in another product, verify host coupling, read authorization, direct Filament save paths, close-versus-move races, audit/event transaction behavior, actual response schemas, and migration compatibility. These checks address concrete differences between the target independent-module architecture and the inspected implementation. They belong in the owning code change; documentation must not present them as already fixed.
