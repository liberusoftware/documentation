# Crm Dialer And Outreach Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-dialer-and-outreach). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-dialer-and-outreach-flutter
**Matching core package:** module-crm-crm-dialer-and-outreach ([implementation](../core/crm-dialer-and-outreach.md))
**Matching API package:** module-crm-crm-dialer-and-outreach-api ([contract](../api/crm-dialer-and-outreach.md))

## Implementation plan

This adapter presents Crm Dialer And Outreach for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Dialer And Outreach API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-dialer-and-outreach.md), and [API module](../api/crm-dialer-and-outreach.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-dialer-and-outreach`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-dialer-and-outreach-flutter`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-flutter) (`module_crm_dialer_and_outreach_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-dialer-and-outreach-dart-mobile`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-dart-mobile) (`module_crm_dialer_and_outreach_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-dialer-and-outreach-dart-desktop`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-dart-desktop) (`module_crm_dialer_and_outreach_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-dialer-and-outreach.md) · [Core plan](../core/crm-dialer-and-outreach.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Power/preview/progressive dialing** | Adaptive mobile cards/sheets for `power/preview/progressive dialing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `power/preview/progressive dialing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Prioritized lists** | Adaptive mobile cards/sheets for `prioritized lists` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `prioritized lists` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Scripts** | Adaptive mobile cards/sheets for `scripts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `scripts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Local-time policy** | Adaptive mobile cards/sheets for `local-time policy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `local-time policy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Retries** | Adaptive mobile cards/sheets for `retries` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `retries` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Voicemail drop** | Adaptive mobile cards/sheets for `voicemail drop` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `voicemail drop` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Answer detection adapters** | Adaptive mobile cards/sheets for `answer detection adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `answer detection adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Outcomes** | Adaptive mobile cards/sheets for `outcomes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `outcomes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Compliance controls** | Adaptive mobile cards/sheets for `compliance controls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `compliance controls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DialerQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Queries/DialerQuery.php) | `public function lists(int $teamId)`<br>`public function calls(int $teamId, int $listId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDialerList.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/CreateDialerList.php) | `public function __construct(private readonly DialerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): DialerList` |
| [QueueDialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/QueueDialerCall.php) | `public function __construct(private readonly DialerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DialerList $list, array $input): DialerCall` |
| [RecordCallOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/RecordCallOutcome.php) | `public function execute(int $teamId, int $userId, DialerCall $call, array $input): DialerEvent` |
| [RetryDialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/RetryDialerCall.php) | `public function execute(int $teamId, DialerCall $call, int $maxAttempts = 3): DialerCall` |
| [DialerPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Services/DialerPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerCall.php) | No literal fillable array detected; inspect the model and API schema. |
| [DialerEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [DialerList.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerList.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [DialerController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-api/src/Http/Controllers/DialerController.php) | `public function __construct(private readonly DialerQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateDialerList $action): JsonResponse`<br>`public function queue(DialerList $list, QueueDialerCall $action): JsonResponse`<br>`public function outcome(DialerCall $call, RecordCallOutcome $action): JsonResponse`<br>`public function retry(DialerCall $call, RetryDialerCall $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-dialer-and-outreach-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/dialer-and-outreach')->group(function (): void {
Route::get('lists', [DialerController::class, 'index']);
Route::post('lists', [DialerController::class, 'store']);
Route::post('lists/{list}/calls', [DialerController::class, 'queue']);
Route::post('calls/{call}/outcome', [DialerController::class, 'outcome']);
Route::post('calls/{call}/retry', [DialerController::class, 'retry']);
```
<!-- layer-implementation-plan:end -->
