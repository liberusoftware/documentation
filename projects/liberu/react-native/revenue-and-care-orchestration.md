# Liberu: Revenue and Care Orchestration React Native + Expo

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-liberu-revenue-and-care-orchestration-react-native`

Implement the staff daily queue, health detail, guarded click-to-call, recovery request, push alert, and AI approval flows over the [API](../api/revenue-and-care-orchestration.md). Use secure storage, no sensitive offline cache, typed navigation, deep links, push permission fallback, idempotent mutations, conflict-aware retry, dynamic type, screen-reader labels, RTL, and rotation support.

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `revenue-and-care-orchestration`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-liberu-official-mobile-react`](https://github.com/liberusoftware/project-liberu-official-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/revenue-and-care-orchestration.md)) |
| Capability React Native module skeleton | [`module-planned-liberu-revenue-and-care-orchestration-40451d50-react-native`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-react-native) (`@liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Customer health constellation** | Progressive mobile list/detail/sheet flow for `customer health constellation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-liberu-official-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Revenue-aware service recovery** | Progressive mobile list/detail/sheet flow for `revenue-aware service recovery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-liberu-official-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contact-protection ledger** | Progressive mobile list/detail/sheet flow for `contact-protection ledger` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-liberu-official-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cross-brand consent and quiet-hour evaluation** | Progressive mobile list/detail/sheet flow for `cross-brand consent and quiet-hour evaluation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-liberu-official-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval-gated AI recommendations** | Progressive mobile list/detail/sheet flow for `approval-gated ai recommendations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-liberu-official-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Mobile-ready daily queues** | Progressive mobile list/detail/sheet flow for `mobile-ready daily queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-liberu-official-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
