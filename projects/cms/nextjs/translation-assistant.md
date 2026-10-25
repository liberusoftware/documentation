# Translation Assistant: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-cms-translation-assistant`.

**Proposed design identifier:** `module-cms-translation-assistant-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/translation-assistant.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **3 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-cms-translation-assistant](../../../modules/source/liberusoftware--module-cms-translation-assistant.md) |
| API | [liberusoftware/module-cms-translation-assistant-api](../../../modules/source/liberusoftware--module-cms-translation-assistant-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Draft translations | A focused authorized view or workflow section for draft translations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Glossary/style enforcement | A focused authorized view or workflow section for glossary/style enforcement; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Confidence | A focused authorized view or workflow section for confidence; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Review | A focused authorized view or workflow section for review; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Provider/model provenance | A focused authorized view or workflow section for provider/model provenance; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [TranslationAssistantQuery.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Queries/TranslationAssistantQuery.php) | `public function drafts(array $filters = [], int $perPage = 25, ?int $teamId = null): LengthAwarePaginator`<br>`public function draft(int\|string $id, ?int $teamId = null): ?TranslationDraft`<br>`public function glossary(?string $sourceLocale = null, ?string $targetLocale = null, ?int $teamId = null): array`<br>`public function styleRules(?string $locale = null, ?int $teamId = null): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [TranslationAssistantService.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Services/TranslationAssistantService.php) | `public function draft(string $subjectType, int\|string $subjectId, string $sourceLocale, string $targetLocale, string $sourceText, string $translatedText, float $confidence, string $provider, string $model, array $provenance = [], ?int $teamId = null): TranslationDraft`<br>`public function check(TranslationDraft $draft): TranslationDraft`<br>`public function review(TranslationDraft $draft, string $decision, string $reviewerType, int\|string $reviewerId): TranslationDraft`<br>`public function updateDraft(TranslationDraft $draft, array $attributes): TranslationDraft`<br>`public function removeDraft(TranslationDraft $draft): void`<br>`public function addGlossary(string $sourceLocale, string $targetLocale, string $sourceTerm, string $preferredTerm, array $forbiddenTerms = [], ?int $teamId = null): GlossaryEntry`<br>`public function addStyleRule(string $locale, string $name, string $pattern, string $message, string $severity = 'warning', ?int $teamId = null): StyleRule` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [GlossaryEntry.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Models/GlossaryEntry.php) | `source_locale`, `target_locale`, `source_term`, `preferred_term`, `forbidden_terms`, `team_id` |
| [StyleRule.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Models/StyleRule.php) | `locale`, `name`, `pattern`, `message`, `severity`, `team_id` |
| [TranslationDraft.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Models/TranslationDraft.php) | `subject_type`, `subject_id`, `source_locale`, `target_locale`, `source_text`, `translated_text`, `confidence`, `status`, `provider`, `model`, `provenance`, `violations`, `reviewer_type`, `reviewer_id`, `reviewed_at`, `team_id` |

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
