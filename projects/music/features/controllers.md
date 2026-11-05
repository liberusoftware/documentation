# Liberu Music: Controllers and Hardware Integration — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

MIDI port mapping, controller learn, control surfaces, feedback and external clock synchronization.

**Required journey:** Learn a control, map transport, reconnect hardware and reconcile feedback.

**Invariant:** Lost devices release held notes and stale remote sessions cannot control transport.

**Dependencies:** audio-devices, midi-sequencing, audio-engine. Dependencies use public contracts rather than private tables or models.

## Acceptance

Check disconnect, MIDI feedback loops, clock jitter and reconnect mappings. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/controllers.md), [API plan](../api/controllers.md) and [surface support](../PRESENTATION.md).
