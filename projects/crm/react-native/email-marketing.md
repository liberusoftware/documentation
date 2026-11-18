# Email Marketing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#email-marketing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-email-marketing-react-native
**Matching core package:** module-crm-email-marketing ([implementation](../core/email-marketing.md))
**Matching API package:** module-crm-email-marketing-api ([contract](../api/email-marketing.md))

## Implementation plan

This adapter presents Email Marketing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Email Marketing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/email-marketing.md), and [API module](../api/email-marketing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `email-marketing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/email-marketing.md)) |
| Capability React Native module skeleton | [`module-crm-email-marketing-react-native`](https://github.com/liberusoftware/module-crm-email-marketing-react-native) (`@liberusoftware/module-crm-email-marketing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Drag-and-drop and code templates** | Progressive mobile list/detail/sheet flow for `drag-and-drop and code templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Personalization** | Progressive mobile list/detail/sheet flow for `personalization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dynamic content** | Progressive mobile list/detail/sheet flow for `dynamic content` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Test sends** | Progressive mobile list/detail/sheet flow for `test sends` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Inbox previews** | Progressive mobile list/detail/sheet flow for `inbox previews` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deliverability controls** | Progressive mobile list/detail/sheet flow for `deliverability controls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Scheduling** | Progressive mobile list/detail/sheet flow for `scheduling` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Throttling** | Progressive mobile list/detail/sheet flow for `throttling` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Analytics** | Progressive mobile list/detail/sheet flow for `analytics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EmailMarketingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Queries/EmailMarketingQuery.php) | `public function campaigns(int $teamId)`<br>`public function analytics(int $teamId, int $campaignId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/CreateEmailCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailCampaign` |
| [RecordMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/RecordMarketingEvent.php) | `public function execute(int $teamId, EmailCampaign $campaign, array $input): EmailMarketingEvent` |
| [ScheduleCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/ScheduleCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EmailCampaign $campaign, array $input): EmailCampaign` |
| [EmailMarketingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Services/EmailMarketingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailMarketingEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EmailMarketingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-api/src/Http/Controllers/EmailMarketingController.php) | `public function __construct(private readonly EmailMarketingQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateEmailCampaign $action): JsonResponse`<br>`public function schedule(EmailCampaign $campaign, ScheduleCampaign $action): JsonResponse`<br>`public function event(EmailCampaign $campaign, RecordMarketingEvent $action): JsonResponse`<br>`public function analytics(EmailCampaign $campaign): JsonResponse` |

**Observed route declarations:**

[modules/crm-email-marketing-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/email-marketing')->group(function (): void {
Route::get('campaigns', [EmailMarketingController::class, 'index']);
Route::post('campaigns', [EmailMarketingController::class, 'store']);
Route::post('campaigns/{campaign}/schedule', [EmailMarketingController::class, 'schedule']);
Route::post('campaigns/{campaign}/events', [EmailMarketingController::class, 'event']);
Route::get('campaigns/{campaign}/analytics', [EmailMarketingController::class, 'analytics']);
```
<!-- layer-implementation-plan:end -->
