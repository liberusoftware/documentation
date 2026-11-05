# Liberu Music: Controllers and Hardware Integration — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-controllers`. See [domain specification](../features/controllers.md).

## Public application boundary

Own mIDI port mapping, controller learn, control surfaces, feedback and external clock synchronization. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Lost devices release held notes and stale remote sessions cannot control transport.

**Dependencies:** audio-devices, midi-sequencing, audio-engine. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Check disconnect, MIDI feedback loops, clock jitter and reconnect mappings. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
