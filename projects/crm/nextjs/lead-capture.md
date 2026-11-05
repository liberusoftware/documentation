# Lead Capture: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-lead-capture`.

**Proposed design identifier:** `module-crm-lead-capture-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/lead-capture.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-lead-capture](../../../modules/source/liberusoftware--module-crm-lead-capture.md) |
| API | [liberusoftware/module-crm-lead-capture-api](../../../modules/source/liberusoftware--module-crm-lead-capture-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Leads inbox | A focused authorized view or workflow section for leads inbox; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Manual/import/API capture | A focused authorized view or workflow section for manual/import/api capture; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Forms | A focused authorized view or workflow section for forms; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Surveys | A focused authorized view or workflow section for surveys; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| QR codes | A focused authorized view or workflow section for qr codes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Chat | A focused authorized view or workflow section for chat; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Calls | A focused authorized view or workflow section for calls; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Advertisements | A focused authorized view or workflow section for advertisements; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Events | A focused authorized view or workflow section for events; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Referrals | A focused authorized view or workflow section for referrals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Source metadata | A focused authorized view or workflow section for source metadata; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [CaptureQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Queries/CaptureQuery.php) | `public function forTeam(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CaptureLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CaptureLead.php) | `public function execute(int $teamId, int $userId, array $input): CapturedLead`<br>`public function executeLegacy(int $teamId, ?int $actorId, array $input): LeadCapture` |
| [CreateCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureForm.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureForm` |
| [CreateCaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureQrCode.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureQrCode` |
| [RecordCaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordCaptureEvent.php) | `public function execute(int $teamId, int $userId, CapturedLead $lead, array $input): CaptureEvent` |
| [RecordReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordReferral.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureReferral` |
| [SubmitCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/SubmitCaptureForm.php) | `public function execute(CaptureForm $form, ?int $actorId, array $payload): LeadCapture` |
| [UpdateCaptureStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/UpdateCaptureStatus.php) | `public function execute(LeadCapture $capture, string $status, ?string $failureReason = null): LeadCapture` |
| [CaptureDeduplicator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureDeduplicator.php) | `public function key(array $attributes): string`<br>`public function find(int $teamId, string $key): ?LeadCapture` |
| [CaptureReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [LeadCapturePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/LeadCapturePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [CaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureForm.php) | `team_id`, `actor_id`, `kind`, `name`, `slug`, `status`, `schema`, `settings`, `submissions_count` |
| [CaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureQrCode.php) | `team_id`, `actor_id`, `name`, `code`, `destination`, `status`, `metadata`, `scan_count` |
| [CaptureReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureReferral.php) | `team_id`, `actor_id`, `code`, `referrer_type`, `referrer_id`, `referred_type`, `referred_id`, `status`, `metadata` |
| [CapturedLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CapturedLead.php) | No literal fillable array detected; inspect the model and API schema. |
| [LeadCapture.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/LeadCapture.php) | `team_id`, `actor_id`, `kind`, `status`, `name`, `email`, `phone`, `source`, `source_medium`, `source_campaign`, `external_id`, `dedupe_key`, `source_metadata`, `payload`, `provenance`, `captured_at`, `processed_at`, `failure_reason` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-lead-capture-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/lead-capture')->group(function (): void {
Route::get('/', [LeadCaptureController::class, 'index']);
Route::post('/', [LeadCaptureController::class, 'store']);
Route::post('{lead}/events', [LeadCaptureController::class, 'event']);
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
