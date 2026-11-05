# Liberu Music: Automation and Modulation — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-automation-modulation`. See [domain specification](../features/automation-modulation.md).

## Public application boundary

Own parameter automation lanes, read/write/touch/latch modes, envelopes, LFOs and modulation mappings. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Automation and modulation have declared precedence and bounded parameter ranges.

**Dependencies:** audio-engine, mixer-routing. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Verify sample scheduling, seek/chase state and smoothing under dense automation. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
