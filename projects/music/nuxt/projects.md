# Liberu Music: Projects and Sessions — Nuxt

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-projects-nuxt`. Uses [core](../core/projects.md) and, for remote access, [API](../api/projects.md).

## Surface workflow

Present: create a session, add tracks, save a checkpoint and recover an interrupted edit. Domain scope: project documents, tracks, folders, templates, revision history, autosave and portable session manifests.

Use API-backed composables with workspace-scoped cache keys. Initialize AudioWorklet/device access only on the client after a user gesture; clear private cached data at logout.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Recover an autosave and reopen a portable session without missing references. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: every saved revision resolves immutable media references and a declared schema version.
