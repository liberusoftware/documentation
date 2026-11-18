# Cms Taxonomy React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-taxonomy). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-taxonomy-react-native
**Matching core package:** module-cms-cms-taxonomy ([implementation](../core/cms-taxonomy.md))
**Matching API package:** module-cms-cms-taxonomy-api ([contract](../api/cms-taxonomy.md))

## Implementation plan

This adapter presents Cms Taxonomy for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Taxonomy API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cms-taxonomy.md), and [API module](../api/cms-taxonomy.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cms-taxonomy`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-taxonomy.md)) |
| Capability React Native module skeleton | [`module-cms-taxonomy-react-native`](https://github.com/liberusoftware/module-cms-taxonomy-react-native) (`@liberusoftware/module-cms-taxonomy-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Vocabularies** | Progressive mobile list/detail/sheet flow for `vocabularies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Hierarchical terms** | Progressive mobile list/detail/sheet flow for `hierarchical terms` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Synonyms** | Progressive mobile list/detail/sheet flow for `synonyms` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Relationships** | Progressive mobile list/detail/sheet flow for `relationships` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Ordering** | Progressive mobile list/detail/sheet flow for `ordering` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Permissions** | Progressive mobile list/detail/sheet flow for `permissions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Localization** | Progressive mobile list/detail/sheet flow for `localization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Term merging** | Progressive mobile list/detail/sheet flow for `term merging` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TaxonomyQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Queries/TaxonomyQuery.php) | `public function taxonomies(?string $key = null, ?string $search = null, int $perPage = 15): LengthAwarePaginator`<br>`public function taxonomy(int $id): ?Taxonomy`<br>`public function term(int $id): ?Term`<br>`public function terms(int $taxonomyId, ?string $search = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TaxonomyService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Services/TaxonomyService.php) | `public function create(string $key, string $name, bool $hierarchical = true, bool $exclusive = false, ?int $teamId = null, ?string $description = null): Taxonomy`<br>`public function update(Taxonomy $taxonomy, array $attributes): Taxonomy`<br>`public function delete(Taxonomy $taxonomy): void`<br>`public function addTerm(Taxonomy $taxonomy, string $name, ?string $slug = null, ?int $parentId = null, array $synonyms = [], array $translations = [], ?int $position = null): Term`<br>`public function move(Term $term, ?int $parentId, ?int $position = null): Term`<br>`public function assign(Term $term, string $subjectType, int\|string $subjectId): TermAssignment`<br>`public function unassign(Term $term, string $subjectType, int\|string $subjectId): int`<br>`public function merge(Term $from, Term $into): Term`<br>`public function terms(Taxonomy $taxonomy, ?string $search = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Taxonomy.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Models/Taxonomy.php) | `key`, `name`, `description`, `hierarchical`, `exclusive`, `team_id` |
| [Term.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Models/Term.php) | `taxonomy_id`, `parent_id`, `slug`, `name`, `description`, `synonyms`, `translations`, `position`, `team_id` |
| [TermAssignment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Models/TermAssignment.php) | `term_id`, `subject_type`, `subject_id`, `team_id` |
<!-- layer-implementation-plan:end -->
