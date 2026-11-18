# Customer Self Service Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-self-service). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-customer-self-service-flutter
**Matching core package:** module-crm-customer-self-service ([implementation](../core/customer-self-service.md))
**Matching API package:** module-crm-customer-self-service-api ([contract](../api/customer-self-service.md))

## Implementation plan

This adapter presents Customer Self Service for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Customer Self Service API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/customer-self-service.md), and [API module](../api/customer-self-service.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `customer-self-service`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-customer-self-service-flutter`](https://github.com/liberusoftware/module-crm-customer-self-service-flutter) (`module_crm_customer_self_service_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-customer-self-service-dart-mobile`](https://github.com/liberusoftware/module-crm-customer-self-service-dart-mobile) (`module_crm_customer_self_service_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-customer-self-service-dart-desktop`](https://github.com/liberusoftware/module-crm-customer-self-service-dart-desktop) (`module_crm_customer_self_service_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/customer-self-service.md) · [Core plan](../core/customer-self-service.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Customer portal** | Adaptive mobile cards/sheets for `customer portal` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `customer portal` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Case submission/status** | Adaptive mobile cards/sheets for `case submission/status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `case submission/status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Knowledge search** | Adaptive mobile cards/sheets for `knowledge search` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `knowledge search` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Community links** | Adaptive mobile cards/sheets for `community links` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `community links` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Appointments** | Adaptive mobile cards/sheets for `appointments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `appointments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Documents** | Adaptive mobile cards/sheets for `documents` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `documents` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Invoices/orders references** | Adaptive mobile cards/sheets for `invoices/orders references` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `invoices/orders references` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Profile** | Adaptive mobile cards/sheets for `profile` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `profile` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Preferences** | Adaptive mobile cards/sheets for `preferences` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `preferences` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SelfServiceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Queries/SelfServiceQuery.php) | `public function profile(int $teamId, int $userId): ?SelfServiceProfile`<br>`public function cases(int $teamId, int $profileId)`<br>`public function search(int $teamId, string $term)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SubmitSelfServiceCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/SubmitSelfServiceCase.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, SelfServiceProfile $profile, array $input): SelfServiceCase` |
| [UpdateSelfServicePreferences.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/UpdateSelfServicePreferences.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, SelfServiceProfile $profile, array $input): SelfServiceProfile` |
| [UpsertSelfServiceProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/UpsertSelfServiceProfile.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SelfServiceProfile` |
| [SelfServicePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Services/SelfServicePolicy.php) | `public function canAccess(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SelfServiceCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceReference.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceReference.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceResource.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SelfServiceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-api/src/Http/Controllers/SelfServiceController.php) | `public function __construct(private readonly SelfServiceQuery $query)`<br>`public function profile(): JsonResponse`<br>`public function storeProfile(UpsertSelfServiceProfile $action): JsonResponse`<br>`public function preferences(UpdateSelfServicePreferences $action): JsonResponse`<br>`public function cases(): JsonResponse`<br>`public function submitCase(SubmitSelfServiceCase $action): JsonResponse`<br>`public function knowledge(): JsonResponse` |

**Observed route declarations:**

[modules/crm-customer-self-service-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/customer-self-service')->group(function (): void {
Route::get('profile', [SelfServiceController::class, 'profile']);
Route::put('profile', [SelfServiceController::class, 'storeProfile']);
Route::put('profile/preferences', [SelfServiceController::class, 'preferences']);
Route::get('cases', [SelfServiceController::class, 'cases']);
Route::post('cases', [SelfServiceController::class, 'submitCase']);
Route::get('knowledge', [SelfServiceController::class, 'knowledge']);
```
<!-- layer-implementation-plan:end -->
