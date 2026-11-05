# Liberu Music: Audio Effects and Amp Processing — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

EQ, dynamics, delay, reverb, modulation effects and independently designed amp/cabinet processing.

**Required journey:** Build an effects chain, automate controls and compare latency-aligned bypass.

**Invariant:** Parameter changes are smoothed and bypass preserves reported latency.

**Dependencies:** audio-engine, presets. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test impulses, silence, finite outputs, parameter smoothing and CPU limits. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/effects.md), [API plan](../api/effects.md) and [surface support](../PRESENTATION.md).
