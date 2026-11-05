# Discovery: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-genealogy-discovery`.

**Proposed design identifier:** `module-genealogy-discovery-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/discovery.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-genealogy-discovery](../../../modules/source/liberusoftware--module-genealogy-discovery.md) |
| API | [liberusoftware/module-genealogy-discovery-api](../../../modules/source/liberusoftware--module-genealogy-discovery-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Person/place/source search | A focused authorized view or workflow section for person/place/source search; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Hints | A focused authorized view or workflow section for hints; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Duplicates | A focused authorized view or workflow section for duplicates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Relationship paths | A focused authorized view or workflow section for relationship paths; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Privacy-aware indexes | A focused authorized view or workflow section for privacy-aware indexes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [DiscoverySearch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/DiscoverySearch.php) | `public function execute(string $term, array $options = []): array` |
| [DuplicateCandidates.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/DuplicateCandidates.php) | `public function execute(int $limit = 100, int $minimumConfidence = 70): array` |
| [RelationshipPath.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/RelationshipPath.php) | `public function execute(string $from, string $to, int $maxDepth = 6, bool $publicOnly = false): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/CreateDiscoveryMatch.php) | `public function execute(array $attributes): DiscoveryMatch` |
| [DeleteDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/DeleteDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match): void` |
| [ReviewDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/ReviewDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match, string $status): DiscoveryMatch` |
| [ScanDuplicateCandidates.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/ScanDuplicateCandidates.php) | `public function execute(float $threshold = 0.7, int $limit = 100): array` |
| [UpdateDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/UpdateDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match, array $attributes): DiscoveryMatch` |
| [ExternalRecordMatcher.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/ExternalRecordMatcher.php) | `public function execute(array $person, array $weights = []): array`<br>`public function scoreCandidates(array $person, array $candidates, array $weights = []): array` |
| [SmartMatchingService.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/SmartMatchingService.php) | `public function findMatches(Person $person, iterable $providers, int $minimumConfidence = 60, int $limit = 10): array`<br>`public function persist(Model $user, Person $person, array $matches): Collection` |
| [SocialFamilyDiscovery.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/SocialFamilyDiscovery.php) | `public function enable(ConnectedAccount $account): bool`<br>`public function disable(ConnectedAccount $account): bool`<br>`public function sync(ConnectedAccount $account): bool`<br>`public function privacy(int\|string $userId): SocialConnectionPrivacy`<br>`public function updatePrivacy(int\|string $userId, array $settings): SocialConnectionPrivacy`<br>`public function needsSync(ConnectedAccount $account): bool`<br>`public function findPotentialConnections(Model $user): Collection`<br>`public function processMatches(Model $user): int` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [DiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/DiscoveryMatch.php) | `team_id`, `kind`, `name`, `subject_id`, `related_id`, `confidence`, `rationale`, `source_type`, `detected_at`, `reviewed_at`, `status`, `metadata` |
| [SmartMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SmartMatch.php) | `team_id`, `user_id`, `person_id`, `external_tree_id`, `external_person_id`, `match_source`, `record_category`, `match_data`, `search_criteria`, `confidence_score`, `status`, `reviewed_at` |
| [SocialConnectionPrivacy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SocialConnectionPrivacy.php) | `user_id`, `allow_family_discovery`, `show_profile_to_matches`, `share_tree_with_matches`, `allow_contact_from_matches`, `blocked_users` |
| [SocialFamilyConnection.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SocialFamilyConnection.php) | `user_id`, `connected_account_id`, `matched_social_id`, `matched_name`, `matched_email`, `relationship_type`, `confidence_score`, `matching_criteria`, `status` |

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
