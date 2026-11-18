# Mail Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mail). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-mail-flutter
**Matching core package:** module-control-panel-mail ([implementation](../core/mail.md))
**Matching API package:** module-control-panel-mail-api ([contract](../api/mail.md))

## Implementation plan

This adapter presents Mail for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Mail API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/mail.md), and [API module](../api/mail.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `mail`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-mail-flutter`](https://github.com/liberusoftware/module-control-panel-mail-flutter) (`module_control_panel_mail_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-mail-dart-mobile`](https://github.com/liberusoftware/module-control-panel-mail-dart-mobile) (`module_control_panel_mail_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-mail-dart-desktop`](https://github.com/liberusoftware/module-control-panel-mail-dart-desktop) (`module_control_panel_mail_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/mail.md) · [Core plan](../core/mail.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Domains** | Adaptive mobile cards/sheets for `domains` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `domains` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Mailboxes** | Adaptive mobile cards/sheets for `mailboxes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mailboxes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Aliases** | Adaptive mobile cards/sheets for `aliases` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `aliases` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Routing** | Adaptive mobile cards/sheets for `routing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `routing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Quotas** | Adaptive mobile cards/sheets for `quotas` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quotas` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Spam/virus controls** | Adaptive mobile cards/sheets for `spam/virus controls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `spam/virus controls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **DKIM** | Adaptive mobile cards/sheets for `dkim` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `dkim` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delivery diagnostics** | Adaptive mobile cards/sheets for `delivery diagnostics` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delivery diagnostics` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
