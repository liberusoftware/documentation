# Liberu Music: Offline Storage and Synchronization — Flutter

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-sync-offline-flutter`. Uses [core](../core/sync-offline.md) and, for remote access, [API](../api/sync-offline.md).

## Surface workflow

Present: pin a session, edit offline, reconnect and resolve divergent revisions. Domain scope: local journals, pinned assets, resumable transfer, revision reconciliation and storage quotas.

Use a versioned native engine interface and keep DSP off the Dart UI isolate. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Store credentials in platform secure storage.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Test expired credentials, interrupted uploads, full disk and divergent offline revisions. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: a successful local save remains recoverable while remote synchronization is pending.
