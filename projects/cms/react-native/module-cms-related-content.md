# Module Cms Related Content React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-related-content). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-module-cms-related-content-react-native
**Matching core package:** module-cms-module-cms-related-content ([implementation](../core/module-cms-related-content.md))
**Matching API package:** module-cms-module-cms-related-content-api ([contract](../api/module-cms-related-content.md))

## Implementation plan

This adapter presents Module Cms Related Content for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Cms Related Content API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-cms-related-content.md), and [API module](../api/module-cms-related-content.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-cms-related-content`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-related-content.md)) |
| Capability React Native module skeleton | [`module-cms-related-content-react-native`](https://github.com/liberusoftware/module-cms-related-content-react-native) (`@liberusoftware/module-cms-related-content-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Manual/rule/search-driven relationships** | Progressive mobile list/detail/sheet flow for `manual/rule/search-driven relationships` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Similarity** | Progressive mobile list/detail/sheet flow for `similarity` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recency** | Progressive mobile list/detail/sheet flow for `recency` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Taxonomy** | Progressive mobile list/detail/sheet flow for `taxonomy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Exclusions** | Progressive mobile list/detail/sheet flow for `exclusions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Explainability** | Progressive mobile list/detail/sheet flow for `explainability` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fallback** | Progressive mobile list/detail/sheet flow for `fallback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RelatedContentService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-related-content/src/Services/RelatedContentService.php) | `public function relate(string $sourceType, int $sourceId, string $targetType, int $targetId, string $mode = 'manual', float $score = 1, array $taxonomy = [], ?int $teamId = null): RelatedContent`<br>`public function exclude(string $sourceType, int $sourceId, string $targetType, int $targetId, ?int $teamId = null): RelatedContent`<br>`public function remove(string $sourceType, int $sourceId, string $targetType, int $targetId, ?int $teamId = null): int`<br>`public function related(string $sourceType, int $sourceId, int $limit = 10, array $taxonomy = [], ?int $teamId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RelatedContent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-related-content/src/Models/RelatedContent.php) | `source_type`, `source_id`, `target_type`, `target_id`, `mode`, `score`, `explanation`, `taxonomy`, `excluded`, `team_id` |
<!-- layer-implementation-plan:end -->
