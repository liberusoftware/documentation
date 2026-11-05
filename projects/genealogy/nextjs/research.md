# Research: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-genealogy-research`.

**Proposed design identifier:** `module-genealogy-research-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/research.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-genealogy-research](../../../modules/source/liberusoftware--module-genealogy-research.md) |
| API | [liberusoftware/module-genealogy-research-api](../../../modules/source/liberusoftware--module-genealogy-research-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Questions | A focused authorized view or workflow section for questions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Plans | A focused authorized view or workflow section for plans; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Tasks | A focused authorized view or workflow section for tasks; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Logs | A focused authorized view or workflow section for logs; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Correspondence | A focused authorized view or workflow section for correspondence; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Negative searches | A focused authorized view or workflow section for negative searches; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Findings | A focused authorized view or workflow section for findings; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateChecklist.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateChecklist.php) | `public function execute(Model $user, string $name, ?ChecklistTemplate $template = null, array $attributes = []): UserChecklist` |
| [CreateResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateResearchEntry.php) | `public function execute(array $attributes): ResearchEntry`<br>`public function validate(array $values): void` |
| [CreateResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateResearchProject.php) | `public function execute(array $attributes): ResearchProject`<br>`public function validate(array $values): void` |
| [DeleteResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/DeleteResearchEntry.php) | `public function execute(ResearchEntry $entry): void` |
| [DeleteResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/DeleteResearchProject.php) | `public function execute(ResearchProject $project): void` |
| [UpdateResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/UpdateResearchEntry.php) | `public function execute(ResearchEntry $entry, array $attributes): ResearchEntry` |
| [UpdateResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/UpdateResearchProject.php) | `public function execute(ResearchProject $project, array $attributes): ResearchProject` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ChecklistTemplate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ChecklistTemplate.php) | `team_id`, `created_by`, `name`, `description`, `category`, `is_public`, `is_default`, `tags`, `difficulty_level`, `estimated_time` |
| [ChecklistTemplateItem.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ChecklistTemplateItem.php) | `checklist_template_id`, `title`, `description`, `sort_order`, `category`, `is_required`, `estimated_time`, `resources`, `tips` |
| [ResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ResearchEntry.php) | `team_id`, `research_project_id`, `kind`, `title`, `body`, `status`, `due_date`, `completed_at`, `metadata` |
| [ResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ResearchProject.php) | `team_id`, `name`, `status`, `metadata` |
| [UserChecklist.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/UserChecklist.php) | `team_id`, `user_id`, `checklist_template_id`, `name`, `description`, `subject_type`, `subject_id`, `status`, `started_at`, `completed_at`, `notes`, `priority`, `due_date` |
| [UserChecklistItem.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/UserChecklistItem.php) | `checklist_id`, `template_item_id`, `title`, `description`, `sort_order`, `is_completed`, `completed_at`, `notes`, `estimated_time`, `actual_time`, `resources`, `tips` |

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
