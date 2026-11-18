# Liberu Music: Audio Engine and Transport — React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#audio-engine). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-audio-engine-react-native`. Uses [core](../core/audio-engine.md) and, for remote access, [API](../api/audio-engine.md).

## Surface workflow

Present: load a graph snapshot, start playback, seek and safely stop. Domain scope: native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering.

Use native audio workers and typed transport bindings. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Persist local capture before upload; store credentials in Keychain/Keystore.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Measure callback deadlines, underruns, seek accuracy and latency compensation on reference hardware. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: audio callbacks never wait for network, database, allocation or UI locks.

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `audio-engine`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/audio-engine.md)) |
| Capability React Native module skeleton | [`module-music-audio-engine-react-native`](https://github.com/liberusoftware/module-music-audio-engine-react-native) (`@liberusoftware/module-music-audio-engine-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Native audio graph** | Progressive mobile list/detail/sheet flow for `native audio graph` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sample clock** | Progressive mobile list/detail/sheet flow for `sample clock` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Play/stop/seek** | Progressive mobile list/detail/sheet flow for `play/stop/seek` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Buffers** | Progressive mobile list/detail/sheet flow for `buffers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Latency compensation** | Progressive mobile list/detail/sheet flow for `latency compensation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Offline graph rendering** | Progressive mobile list/detail/sheet flow for `offline graph rendering` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
