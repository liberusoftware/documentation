# Liberu Music: Composition, Chords and Score — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-composition-score`. See [domain specification](../features/composition-score.md).

## Public application boundary

Own chord tracks, scales, voicings, articulation maps and notation views with printable parts. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Score interpretation never destroys the expressive timing of the source MIDI.

**Dependencies:** midi-sequencing, tempo-groove. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Check enharmonic spelling, meter layout and articulation fallback on unsupported instruments. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
