# Contact Center Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#contact-center). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-contact-center-flutter
**Matching core package:** module-crm-contact-center ([implementation](../core/contact-center.md))
**Matching API package:** module-crm-contact-center-api ([contract](../api/contact-center.md))

## Implementation plan

This adapter presents Contact Center for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Contact Center API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/contact-center.md), and [API module](../api/contact-center.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `contact-center`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-contact-center-flutter`](https://github.com/liberusoftware/module-crm-contact-center-flutter) (`module_crm_contact_center_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-contact-center-dart-mobile`](https://github.com/liberusoftware/module-crm-contact-center-dart-mobile) (`module_crm_contact_center_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-contact-center-dart-desktop`](https://github.com/liberusoftware/module-crm-contact-center-dart-desktop) (`module_crm_contact_center_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/contact-center.md) · [Core plan](../core/contact-center.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Agent presence** | Adaptive mobile cards/sheets for `agent presence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `agent presence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Capacity** | Adaptive mobile cards/sheets for `capacity` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `capacity` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Skills** | Adaptive mobile cards/sheets for `skills` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `skills` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Routing** | Adaptive mobile cards/sheets for `routing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `routing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Supervisor views** | Adaptive mobile cards/sheets for `supervisor views` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `supervisor views` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Whisper/barge policy** | Adaptive mobile cards/sheets for `whisper/barge policy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `whisper/barge policy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Quality review** | Adaptive mobile cards/sheets for `quality review` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quality review` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Workforce demand** | Adaptive mobile cards/sheets for `workforce demand` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `workforce demand` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Queue SLA** | Adaptive mobile cards/sheets for `queue sla` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `queue sla` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Overflow** | Adaptive mobile cards/sheets for `overflow` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `overflow` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ContactCenterQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Queries/ContactCenterQuery.php) | `public function agents(int $teamId): Builder`<br>`public function supervisorView(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ReviewQuality.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/ReviewQuality.php) | `public function execute(int $teamId, int $eventId, int $reviewerId, array $scorecard): ContactCenterEvent` |
| [RouteInteraction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/RouteInteraction.php) | `public function execute(int $teamId, string $queueKey, string $requiredSkill, int $slaSeconds = 300): ContactCenterEvent` |
| [SetAgentPresence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/SetAgentPresence.php) | `public function execute(int $teamId, int $userId, string $presence, int $capacity = 1, array $skills = []): ContactCenterAgent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContactCenterAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Models/ContactCenterAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContactCenterEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Models/ContactCenterEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ContactCenterController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center-api/src/Http/Controllers/ContactCenterController.php) | `public function __construct(private readonly ContactCenterQuery $query)`<br>`public function agents(): JsonResponse`<br>`public function presence(SetAgentPresence $a): JsonResponse`<br>`public function route(RouteInteraction $a): JsonResponse`<br>`public function supervisor(): JsonResponse` |

**Observed route declarations:**

[modules/crm-contact-center-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/contact-center')->group(function (): void {
Route::get('agents', [ContactCenterController::class, 'agents']);
Route::post('presence', [ContactCenterController::class, 'presence']);
Route::post('route', [ContactCenterController::class, 'route']);
Route::get('supervisor', [ContactCenterController::class, 'supervisor']);
```
<!-- layer-implementation-plan:end -->
