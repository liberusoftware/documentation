# Liberu Music: Instruments and Samplers — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-instruments`. See [domain specification](../features/instruments.md).

## Public application boundary

Own built-in synth, drum machine, sampler, multisamples, voice allocation and portable instrument presets. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Voice limits are bounded and missing samples produce explicit recoverable state.

**Dependencies:** audio-engine, media-library, presets. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Test voice stealing, sustained notes, missing samples and deterministic seeded patches. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
