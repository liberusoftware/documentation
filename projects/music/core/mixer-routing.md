# Liberu Music: Mixer and Routing — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-mixer-routing`. See [domain specification](../features/mixer-routing.md).

## Public application boundary

Own channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Routing cycles are rejected unless an explicitly supported delayed feedback node exists.

**Dependencies:** audio-engine, projects. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Verify routing cycle detection, solo behavior, channel layouts and delay compensation. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
