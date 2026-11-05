# Liberu Music: Clip Launcher and Scenes — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Quantized clip launch, scenes, follow actions and recording performances into the arrangement.

**Required journey:** Launch a scene, override one clip and capture the performance to the timeline.

**Invariant:** Launch decisions execute on the engine clock at the chosen musical boundary.

**Dependencies:** audio-engine, arrangement, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify quantized launches during tempo changes and reject invalid follow-action cycles. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/clip-launcher.md), [API plan](../api/clip-launcher.md) and [surface support](../PRESENTATION.md).
