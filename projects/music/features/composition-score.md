# Liberu Music: Composition, Chords and Score — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Chord tracks, scales, voicings, articulation maps and notation views with printable parts.

**Required journey:** Create a chord progression, map articulations and print a part.

**Invariant:** Score interpretation never destroys the expressive timing of the source MIDI.

**Dependencies:** midi-sequencing, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Check enharmonic spelling, meter layout and articulation fallback on unsupported instruments. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/composition-score.md), [API plan](../api/composition-score.md) and [surface support](../PRESENTATION.md).
