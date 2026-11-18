# Enrichment Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#enrichment). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-enrichment-flutter
**Matching core package:** module-crm-enrichment ([implementation](../core/enrichment.md))
**Matching API package:** module-crm-enrichment-api ([contract](../api/enrichment.md))

## Implementation plan

This adapter presents Enrichment for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Enrichment API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/enrichment.md), and [API module](../api/enrichment.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `enrichment`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-enrichment-flutter`](https://github.com/liberusoftware/module-crm-enrichment-flutter) (`module_crm_enrichment_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-enrichment-dart-mobile`](https://github.com/liberusoftware/module-crm-enrichment-dart-mobile) (`module_crm_enrichment_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-enrichment-dart-desktop`](https://github.com/liberusoftware/module-crm-enrichment-dart-desktop) (`module_crm_enrichment_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/enrichment.md) · [Core plan](../core/enrichment.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Company/contact firmographic** | Adaptive mobile cards/sheets for `company/contact firmographic` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `company/contact firmographic` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Demographic** | Adaptive mobile cards/sheets for `demographic` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `demographic` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Technographic** | Adaptive mobile cards/sheets for `technographic` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `technographic` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Social** | Adaptive mobile cards/sheets for `social` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `social` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Verification** | Adaptive mobile cards/sheets for `verification` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `verification` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Change monitoring** | Adaptive mobile cards/sheets for `change monitoring` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `change monitoring` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Confidence** | Adaptive mobile cards/sheets for `confidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `confidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Field-level provenance** | Adaptive mobile cards/sheets for `field-level provenance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `field-level provenance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Provider adapters** | Adaptive mobile cards/sheets for `provider adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provider adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EnrichmentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Queries/EnrichmentQuery.php) | `public function profiles(int $teamId)`<br>`public function changes(int $teamId, int $profileId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordChange.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/RecordChange.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, array $input): EnrichmentChange` |
| [RecordProvenance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/RecordProvenance.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, array $input): EnrichmentField` |
| [UpsertEnrichment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/UpsertEnrichment.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EnrichmentProfile` |
| [VerifyProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/VerifyProfile.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, bool $verified): EnrichmentProfile` |
| [EnrichmentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Services/EnrichmentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EnrichmentChange.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentChange.php) | No literal fillable array detected; inspect the model and API schema. |
| [EnrichmentField.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentField.php) | No literal fillable array detected; inspect the model and API schema. |
| [EnrichmentProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentProfile.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EnrichmentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-api/src/Http/Controllers/EnrichmentController.php) | `public function __construct(private readonly EnrichmentQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(UpsertEnrichment $action): JsonResponse`<br>`public function provenance(EnrichmentProfile $profile, RecordProvenance $action): JsonResponse`<br>`public function change(EnrichmentProfile $profile, RecordChange $action): JsonResponse`<br>`public function verify(EnrichmentProfile $profile, VerifyProfile $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-enrichment-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/enrichment')->group(function (): void {
Route::get('profiles', [EnrichmentController::class, 'index']);
Route::post('profiles', [EnrichmentController::class, 'store']);
Route::post('profiles/{profile}/provenance', [EnrichmentController::class, 'provenance']);
Route::post('profiles/{profile}/changes', [EnrichmentController::class, 'change']);
Route::post('profiles/{profile}/verify', [EnrichmentController::class, 'verify']);
```
<!-- layer-implementation-plan:end -->
