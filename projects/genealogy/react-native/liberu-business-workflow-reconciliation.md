# Liberu Business Workflow Reconciliation React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-business-workflow-reconciliation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-liberu-business-workflow-reconciliation-react-native
**Matching core package:** module-genealogy-liberu-business-workflow-reconciliation ([implementation](../core/liberu-business-workflow-reconciliation.md))
**Matching API package:** module-genealogy-liberu-business-workflow-reconciliation-api ([contract](../api/liberu-business-workflow-reconciliation.md))

## Implementation plan

This adapter presents Liberu Business Workflow Reconciliation for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Liberu Business Workflow Reconciliation API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/liberu-business-workflow-reconciliation.md), and [API module](../api/liberu-business-workflow-reconciliation.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `liberu-business-workflow-reconciliation`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-genealogy-mobile-react`](https://github.com/liberusoftware/project-genealogy-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/liberu-business-workflow-reconciliation.md)) |
| Capability React Native module skeleton | [`module-module-liberu-business-workflow-reconciliation-3b42eab6-react-native`](https://github.com/liberusoftware/module-module-liberu-business-workflow-reconciliation-3b42eab6-react-native) (`@liberusoftware/module-module-liberu-business-workflow-reconciliation-3b42eab6-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Workflow run registry** | Progressive mobile list/detail/sheet flow for `workflow run registry` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **State mapping** | Progressive mobile list/detail/sheet flow for `state mapping` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation rules** | Progressive mobile list/detail/sheet flow for `reconciliation rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recovery coordination** | Progressive mobile list/detail/sheet flow for `recovery coordination` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Audit timeline** | Progressive mobile list/detail/sheet flow for `audit timeline` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReconciliationCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/src/Actions/CreateReconciliationCase.php) | `public function execute(array $attributes): ReconciliationCase` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkflowRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/Models/WorkflowRun.php) | `team_id`, `correlation_id`, `workflow_key`, `contract_version`, `state`, `steps`, `last_error` |
<!-- layer-implementation-plan:end -->
