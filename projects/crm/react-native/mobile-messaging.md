# Mobile Messaging React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mobile-messaging). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-mobile-messaging-react-native
**Matching core package:** module-crm-mobile-messaging ([implementation](../core/mobile-messaging.md))
**Matching API package:** module-crm-mobile-messaging-api ([contract](../api/mobile-messaging.md))

## Implementation plan

This adapter presents Mobile Messaging for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Mobile Messaging API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/mobile-messaging.md), and [API module](../api/mobile-messaging.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `mobile-messaging`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/mobile-messaging.md)) |
| Capability React Native module skeleton | [`module-crm-mobile-messaging-react-native`](https://github.com/liberusoftware/module-crm-mobile-messaging-react-native) (`@liberusoftware/module-crm-mobile-messaging-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Consent-aware SMS/MMS/WhatsApp/push campaigns** | Progressive mobile list/detail/sheet flow for `consent-aware sms/mms/whatsapp/push campaigns` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Short links** | Progressive mobile list/detail/sheet flow for `short links` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Keywords** | Progressive mobile list/detail/sheet flow for `keywords` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Opt-in/out** | Progressive mobile list/detail/sheet flow for `opt-in/out` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quiet hours** | Progressive mobile list/detail/sheet flow for `quiet hours` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sender governance** | Progressive mobile list/detail/sheet flow for `sender governance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery/reply handling** | Progressive mobile list/detail/sheet flow for `delivery/reply handling` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CampaignQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Queries/CampaignQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/CreateCampaign.php) | `public function __construct(private readonly MobileMessagingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MessagingCampaign` |
| [RecordMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/RecordMessage.php) | `public function __construct(private readonly MobileMessagingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MessagingCampaign $campaign, array $input): MessagingMessage` |
| [UpsertContactConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/UpsertContactConsent.php) | `public function __construct(private readonly MobileMessagingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MessagingContact` |
| [MobileMessagingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Services/MobileMessagingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MessagingCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MobileMessagingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging-api/src/Http/Controllers/MobileMessagingController.php) | `public function index(Request $r, CampaignQuery $q): JsonResponse`<br>`public function consent(Request $r, UpsertContactConsent $a): JsonResponse`<br>`public function store(Request $r, CreateCampaign $a): JsonResponse`<br>`public function message(Request $r, MessagingCampaign $campaign, RecordMessage $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
