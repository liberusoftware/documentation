# Liberu Music: Video and Timecode — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization.

**Required journey:** Import a reference video, align cues and export audio against the picture revision.

**Invariant:** Frame rate, drop-frame mode and project offset are explicit metadata.

**Dependencies:** projects, audio-engine, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify supported frame-rate conversions, long-session drift and missing video recovery. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/video-timecode.md), [API plan](../api/video-timecode.md) and [surface support](../PRESENTATION.md).
