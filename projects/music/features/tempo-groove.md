# Liberu Music: Tempo, Meter and Groove — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Tempo maps, meter changes, groove templates, swing, metronome and musical/sample-time conversion.

**Required journey:** Set a tempo ramp, change meter and apply reversible groove quantization.

**Invariant:** Time conversion is deterministic at tempo and meter boundaries.

**Dependencies:** projects. Dependencies use public contracts rather than private tables or models.

## Acceptance

Check conversion round trips, ramp integration and metronome alignment. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/tempo-groove.md), [API plan](../api/tempo-groove.md) and [surface support](../PRESENTATION.md).
