# Relationships React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#relationships). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-relationships-react-native
**Matching core package:** module-genealogy-relationships ([implementation](../core/relationships.md))
**Matching API package:** module-genealogy-relationships-api ([contract](../api/relationships.md))

## Implementation plan

This adapter presents Relationships for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Relationships API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/relationships.md), and [API module](../api/relationships.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `relationships`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-genealogy-mobile-react`](https://github.com/liberusoftware/project-genealogy-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/relationships.md)) |
| Capability React Native module skeleton | [`module-genealogy-relationships-react-native`](https://github.com/liberusoftware/module-genealogy-relationships-react-native) (`@liberusoftware/module-genealogy-relationships-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Parent** | Progressive mobile list/detail/sheet flow for `parent` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Partner** | Progressive mobile list/detail/sheet flow for `partner` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Household** | Progressive mobile list/detail/sheet flow for `household` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Adoption** | Progressive mobile list/detail/sheet flow for `adoption` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Guardianship** | Progressive mobile list/detail/sheet flow for `guardianship` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Uncertain links** | Progressive mobile list/detail/sheet flow for `uncertain links` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Graph validation** | Progressive mobile list/detail/sheet flow for `graph validation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [GraphValidator.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/GraphValidator.php) | `public function validate(string $personId, string $relatedPersonId, string $type, ?string $ignoreRelationshipId = null): array`<br>`public function assertValid(string $personId, string $relatedPersonId, string $type, ?string $ignoreRelationshipId = null): void` |
| [ParentGraph.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/ParentGraph.php) | `public function relatedPeople(string $teamId, array $personIds, bool $ancestors): array` |
| [RelationshipCalculator.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/RelationshipCalculator.php) | `public function between(string $firstPersonId, string $secondPersonId, ?string $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/CreateRelationship.php) | `public function execute(array $attributes): Relationship` |
| [DeleteRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/DeleteRelationship.php) | `public function execute(Relationship $relationship): void` |
| [RecordRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/RecordRelationship.php) | `public function execute(array $attributes): Relationship` |
| [UpdateRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/UpdateRelationship.php) | `public function __construct(private readonly GraphValidator $validator)`<br>`public function execute(Relationship $relationship, array $attributes): Relationship` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Relationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Models/Relationship.php) | `team_id`, `person_id`, `related_person_id`, `type`, `confidence`, `metadata` |
<!-- layer-implementation-plan:end -->
