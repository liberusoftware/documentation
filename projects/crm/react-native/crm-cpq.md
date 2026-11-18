# Crm Cpq React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-cpq). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-cpq-react-native
**Matching core package:** module-crm-crm-cpq ([implementation](../core/crm-cpq.md))
**Matching API package:** module-crm-crm-cpq-api ([contract](../api/crm-cpq.md))

## Implementation plan

This adapter presents Crm Cpq for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Cpq API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-cpq.md), and [API module](../api/crm-cpq.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-cpq`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-cpq.md)) |
| Capability React Native module skeleton | [`module-crm-cpq-react-native`](https://github.com/liberusoftware/module-crm-cpq-react-native) (`@liberusoftware/module-crm-cpq-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Guided configuration** | Progressive mobile list/detail/sheet flow for `guided configuration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Compatibility rules** | Progressive mobile list/detail/sheet flow for `compatibility rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Price books** | Progressive mobile list/detail/sheet flow for `price books` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tiers** | Progressive mobile list/detail/sheet flow for `tiers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Discounts** | Progressive mobile list/detail/sheet flow for `discounts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Margin guardrails** | Progressive mobile list/detail/sheet flow for `margin guardrails` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Amendments** | Progressive mobile list/detail/sheet flow for `amendments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Renewals** | Progressive mobile list/detail/sheet flow for `renewals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Authoritative pricing adapters** | Progressive mobile list/detail/sheet flow for `authoritative pricing adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CpqQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Queries/CpqQuery.php) | `public function quotes(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PriceQuote.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Actions/PriceQuote.php) | `public function execute(int $teamId, int $userId, array $input): CpqQuote` |
| [SubmitQuote.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Actions/SubmitQuote.php) | `public function execute(int $teamId, int $userId, CpqQuote $quote): CpqApproval` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CpqApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Models/CpqApproval.php) | No literal fillable array detected; inspect the model and API schema. |
| [CpqQuote.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Models/CpqQuote.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CpqController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq-api/src/Http/Controllers/CpqController.php) | `public function __construct(private readonly CpqQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function show(int $quote): CpqQuoteResource`<br>`public function store(PriceQuote $action): JsonResponse`<br>`public function submit(int $quote, SubmitQuote $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-cpq-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/cpq')->group(function (): void {
Route::get('quotes', [CpqController::class, 'index']);
Route::post('quotes', [CpqController::class, 'store']);
Route::get('quotes/{quote}', [CpqController::class, 'show']);
Route::post('quotes/{quote}/submit', [CpqController::class, 'submit']);
```
<!-- layer-implementation-plan:end -->
