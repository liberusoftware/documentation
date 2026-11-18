# Crm Affiliate Management Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-affiliate-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-affiliate-management-flutter
**Matching core package:** module-crm-crm-affiliate-management ([implementation](../core/crm-affiliate-management.md))
**Matching API package:** module-crm-crm-affiliate-management-api ([contract](../api/crm-affiliate-management.md))

## Implementation plan

This adapter presents Crm Affiliate Management for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Affiliate Management API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-affiliate-management.md), and [API module](../api/crm-affiliate-management.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-affiliate-management`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-affiliate-management-flutter`](https://github.com/liberusoftware/module-crm-affiliate-management-flutter) (`module_crm_affiliate_management_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-affiliate-management-dart-mobile`](https://github.com/liberusoftware/module-crm-affiliate-management-dart-mobile) (`module_crm_affiliate_management_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-affiliate-management-dart-desktop`](https://github.com/liberusoftware/module-crm-affiliate-management-dart-desktop) (`module_crm_affiliate_management_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-affiliate-management.md) · [Core plan](../core/crm-affiliate-management.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Affiliates and partner profiles** | Adaptive mobile cards/sheets for `affiliates and partner profiles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `affiliates and partner profiles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Applications and onboarding approval** | Adaptive mobile cards/sheets for `applications and onboarding approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `applications and onboarding approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Links, campaigns, and clicks** | Adaptive mobile cards/sheets for `links, campaigns, and clicks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `links, campaigns, and clicks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Conversions and commission rules** | Adaptive mobile cards/sheets for `conversions and commission rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `conversions and commission rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Payout approvals/exports, disputes, assets, and portal** | Adaptive mobile cards/sheets for `payout approvals/exports, disputes, assets, and portal` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `payout approvals/exports, disputes, assets, and portal` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AffiliateQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Queries/AffiliateQuery.php) | `public function affiliates(int $teamId): Builder`<br>`public function events(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApplyAffiliate.php) | `public function execute(int $teamId, array $input): Affiliate` |
| [ApproveAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliate.php) | `public function execute(int $teamId, Affiliate $affiliate): Affiliate` |
| [ApproveAffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliatePayout.php) | `public function execute(int $teamId, int $actorId, AffiliatePayout $payout): AffiliatePayout` |
| [CreateAffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/CreateAffiliateLink.php) | `public function execute(int $teamId, Affiliate $affiliate, array $input): AffiliateLink` |
| [RecordAffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/RecordAffiliateEvent.php) | `public function execute(int $teamId, AffiliateLink $link, array $input): AffiliateEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Affiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/Affiliate.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateLink.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliatePayout.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AffiliateController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-api/src/Http/Controllers/AffiliateController.php) | `public function __construct(private readonly AffiliateQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(ApplyAffiliate $action): JsonResponse`<br>`public function approve(Affiliate $affiliate, ApproveAffiliate $action): JsonResponse`<br>`public function link(Affiliate $affiliate, CreateAffiliateLink $action): JsonResponse`<br>`public function event(AffiliateLink $link, RecordAffiliateEvent $action): JsonResponse`<br>`public function events(): JsonResponse` |

**Observed route declarations:**

[modules/crm-affiliate-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/affiliate-management')->group(function (): void {
Route::get('affiliates', [AffiliateController::class, 'index']);
Route::post('affiliates', [AffiliateController::class, 'store']);
Route::post('affiliates/{affiliate}/approve', [AffiliateController::class, 'approve']);
Route::post('affiliates/{affiliate}/links', [AffiliateController::class, 'link']);
Route::post('links/{link}/events', [AffiliateController::class, 'event']);
Route::get('events', [AffiliateController::class, 'events']);
```
<!-- layer-implementation-plan:end -->
