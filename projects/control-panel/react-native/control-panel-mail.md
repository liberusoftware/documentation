# Control Panel Mail React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-mail). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-mail-react-native
**Matching core package:** module-control-panel-control-panel-mail ([implementation](../core/control-panel-mail.md))
**Matching API package:** module-control-panel-control-panel-mail-api ([contract](../api/control-panel-mail.md))

## Implementation plan

This adapter presents Control Panel Mail for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Mail API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/control-panel-mail.md), and [API module](../api/control-panel-mail.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `control-panel-mail`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-mail.md)) |
| Capability React Native module skeleton | [`module-control-panel-mail-react-native`](https://github.com/liberusoftware/module-control-panel-mail-react-native) (`@liberusoftware/module-control-panel-mail-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Domains** | Progressive mobile list/detail/sheet flow for `domains` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Mailboxes** | Progressive mobile list/detail/sheet flow for `mailboxes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Aliases** | Progressive mobile list/detail/sheet flow for `aliases` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Routing** | Progressive mobile list/detail/sheet flow for `routing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quotas** | Progressive mobile list/detail/sheet flow for `quotas` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Spam/virus controls** | Progressive mobile list/detail/sheet flow for `spam/virus controls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **DKIM** | Progressive mobile list/detail/sheet flow for `dkim` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery diagnostics** | Progressive mobile list/detail/sheet flow for `delivery diagnostics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListMailAccounts.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Queries/ListMailAccounts.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureMailAuthentication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailAuthentication.php) | `public function __construct(private readonly RotateDkimKey $rotateDkimKey)`<br>`public function execute(MailDomain $domain, array $attributes = []): MailDomain` |
| [ConfigureMailControls.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailControls.php) | `public function execute(array $a): MailControl` |
| [CreateMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAccount.php) | `public function execute(array $attributes): MailAccount` |
| [CreateMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAlias.php) | `public function execute(array $a): MailAlias` |
| [CreateMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailRoute.php) | `public function execute(array $attributes): MailRoute` |
| [DeleteMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAccount.php) | `public function execute(MailAccount $account): void` |
| [DeleteMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAlias.php) | `public function execute(MailAlias $alias): void` |
| [DeleteMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailRoute.php) | `public function execute(MailRoute $route): void` |
| [RecordDeliveryDiagnostic.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordDeliveryDiagnostic.php) | `public function execute(array $a): DeliveryDiagnostic` |
| [RecordMailOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordMailOperation.php) | `public function execute(array $a): MailOperation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DeliveryDiagnostic.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DeliveryDiagnostic.php) | `id`, `team_id`, `mail_account_id`, `message_id`, `recipient`, `status`, `response`, `checked_at` |
| [DkimKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DkimKey.php) | `id`, `team_id`, `domain`, `selector`, `public_key`, `private_key`, `active`, `rotated_at` |
| [MailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAccount.php) | `team_id`, `domain`, `address`, `status`, `quota_bytes`, `settings` |
| [MailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAlias.php) | `id`, `team_id`, `domain`, `address`, `destinations`, `active` |
| [MailControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailControl.php) | `id`, `team_id`, `mail_account_id`, `spam_filter_enabled`, `spam_threshold`, `spam_action`, `virus_scan_enabled`, `autoresponder_enabled`, `autoresponder_subject`, `autoresponder_message`, `autoresponder_start_at`, `autoresponder_end_at`, `keep_copy_on_server` |
| [MailDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailDomain.php) | `id`, `team_id`, `domain`, `status`, `dkim`, `spf`, `dmarc` |
| [MailOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailOperation.php) | `id`, `team_id`, `mail_account_id`, `operation`, `status`, `details` |
| [MailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailRoute.php) | `id`, `team_id`, `domain`, `source_pattern`, `destination`, `priority`, `active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MailAccountController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/src/Http/Controllers/MailAccountController.php) | `public function index(Request $request, ListMailAccounts $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateMailAccount $create): JsonResponse`<br>`public function update(Request $request, string $id, UpdateMailAccount $update): JsonResponse`<br>`public function delete(Request $request, string $id, DeleteMailAccount $delete): JsonResponse`<br>`public function operation(Request $request, RecordMailOperation $record): JsonResponse`<br>`public function alias(Request $request, CreateMailAlias $create): JsonResponse`<br>`public function updateAlias(Request $request, string $id, UpdateMailAlias $update): JsonResponse`<br>`public function deleteAlias(Request $request, string $id, DeleteMailAlias $delete): JsonResponse`<br>`public function updateRoute(Request $request, string $id, UpdateMailRoute $update): JsonResponse`<br>`public function deleteRoute(Request $request, string $id, DeleteMailRoute $delete): JsonResponse`<br>`public function route(Request $request, CreateMailRoute $create): JsonResponse`<br>`public function controls(Request $request, ConfigureMailControls $configure): JsonResponse`<br>`public function diagnostic(Request $request, RecordDeliveryDiagnostic $record): JsonResponse`<br>`public function rotateDkim(Request $request, RotateDkimKey $rotate): JsonResponse`<br>`public function authentication(Request $request, ConfigureMailAuthentication $configure): JsonResponse`<br>`public function domain(Request $request, RegisterMailDomain $register): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-mail-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/mail')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [MailAccountController::class, 'index'])->name('control-panel.mail.index');
Route::post('/', [MailAccountController::class, 'store'])->name('control-panel.mail.store');
Route::post('/operations', [MailAccountController::class, 'operation'])->name('control-panel.mail.operations.store');
Route::post('/aliases', [MailAccountController::class, 'alias'])->name('control-panel.mail.aliases.store');
Route::patch('/aliases/{alias}', [MailAccountController::class, 'updateAlias'])->name('control-panel.mail.aliases.update');
Route::delete('/aliases/{alias}', [MailAccountController::class, 'deleteAlias'])->name('control-panel.mail.aliases.delete');
Route::post('/routes', [MailAccountController::class, 'route'])->name('control-panel.mail.routes.store');
Route::patch('/routes/{route}', [MailAccountController::class, 'updateRoute'])->name('control-panel.mail.routes.update');
Route::delete('/routes/{route}', [MailAccountController::class, 'deleteRoute'])->name('control-panel.mail.routes.delete');
Route::post('/controls', [MailAccountController::class, 'controls'])->name('control-panel.mail.controls.store');
Route::post('/delivery-diagnostics', [MailAccountController::class, 'diagnostic'])->name('control-panel.mail.delivery-diagnostics.store');
Route::post('/dkim/rotate', [MailAccountController::class, 'rotateDkim'])->name('control-panel.mail.dkim.rotate');
Route::post('/authentication/configure', [MailAccountController::class, 'authentication'])->name('control-panel.mail.authentication.configure');
Route::post('/domains', [MailAccountController::class, 'domain'])->name('control-panel.mail.domains.store');
Route::patch('/{mailAccount}', [MailAccountController::class, 'update'])->name('control-panel.mail.update');
Route::delete('/{mailAccount}', [MailAccountController::class, 'delete'])->name('control-panel.mail.delete');
Route::get('/{mailAccount}', [MailAccountController::class, 'show'])->name('control-panel.mail.show');
```
<!-- layer-implementation-plan:end -->
