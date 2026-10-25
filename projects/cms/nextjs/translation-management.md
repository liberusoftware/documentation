# Translation Management: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-cms-translation-management`.

**Proposed design identifier:** `module-cms-translation-management-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/translation-management.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **3 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-cms-translation-management](../../../modules/source/liberusoftware--module-cms-translation-management.md) |
| API | [liberusoftware/module-cms-translation-management-api](../../../modules/source/liberusoftware--module-cms-translation-management-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Jobs | A focused authorized view or workflow section for jobs; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Source changes | A focused authorized view or workflow section for source changes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Assignments | A focused authorized view or workflow section for assignments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Vendor adapters | A focused authorized view or workflow section for vendor adapters; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Machine translation | A focused authorized view or workflow section for machine translation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Review | A focused authorized view or workflow section for review; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Memory/glossaries | A focused authorized view or workflow section for memory/glossaries; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Status | A focused authorized view or workflow section for status; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Cost | A focused authorized view or workflow section for cost; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reconciliation | A focused authorized view or workflow section for reconciliation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [TranslationJobQuery.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Queries/TranslationJobQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $publicId): ?TranslationJob` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [TranslationManagementService.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Actions/TranslationManagementService.php) | `public function createJob(array $attributes): TranslationJob`<br>`public function addSourceChange(TranslationJob $job, array $attributes): TranslationSourceChange`<br>`public function queue(TranslationJob $job): TranslationJob`<br>`public function cancel(TranslationJob $job): TranslationJob`<br>`public function translate(TranslationSourceChange $change, string $vendorKey, array $context = []): TranslationSourceChange`<br>`public function assign(TranslationSourceChange $change, string $assigneeType, int\|string $assigneeId, string $role, ?string $dueAt = null): TranslationAssignment`<br>`public function review(TranslationSourceChange $change, string $decision, ?string $notes = null): TranslationSourceChange`<br>`public function addVendor(array $attributes): TranslationVendor`<br>`public function remember(string $sourceLocale, string $targetLocale, string $sourceText, string $translatedText, array $metadata = [], int\|string\|null $teamId = null): TranslationMemory`<br>`public function glossary(array $attributes): TranslationGlossary`<br>`public function reconcile(TranslationJob $job): TranslationJob` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [TranslationAssignment.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationAssignment.php) | `job_id`, `source_change_id`, `assignee_type`, `assignee_id`, `role`, `status`, `due_at`, `completed_at`, `team_id` |
| [TranslationGlossary.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationGlossary.php) | `source_locale`, `target_locale`, `source_term`, `preferred_term`, `forbidden_terms`, `team_id` |
| [TranslationJob.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationJob.php) | `public_id`, `external_key`, `name`, `source_locale`, `target_locale`, `status`, `vendor_key`, `total_units`, `completed_units`, `estimated_cost`, `actual_cost`, `currency`, `metadata`, `queued_at`, `completed_at`, `team_id` |
| [TranslationMemory.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationMemory.php) | `source_locale`, `target_locale`, `source_hash`, `source_text`, `translated_text`, `status`, `metadata`, `team_id` |
| [TranslationSourceChange.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationSourceChange.php) | `job_id`, `subject_type`, `subject_id`, `field`, `source_text`, `source_hash`, `source_version`, `translated_text`, `translated_hash`, `status`, `provider`, `model`, `cost`, `provenance`, `review_notes`, `translated_at`, `reviewed_at`, `team_id` |
| [TranslationVendor.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationVendor.php) | `key`, `name`, `driver`, `settings`, `status`, `team_id` |

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
