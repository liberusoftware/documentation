# Email Productivity Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#email-productivity). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-email-productivity-flutter
**Matching core package:** module-crm-email-productivity ([implementation](../core/email-productivity.md))
**Matching API package:** module-crm-email-productivity-api ([contract](../api/email-productivity.md))

## Implementation plan

This adapter presents Email Productivity for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Email Productivity API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/email-productivity.md), and [API module](../api/email-productivity.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `email-productivity`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-email-productivity-flutter`](https://github.com/liberusoftware/module-crm-email-productivity-flutter) (`module_crm_email_productivity_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-email-productivity-dart-mobile`](https://github.com/liberusoftware/module-crm-email-productivity-dart-mobile) (`module_crm_email_productivity_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-email-productivity-dart-desktop`](https://github.com/liberusoftware/module-crm-email-productivity-dart-desktop) (`module_crm_email_productivity_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/email-productivity.md) · [Core plan](../core/email-productivity.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Mailbox sync** | Adaptive mobile cards/sheets for `mailbox sync` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mailbox sync` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Send/log** | Adaptive mobile cards/sheets for `send/log` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `send/log` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Templates** | Adaptive mobile cards/sheets for `templates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `templates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Snippets** | Adaptive mobile cards/sheets for `snippets` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `snippets` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Scheduling** | Adaptive mobile cards/sheets for `scheduling` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `scheduling` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Open/click/reply tracking policy** | Adaptive mobile cards/sheets for `open/click/reply tracking policy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `open/click/reply tracking policy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Shared/team inbox** | Adaptive mobile cards/sheets for `shared/team inbox` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `shared/team inbox` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Signatures** | Adaptive mobile cards/sheets for `signatures` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `signatures` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Sidebars** | Adaptive mobile cards/sheets for `sidebars` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sidebars` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Gmail/Outlook adapters** | Adaptive mobile cards/sheets for `gmail/outlook adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `gmail/outlook adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EmailProductivityQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Queries/EmailProductivityQuery.php) | `public function mailboxes(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function messages(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectMailbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/ConnectMailbox.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailMailbox` |
| [CreateEmailTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/CreateEmailTemplate.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailTemplate` |
| [RecordEmailEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/RecordEmailEvent.php) | `public function execute(int $teamId, EmailMessage $message, array $input): EmailEvent` |
| [SendEmail.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/SendEmail.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailMessage` |
| [EmailProductivityPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Services/EmailProductivityPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EmailEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMailbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailMailbox.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EmailProductivityController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity-api/src/Http/Controllers/EmailProductivityController.php) | `public function __construct(private readonly EmailProductivityQuery $query)`<br>`public function mailboxes(): JsonResponse`<br>`public function templates(): JsonResponse`<br>`public function messages(): JsonResponse`<br>`public function connect(ConnectMailbox $action): JsonResponse`<br>`public function template(CreateEmailTemplate $action): JsonResponse`<br>`public function send(SendEmail $action): JsonResponse`<br>`public function event(EmailMessage $message, RecordEmailEvent $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-email-productivity-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/email-productivity')->group(function (): void {
Route::get('mailboxes', [EmailProductivityController::class, 'mailboxes']);
Route::get('templates', [EmailProductivityController::class, 'templates']);
Route::get('messages', [EmailProductivityController::class, 'messages']);
Route::post('mailboxes', [EmailProductivityController::class, 'connect']);
Route::post('templates', [EmailProductivityController::class, 'template']);
Route::post('messages', [EmailProductivityController::class, 'send']);
Route::post('messages/{message}/events', [EmailProductivityController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
