# Control Panel Security Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-security). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-security-flutter
**Matching core package:** module-control-panel-control-panel-security ([implementation](../core/control-panel-security.md))
**Matching API package:** module-control-panel-control-panel-security-api ([contract](../api/control-panel-security.md))

## Implementation plan

This adapter presents Control Panel Security for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Security API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/control-panel-security.md), and [API module](../api/control-panel-security.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `control-panel-security`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-security-flutter`](https://github.com/liberusoftware/module-control-panel-security-flutter) (`module_control_panel_security_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-security-dart-mobile`](https://github.com/liberusoftware/module-control-panel-security-dart-mobile) (`module_control_panel_security_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-security-dart-desktop`](https://github.com/liberusoftware/module-control-panel-security-dart-desktop) (`module_control_panel_security_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/control-panel-security.md) · [Core plan](../core/control-panel-security.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Hardening** | Adaptive mobile cards/sheets for `hardening` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `hardening` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Patching** | Adaptive mobile cards/sheets for `patching` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `patching` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **MFA/RBAC** | Adaptive mobile cards/sheets for `mfa/rbac` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mfa/rbac` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Secrets** | Adaptive mobile cards/sheets for `secrets` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `secrets` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Malware** | Adaptive mobile cards/sheets for `malware` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `malware` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Intrusion controls** | Adaptive mobile cards/sheets for `intrusion controls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `intrusion controls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Vulnerability and compliance status** | Adaptive mobile cards/sheets for `vulnerability and compliance status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `vulnerability and compliance status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListFindings.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Queries/ListFindings.php) | `public function execute(string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureFail2ban.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/ConfigureFail2ban.php) | `public function execute(array $attributes): Fail2banSetting` |
| [RecordFail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordFail2banBan.php) | `public function execute(Fail2banSetting $setting, array $attributes): Fail2banBan` |
| [RecordFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordFinding.php) | `public function execute(array $attributes): SecurityFinding` |
| [RecordSecurityResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordSecurityResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [ResolveSecurityFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/ResolveSecurityFinding.php) | `public function execute(SecurityFinding $finding): SecurityFinding` |
| [StoreSecret.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/StoreSecret.php) | `public function execute(array $attributes): SecretRecord` |
| [UnbanFail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/UnbanFail2banBan.php) | `public function execute(Fail2banBan $ban): Fail2banBan` |
| [UpdateSecurityFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/UpdateSecurityFinding.php) | `public function execute(SecurityFinding $finding, array $attributes): SecurityFinding` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ComplianceStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/ComplianceStatus.php) | `team_id`, `framework`, `control`, `status`, `score`, `evidence`, `assessed_at`, `expires_at` |
| [Fail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/Fail2banBan.php) | `team_id`, `jail_name`, `ip_address`, `banned_at`, `unbanned_at`, `ban_count`, `reason` |
| [Fail2banSetting.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/Fail2banSetting.php) | `team_id`, `jail_name`, `enabled`, `max_retry`, `find_time`, `ban_time`, `whitelist_ips` |
| [HardeningControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/HardeningControl.php) | `team_id`, `subject_type`, `subject_id`, `control`, `desired`, `observed`, `status`, `evidence`, `checked_at` |
| [IntrusionControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/IntrusionControl.php) | `team_id`, `subject_type`, `subject_id`, `kind`, `action`, `threshold`, `window_seconds`, `enabled`, `metadata` |
| [MalwareScan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/MalwareScan.php) | `team_id`, `subject_type`, `subject_id`, `status`, `scanner`, `findings`, `started_at`, `finished_at` |
| [MfaRbacPolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/MfaRbacPolicy.php) | `team_id`, `subject_type`, `subject_id`, `mfa_required`, `roles`, `permissions`, `status`, `metadata` |
| [PatchRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/PatchRecord.php) | `team_id`, `subject_type`, `subject_id`, `package`, `current_version`, `target_version`, `severity`, `status`, `published_at`, `installed_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SecurityFindingController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/src/Http/Controllers/SecurityFindingController.php) | `public function index(Request $request, ListFindings $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, RecordFinding $record): JsonResponse`<br>`public function resolve(Request $request, string $id, ResolveSecurityFinding $resolve): JsonResponse`<br>`public function update(Request $request, string $id, UpdateSecurityFinding $update): JsonResponse`<br>`public function hardening(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function patch(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function patches(Request $request): JsonResponse`<br>`public function policy(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function policies(Request $request): JsonResponse`<br>`public function secret(Request $request, StoreSecret $store): JsonResponse`<br>`public function secrets(Request $request): JsonResponse`<br>`public function malware(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function malwareScans(Request $request): JsonResponse`<br>`public function intrusion(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function intrusionControls(Request $request): JsonResponse`<br>`public function fail2ban(Request $request, ConfigureFail2ban $configure): JsonResponse`<br>`public function fail2banBans(Request $request, string $jail, RecordFail2banBan $record): JsonResponse`<br>`public function listFail2banBans(Request $request, string $jail): JsonResponse`<br>`public function unbanFail2ban(Request $request, string $ban, UnbanFail2banBan $unban): JsonResponse`<br>`public function compliance(Request $request, RecordSecurityResource $record): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-security-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/security')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [SecurityFindingController::class, 'index'])->name('control-panel.security.index');
Route::post('/', [SecurityFindingController::class, 'store'])->name('control-panel.security.store');
Route::post('{finding}/resolve', [SecurityFindingController::class, 'resolve'])->name('control-panel.security.resolve');
Route::patch('{finding}', [SecurityFindingController::class, 'update'])->name('control-panel.security.update');
Route::post('hardening', [SecurityFindingController::class, 'hardening'])->name('control-panel.security.hardening.store');
Route::post('patches', [SecurityFindingController::class, 'patch'])->name('control-panel.security.patches.store');
Route::post('mfa-rbac', [SecurityFindingController::class, 'policy'])->name('control-panel.security.mfa-rbac.store');
Route::get('mfa-rbac', [SecurityFindingController::class, 'policies'])->name('control-panel.security.mfa-rbac.index');
Route::post('secrets', [SecurityFindingController::class, 'secret'])->name('control-panel.security.secrets.store');
Route::get('secrets', [SecurityFindingController::class, 'secrets'])->name('control-panel.security.secrets.index');
Route::post('malware-scans', [SecurityFindingController::class, 'malware'])->name('control-panel.security.malware.store');
Route::get('malware-scans', [SecurityFindingController::class, 'malwareScans'])->name('control-panel.security.malware.index');
Route::post('intrusion-controls', [SecurityFindingController::class, 'intrusion'])->name('control-panel.security.intrusion.store');
Route::get('intrusion-controls', [SecurityFindingController::class, 'intrusionControls'])->name('control-panel.security.intrusion.index');
Route::get('patches', [SecurityFindingController::class, 'patches'])->name('control-panel.security.patches.index');
Route::post('fail2ban', [SecurityFindingController::class, 'fail2ban'])->name('control-panel.security.fail2ban.store');
Route::get('fail2ban/{jail}/bans', [SecurityFindingController::class, 'listFail2banBans'])->name('control-panel.security.fail2ban.bans.index');
Route::post('fail2ban/{jail}/bans', [SecurityFindingController::class, 'fail2banBans'])->name('control-panel.security.fail2ban.bans.store');
Route::post('fail2ban/bans/{ban}/unban', [SecurityFindingController::class, 'unbanFail2ban'])->name('control-panel.security.fail2ban.bans.unban');
Route::post('compliance', [SecurityFindingController::class, 'compliance'])->name('control-panel.security.compliance.store');
Route::get('{finding}', [SecurityFindingController::class, 'show'])->name('control-panel.security.show');
```
<!-- layer-implementation-plan:end -->
