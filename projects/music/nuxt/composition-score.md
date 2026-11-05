# Liberu Music: Composition, Chords and Score — Nuxt

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-composition-score-nuxt`. Uses [core](../core/composition-score.md) and, for remote access, [API](../api/composition-score.md).

## Surface workflow

Present: create a chord progression, map articulations and print a part. Domain scope: chord tracks, scales, voicings, articulation maps and notation views with printable parts.

Use API-backed composables with workspace-scoped cache keys. Initialize AudioWorklet/device access only on the client after a user gesture; clear private cached data at logout.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Check enharmonic spelling, meter layout and articulation fallback on unsupported instruments. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: score interpretation never destroys the expressive timing of the source MIDI.
