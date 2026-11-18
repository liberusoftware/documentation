# Liberu Music: Presets, Racks and Templates — Next.js

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#presets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-presets-nextjs`. Uses [core](../core/presets.md) and, for remote access, [API](../api/presets.md).

## Surface workflow

Present: save a rack with macro mappings, share it and preview migration before loading. Domain scope: versioned instrument/effect presets, device racks, macros and reusable session templates.

Use reviewed API DTOs for server data and explicit client components for timeline, AudioWorklet and device access. Keep tokens server-side where practical and never serialize credentials into component props.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Test version migration, unavailable devices and safe restoration after failed load. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: preset loading validates schema and dependencies before changing the active graph.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `presets`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/presets.md)) |
| Capability Next.js module skeleton | [`module-music-presets-nextjs`](https://github.com/liberusoftware/module-music-presets-nextjs) (`@liberusoftware/module-music-presets-nextjs`) | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Versioned instrument/effect presets** | Server Component fetches authorized `versioned instrument/effect presets` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Device racks** | Server Component fetches authorized `device racks` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Macros** | Server Component fetches authorized `macros` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Reusable session templates** | Server Component fetches authorized `reusable session templates` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-music-daw-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
