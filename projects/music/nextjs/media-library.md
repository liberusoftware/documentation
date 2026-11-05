# Liberu Music: Media Library and Content — Next.js

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-media-library-nextjs`. Uses [core](../core/media-library.md) and, for remote access, [API](../api/media-library.md).

## Surface workflow

Present: import recordings, index peaks, find samples and resolve a missing asset. Domain scope: content-addressed audio assets, waveform peaks, metadata, tags, search, packs and rights provenance.

Use reviewed API DTOs for server data and explicit client components for timeline, AudioWorklet and device access. Keep tokens server-side where practical and never serialize credentials into component props.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify checksums, resumable upload, duplicate detection and referenced-asset retention. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: only verified complete assets become available to a session revision.
