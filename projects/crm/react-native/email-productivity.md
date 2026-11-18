# Email Productivity React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#email-productivity). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-email-productivity-react-native
**Matching core package:** module-crm-email-productivity ([implementation](../core/email-productivity.md))
**Matching API package:** module-crm-email-productivity-api ([contract](../api/email-productivity.md))

## Implementation plan

This adapter presents Email Productivity for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Email Productivity API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/email-productivity.md), and [API module](../api/email-productivity.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `email-productivity`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/email-productivity.md)) |
| Capability React Native module skeleton | [`module-crm-email-productivity-react-native`](https://github.com/liberusoftware/module-crm-email-productivity-react-native) (`@liberusoftware/module-crm-email-productivity-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Mailbox sync** | Progressive mobile list/detail/sheet flow for `mailbox sync` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Send/log** | Progressive mobile list/detail/sheet flow for `send/log` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Snippets** | Progressive mobile list/detail/sheet flow for `snippets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Scheduling** | Progressive mobile list/detail/sheet flow for `scheduling` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Open/click/reply tracking policy** | Progressive mobile list/detail/sheet flow for `open/click/reply tracking policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Shared/team inbox** | Progressive mobile list/detail/sheet flow for `shared/team inbox` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Signatures** | Progressive mobile list/detail/sheet flow for `signatures` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sidebars** | Progressive mobile list/detail/sheet flow for `sidebars` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Gmail/Outlook adapters** | Progressive mobile list/detail/sheet flow for `gmail/outlook adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
