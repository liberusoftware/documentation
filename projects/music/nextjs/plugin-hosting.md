# Liberu Music: Plugin Hosting and Isolation — Next.js

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-plugin-hosting-nextjs`. Uses [core](../core/plugin-hosting.md) and, for remote access, [API](../api/plugin-hosting.md).

## Surface workflow

Present: scan an approved directory, load a plugin, save state and recover a crashed instance. Domain scope: plugin discovery, scanning, process isolation, state snapshots, compatibility and missing-plugin recovery.

Use reviewed API DTOs for server data and explicit client components for timeline, AudioWorklet and device access. Keep tokens server-side where practical and never serialize credentials into component props.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Crash a scanner/worker and reopen a session with the plugin absent. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: untrusted plugin scans never run in the main application process.
