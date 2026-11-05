# Liberu Music: Tempo, Meter and Groove — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-tempo-groove`. See [domain specification](../features/tempo-groove.md).

## Public application boundary

Own tempo maps, meter changes, groove templates, swing, metronome and musical/sample-time conversion. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Time conversion is deterministic at tempo and meter boundaries.

**Dependencies:** projects. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Check conversion round trips, ramp integration and metronome alignment. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
