# Lead Qualification: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-lead-qualification`.

**Proposed design identifier:** `module-crm-lead-qualification-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/lead-qualification.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-lead-qualification](../../../modules/source/liberusoftware--module-crm-lead-qualification.md) |
| API | [liberusoftware/module-crm-lead-qualification-api](../../../modules/source/liberusoftware--module-crm-lead-qualification-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Lifecycle stages | A focused authorized view or workflow section for lifecycle stages; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Fit/engagement scoring | A focused authorized view or workflow section for fit/engagement scoring; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| MQL/PQL/SQL/service-qualified rules | A focused authorized view or workflow section for mql/pql/sql/service-qualified rules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Qualification frameworks | A focused authorized view or workflow section for qualification frameworks; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Disqualification | A focused authorized view or workflow section for disqualification; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Nurture | A focused authorized view or workflow section for nurture; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Conversion | A focused authorized view or workflow section for conversion; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [LeadQualificationQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Queries/LeadQualificationQuery.php) | `public function forTeam(int $teamId): Builder` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ConvertQualification.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/ConvertQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId, ?string $reason = null): LeadQualification` |
| [CreateFramework.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/CreateFramework.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): QualificationFramework` |
| [CreateQualification.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/CreateQualification.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): LeadQualification` |
| [DisqualifyQualification.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/DisqualifyQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId, string $reason): LeadQualification` |
| [EnrollNurture.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/EnrollNurture.php) | `public function execute(LeadQualification $qualification, ?int $actorId, array $attributes): NurtureEnrollment` |
| [EvaluateQualification.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/EvaluateQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId): LeadQualification` |
| [RecordQualificationEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/RecordQualificationEvent.php) | `public function execute(int $teamId, int $userId, QualifiedLead $lead, array $input): QualificationEvent` |
| [ScoreLead.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/ScoreLead.php) | `public function execute(int $teamId, int $userId, QualifiedLead $lead, array $input): QualifiedLead` |
| [TransitionLifecycle.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/TransitionLifecycle.php) | `public function execute(LeadQualification $qualification, ?int $actorId, string $stage, ?string $reason = null): LeadQualification` |
| [UpdateScores.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/UpdateScores.php) | `public function execute(LeadQualification $qualification, ?int $actorId, array $scores): LeadQualification` |
| [UpsertLead.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/UpsertLead.php) | `public function execute(int $teamId, int $userId, array $input): QualifiedLead` |
| [LeadQualificationPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Services/LeadQualificationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |
| [QualificationAudit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Services/QualificationAudit.php) | `public function record(LeadQualification $qualification, ?int $actorId, string $event, array $details = []): void` |
| [QualificationReport.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Services/QualificationReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [QualificationScorer.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Services/QualificationScorer.php) | `public function scores(array $attributes): array` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [LeadQualification.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/LeadQualification.php) | `team_id`, `actor_id`, `subject_type`, `subject_id`, `framework_id`, `lifecycle_stage`, `fit_score`, `engagement_score`, `total_score`, `qualification_status`, `disqualification_reason`, `nurture_until`, `converted_at`, `version`, `metadata` |
| [NurtureEnrollment.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/NurtureEnrollment.php) | `team_id`, `qualification_id`, `actor_id`, `status`, `sequence`, `starts_at`, `ends_at`, `metadata` |
| [QualificationEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [QualificationFramework.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationFramework.php) | `team_id`, `actor_id`, `name`, `status`, `mql_threshold`, `pql_threshold`, `sql_threshold`, `service_qualified_threshold`, `rules`, `settings` |
| [QualificationRule.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationRule.php) | No literal fillable array detected; inspect the model and API schema. |
| [QualifiedLead.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualifiedLead.php) | No literal fillable array detected; inspect the model and API schema. |
| [StageHistory.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/StageHistory.php) | `team_id`, `qualification_id`, `actor_id`, `from_stage`, `to_stage`, `reason` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-lead-qualification-api/routes/api.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/lead-qualification')->group(function (): void {
Route::get('/', [LeadQualificationController::class, 'index']);
Route::post('/', [LeadQualificationController::class, 'store']);
Route::post('{lead}/score', [LeadQualificationController::class, 'score']);
Route::post('{lead}/events', [LeadQualificationController::class, 'event']);
```

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
