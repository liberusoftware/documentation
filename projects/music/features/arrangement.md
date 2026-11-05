# Liberu Music: Arrangement and Audio Editing — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Timeline clips, fades, splits, slip edits, crossfades, markers, warp anchors and nondestructive pitch/time changes.

**Required journey:** Arrange clips, trim and crossfade, stretch to tempo and undo the edit group.

**Invariant:** Edits preserve source audio and explicitly distinguish musical time from sample time.

**Dependencies:** projects, media-library, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify sample boundaries, crossfade continuity and undo/redo across tempo changes. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/arrangement.md), [API plan](../api/arrangement.md) and [surface support](../PRESENTATION.md).
