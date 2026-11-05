# Liberu Music: Automation and Modulation — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Parameter automation lanes, read/write/touch/latch modes, envelopes, LFOs and modulation mappings.

**Required journey:** Record a fader move, edit its curve and add a reversible modulator mapping.

**Invariant:** Automation and modulation have declared precedence and bounded parameter ranges.

**Dependencies:** audio-engine, mixer-routing. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify sample scheduling, seek/chase state and smoothing under dense automation. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/automation-modulation.md), [API plan](../api/automation-modulation.md) and [surface support](../PRESENTATION.md).
