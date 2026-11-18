# Accounting Regional Packs React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-regional-packs). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-regional-packs-react-native
**Matching core package:** module-accounting-accounting-regional-packs ([implementation](../core/accounting-regional-packs.md))
**Matching API package:** module-accounting-accounting-regional-packs-api ([contract](../api/accounting-regional-packs.md))

## Implementation plan

This adapter presents Accounting Regional Packs for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Regional Packs API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-regional-packs.md), and [API module](../api/accounting-regional-packs.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-regional-packs`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-regional-packs.md)) |
| Capability React Native module skeleton | [`module-accounting-regional-packs-react-native`](https://github.com/liberusoftware/module-accounting-regional-packs-react-native) (`@liberusoftware/module-accounting-regional-packs-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Country-specific tax** | Progressive mobile list/detail/sheet flow for `country-specific tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reports** | Progressive mobile list/detail/sheet flow for `reports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Document formats** | Progressive mobile list/detail/sheet flow for `document formats` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Filing calendars** | Progressive mobile list/detail/sheet flow for `filing calendars` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Account templates** | Progressive mobile list/detail/sheet flow for `account templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Terminology** | Progressive mobile list/detail/sheet flow for `terminology` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Compliance tests** | Progressive mobile list/detail/sheet flow for `compliance tests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRegionalPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Actions/CreateRegionalPack.php) | `public function handle(array $attributes): RegionalPack` |
| [PublishRegionalPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Actions/PublishRegionalPack.php) | `public function handle(RegionalPack $pack, array $artifacts): RegionalPack` |
| [RunComplianceTests.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Actions/RunComplianceTests.php) | `public function handle(RegionalPack $pack): RegionalPack` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RegionalPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Models/RegionalPack.php) | `country_code`, `locale`, `currency`, `version`, `status`, `effective_from`, `effective_to`, `metadata` |
| [RegionalPackArtifact.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Models/RegionalPackArtifact.php) | `pack_id`, `type`, `key`, `definition`, `status`, `test_results`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [RegionalPacksController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs-api/src/Http/Controllers/RegionalPacksController.php) | `public function index(): mixed`<br>`public function store(Request $request, CreateRegionalPack $action): RegionalPack`<br>`public function show(RegionalPack $pack): RegionalPack`<br>`public function publish(Request $request, RegionalPack $pack, PublishRegionalPack $action): RegionalPack`<br>`public function test(RegionalPack $pack, RunComplianceTests $action): RegionalPack` |

**Observed route declarations:**

[modules/accounting-regional-packs-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/regional-packs')->group(function (): void {
Route::get('/', [RegionalPacksController::class, 'index']);
Route::post('/', [RegionalPacksController::class, 'store']);
Route::get('/{pack}', [RegionalPacksController::class, 'show']);
Route::post('/{pack}/publish', [RegionalPacksController::class, 'publish']);
Route::post('/{pack}/compliance-tests', [RegionalPacksController::class, 'test']);
```
<!-- layer-implementation-plan:end -->
