# Genealogy People React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-people). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-genealogy-people-react-native
**Matching core package:** module-genealogy-genealogy-people ([implementation](../core/genealogy-people.md))
**Matching API package:** module-genealogy-genealogy-people-api ([contract](../api/genealogy-people.md))

## Implementation plan

This adapter presents Genealogy People for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Genealogy People API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/genealogy-people.md), and [API module](../api/genealogy-people.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `genealogy-people`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-genealogy-mobile-react`](https://github.com/liberusoftware/project-genealogy-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/genealogy-people.md)) |
| Capability React Native module skeleton | [`module-genealogy-people-react-native`](https://github.com/liberusoftware/module-genealogy-people-react-native) (`@liberusoftware/module-genealogy-people-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Names** | Progressive mobile list/detail/sheet flow for `names` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Identities** | Progressive mobile list/detail/sheet flow for `identities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attributes** | Progressive mobile list/detail/sheet flow for `attributes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Life events** | Progressive mobile list/detail/sheet flow for `life events` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Living/deceased status** | Progressive mobile list/detail/sheet flow for `living/deceased status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Merge candidates** | Progressive mobile list/detail/sheet flow for `merge candidates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreateMergeCandidate.php) | `public function execute(array $attributes): MergeCandidate` |
| [CreatePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePerson.php) | `public function execute(array $attributes): Person` |
| [CreatePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonAssociation.php) | `public function execute(array $attributes): PersonAssociation` |
| [CreatePersonIdentity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonIdentity.php) | `public function execute(array $attributes): PersonIdentity` |
| [CreatePersonLifeEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonLifeEvent.php) | `public function execute(array $attributes): PersonLifeEvent` |
| [CreatePersonName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonName.php) | `public function execute(array $attributes): PersonName` |
| [DeletePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePerson.php) | `public function execute(Person $person): void` |
| [DeletePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePersonAssociation.php) | `public function execute(PersonAssociation $association): void` |
| [DeletePersonSupportingRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePersonSupportingRecord.php) | `public function execute(Model $record): void` |
| [MergePersons.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/MergePersons.php) | `public function execute(Person $primary, Person $duplicate): Person` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/MergeCandidate.php) | `team_id`, `person_id`, `candidate_person_id`, `status`, `score`, `reason`, `metadata`, `reviewed_at` |
| [Person.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/Person.php) | `team_id`, `given_name`, `family_name`, `display_name`, `sex`, `aliases`, `attributes`, `birth_date`, `death_date`, `birth_place`, `death_place`, `is_public`, `metadata` |
| [PersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonAssociation.php) | `team_id`, `person_id`, `associated_person_id`, `associated_external_id`, `relationship`, `description`, `metadata` |
| [PersonIdentity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonIdentity.php) | `team_id`, `person_id`, `type`, `value`, `label`, `is_verified`, `metadata` |
| [PersonLifeEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonLifeEvent.php) | `team_id`, `person_id`, `type`, `date`, `place`, `description`, `metadata` |
| [PersonName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonName.php) | `team_id`, `person_id`, `type`, `given_name`, `family_name`, `prefix`, `suffix`, `is_preferred`, `metadata` |
<!-- layer-implementation-plan:end -->
