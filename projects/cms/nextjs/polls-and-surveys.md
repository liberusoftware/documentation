# Polls and Surveys: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-cms-polls-and-surveys`.

**Proposed design identifier:** `module-cms-polls-and-surveys-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/polls-and-surveys.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **3 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-cms-polls-and-surveys](../../../modules/source/liberusoftware--module-cms-polls-and-surveys.md) |
| API | [liberusoftware/module-cms-polls-and-surveys-api](../../../modules/source/liberusoftware--module-cms-polls-and-surveys-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Questions | A focused authorized view or workflow section for questions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Branching | A focused authorized view or workflow section for branching; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Anonymous/authenticated response policy | A focused authorized view or workflow section for anonymous/authenticated response policy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Schedules | A focused authorized view or workflow section for schedules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Results | A focused authorized view or workflow section for results; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Exports | A focused authorized view or workflow section for exports; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Privacy controls | A focused authorized view or workflow section for privacy controls; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [PollService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-polls-and-surveys/src/Services/PollService.php) | `public function create(array $attributes, ?int $teamId = null): Poll`<br>`public function update(Poll $poll, array $attributes): Poll`<br>`public function saveQuestion(Poll $poll, array $attributes, ?Question $question = null): Question`<br>`public function deleteQuestion(Question $question): void`<br>`public function submit(Poll $poll, array $answers, ?int $userId = null, ?string $respondentKey = null): Response`<br>`public function results(Poll $poll): array`<br>`public function export(Poll $poll, bool $includeRespondentIdentity = false): array`<br>`public function eraseResponse(Response $response): void` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Poll.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-polls-and-surveys/src/Models/Poll.php) | `title`, `key`, `description`, `starts_at`, `ends_at`, `allow_anonymous`, `allow_multiple`, `active`, `results_public`, `team_id` |
| [Question.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-polls-and-surveys/src/Models/Question.php) | `poll_id`, `key`, `type`, `prompt`, `options`, `branching`, `position`, `required` |
| [Response.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-polls-and-surveys/src/Models/Response.php) | `poll_id`, `user_id`, `respondent_hash`, `answers`, `submitted_at`, `team_id` |

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
