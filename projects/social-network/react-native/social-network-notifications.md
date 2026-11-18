# Social Network Notifications React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-notifications). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-notifications-react-native
**Matching core package:** module-social-network-social-network-notifications ([implementation](../core/social-network-notifications.md))
**Matching API package:** module-social-network-social-network-notifications-api ([contract](../api/social-network-notifications.md))

## Implementation plan

This adapter presents Social Network Notifications for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Notifications API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-notifications.md), and [API module](../api/social-network-notifications.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-notifications`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-notifications.md)) |
| Capability React Native module skeleton | [`module-social-network-notifications-react-native`](https://github.com/liberusoftware/module-social-network-notifications-react-native) (`@liberusoftware/module-social-network-notifications-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Preferences** | Progressive mobile list/detail/sheet flow for `preferences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **In-app/email/push delivery** | Progressive mobile list/detail/sheet flow for `in-app/email/push delivery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Grouping** | Progressive mobile list/detail/sheet flow for `grouping` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Digests** | Progressive mobile list/detail/sheet flow for `digests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quiet hours** | Progressive mobile list/detail/sheet flow for `quiet hours` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Read state** | Progressive mobile list/detail/sheet flow for `read state` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/CreateNotification.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(string $profileId, string $kind, array $payload = [], string $channel = 'in_app', ?string $groupKey = null): SocialNotification` |
| [DismissNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/DismissNotification.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, string $id): SocialNotification` |
| [MarkAllRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/MarkAllRead.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile): int` |
| [MarkRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/MarkRead.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, string $id): SocialNotification` |
| [UnreadCount.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/UnreadCount.php) | `public function __construct(private NotificationAuthorizer $authorizer)`<br>`public function handle(Profile $profile): int` |
| [UpdatePreferences.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/UpdatePreferences.php) | `public function __construct(private NotificationAuthorizer $authorizer)`<br>`public function handle(Profile $profile, array $data): NotificationPreference` |
| [NotificationAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Contracts/NotificationAuthorizer.php) | `public function manage(Profile $profile): void`<br>`public function view(Profile $profile): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [NotificationPreference.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Models/NotificationPreference.php) | `profile_id`, `channels`, `quiet_hours`, `digest` |
| [SocialNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Models/SocialNotification.php) | `id`, `profile_id`, `kind`, `group_key`, `state`, `channel`, `payload`, `read_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [NotificationsController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-api/src/Http/Controllers/NotificationsController.php) | `public function index(Request $request, GetProfile $get): JsonResponse`<br>`public function preferences(Request $request, GetProfile $get, UpdatePreferences $update): JsonResponse`<br>`public function unreadCount(Request $request, GetProfile $get, UnreadCount $count): JsonResponse`<br>`public function readAll(Request $request, GetProfile $get, MarkAllRead $read): JsonResponse`<br>`public function read(string $notification, Request $request, GetProfile $get, MarkRead $read): JsonResponse`<br>`public function dismiss(string $notification, Request $request, GetProfile $get, DismissNotification $dismiss): JsonResponse` |

**Observed route declarations:**

[modules/social-network-notifications-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/notifications')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.notifications.api.')->group(function (): void {
Route::get('/', [NotificationsController::class, 'index'])->name('index');
Route::get('/unread-count', [NotificationsController::class, 'unreadCount'])->name('unread-count');
Route::post('/read-all', [NotificationsController::class, 'readAll'])->name('read-all');
Route::patch('/preferences', [NotificationsController::class, 'preferences'])->name('preferences');
Route::post('/{notification}/read', [NotificationsController::class, 'read'])->name('read');
Route::post('/{notification}/dismiss', [NotificationsController::class, 'dismiss'])->name('dismiss');
```
<!-- layer-implementation-plan:end -->
