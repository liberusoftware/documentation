# Liberu Music: Projects and Sessions — React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#projects). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-projects-react-native`. Uses [core](../core/projects.md) and, for remote access, [API](../api/projects.md).

## Surface workflow

Present: create a session, add tracks, save a checkpoint and recover an interrupted edit. Domain scope: project documents, tracks, folders, templates, revision history, autosave and portable session manifests.

Use native audio workers and typed transport bindings. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Persist local capture before upload; store credentials in Keychain/Keystore.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Recover an autosave and reopen a portable session without missing references. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: every saved revision resolves immutable media references and a declared schema version.

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `projects`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/projects.md)) |
| Capability React Native module skeleton | [`module-music-projects-react-native`](https://github.com/liberusoftware/module-music-projects-react-native) (`@liberusoftware/module-music-projects-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Project documents** | Progressive mobile list/detail/sheet flow for `project documents` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tracks** | Progressive mobile list/detail/sheet flow for `tracks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Folders** | Progressive mobile list/detail/sheet flow for `folders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Revision history** | Progressive mobile list/detail/sheet flow for `revision history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Autosave** | Progressive mobile list/detail/sheet flow for `autosave` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Portable session manifests** | Progressive mobile list/detail/sheet flow for `portable session manifests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-music-daw-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
