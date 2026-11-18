# Liberu Music: Video and Timecode — Next.js

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#video-timecode). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-video-timecode-nextjs`. Uses [core](../core/video-timecode.md) and, for remote access, [API](../api/video-timecode.md).

## Surface workflow

Present: import a reference video, align cues and export audio against the picture revision. Domain scope: reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization.

Use reviewed API DTOs for server data and explicit client components for timeline, AudioWorklet and device access. Keep tokens server-side where practical and never serialize credentials into component props.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify supported frame-rate conversions, long-session drift and missing video recovery. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: frame rate, drop-frame mode and project offset are explicit metadata.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `video-timecode`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/video-timecode.md)) |
| Capability Next.js module skeleton | [`module-music-video-timecode-nextjs`](https://github.com/liberusoftware/module-music-video-timecode-nextjs) (`@liberusoftware/module-music-video-timecode-nextjs`) | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Reference video** | Server Component fetches authorized `reference video` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Frame-rate-aware timeline display** | Server Component fetches authorized `frame-rate-aware timeline display` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Timecode offsets** | Server Component fetches authorized `timecode offsets` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Audio-to-picture synchronization** | Server Component fetches authorized `audio-to-picture synchronization` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
