# Liberu Music: Audio Devices and Monitoring — Nuxt

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-audio-devices-nuxt`. Uses [core](../core/audio-devices.md) and, for remote access, [API](../api/audio-devices.md).

## Surface workflow

Present: select an interface, map inputs, check levels and recover from disconnect. Domain scope: device discovery, input/output channel mapping, sample rates, buffer sizes and direct/software monitoring.

Use API-backed composables with workspace-scoped cache keys. Initialize AudioWorklet/device access only on the client after a user gesture; clear private cached data at logout.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Unplug an active interface, deny microphone permission and verify safe recovery. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: a device change must never silently arm a different input or enable a feedback path.
