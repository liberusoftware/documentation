# Cms Notifications And Subscriptions React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-notifications-and-subscriptions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-notifications-and-subscriptions-react-native
**Matching core package:** module-cms-cms-notifications-and-subscriptions ([implementation](../core/cms-notifications-and-subscriptions.md))
**Matching API package:** module-cms-cms-notifications-and-subscriptions-api ([contract](../api/cms-notifications-and-subscriptions.md))

## Implementation plan

This adapter presents Cms Notifications And Subscriptions for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Notifications And Subscriptions API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cms-notifications-and-subscriptions.md), and [API module](../api/cms-notifications-and-subscriptions.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cms-notifications-and-subscriptions`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-notifications-and-subscriptions.md)) |
| Capability React Native module skeleton | [`module-cms-notifications-and-subscriptions-react-native`](https://github.com/liberusoftware/module-cms-notifications-and-subscriptions-react-native) (`@liberusoftware/module-cms-notifications-and-subscriptions-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Follow content/terms/authors** | Progressive mobile list/detail/sheet flow for `follow content/terms/authors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Publication/update digests** | Progressive mobile list/detail/sheet flow for `publication/update digests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Frequency** | Progressive mobile list/detail/sheet flow for `frequency` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Channel preferences** | Progressive mobile list/detail/sheet flow for `channel preferences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Unsubscribe** | Progressive mobile list/detail/sheet flow for `unsubscribe` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery state** | Progressive mobile list/detail/sheet flow for `delivery state` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SubscriptionService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-notifications-and-subscriptions/src/Services/SubscriptionService.php) | `public function follow(string $subscriberType, int\|string $subscriberId, string $subjectType, int\|string $subjectId, string $frequency = 'instant', array $channels = ['mail'], ?string $locale = null, ?int $teamId = null): Subscription`<br>`public function updatePreferences(Subscription $subscription, string $frequency, array $channels, ?string $locale = null): Subscription`<br>`public function unsubscribe(Subscription $subscription): Subscription`<br>`public function queueEvent(string $event, string $subjectType, int\|string $subjectId, array $payload = [], ?int $teamId = null): int`<br>`public function pending(?string $channel = null): array`<br>`public function markSent(Delivery $delivery): Delivery`<br>`public function markFailed(Delivery $delivery): Delivery` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Delivery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-notifications-and-subscriptions/src/Models/Delivery.php) | `subscription_id`, `event`, `channel`, `payload`, `status`, `attempts`, `sent_at`, `failed_at`, `team_id` |
| [Subscription.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-notifications-and-subscriptions/src/Models/Subscription.php) | `subscriber_type`, `subscriber_id`, `subject_type`, `subject_id`, `frequency`, `channels`, `locale`, `active`, `unsubscribed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
