# Liberu Music: Audio Engine and Transport — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering.

**Required journey:** Load a graph snapshot, start playback, seek and safely stop.

**Invariant:** Audio callbacks never wait for network, database, allocation or UI locks.

**Dependencies:** projects. Dependencies use public contracts rather than private tables or models.

## Acceptance

Measure callback deadlines, underruns, seek accuracy and latency compensation on reference hardware. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/audio-engine.md), [API plan](../api/audio-engine.md) and [surface support](../PRESENTATION.md).
