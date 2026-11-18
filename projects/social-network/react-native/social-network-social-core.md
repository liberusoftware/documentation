# Social Network Social Core React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-social-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-social-core-react-native
**Matching core package:** module-social-network-social-network-social-core ([implementation](../core/social-network-social-core.md))
**Matching API package:** module-social-network-social-network-social-core-api ([contract](../api/social-network-social-core.md))

## Implementation plan

This adapter presents Social Network Social Core for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Social Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-social-core.md), and [API module](../api/social-network-social-core.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-social-core`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-social-core.md)) |
| Capability React Native module skeleton | [`module-social-network-social-core-react-native`](https://github.com/liberusoftware/module-social-network-social-core-react-native) (`@liberusoftware/module-social-network-social-core-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Network settings** | Progressive mobile list/detail/sheet flow for `network settings` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deployment mode** | Progressive mobile list/detail/sheet flow for `deployment mode` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Terminology** | Progressive mobile list/detail/sheet flow for `terminology` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Feature policy** | Progressive mobile list/detail/sheet flow for `feature policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Shared IDs** | Progressive mobile list/detail/sheet flow for `shared ids` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Events** | Progressive mobile list/detail/sheet flow for `events` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
