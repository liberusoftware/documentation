# Notifications Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#notifications). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-notifications-flutter
**Matching core package:** module-genealogy-notifications ([implementation](../core/notifications.md))
**Matching API package:** module-genealogy-notifications-api ([contract](../api/notifications.md))

## Implementation plan

This adapter presents Notifications for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Notifications API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/notifications.md), and [API module](../api/notifications.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `notifications`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-genealogy-mobile-flutter`](https://github.com/liberusoftware/project-genealogy-mobile-flutter) | [`module-notifications-flutter`](https://github.com/liberusoftware/module-notifications-flutter) (`module_notifications_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-genealogy-dart-mobile`](https://github.com/liberusoftware/project-genealogy-dart-mobile) | [`module-notifications-dart-mobile`](https://github.com/liberusoftware/module-notifications-dart-mobile) (`module_notifications_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-genealogy-dart-desktop`](https://github.com/liberusoftware/project-genealogy-dart-desktop) | [`module-notifications-dart-desktop`](https://github.com/liberusoftware/module-notifications-dart-desktop) (`module_notifications_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | [API plan](../api/notifications.md) · [Core plan](../core/notifications.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Templates** | Adaptive mobile cards/sheets for `templates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `templates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Channels** | Adaptive mobile cards/sheets for `channels` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `channels` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Preferences** | Adaptive mobile cards/sheets for `preferences` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `preferences` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Inbox** | Adaptive mobile cards/sheets for `inbox` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `inbox` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delivery status** | Adaptive mobile cards/sheets for `delivery status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delivery status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Retries** | Adaptive mobile cards/sheets for `retries` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `retries` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Quiet hours** | Adaptive mobile cards/sheets for `quiet hours` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quiet hours` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Localization** | Adaptive mobile cards/sheets for `localization` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `localization` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

**Observed route declarations:**

[modules/notifications-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/notifications-api/routes/api.php)

```php
Route::prefix('api/v1/notifications')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('notifications-api.status');
```

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
