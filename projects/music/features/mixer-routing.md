# Liberu Music: Mixer and Routing — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots.

**Required journey:** Route tracks through a bus, add a sidechain and save a mix snapshot.

**Invariant:** Routing cycles are rejected unless an explicitly supported delayed feedback node exists.

**Dependencies:** audio-engine, projects. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify routing cycle detection, solo behavior, channel layouts and delay compensation. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/mixer-routing.md), [API plan](../api/mixer-routing.md) and [surface support](../PRESENTATION.md).
