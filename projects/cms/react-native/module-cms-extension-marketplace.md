# Module Cms Extension Marketplace React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-extension-marketplace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-module-cms-extension-marketplace-react-native
**Matching core package:** module-cms-module-cms-extension-marketplace ([implementation](../core/module-cms-extension-marketplace.md))
**Matching API package:** module-cms-module-cms-extension-marketplace-api ([contract](../api/module-cms-extension-marketplace.md))

## Implementation plan

This adapter presents Module Cms Extension Marketplace for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Cms Extension Marketplace API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-cms-extension-marketplace.md), and [API module](../api/module-cms-extension-marketplace.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-cms-extension-marketplace`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-extension-marketplace.md)) |
| Capability React Native module skeleton | [`module-cms-extension-marketplace-react-native`](https://github.com/liberusoftware/module-cms-extension-marketplace-react-native) (`@liberusoftware/module-cms-extension-marketplace-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Publishers** | Progressive mobile list/detail/sheet flow for `publishers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Listings** | Progressive mobile list/detail/sheet flow for `listings` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Categories** | Progressive mobile list/detail/sheet flow for `categories` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Versions** | Progressive mobile list/detail/sheet flow for `versions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Signing** | Progressive mobile list/detail/sheet flow for `signing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reviews** | Progressive mobile list/detail/sheet flow for `reviews` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Licensing** | Progressive mobile list/detail/sheet flow for `licensing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Trials** | Progressive mobile list/detail/sheet flow for `trials` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Security status** | Progressive mobile list/detail/sheet flow for `security status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Support** | Progressive mobile list/detail/sheet flow for `support` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Distribution** | Progressive mobile list/detail/sheet flow for `distribution` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ExtensionMarketplaceQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Queries/ExtensionMarketplaceQuery.php) | `public function catalog(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key): ?ExtensionListing` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExtensionMarketplaceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Services/ExtensionMarketplaceService.php) | `public function publisher(array $attributes, ?int $teamId = null): ExtensionPublisher`<br>`public function category(array $attributes): ExtensionCategory`<br>`public function listing(array $attributes, ?int $teamId = null): ExtensionListing`<br>`public function version(ExtensionListing $listing, array $attributes): ExtensionVersion`<br>`public function sign(ExtensionVersion $version, string $signature, string $key): ExtensionVersion`<br>`public function security(ExtensionListing $listing, string $status): ExtensionListing`<br>`public function review(ExtensionListing $listing, string $type, int\|string $subject, int $rating, ?string $body = null, ?int $teamId = null): ExtensionReview`<br>`public function license(ExtensionListing $listing, string $subjectType, int\|string $subject, ?int $days = null): ExtensionLicense`<br>`public function trial(ExtensionListing $listing, string $subjectType, int\|string $subject, int $days = 14): ExtensionTrial`<br>`public function support(ExtensionListing $listing, array $attributes): ExtensionSupport`<br>`public function distribute(ExtensionVersion $version, array $attributes): ExtensionDistribution`<br>`public function ratingSummary(ExtensionListing $listing): array`<br>`public function publish(ExtensionListing $listing): ExtensionListing` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ExtensionCategory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionCategory.php) | `key`, `name`, `description` |
| [ExtensionDistribution.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionDistribution.php) | `version_id`, `channel`, `url`, `checksum`, `status` |
| [ExtensionLicense.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionLicense.php) | `listing_id`, `license_key`, `subject_type`, `subject_id`, `status`, `starts_at`, `ends_at` |
| [ExtensionListing.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionListing.php) | `publisher_id`, `category_id`, `key`, `name`, `description`, `license`, `status`, `security_status`, `metadata`, `team_id` |
| [ExtensionPublisher.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionPublisher.php) | `key`, `name`, `website`, `status`, `team_id` |
| [ExtensionReview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionReview.php) | `listing_id`, `reviewer_type`, `reviewer_id`, `rating`, `review`, `status`, `team_id` |
| [ExtensionSupport.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionSupport.php) | `listing_id`, `channel`, `url`, `response_hours` |
| [ExtensionTrial.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionTrial.php) | `listing_id`, `subject_type`, `subject_id`, `status`, `starts_at`, `ends_at` |
<!-- layer-implementation-plan:end -->
