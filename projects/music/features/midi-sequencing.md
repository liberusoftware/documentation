# Liberu Music: MIDI and Expressive Editing — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export.

**Required journey:** Record a MIDI phrase, quantize selected notes and edit per-note expression.

**Invariant:** Notes and expression retain stable identifiers and explicit time units.

**Dependencies:** projects, audio-engine, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Round-trip supported MIDI events and test note-off cleanup after stop or device loss. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/midi-sequencing.md), [API plan](../api/midi-sequencing.md) and [surface support](../PRESENTATION.md).
