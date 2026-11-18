# Catalog React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catalog). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-ecommerce-catalog-react-native
**Matching core package:** module-ecommerce-catalog ([implementation](../core/catalog.md))
**Matching API package:** module-ecommerce-catalog-api ([contract](../api/catalog.md))

## Implementation plan

This adapter presents Catalog for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Catalog API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/catalog.md), and [API module](../api/catalog.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `catalog`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-ecommerce-mobile-react`](https://github.com/liberusoftware/project-ecommerce-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/catalog.md)) |
| Capability React Native module skeleton | [`module-ecommerce-catalog-react-native`](https://github.com/liberusoftware/module-ecommerce-catalog-react-native) (`@liberusoftware/module-ecommerce-catalog-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Products** | Progressive mobile list/detail/sheet flow for `products` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Variants** | Progressive mobile list/detail/sheet flow for `variants` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Categories** | Progressive mobile list/detail/sheet flow for `categories` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Collections** | Progressive mobile list/detail/sheet flow for `collections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tags** | Progressive mobile list/detail/sheet flow for `tags` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Brands** | Progressive mobile list/detail/sheet flow for `brands` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Vendors** | Progressive mobile list/detail/sheet flow for `vendors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Channel publication** | Progressive mobile list/detail/sheet flow for `channel publication` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Visibility** | Progressive mobile list/detail/sheet flow for `visibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Effective dates** | Progressive mobile list/detail/sheet flow for `effective dates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-ecommerce-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
