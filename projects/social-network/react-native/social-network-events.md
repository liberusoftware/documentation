# Social Network Events React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-events). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-events-react-native
**Matching core package:** module-social-network-social-network-events ([implementation](../core/social-network-events.md))
**Matching API package:** module-social-network-social-network-events-api ([contract](../api/social-network-events.md))

## Implementation plan

This adapter presents Social Network Events for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Events API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-events.md), and [API module](../api/social-network-events.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-events`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-events.md)) |
| Capability React Native module skeleton | [`module-social-network-events-react-native`](https://github.com/liberusoftware/module-social-network-events-react-native) (`@liberusoftware/module-social-network-events-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Events** | Progressive mobile list/detail/sheet flow for `events` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Invitations** | Progressive mobile list/detail/sheet flow for `invitations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attendance** | Progressive mobile list/detail/sheet flow for `attendance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Capacity** | Progressive mobile list/detail/sheet flow for `capacity` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Schedules** | Progressive mobile list/detail/sheet flow for `schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Locations** | Progressive mobile list/detail/sheet flow for `locations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reminders** | Progressive mobile list/detail/sheet flow for `reminders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Updates** | Progressive mobile list/detail/sheet flow for `updates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/AddEventUpdate.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event, string $body): EventUpdate` |
| [CreateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/CreateEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, array $data): Event` |
| [InviteProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/InviteProfile.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $owner, Event $event, Profile $invitee): Invitation` |
| [ListEvents.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ListEvents.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [PublishEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/PublishEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event): Event` |
| [ScheduleReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ScheduleReminder.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Event $event, string $sendAt): EventReminder` |
| [SetAttendance.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/SetAttendance.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Event $event, string $state): void` |
| [UpdateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/UpdateEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event, array $data): Event` |
| [EventsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Contracts/EventsAuthorizer.php) | `public function create(Profile $owner): void`<br>`public function manage(Profile $owner, Event $event): void`<br>`public function attend(Profile $profile, Event $event): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Event.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Event.php) | `id`, `owner_profile_id`, `state`, `visibility`, `timezone`, `title`, `description`, `starts_at`, `ends_at`, `capacity`, `location`, `metadata` |
| [EventReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventReminder.php) | `event_id`, `profile_id`, `send_at`, `sent_at` |
| [EventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventUpdate.php) | `event_id`, `author_profile_id`, `body` |
| [Invitation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Invitation.php) | `event_id`, `profile_id`, `state` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EventsController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-api/src/Http/Controllers/EventsController.php) | `public function index(Request $request, GetProfile $get, ListEvents $list): JsonResponse`<br>`public function store(Request $request, GetProfile $get, CreateEvent $create): JsonResponse`<br>`public function update(Event $event, Request $request, GetProfile $get, UpdateEvent $update): JsonResponse`<br>`public function publish(Event $event, Request $request, GetProfile $get, PublishEvent $publish): JsonResponse`<br>`public function invite(Event $event, Request $request, GetProfile $get, InviteProfile $invite): JsonResponse`<br>`public function attendance(Event $event, Request $request, GetProfile $get, SetAttendance $set): JsonResponse`<br>`public function updateLog(Event $event, Request $request, GetProfile $get, AddEventUpdate $add): JsonResponse`<br>`public function reminder(Event $event, Request $request, GetProfile $get, ScheduleReminder $schedule): JsonResponse` |

**Observed route declarations:**

[modules/social-network-events-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/events')
Route::get('/', [EventsController::class, 'index'])->name('index');
Route::post('/', [EventsController::class, 'store'])->name('store');
Route::patch('/{event}', [EventsController::class, 'update'])->name('update');
Route::post('/{event}/publish', [EventsController::class, 'publish'])->name('publish');
Route::post('/{event}/invitations', [EventsController::class, 'invite'])->name('invite');
Route::post('/{event}/attendance', [EventsController::class, 'attendance'])->name('attendance');
Route::post('/{event}/updates', [EventsController::class, 'updateLog'])->name('updates.store');
Route::post('/{event}/reminders', [EventsController::class, 'reminder'])->name('reminders.store');
```
<!-- layer-implementation-plan:end -->
