# Liberu Music: MIDI and Expressive Editing — React Native + Expo

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-midi-sequencing-react-native`. Uses [core](../core/midi-sequencing.md) and, for remote access, [API](../api/midi-sequencing.md).

## Surface workflow

Present: record a MIDI phrase, quantize selected notes and edit per-note expression. Domain scope: piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export.

Use native audio workers and typed transport bindings. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Persist local capture before upload; store credentials in Keychain/Keystore.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Round-trip supported MIDI events and test note-off cleanup after stop or device loss. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: notes and expression retain stable identifiers and explicit time units.
