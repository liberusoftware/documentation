# Liberu Music: Audio Engine and Transport — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-audio-engine`. See [domain specification](../features/audio-engine.md).

## Public application boundary

Own native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Audio callbacks never wait for network, database, allocation or UI locks.

**Dependencies:** projects. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Measure callback deadlines, underruns, seek accuracy and latency compensation on reference hardware. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
