# Liberu Music: Mixer and Routing — Next.js

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mixer-routing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-mixer-routing-nextjs`. Uses [core](../core/mixer-routing.md) and, for remote access, [API](../api/mixer-routing.md).

## Surface workflow

Present: route tracks through a bus, add a sidechain and save a mix snapshot. Domain scope: channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots.

Use reviewed API DTOs for server data and explicit client components for timeline, AudioWorklet and device access. Keep tokens server-side where practical and never serialize credentials into component props.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify routing cycle detection, solo behavior, channel layouts and delay compensation. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: routing cycles are rejected unless an explicitly supported delayed feedback node exists.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `mixer-routing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/mixer-routing.md)) |
| Capability Next.js module skeleton | [`module-music-mixer-routing-nextjs`](https://github.com/liberusoftware/module-music-mixer-routing-nextjs) (`@liberusoftware/module-music-mixer-routing-nextjs`) | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Channels** | Server Component fetches authorized `channels` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Buses** | Server Component fetches authorized `buses` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Sends** | Server Component fetches authorized `sends` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Sidechains** | Server Component fetches authorized `sidechains` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Pan** | Server Component fetches authorized `pan` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Gain** | Server Component fetches authorized `gain` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Groups** | Server Component fetches authorized `groups` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Solo/mute** | Server Component fetches authorized `solo/mute` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Routing snapshots** | Server Component fetches authorized `routing snapshots` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
