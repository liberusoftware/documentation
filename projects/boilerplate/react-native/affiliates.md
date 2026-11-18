# Affiliates and Partner Programs React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#affiliates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-affiliates-react-native`
**Matching domain module:** `affiliates`
**Matching core package:** `module-affiliates` ([implementation](../core/affiliates.md))
**Matching API package:** `module-affiliates-api` ([contract](../api/affiliates.md))
**Architecture specification:** [AFFILIATES.md](../../../architecture/AFFILIATES.md)

## Implementation plan

This adapter presents Affiliates and Partner Programs (`liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)`) for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Affiliates and Partner Programs API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [AFFILIATES.md](../../../architecture/AFFILIATES.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/affiliates.md), and [API module](../api/affiliates.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `affiliates`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/affiliates.md)) |
| Capability React Native module skeleton | `module-boilerplate-affiliates-react-native` | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Affiliate program and commission tier rules** | Progressive mobile list/detail/sheet flow for `affiliate program and commission tier rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Partner applications, KYC/tax readiness, and approval** | Progressive mobile list/detail/sheet flow for `partner applications, kyc/tax readiness, and approval` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tracking links, campaign parameters, and promo codes** | Progressive mobile list/detail/sheet flow for `tracking links, campaign parameters, and promo codes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Authoritative conversion ingestion and hold ledger** | Progressive mobile list/detail/sheet flow for `authoritative conversion ingestion and hold ledger` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Automated refund, cancellation, and dispute clawbacks** | Progressive mobile list/detail/sheet flow for `automated refund, cancellation, and dispute clawbacks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Self-referral, velocity, and fraud screening** | Progressive mobile list/detail/sheet flow for `self-referral, velocity, and fraud screening` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payout approval batches and settlement handoff** | Progressive mobile list/detail/sheet flow for `payout approval batches and settlement handoff` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
