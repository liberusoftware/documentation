# Liberu Music: Controllers and Hardware Integration — React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#controllers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-controllers-react-native`. Uses [core](../core/controllers.md) and, for remote access, [API](../api/controllers.md).

## Surface workflow

Present: learn a control, map transport, reconnect hardware and reconcile feedback. Domain scope: mIDI port mapping, controller learn, control surfaces, feedback and external clock synchronization.

Use native audio workers and typed transport bindings. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Persist local capture before upload; store credentials in Keychain/Keystore.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Check disconnect, MIDI feedback loops, clock jitter and reconnect mappings. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: lost devices release held notes and stale remote sessions cannot control transport.

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `controllers`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/controllers.md)) |
| Capability React Native module skeleton | [`module-music-controllers-react-native`](https://github.com/liberusoftware/module-music-controllers-react-native) (`@liberusoftware/module-music-controllers-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **MIDI port mapping** | Progressive mobile list/detail/sheet flow for `midi port mapping` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Controller learn** | Progressive mobile list/detail/sheet flow for `controller learn` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Control surfaces** | Progressive mobile list/detail/sheet flow for `control surfaces` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Feedback** | Progressive mobile list/detail/sheet flow for `feedback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **External clock synchronization** | Progressive mobile list/detail/sheet flow for `external clock synchronization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
