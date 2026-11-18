# Social Network Moderation React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-moderation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-moderation-react-native
**Matching core package:** module-social-network-social-network-moderation ([implementation](../core/social-network-moderation.md))
**Matching API package:** module-social-network-social-network-moderation-api ([contract](../api/social-network-moderation.md))

## Implementation plan

This adapter presents Social Network Moderation for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Moderation API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-moderation.md), and [API module](../api/social-network-moderation.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-moderation`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-moderation.md)) |
| Capability React Native module skeleton | [`module-social-network-moderation-react-native`](https://github.com/liberusoftware/module-social-network-moderation-react-native) (`@liberusoftware/module-social-network-moderation-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Reports** | Progressive mobile list/detail/sheet flow for `reports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Queues** | Progressive mobile list/detail/sheet flow for `queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Policy/rules** | Progressive mobile list/detail/sheet flow for `policy/rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Evidence** | Progressive mobile list/detail/sheet flow for `evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Actions** | Progressive mobile list/detail/sheet flow for `actions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Appeals** | Progressive mobile list/detail/sheet flow for `appeals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sanctions** | Progressive mobile list/detail/sheet flow for `sanctions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transparency** | Progressive mobile list/detail/sheet flow for `transparency` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Actions/CreateReport.php) | `public function __construct(private ModerationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $reporter, string $targetType, string $targetId, string $reason, ?string $details = null): ModerationReport` |
| [DecideReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Actions/DecideReport.php) | `public function __construct(private ModerationAuthorizer $authorizer)`<br>`public function handle(Profile $actor, ModerationReport $report, string $action, ?string $reason = null, array $evidence = []): ModerationDecision` |
| [ModerationAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Contracts/ModerationAuthorizer.php) | `public function report(Profile $reporter): void`<br>`public function decide(Profile $actor): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModerationDecision.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Models/ModerationDecision.php) | `report_id`, `actor_profile_id`, `action`, `reason`, `evidence` |
| [ModerationReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Models/ModerationReport.php) | `id`, `reporter_profile_id`, `target_type`, `target_id`, `reason`, `details`, `state`, `assigned_to` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ModerationController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation-api/src/Http/Controllers/ModerationController.php) | `public function report(Request $request, GetProfile $get, CreateReport $create): JsonResponse`<br>`public function decide(string $report, Request $request, GetProfile $get, DecideReport $decide): JsonResponse` |

**Observed route declarations:**

[modules/social-network-moderation-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/moderation')->middleware(['auth:sanctum', 'throttle:30,1'])->name('social-network.moderation.api.')->group(function (): void {
Route::post('/reports', [ModerationController::class, 'report'])->name('report');
Route::post('/reports/{report}/decide', [ModerationController::class, 'decide'])->name('decide');
```
<!-- layer-implementation-plan:end -->
