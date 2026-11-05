# Liberu Music: Video and Timecode — React + Inertia

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-video-timecode-react`. Uses [core](../core/video-timecode.md) and, for remote access, [API](../api/video-timecode.md).

## Surface workflow

Present: import a reference video, align cues and export audio against the picture revision. Domain scope: reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization.

Use typed Inertia props and authorized Laravel actions for server state. Keep timeline gestures, engine handles and transient meters in client state; dispose audio contexts and subscriptions on navigation.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify supported frame-rate conversions, long-session drift and missing video recovery. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: frame rate, drop-frame mode and project offset are explicit metadata.
