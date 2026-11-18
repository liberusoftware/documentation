# Orders And Payments Workspace React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#orders-and-payments-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-orders-and-payments-workspace-react-native
**Matching core package:** module-crm-orders-and-payments-workspace ([implementation](../core/orders-and-payments-workspace.md))
**Matching API package:** module-crm-orders-and-payments-workspace-api ([contract](../api/orders-and-payments-workspace.md))

## Implementation plan

This adapter presents Orders And Payments Workspace for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Orders And Payments Workspace API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/orders-and-payments-workspace.md), and [API module](../api/orders-and-payments-workspace.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `orders-and-payments-workspace`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/orders-and-payments-workspace.md)) |
| Capability React Native module skeleton | [`module-crm-orders-and-payments-workspace-react-native`](https://github.com/liberusoftware/module-crm-orders-and-payments-workspace-react-native) (`@liberusoftware/module-crm-orders-and-payments-workspace-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Payment links** | Progressive mobile list/detail/sheet flow for `payment links` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deposits** | Progressive mobile list/detail/sheet flow for `deposits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Order/subscription references** | Progressive mobile list/detail/sheet flow for `order/subscription references` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Invoice/payment status** | Progressive mobile list/detail/sheet flow for `invoice/payment status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Refunds/disputes visibility** | Progressive mobile list/detail/sheet flow for `refunds/disputes visibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Billing/Ecommerce handoff** | Progressive mobile list/detail/sheet flow for `billing/ecommerce handoff` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TransactionQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Queries/TransactionQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTransaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Actions/CreateTransaction.php) | `public function __construct(private readonly OrdersPaymentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PaymentTransaction` |
| [RecordPaymentEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Actions/RecordPaymentEvent.php) | `public function __construct(private readonly OrdersPaymentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, PaymentTransaction $transaction, array $input): PaymentEvent` |
| [OrdersPaymentsPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Services/OrdersPaymentsPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PaymentEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Models/PaymentEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentTransaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Models/PaymentTransaction.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [OrdersPaymentsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace-api/src/Http/Controllers/OrdersPaymentsController.php) | `public function index(Request $request, TransactionQuery $query): JsonResponse`<br>`public function store(Request $request, CreateTransaction $action): JsonResponse`<br>`public function event(Request $request, PaymentTransaction $transaction, RecordPaymentEvent $action): JsonResponse` |
<!-- layer-implementation-plan:end -->
