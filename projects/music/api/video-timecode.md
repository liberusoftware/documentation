# Liberu Music: Video and Timecode — API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#video-timecode). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-video-timecode-api`. Depends on the [core contract](../core/video-timecode.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization. The first consumer journey is: import a reference video, align cues and export audio against the picture revision. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Verify supported frame-rate conversions, long-session drift and missing video recovery. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: frame rate, drop-frame mode and project offset are explicit metadata. Follow [API architecture](../../../architecture/API.md).

<!-- layer-implementation-plan:start -->
## Product API backend and feature-to-operation plan

This API contract is composed into [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) ([Laravel API backends](../../../guides/LARAVEL-API-BACKENDS.md)) to serve [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react), [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue), [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react), [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter), [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile), and [`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop).

| Feature / aspect | HTTP query and command contract | DTO projection, concurrency & error semantics |
| --- | --- | --- |
| **Reference video** | Expose workspace-scoped read query and explicit command endpoint for `reference video` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Frame-rate-aware timeline display** | Expose workspace-scoped read query and explicit command endpoint for `frame-rate-aware timeline display` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Timecode offsets** | Expose workspace-scoped read query and explicit command endpoint for `timecode offsets` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Audio-to-picture synchronization** | Expose workspace-scoped read query and explicit command endpoint for `audio-to-picture synchronization` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
<!-- layer-implementation-plan:end -->
