# Liberu Music: Audio Engine and Transport — Livewire

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-audio-engine-livewire`. Uses [core](../core/audio-engine.md) and, for remote access, [API](../api/audio-engine.md).

## Surface workflow

Present: load a graph snapshot, start playback, seek and safely stop. Domain scope: native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering.

Use server-rendered forms for metadata and review. Keep frequent meter/waveform updates in a client component with explicit lifecycle cleanup; avoid server round trips for audio control loops.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Measure callback deadlines, underruns, seek accuracy and latency compensation on reference hardware. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: audio callbacks never wait for network, database, allocation or UI locks.
