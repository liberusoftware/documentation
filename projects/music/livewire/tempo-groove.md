# Liberu Music: Tempo, Meter and Groove — Livewire

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-tempo-groove-livewire`. Uses [core](../core/tempo-groove.md) and, for remote access, [API](../api/tempo-groove.md).

## Surface workflow

Present: set a tempo ramp, change meter and apply reversible groove quantization. Domain scope: tempo maps, meter changes, groove templates, swing, metronome and musical/sample-time conversion.

Use server-rendered forms for metadata and review. Keep frequent meter/waveform updates in a client component with explicit lifecycle cleanup; avoid server round trips for audio control loops.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Check conversion round trips, ramp integration and metronome alignment. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: time conversion is deterministic at tempo and meter boundaries.
