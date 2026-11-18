# Partner Relationship Management Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#partner-relationship-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-partner-relationship-management-flutter
**Matching core package:** module-crm-partner-relationship-management ([implementation](../core/partner-relationship-management.md))
**Matching API package:** module-crm-partner-relationship-management-api ([contract](../api/partner-relationship-management.md))

## Implementation plan

This adapter presents Partner Relationship Management for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Partner Relationship Management API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/partner-relationship-management.md), and [API module](../api/partner-relationship-management.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `partner-relationship-management`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-partner-relationship-management-flutter`](https://github.com/liberusoftware/module-crm-partner-relationship-management-flutter) (`module_crm_partner_relationship_management_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-partner-relationship-management-dart-mobile`](https://github.com/liberusoftware/module-crm-partner-relationship-management-dart-mobile) (`module_crm_partner_relationship_management_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-partner-relationship-management-dart-desktop`](https://github.com/liberusoftware/module-crm-partner-relationship-management-dart-desktop) (`module_crm_partner_relationship_management_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/partner-relationship-management.md) · [Core plan](../core/partner-relationship-management.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Partner accounts** | Adaptive mobile cards/sheets for `partner accounts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `partner accounts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Contacts** | Adaptive mobile cards/sheets for `contacts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `contacts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tiers** | Adaptive mobile cards/sheets for `tiers` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tiers` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Recruitment** | Adaptive mobile cards/sheets for `recruitment` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recruitment` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Onboarding** | Adaptive mobile cards/sheets for `onboarding` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `onboarding` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Competencies** | Adaptive mobile cards/sheets for `competencies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `competencies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Agreements** | Adaptive mobile cards/sheets for `agreements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `agreements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Enablement** | Adaptive mobile cards/sheets for `enablement` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `enablement` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Certification** | Adaptive mobile cards/sheets for `certification` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `certification` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Plans** | Adaptive mobile cards/sheets for `plans` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `plans` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Performance** | Adaptive mobile cards/sheets for `performance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `performance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PartnerQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Queries/PartnerQuery.php) | `public function partners(int $teamId)`<br>`public function contacts(int $teamId)`<br>`public function activities(int $teamId)`<br>`public function performance(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddPartnerContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/AddPartnerContact.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerContact` |
| [ChangePartnerStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/ChangePartnerStatus.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $partnerId, string $status): PartnerAccount` |
| [CreatePartner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/CreatePartner.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerAccount` |
| [RecordPartnerActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/RecordPartnerActivity.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerActivity` |
| [RecordPartnerPerformance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/RecordPartnerPerformance.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerPerformance` |
| [PartnerPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Services/PartnerPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PartnerAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerActivity.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerPerformance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerPerformance.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PartnerRelationshipManagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management-api/src/Http/Controllers/PartnerRelationshipManagementController.php) | `public function partners(Request $r, PartnerQuery $q)`<br>`public function partner(Request $r, CreatePartner $a)`<br>`public function contact(Request $r, AddPartnerContact $a)`<br>`public function status(Request $r, int $partner, string $status, ChangePartnerStatus $a)`<br>`public function activity(Request $r, RecordPartnerActivity $a)`<br>`public function performance(Request $r, RecordPartnerPerformance $a)` |

**Observed route declarations:**

[modules/crm-partner-relationship-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/partner-relationship-management')->group(function (): void {
Route::get('/partners', [PartnerRelationshipManagementController::class, 'partners']);
Route::post('/partners', [PartnerRelationshipManagementController::class, 'partner']);
Route::post('/contacts', [PartnerRelationshipManagementController::class, 'contact']);
Route::post('/partners/{partner}/{status}', [PartnerRelationshipManagementController::class, 'status'])->whereIn('status', ['prospect', 'onboarding', 'active', 'suspended', 'inactive']);
Route::post('/activities', [PartnerRelationshipManagementController::class, 'activity']);
Route::post('/performance', [PartnerRelationshipManagementController::class, 'performance']);
```
<!-- layer-implementation-plan:end -->
