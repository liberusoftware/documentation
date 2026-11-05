# Liberu Music: Audio Devices and Monitoring — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Device discovery, input/output channel mapping, sample rates, buffer sizes and direct/software monitoring.

**Required journey:** Select an interface, map inputs, check levels and recover from disconnect.

**Invariant:** A device change must never silently arm a different input or enable a feedback path.

**Dependencies:** audio-engine. Dependencies use public contracts rather than private tables or models.

## Acceptance

Unplug an active interface, deny microphone permission and verify safe recovery. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/audio-devices.md), [API plan](../api/audio-devices.md) and [surface support](../PRESENTATION.md).
