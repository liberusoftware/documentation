# Liberu Music: Live Performance and Setlists — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-live-performance`. See [domain specification](../features/live-performance.md).

## Public application boundary

Own setlists, cue preparation, preloaded projects, scene transitions and performance recovery. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Set changes are preflighted for missing assets and bounded CPU/memory use.

**Dependencies:** clip-launcher, controllers, audio-engine. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Measure transition gaps and peak memory; rehearse missing-media and device-failure paths. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
