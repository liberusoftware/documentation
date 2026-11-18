# Jetstream Bridge Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#jetstream-bridge). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-jetstream-bridge-flutter
**Matching core package:** module-browser-game-jetstream-bridge ([implementation](../core/jetstream-bridge.md))
**Matching API package:** module-browser-game-jetstream-bridge-api ([contract](../api/jetstream-bridge.md))

## Implementation plan

This adapter presents Jetstream Bridge for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Jetstream Bridge API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/jetstream-bridge.md), and [API module](../api/jetstream-bridge.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `jetstream-bridge`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-browser-game-mobile-flutter`](https://github.com/liberusoftware/project-browser-game-mobile-flutter) | [`module-jetstream-bridge-flutter`](https://github.com/liberusoftware/module-jetstream-bridge-flutter) (`module_jetstream_bridge_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-browser-game-dart-mobile`](https://github.com/liberusoftware/project-browser-game-dart-mobile) | [`module-jetstream-bridge-dart-mobile`](https://github.com/liberusoftware/module-jetstream-bridge-dart-mobile) (`module_jetstream_bridge_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-browser-game-dart-desktop`](https://github.com/liberusoftware/project-browser-game-dart-desktop) | [`module-jetstream-bridge-dart-desktop`](https://github.com/liberusoftware/module-jetstream-bridge-dart-desktop) (`module_jetstream_bridge_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | [API plan](../api/jetstream-bridge.md) · [Core plan](../core/jetstream-bridge.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Jetstream-compatible profile** | Adaptive mobile cards/sheets for `jetstream-compatible profile` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `jetstream-compatible profile` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Security** | Adaptive mobile cards/sheets for `security` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `security` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Team** | Adaptive mobile cards/sheets for `team` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `team` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Token** | Adaptive mobile cards/sheets for `token` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `token` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Session** | Adaptive mobile cards/sheets for `session` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `session` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Account-deletion action contracts** | Adaptive mobile cards/sheets for `account-deletion action contracts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `account-deletion action contracts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateNewUser.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/CreateNewUser.php) | `public function __construct( private readonly RegistrationPolicy $registration, private readonly InvitationValidator $invitations, private readonly IdentifierNormalizer $normalizer, )`<br>`public function create(array $input): User` |
| [PasswordValidationRules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/PasswordValidationRules.php) | No named public method detected by the static index. |
| [ResetUserPassword.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/ResetUserPassword.php) | `public function reset(User $user, array $input): void` |
| [UpdateUserPassword.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/UpdateUserPassword.php) | `public function update(User $user, array $input): void` |
| [UpdateUserProfileInformation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/UpdateUserProfileInformation.php) | `public function __construct(private readonly IdentifierNormalizer $normalizer)`<br>`public function update(User $user, array $input): void` |
| [DeleteUser.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Jetstream/DeleteUser.php) | `public function __construct(DeletesTeams $deletesTeams)`<br>`public function delete($user)` |

**Observed route declarations:**

[modules/jetstream-bridge-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/jetstream-bridge-api/routes/api.php)

```php
Route::prefix('api/v1/jetstream-bridge')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('jetstream-bridge-api.status');
```
<!-- layer-implementation-plan:end -->
