# Revenue Intelligence Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-revenue-intelligence-flutter
**Matching core package:** module-crm-revenue-intelligence ([implementation](../core/revenue-intelligence.md))
**Matching API package:** module-crm-revenue-intelligence-api ([contract](../api/revenue-intelligence.md))

## Implementation plan

This adapter presents Revenue Intelligence for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Revenue Intelligence API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/revenue-intelligence.md), and [API module](../api/revenue-intelligence.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `revenue-intelligence`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-revenue-intelligence-flutter`](https://github.com/liberusoftware/module-crm-revenue-intelligence-flutter) (`module_crm_revenue_intelligence_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-revenue-intelligence-dart-mobile`](https://github.com/liberusoftware/module-crm-revenue-intelligence-dart-mobile) (`module_crm_revenue_intelligence_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-revenue-intelligence-dart-desktop`](https://github.com/liberusoftware/module-crm-revenue-intelligence-dart-desktop) (`module_crm_revenue_intelligence_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/revenue-intelligence.md) · [Core plan](../core/revenue-intelligence.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Pipeline inspection** | Adaptive mobile cards/sheets for `pipeline inspection` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `pipeline inspection` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Health/risk** | Adaptive mobile cards/sheets for `health/risk` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `health/risk` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Engagement gaps** | Adaptive mobile cards/sheets for `engagement gaps` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `engagement gaps` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Opportunity scoring** | Adaptive mobile cards/sheets for `opportunity scoring` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `opportunity scoring` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Relationship maps** | Adaptive mobile cards/sheets for `relationship maps` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `relationship maps` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **White-space/next-product suggestions** | Adaptive mobile cards/sheets for `white-space/next-product suggestions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `white-space/next-product suggestions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Anomaly detection** | Adaptive mobile cards/sheets for `anomaly detection` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `anomaly detection` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Alerts** | Adaptive mobile cards/sheets for `alerts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `alerts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueIntelligenceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Queries/RevenueIntelligenceQuery.php) | `public function insights(int $teamId)`<br>`public function alerts(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/CreateAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueIntelligenceAlert` |
| [RecordInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/RecordInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueInsight` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/ResolveAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $alertId): RevenueIntelligenceAlert` |
| [UpdateInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/UpdateInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $insightId, array $input): RevenueInsight` |
| [RevenueIntelligencePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Services/RevenueIntelligencePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueInsight.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueIntelligenceAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueIntelligenceAlert.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [RevenueIntelligenceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-api/src/Http/Controllers/RevenueIntelligenceController.php) | `public function insights(Request $r, RevenueIntelligenceQuery $q)`<br>`public function insight(Request $r, RecordInsight $a)`<br>`public function alerts(Request $r, RevenueIntelligenceQuery $q)`<br>`public function alert(Request $r, CreateAlert $a)`<br>`public function resolve(Request $r, int $alert, ResolveAlert $a)` |

**Observed route declarations:**

[modules/crm-revenue-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/revenue-intelligence')->group(function (): void {
Route::get('/insights', [RevenueIntelligenceController::class, 'insights']);
Route::post('/insights', [RevenueIntelligenceController::class, 'insight']);
Route::get('/alerts', [RevenueIntelligenceController::class, 'alerts']);
Route::post('/alerts', [RevenueIntelligenceController::class, 'alert']);
Route::post('/alerts/{alert}/resolve', [RevenueIntelligenceController::class, 'resolve']);
```
<!-- layer-implementation-plan:end -->
