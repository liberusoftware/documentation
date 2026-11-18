# Crm Advertising React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-advertising). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-advertising-react-native
**Matching core package:** module-crm-crm-advertising ([implementation](../core/crm-advertising.md))
**Matching API package:** module-crm-crm-advertising-api ([contract](../api/crm-advertising.md))

## Implementation plan

This adapter presents Crm Advertising for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Advertising API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-advertising.md), and [API module](../api/crm-advertising.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-advertising`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-advertising.md)) |
| Capability React Native module skeleton | [`module-crm-advertising-react-native`](https://github.com/liberusoftware/module-crm-advertising-react-native) (`@liberusoftware/module-crm-advertising-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Ad-account connections** | Progressive mobile list/detail/sheet flow for `ad-account connections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Campaign visibility** | Progressive mobile list/detail/sheet flow for `campaign visibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lead-ad ingestion** | Progressive mobile list/detail/sheet flow for `lead-ad ingestion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **CRM audiences** | Progressive mobile list/detail/sheet flow for `crm audiences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Offline/server conversions** | Progressive mobile list/detail/sheet flow for `offline/server conversions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Spend/performance sync** | Progressive mobile list/detail/sheet flow for `spend/performance sync` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attribution** | Progressive mobile list/detail/sheet flow for `attribution` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AdvertisingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Queries/AdvertisingQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AdvertisingRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AdvertisingRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AdvertisingRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Models/AdvertisingRecord.php) | `team_id`, `kind`, `name`, `status`, `external_id`, `platform`, `payload`, `starts_at`, `ends_at`, `completed_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AdvertisingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-api/src/Http/Controllers/AdvertisingController.php) | `public function __construct(private readonly AdvertisingQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, UpsertRecord $upsert): JsonResponse`<br>`public function show(int $record): AdvertisingResource`<br>`public function update(Request $request, int $record, UpsertRecord $upsert): JsonResponse`<br>`public function transition(Request $request, int $record, TransitionRecord $transition): JsonResponse`<br>`public function destroy(int $record, TransitionRecord $transition): JsonResponse` |

**Observed route declarations:**

[modules/crm-advertising-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/advertising')->group(function (): void {
Route::get('records', [AdvertisingController::class, 'index']);
Route::post('records', [AdvertisingController::class, 'store']);
Route::get('records/{record}', [AdvertisingController::class, 'show']);
Route::patch('records/{record}', [AdvertisingController::class, 'update']);
Route::post('records/{record}/transition', [AdvertisingController::class, 'transition']);
Route::delete('records/{record}', [AdvertisingController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
