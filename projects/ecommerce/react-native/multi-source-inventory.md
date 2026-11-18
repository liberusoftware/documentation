# Multi Source Inventory React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multi-source-inventory). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-ecommerce-multi-source-inventory-react-native
**Matching core package:** module-ecommerce-multi-source-inventory ([implementation](../core/multi-source-inventory.md))
**Matching API package:** module-ecommerce-multi-source-inventory-api ([contract](../api/multi-source-inventory.md))

## Implementation plan

This adapter presents Multi Source Inventory for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Multi Source Inventory API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/multi-source-inventory.md), and [API module](../api/multi-source-inventory.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `multi-source-inventory`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-ecommerce-mobile-react`](https://github.com/liberusoftware/project-ecommerce-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/multi-source-inventory.md)) |
| Capability React Native module skeleton | [`module-ecommerce-multi-source-inventory-react-native`](https://github.com/liberusoftware/module-ecommerce-multi-source-inventory-react-native) (`@liberusoftware/module-ecommerce-multi-source-inventory-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Sources/warehouses/stores/drop shippers** | Progressive mobile list/detail/sheet flow for `sources/warehouses/stores/drop shippers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Stocks** | Progressive mobile list/detail/sheet flow for `stocks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Channel assignment** | Progressive mobile list/detail/sheet flow for `channel assignment` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Aggregated salable quantity** | Progressive mobile list/detail/sheet flow for `aggregated salable quantity` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Priority/distance rules** | Progressive mobile list/detail/sheet flow for `priority/distance rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Source health** | Progressive mobile list/detail/sheet flow for `source health` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
