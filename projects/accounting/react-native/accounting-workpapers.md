# Accounting Workpapers React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-workpapers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-workpapers-react-native
**Matching core package:** module-accounting-accounting-workpapers ([implementation](../core/accounting-workpapers.md))
**Matching API package:** module-accounting-accounting-workpapers-api ([contract](../api/accounting-workpapers.md))

## Implementation plan

This adapter presents Accounting Workpapers for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Workpapers API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-workpapers.md), and [API module](../api/accounting-workpapers.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-workpapers`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-workpapers.md)) |
| Capability React Native module skeleton | [`module-accounting-workpapers-react-native`](https://github.com/liberusoftware/module-accounting-workpapers-react-native) (`@liberusoftware/module-accounting-workpapers-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Lead schedules** | Progressive mobile list/detail/sheet flow for `lead schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **References** | Progressive mobile list/detail/sheet flow for `references` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attachments** | Progressive mobile list/detail/sheet flow for `attachments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Procedures** | Progressive mobile list/detail/sheet flow for `procedures` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Conclusions** | Progressive mobile list/detail/sheet flow for `conclusions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Preparer/reviewer** | Progressive mobile list/detail/sheet flow for `preparer/reviewer` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rollover** | Progressive mobile list/detail/sheet flow for `rollover` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Export** | Progressive mobile list/detail/sheet flow for `export` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddWorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperAttachment.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperAttachment` |
| [AddWorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperProcedure.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperProcedure` |
| [AddWorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperReference.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperReference` |
| [AssignWorkpaperReviewer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AssignWorkpaperReviewer.php) | `public function handle(Workpaper $workpaper, int $reviewerId): Workpaper` |
| [ConcludeWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/ConcludeWorkpaper.php) | `public function handle(Workpaper $workpaper, string $conclusion): Workpaper` |
| [CreateWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/CreateWorkpaper.php) | `public function handle(array $attributes): Workpaper` |
| [RequestWorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RequestWorkpaperExport.php) | `public function handle(Workpaper $workpaper, string $format): WorkpaperExport` |
| [RolloverWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RolloverWorkpaper.php) | `public function handle(Workpaper $source, array $attributes = []): Workpaper` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Workpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/Workpaper.php) | `team_id`, `title`, `reference`, `status`, `period_start`, `period_end`, `preparer_id`, `reviewer_id`, `conclusion`, `metadata` |
| [WorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperAttachment.php) | `workpaper_id`, `name`, `disk`, `path`, `mime_type`, `size` |
| [WorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperExport.php) | `workpaper_id`, `format`, `status`, `path`, `error` |
| [WorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperProcedure.php) | `workpaper_id`, `description`, `status`, `performed_by`, `performed_at`, `evidence` |
| [WorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperReference.php) | `workpaper_id`, `label`, `target_type`, `target_id`, `notes` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkpapersController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers-api/src/Http/Controllers/WorkpapersController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateWorkpaper $action): mixed`<br>`public function procedure(Request $request, string $workpaper, AddWorkpaperProcedure $action): mixed`<br>`public function reference(Request $request, string $workpaper, AddWorkpaperReference $action): mixed`<br>`public function attachment(Request $request, string $workpaper, AddWorkpaperAttachment $action): mixed`<br>`public function reviewer(Request $request, string $workpaper, AssignWorkpaperReviewer $action): mixed`<br>`public function conclude(Request $request, string $workpaper, ConcludeWorkpaper $action): mixed`<br>`public function rollover(Request $request, string $workpaper, RolloverWorkpaper $action): mixed`<br>`public function export(Request $request, string $workpaper, RequestWorkpaperExport $action): mixed` |

**Observed route declarations:**

[modules/accounting-workpapers-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/workpapers')->middleware('auth:sanctum')->group(function (): void {
Route::get('/', [WorkpapersController::class, 'index'])->middleware('ability:accounting.workpapers.read');
Route::post('/', [WorkpapersController::class, 'store'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/references', [WorkpapersController::class, 'reference'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/attachments', [WorkpapersController::class, 'attachment'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/procedures', [WorkpapersController::class, 'procedure'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/reviewer', [WorkpapersController::class, 'reviewer'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/conclude', [WorkpapersController::class, 'conclude'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/rollover', [WorkpapersController::class, 'rollover'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/exports', [WorkpapersController::class, 'export'])->middleware('ability:accounting.workpapers.write');
```
<!-- layer-implementation-plan:end -->
