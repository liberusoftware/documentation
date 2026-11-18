# Social Network Social Core Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-social-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-social-core-flutter
**Matching core package:** module-social-network-social-network-social-core ([implementation](../core/social-network-social-core.md))
**Matching API package:** module-social-network-social-network-social-core-api ([contract](../api/social-network-social-core.md))

## Implementation plan

This adapter presents Social Network Social Core for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Social Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/social-network-social-core.md), and [API module](../api/social-network-social-core.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `social-network-social-core`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) | [`module-social-network-social-core-flutter`](https://github.com/liberusoftware/module-social-network-social-core-flutter) (`module_social_network_social_core_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) | [`module-social-network-social-core-dart-mobile`](https://github.com/liberusoftware/module-social-network-social-core-dart-mobile) (`module_social_network_social_core_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) | [`module-social-network-social-core-dart-desktop`](https://github.com/liberusoftware/module-social-network-social-core-dart-desktop) (`module_social_network_social_core_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | [API plan](../api/social-network-social-core.md) · [Core plan](../core/social-network-social-core.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Network settings** | Adaptive mobile cards/sheets for `network settings` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `network settings` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Deployment mode** | Adaptive mobile cards/sheets for `deployment mode` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `deployment mode` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Terminology** | Adaptive mobile cards/sheets for `terminology` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `terminology` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Feature policy** | Adaptive mobile cards/sheets for `feature policy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `feature policy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Shared IDs** | Adaptive mobile cards/sheets for `shared ids` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `shared ids` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Events** | Adaptive mobile cards/sheets for `events` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `events` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GetSocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Actions/GetSocialNetworkSettings.php) | `public function __construct(private SocialNetworkSettingsRepository $settings)`<br>`public function handle(int\|string $teamId): SocialNetworkSettings` |
| [UpdateSocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Actions/UpdateSocialNetworkSettings.php) | `public function __construct( private SocialNetworkSettingsRepository $settings, private SocialNetworkSettingsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(int\|string $teamId, array $attributes, int\|string\|null $actorId = null): SocialNetworkSettings` |
| [SocialNetworkSettingsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Contracts/SocialNetworkSettingsAuthorizer.php) | `public function authorize(int\|string $teamId): void` |
| [SocialNetworkSettingsRepository.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Contracts/SocialNetworkSettingsRepository.php) | `public function forTeam(int\|string $teamId): SocialNetworkSettings` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Models/SocialNetworkSettings.php) | `id`, `team_id`, `deployment_mode`, `network_settings`, `terminology`, `feature_policy`, `shared_ids` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SocialCoreSettingsController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-api/src/Http/Controllers/SocialCoreSettingsController.php) | `public function show(Request $request, GetSocialNetworkSettings $get): JsonResponse`<br>`public function update(Request $request, UpdateSocialNetworkSettings $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-social-core-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/social-core')
Route::get('/', [SocialCoreSettingsController::class, 'show'])->name('show');
Route::patch('/', [SocialCoreSettingsController::class, 'update'])->name('update');
```
<!-- layer-implementation-plan:end -->
