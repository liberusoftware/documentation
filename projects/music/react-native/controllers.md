# Liberu Music: Controllers and Hardware Integration — React Native + Expo

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-controllers-react-native`. Uses [core](../core/controllers.md) and, for remote access, [API](../api/controllers.md).

## Surface workflow

Present: learn a control, map transport, reconnect hardware and reconcile feedback. Domain scope: mIDI port mapping, controller learn, control surfaces, feedback and external clock synchronization.

Use native audio workers and typed transport bindings. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Persist local capture before upload; store credentials in Keychain/Keystore.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Check disconnect, MIDI feedback loops, clock jitter and reconnect mappings. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: lost devices release held notes and stale remote sessions cannot control transport.
