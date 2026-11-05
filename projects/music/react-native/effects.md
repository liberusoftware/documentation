# Liberu Music: Audio Effects and Amp Processing — React Native + Expo

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-effects-react-native`. Uses [core](../core/effects.md) and, for remote access, [API](../api/effects.md).

## Surface workflow

Present: build an effects chain, automate controls and compare latency-aligned bypass. Domain scope: eQ, dynamics, delay, reverb, modulation effects and independently designed amp/cabinet processing.

Use native audio workers and typed transport bindings. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Persist local capture before upload; store credentials in Keychain/Keystore.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Test impulses, silence, finite outputs, parameter smoothing and CPU limits. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: parameter changes are smoothed and bypass preserves reported latency.
