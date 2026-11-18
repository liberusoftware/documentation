# Liberu Music: Projects and Sessions — Next.js

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#projects). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-projects-nextjs`. Uses [core](../core/projects.md) and, for remote access, [API](../api/projects.md).

## Surface workflow

Present: create a session, add tracks, save a checkpoint and recover an interrupted edit. Domain scope: project documents, tracks, folders, templates, revision history, autosave and portable session manifests.

Use reviewed API DTOs for server data and explicit client components for timeline, AudioWorklet and device access. Keep tokens server-side where practical and never serialize credentials into component props.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Recover an autosave and reopen a portable session without missing references. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: every saved revision resolves immutable media references and a declared schema version.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `projects`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/projects.md)) |
| Capability Next.js module skeleton | [`module-music-projects-nextjs`](https://github.com/liberusoftware/module-music-projects-nextjs) (`@liberusoftware/module-music-projects-nextjs`) | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Project documents** | Server Component fetches authorized `project documents` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Tracks** | Server Component fetches authorized `tracks` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Folders** | Server Component fetches authorized `folders` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Templates** | Server Component fetches authorized `templates` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Revision history** | Server Component fetches authorized `revision history` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Autosave** | Server Component fetches authorized `autosave` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Portable session manifests** | Server Component fetches authorized `portable session manifests` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
