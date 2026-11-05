# Liberu Music: Video and Timecode — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-video-timecode`. See [domain specification](../features/video-timecode.md).

## Public application boundary

Own reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Frame rate, drop-frame mode and project offset are explicit metadata.

**Dependencies:** projects, audio-engine, tempo-groove. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Verify supported frame-rate conversions, long-session drift and missing video recovery. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
