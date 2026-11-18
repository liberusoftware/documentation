# Module Cms Copilot React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-copilot). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-module-cms-copilot-react-native
**Matching core package:** module-cms-module-cms-copilot ([implementation](../core/module-cms-copilot.md))
**Matching API package:** module-cms-module-cms-copilot-api ([contract](../api/module-cms-copilot.md))

## Implementation plan

This adapter presents Module Cms Copilot for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Cms Copilot API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-cms-copilot.md), and [API module](../api/module-cms-copilot.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-cms-copilot`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-copilot.md)) |
| Capability React Native module skeleton | [`module-cms-cms-copilot-react-native`](https://github.com/liberusoftware/module-cms-cms-copilot-react-native) (`@liberusoftware/module-cms-cms-copilot-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Permission-bounded search** | Progressive mobile list/detail/sheet flow for `permission-bounded search` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Summaries** | Progressive mobile list/detail/sheet flow for `summaries` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Drafting** | Progressive mobile list/detail/sheet flow for `drafting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transforms** | Progressive mobile list/detail/sheet flow for `transforms` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Metadata** | Progressive mobile list/detail/sheet flow for `metadata` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Internal links** | Progressive mobile list/detail/sheet flow for `internal links` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Action confirmation via Automation** | Progressive mobile list/detail/sheet flow for `action confirmation via automation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CopilotHandlerInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Contracts/CopilotHandlerInterface.php) | `public function capability(): string`<br>`public function handle(string $prompt, array $input): array` |
| [CopilotService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Services/CopilotService.php) | `public function submit(?int $teamId, string $capability, string $prompt, array $input = [], ?string $idempotencyKey = null): CopilotRequest`<br>`public function execute(CopilotRequest $request): CopilotRequest`<br>`public function requireConfirmation(CopilotRequest $request): string`<br>`public function confirm(CopilotRequest $request, string $token): CopilotRequest`<br>`public function registerHandler(CopilotHandlerInterface $handler): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CopilotRequest.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Models/CopilotRequest.php) | `team_id`, `capability`, `prompt`, `input`, `result`, `status`, `idempotency_key`, `confirmation_hash`, `confirmed_at`, `failure_reason` |
<!-- layer-implementation-plan:end -->
