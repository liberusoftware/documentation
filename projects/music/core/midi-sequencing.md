# Liberu Music: MIDI and Expressive Editing — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-midi-sequencing`. See [domain specification](../features/midi-sequencing.md).

## Public application boundary

Own piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Notes and expression retain stable identifiers and explicit time units.

**Dependencies:** projects, audio-engine, tempo-groove. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Round-trip supported MIDI events and test note-off cleanup after stop or device loss. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
