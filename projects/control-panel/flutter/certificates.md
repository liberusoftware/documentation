# Certificates Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#certificates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-certificates-flutter
**Matching core package:** module-control-panel-certificates ([implementation](../core/certificates.md))
**Matching API package:** module-control-panel-certificates-api ([contract](../api/certificates.md))

## Implementation plan

This adapter presents Certificates for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Certificates API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/certificates.md), and [API module](../api/certificates.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `certificates`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-certificates-flutter`](https://github.com/liberusoftware/module-control-panel-certificates-flutter) (`module_control_panel_certificates_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-certificates-dart-mobile`](https://github.com/liberusoftware/module-control-panel-certificates-dart-mobile) (`module_control_panel_certificates_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-certificates-dart-desktop`](https://github.com/liberusoftware/module-control-panel-certificates-dart-desktop) (`module_control_panel_certificates_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/certificates.md) · [Core plan](../core/certificates.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **ACME accounts** | Adaptive mobile cards/sheets for `acme accounts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `acme accounts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Issuance** | Adaptive mobile cards/sheets for `issuance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `issuance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Deployment** | Adaptive mobile cards/sheets for `deployment` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `deployment` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Renewal** | Adaptive mobile cards/sheets for `renewal` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `renewal` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Revocation** | Adaptive mobile cards/sheets for `revocation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `revocation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Expiry monitoring** | Adaptive mobile cards/sheets for `expiry monitoring` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `expiry monitoring` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListCertificates.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Queries/ListCertificates.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CheckCertificateExpiry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/CheckCertificateExpiry.php) | `public function execute(Certificate $certificate, int $thresholdDays = 30): CertificateExpiryAlert` |
| [ExpireCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/ExpireCertificate.php) | `public function execute(Certificate $certificate): Certificate` |
| [IssueCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/IssueCertificate.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Certificate` |
| [RecordCertificateOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RecordCertificateOperation.php) | `public function execute(array $attributes): CertificateOperation` |
| [RegisterAcmeAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RegisterAcmeAccount.php) | `public function execute(array $attributes): AcmeAccount` |
| [RegisterCertificateLifecycle.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RegisterCertificateLifecycle.php) | `public function execute(array $a): Model` |
| [RequestCertificateDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RequestCertificateDeployment.php) | `public function execute(Certificate $certificate, array $attributes): CertificateDeployment` |
| [RequestCertificateRenewal.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RequestCertificateRenewal.php) | `public function execute(Certificate $certificate, ?\DateTimeInterface $scheduledAt = null): CertificateRenewal` |
| [RevokeCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RevokeCertificate.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(Certificate $certificate): Certificate` |
| [UpdateCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/UpdateCertificate.php) | `public function execute(Certificate $certificate, array $attributes): Certificate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AcmeAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/AcmeAccount.php) | `id`, `team_id`, `email`, `directory`, `credentials`, `active` |
| [Certificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/Certificate.php) | `team_id`, `domains`, `status`, `issuer`, `certificate_pem`, `private_key`, `issued_at`, `expires_at`, `metadata` |
| [CertificateDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateDeployment.php) | `id`, `team_id`, `certificate_id`, `target_type`, `target_id`, `status`, `deployed_at`, `error`, `metadata` |
| [CertificateExpiryAlert.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateExpiryAlert.php) | `id`, `team_id`, `certificate_id`, `threshold_days`, `status`, `notified_at`, `metadata` |
| [CertificateOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateOperation.php) | `id`, `team_id`, `certificate_id`, `operation`, `status`, `details`, `completed_at` |
| [CertificateRenewal.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateRenewal.php) | `id`, `team_id`, `certificate_id`, `scheduled_at`, `started_at`, `completed_at`, `status`, `attempts`, `error` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CertificateController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-api/src/Http/Controllers/CertificateController.php) | `public function index(Request $request, ListCertificates $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, string $id, UpdateCertificate $update): JsonResponse`<br>`public function store(Request $request, IssueCertificate $issue): JsonResponse`<br>`public function acme(Request $request, RegisterAcmeAccount $register): JsonResponse`<br>`public function operation(Request $request, RecordCertificateOperation $record): JsonResponse`<br>`public function lifecycle(Request $request, RegisterCertificateLifecycle $register): JsonResponse`<br>`public function deploy(Request $request, string $certificate, RequestCertificateDeployment $deploy): JsonResponse`<br>`public function renew(Request $request, string $certificate, RequestCertificateRenewal $renew): JsonResponse`<br>`public function expiryCheck(Request $request, string $certificate, CheckCertificateExpiry $check): JsonResponse`<br>`public function expire(Request $request, string $certificate, ExpireCertificate $expire): JsonResponse`<br>`public function revoke(Request $request, string $certificate, RevokeCertificate $revoke): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-certificates-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/certificates')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [CertificateController::class, 'index'])->name('control-panel.certificates.index');
Route::post('/', [CertificateController::class, 'store'])->name('control-panel.certificates.store');
Route::post('/acme-accounts', [CertificateController::class, 'acme'])->name('control-panel.certificates.acme');
Route::post('/operations', [CertificateController::class, 'operation'])->name('control-panel.certificates.operations');
Route::post('/lifecycle', [CertificateController::class, 'lifecycle'])->name('control-panel.certificates.lifecycle');
Route::post('/{certificate}/deploy', [CertificateController::class, 'deploy'])->name('control-panel.certificates.deploy');
Route::post('/{certificate}/renew', [CertificateController::class, 'renew'])->name('control-panel.certificates.renew');
Route::post('/{certificate}/expiry-check', [CertificateController::class, 'expiryCheck'])->name('control-panel.certificates.expiry-check');
Route::post('/{certificate}/expire', [CertificateController::class, 'expire'])->name('control-panel.certificates.expire');
Route::post('/{certificate}/revoke', [CertificateController::class, 'revoke'])->name('control-panel.certificates.revoke');
Route::get('/{certificate}', [CertificateController::class, 'show'])->name('control-panel.certificates.show');
Route::patch('/{certificate}', [CertificateController::class, 'update'])->name('control-panel.certificates.update');
```
<!-- layer-implementation-plan:end -->
