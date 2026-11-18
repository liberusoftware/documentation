# Dna React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#dna). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-dna-react-native
**Matching core package:** module-genealogy-dna ([implementation](../core/dna.md))
**Matching API package:** module-genealogy-dna-api ([contract](../api/dna.md))

## Implementation plan

This adapter presents Dna for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Dna API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/dna.md), and [API module](../api/dna.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `dna`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-genealogy-mobile-react`](https://github.com/liberusoftware/project-genealogy-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/dna.md)) |
| Capability React Native module skeleton | [`module-genealogy-dna-react-native`](https://github.com/liberusoftware/module-genealogy-dna-react-native) (`@liberusoftware/module-genealogy-dna-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Kits** | Progressive mobile list/detail/sheet flow for `kits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Providers** | Progressive mobile list/detail/sheet flow for `providers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Consent** | Progressive mobile list/detail/sheet flow for `consent` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Match segments** | Progressive mobile list/detail/sheet flow for `match segments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Relationships** | Progressive mobile list/detail/sheet flow for `relationships` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Groups** | Progressive mobile list/detail/sheet flow for `groups` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Notes** | Progressive mobile list/detail/sheet flow for `notes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Revocation** | Progressive mobile list/detail/sheet flow for `revocation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaGroup.php) | `public function execute(array $attributes): DnaGroup`<br>`public function validate(array $values): void` |
| [CreateDnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaKit.php) | `public function execute(array $attributes): DnaKit` |
| [CreateDnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaMatch.php) | `public function execute(array $attributes): DnaMatch` |
| [CreateDnaNote.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaNote.php) | `public function execute(array $attributes): DnaNote` |
| [CreateDnaProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaProvider.php) | `public function execute(array $attributes): DnaProvider` |
| [CreateDnaRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaRelationship.php) | `public function execute(array $attributes): DnaRelationship` |
| [CreateDnaSegment.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaSegment.php) | `public function execute(array $attributes): DnaSegment` |
| [DeleteDnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaGroup.php) | `public function execute(DnaGroup $group): void` |
| [DeleteDnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaKit.php) | `public function __construct(private readonly DnaFileVault $vault)`<br>`public function execute(DnaKit $kit): void` |
| [DeleteDnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaMatch.php) | `public function execute(DnaMatch $match): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DnaConsent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaConsent.php) | `team_id`, `kit_id`, `scope`, `granted`, `policy_version`, `granted_at`, `revoked_at`, `revocation_reason`, `metadata` |
| [DnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaGroup.php) | `team_id`, `name`, `description`, `status`, `metadata` |
| [DnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaKit.php) | `team_id`, `name`, `provider`, `provider_id`, `external_id`, `person_id`, `test_type`, `consent_status`, `consented_at`, `revoked_at`, `revocation_reason`, `status`, `metadata`, `file_path`, `file_hash`, `file_format`, `snp_count` |
| [DnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaMatch.php) | `team_id`, `kit_id`, `external_id`, `display_name`, `predicted_relationship`, `confidence`, `total_cm`, `shared_segments`, `status`, `is_private`, `notes`, `metadata` |
| [DnaNote.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaNote.php) | `team_id`, `noteable_type`, `noteable_id`, `body` |
| [DnaProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaProvider.php) | `team_id`, `name`, `slug`, `status`, `website`, `metadata` |
| [DnaRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaRelationship.php) | `team_id`, `match_id`, `person_id`, `relationship_type`, `confidence`, `status`, `rationale`, `metadata` |
| [DnaSegment.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaSegment.php) | `team_id`, `match_id`, `chromosome`, `start_position`, `end_position`, `centimorgans`, `snps`, `side`, `metadata` |
<!-- layer-implementation-plan:end -->
