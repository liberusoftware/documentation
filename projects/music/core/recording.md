# Liberu Music: Recording and Take Comping — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-recording`. See [domain specification](../features/recording.md).

## Public application boundary

Own track arming, count-in, punch and loop recording, take lanes, comp segments and recoverable disk writes. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Original takes remain immutable; a comp stores references rather than overwriting recordings.

**Dependencies:** audio-engine, audio-devices, media-library. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Capture sustained multitrack audio and recover complete blocks after a forced process exit. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
