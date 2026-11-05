# Liberu Music: Arrangement and Audio Editing — React Native + Expo

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-arrangement-react-native`. Uses [core](../core/arrangement.md) and, for remote access, [API](../api/arrangement.md).

## Surface workflow

Present: arrange clips, trim and crossfade, stretch to tempo and undo the edit group. Domain scope: timeline clips, fades, splits, slip edits, crossfades, markers, warp anchors and nondestructive pitch/time changes.

Use native audio workers and typed transport bindings. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Persist local capture before upload; store credentials in Keychain/Keystore.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify sample boundaries, crossfade continuity and undo/redo across tempo changes. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: edits preserve source audio and explicitly distinguish musical time from sample time.
