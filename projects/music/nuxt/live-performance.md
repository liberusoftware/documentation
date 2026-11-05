# Liberu Music: Live Performance and Setlists — Nuxt

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-live-performance-nuxt`. Uses [core](../core/live-performance.md) and, for remote access, [API](../api/live-performance.md).

## Surface workflow

Present: prepare a set, preload the next song and recover a failed device during rehearsal. Domain scope: setlists, cue preparation, preloaded projects, scene transitions and performance recovery.

Use API-backed composables with workspace-scoped cache keys. Initialize AudioWorklet/device access only on the client after a user gesture; clear private cached data at logout.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Measure transition gaps and peak memory; rehearse missing-media and device-failure paths. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: set changes are preflighted for missing assets and bounded CPU/memory use.
