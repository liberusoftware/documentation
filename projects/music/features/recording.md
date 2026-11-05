# Liberu Music: Recording and Take Comping — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Track arming, count-in, punch and loop recording, take lanes, comp segments and recoverable disk writes.

**Required journey:** Arm tracks, capture multiple takes, select comp ranges and recover a partial capture.

**Invariant:** Original takes remain immutable; a comp stores references rather than overwriting recordings.

**Dependencies:** audio-engine, audio-devices, media-library. Dependencies use public contracts rather than private tables or models.

## Acceptance

Capture sustained multitrack audio and recover complete blocks after a forced process exit. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/recording.md), [API plan](../api/recording.md) and [surface support](../PRESENTATION.md).
