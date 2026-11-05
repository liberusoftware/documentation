# Liberu Music: Live Performance and Setlists — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Setlists, cue preparation, preloaded projects, scene transitions and performance recovery.

**Required journey:** Prepare a set, preload the next song and recover a failed device during rehearsal.

**Invariant:** Set changes are preflighted for missing assets and bounded CPU/memory use.

**Dependencies:** clip-launcher, controllers, audio-engine. Dependencies use public contracts rather than private tables or models.

## Acceptance

Measure transition gaps and peak memory; rehearse missing-media and device-failure paths. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/live-performance.md), [API plan](../api/live-performance.md) and [surface support](../PRESENTATION.md).
