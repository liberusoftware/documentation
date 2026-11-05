# AI Reception and Conversation: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-ai-reception-and-conversation`.

**Proposed design identifier:** `module-crm-ai-reception-and-conversation-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/ai-reception-and-conversation.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-ai-reception-and-conversation](../../../modules/source/liberusoftware--module-crm-ai-reception-and-conversation.md) |
| API | [liberusoftware/module-crm-ai-reception-and-conversation-api](../../../modules/source/liberusoftware--module-crm-ai-reception-and-conversation-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Governed chat/voice agents | A focused authorized view or workflow section for governed chat/voice agents; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approved knowledge/tools | A focused authorized view or workflow section for approved knowledge/tools; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Qualification | A focused authorized view or workflow section for qualification; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Booking | A focused authorized view or workflow section for booking; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Summaries | A focused authorized view or workflow section for summaries; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Confidence | A focused authorized view or workflow section for confidence; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Live handoff | A focused authorized view or workflow section for live handoff; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Testing | A focused authorized view or workflow section for testing; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Human-approval policy | A focused authorized view or workflow section for human-approval policy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ActivateReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/ActivateReceptionAgent.php) | `public function execute(int $teamId, ReceptionAgent $agent): ReceptionAgent` |
| [CreateReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/CreateReceptionAgent.php) | `public function execute(int $teamId, int $ownerId, array $input): ReceptionAgent` |
| [RecordReceptionTurn.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/RecordReceptionTurn.php) | `public function execute(int $teamId, int $actorId, ReceptionConversation $conversation, array $input): ReceptionConversation` |
| [RequestReceptionHandoff.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/RequestReceptionHandoff.php) | `public function execute(int $teamId, int $actorId, ReceptionConversation $conversation, string $reason): ReceptionConversation` |
| [StartReceptionConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/StartReceptionConversation.php) | `public function execute(int $teamId, ReceptionAgent $agent, array $input = []): ReceptionConversation` |
| [ReceptionResponder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Services/ReceptionResponder.php) | `public function respond(ReceptionAgent $agent, ReceptionConversation $conversation, string $input): string` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReceptionAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReceptionConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionConversation.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-ai-reception-and-conversation-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/ai-reception-and-conversation')->group(function (): void {
Route::get('agents', [ReceptionController::class, 'agents']);
Route::post('agents', [ReceptionController::class, 'createAgent']);
Route::post('agents/{agent}/activate', [ReceptionController::class, 'activate']);
Route::post('agents/{agent}/conversations', [ReceptionController::class, 'start']);
Route::post('conversations/{conversation}/turns', [ReceptionController::class, 'turn']);
Route::post('conversations/{conversation}/handoff', [ReceptionController::class, 'handoff']);
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
