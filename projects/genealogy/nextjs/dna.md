# DNA: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-genealogy-dna`.

**Proposed design identifier:** `module-genealogy-dna-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/dna.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-genealogy-dna](../../../modules/source/liberusoftware--module-genealogy-dna.md) |
| API | [liberusoftware/module-genealogy-dna-api](../../../modules/source/liberusoftware--module-genealogy-dna-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Kits | A focused authorized view or workflow section for kits; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Providers | A focused authorized view or workflow section for providers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Consent | A focused authorized view or workflow section for consent; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Match segments | A focused authorized view or workflow section for match segments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Relationships | A focused authorized view or workflow section for relationships; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Groups | A focused authorized view or workflow section for groups; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Notes | A focused authorized view or workflow section for notes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Revocation | A focused authorized view or workflow section for revocation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateDnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaGroup.php) | `public function execute(array $attributes): DnaGroup`<br>`public function validate(array $values): void` |
| [CreateDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaKit.php) | `public function execute(array $attributes): DnaKit` |
| [CreateDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaMatch.php) | `public function execute(array $attributes): DnaMatch` |
| [CreateDnaNote.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaNote.php) | `public function execute(array $attributes): DnaNote` |
| [CreateDnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaProvider.php) | `public function execute(array $attributes): DnaProvider` |
| [CreateDnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaRelationship.php) | `public function execute(array $attributes): DnaRelationship` |
| [CreateDnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaSegment.php) | `public function execute(array $attributes): DnaSegment` |
| [DeleteDnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaGroup.php) | `public function execute(DnaGroup $group): void` |
| [DeleteDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaKit.php) | `public function execute(DnaKit $kit): void` |
| [DeleteDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaMatch.php) | `public function execute(DnaMatch $match): void` |
| [DeleteDnaNote.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaNote.php) | `public function execute(DnaNote $note): void` |
| [DeleteDnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaProvider.php) | `public function execute(DnaProvider $provider): void` |
| [DeleteDnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaRelationship.php) | `public function execute(DnaRelationship $relationship): void` |
| [DeleteDnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaSegment.php) | `public function execute(DnaSegment $segment): void` |
| [GrantDnaConsent.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/GrantDnaConsent.php) | `public function execute(DnaKit $kit, string $scope, ?string $policyVersion = null): DnaConsent` |
| [ImportDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/ImportDnaKit.php) | `public function execute(string $content, array $attributes): DnaKit` |
| [PersistDnaComparison.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/PersistDnaComparison.php) | `public function execute(DnaKit $kitA, DnaKit $kitB): array` |
| [RevokeDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/RevokeDnaKit.php) | `public function execute(DnaKit $kit, string $reason): DnaKit` |
| [UpdateDnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaGroup.php) | `public function execute(DnaGroup $group, array $attributes): DnaGroup` |
| [UpdateDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaKit.php) | `public function execute(DnaKit $kit, array $attributes): DnaKit` |
| [UpdateDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaMatch.php) | `public function execute(DnaMatch $match, array $attributes): DnaMatch` |
| [UpdateDnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaProvider.php) | `public function execute(DnaProvider $provider, array $attributes): DnaProvider` |
| [UpdateDnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaRelationship.php) | `public function execute(DnaRelationship $relationship, array $attributes): DnaRelationship` |
| [UpdateDnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaSegment.php) | `public function execute(DnaSegment $segment, array $attributes): DnaSegment` |
| [AnalyzeDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/AnalyzeDnaMatch.php) | `public function analyze(array $kitA, array $kitB): array` |
| [CompareDnaKits.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/CompareDnaKits.php) | `public function execute(DnaKit $kitA, DnaKit $kitB): array` |
| [DnaFileValidator.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/DnaFileValidator.php) | `public function validate(string $content): array`<br>`public function detectFormat(string $firstLine, string $secondLine = ''): ?string` |
| [DnaFileVault.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/DnaFileVault.php) | `public function encrypt(string $plaintext): string`<br>`public function decrypt(string $ciphertext): string`<br>`public function store(string $plaintext, string $path, string $disk = 'private'): void`<br>`public function read(string $path, string $disk = 'private'): string`<br>`public function delete(string $path, string $disk = 'private'): void` |
| [ParseDnaFile.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/ParseDnaFile.php) | `public function parse(string $content): array` |
| [RelationshipEstimator.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/RelationshipEstimator.php) | `public static function labels(): array`<br>`public function estimate(float $totalSharedCm): array` |
| [SegmentMatcher.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/SegmentMatcher.php) | `public function match(array $kitA, array $kitB): array` |
| [TriangulateDna.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/TriangulateDna.php) | `public function execute(array $matches, float $minimumSharedCm = 20.0): array` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [DnaConsent.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaConsent.php) | `team_id`, `kit_id`, `scope`, `granted`, `policy_version`, `granted_at`, `revoked_at`, `revocation_reason`, `metadata` |
| [DnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaGroup.php) | `team_id`, `name`, `description`, `status`, `metadata` |
| [DnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaKit.php) | `team_id`, `name`, `provider`, `provider_id`, `external_id`, `person_id`, `test_type`, `consent_status`, `consented_at`, `revoked_at`, `revocation_reason`, `status`, `metadata`, `file_path`, `file_hash`, `file_format`, `snp_count` |
| [DnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaMatch.php) | `team_id`, `kit_id`, `external_id`, `display_name`, `predicted_relationship`, `confidence`, `total_cm`, `shared_segments`, `status`, `is_private`, `notes`, `metadata` |
| [DnaNote.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaNote.php) | `team_id`, `noteable_type`, `noteable_id`, `body` |
| [DnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaProvider.php) | `team_id`, `name`, `slug`, `status`, `website`, `metadata` |
| [DnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaRelationship.php) | `team_id`, `match_id`, `person_id`, `relationship_type`, `confidence`, `status`, `rationale`, `metadata` |
| [DnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaSegment.php) | `team_id`, `match_id`, `chromosome`, `start_position`, `end_position`, `centimorgans`, `snps`, `side`, `metadata` |

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
