# Liberu Music: Clip Launcher and Scenes — Filament

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-clip-launcher-filament`. Uses [core](../core/clip-launcher.md) and, for remote access, [API](../api/clip-launcher.md).

## Surface workflow

Present: launch a scene, override one clip and capture the performance to the timeline. Domain scope: quantized clip launch, scenes, follow actions and recording performances into the arrangement.

Provide tenant-scoped resources, read-only revision/engine diagnostics and audited recovery actions. Limit destructive/bulk actions through core policies; do not expose a live DSP graph editor as ordinary CRUD.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify quantized launches during tempo changes and reject invalid follow-action cycles. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: launch decisions execute on the engine clock at the chosen musical boundary.
