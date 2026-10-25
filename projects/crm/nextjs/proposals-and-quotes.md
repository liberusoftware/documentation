# Proposals and Quotes: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-proposals-and-quotes`.

**Proposed design identifier:** `module-crm-proposals-and-quotes-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/proposals-and-quotes.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-proposals-and-quotes](../../../modules/source/liberusoftware--module-crm-proposals-and-quotes.md) |
| API | [liberusoftware/module-crm-proposals-and-quotes-api](../../../modules/source/liberusoftware--module-crm-proposals-and-quotes-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Branded templates | A focused authorized view or workflow section for branded templates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Sections | A focused authorized view or workflow section for sections; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Scope | A focused authorized view or workflow section for scope; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Line items | A focused authorized view or workflow section for line items; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Optional choices | A focused authorized view or workflow section for optional choices; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Versions | A focused authorized view or workflow section for versions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Comments | A focused authorized view or workflow section for comments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approvals | A focused authorized view or workflow section for approvals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Delivery | A focused authorized view or workflow section for delivery; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Engagement | A focused authorized view or workflow section for engagement; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Acceptance | A focused authorized view or workflow section for acceptance; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Expiry | A focused authorized view or workflow section for expiry; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ProposalQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Queries/ProposalQuery.php) | `public function templates(int $teamId)`<br>`public function proposals(int $teamId)`<br>`public function versions(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddProposalComment.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/AddProposalComment.php) | `public function execute(int $teamId, int $userId, array $input): ProposalEvent` |
| [ChangeProposalStatus.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/ChangeProposalStatus.php) | `public function execute(int $teamId, int $userId, int $proposalId, string $status): Proposal` |
| [CreateProposal.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposal.php) | `public function execute(int $teamId, int $userId, array $input): Proposal` |
| [CreateProposalTemplate.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalTemplate.php) | `public function execute(int $teamId, int $userId, array $input): ProposalTemplate` |
| [CreateProposalVersion.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalVersion.php) | `public function execute(int $teamId, int $userId, array $input): ProposalVersion` |
| [UpdateProposal.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/UpdateProposal.php) | `public function execute(int $teamId, int $userId, int $proposalId, array $input): Proposal` |
| [ProposalPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Services/ProposalPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Proposal.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/Proposal.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalTemplate.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalVersion.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalVersion.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-proposals-and-quotes-api/routes/api.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/proposals-and-quotes')->group(function (): void {
Route::get('/templates', [ProposalsAndQuotesController::class, 'templates']);
Route::post('/templates', [ProposalsAndQuotesController::class, 'template']);
Route::get('/proposals', [ProposalsAndQuotesController::class, 'proposals']);
Route::post('/proposals', [ProposalsAndQuotesController::class, 'proposal']);
Route::post('/versions', [ProposalsAndQuotesController::class, 'version']);
Route::post('/proposals/{proposal}/{status}', [ProposalsAndQuotesController::class, 'status'])->whereIn('status', ['approved', 'delivered', 'accepted', 'rejected', 'expired']);
Route::post('/comments', [ProposalsAndQuotesController::class, 'comment']);
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
