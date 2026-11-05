# Liberu Music: Arrangement and Audio Editing — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-arrangement`. See [domain specification](../features/arrangement.md).

## Public application boundary

Own timeline clips, fades, splits, slip edits, crossfades, markers, warp anchors and nondestructive pitch/time changes. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Edits preserve source audio and explicitly distinguish musical time from sample time.

**Dependencies:** projects, media-library, tempo-groove. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Verify sample boundaries, crossfade continuity and undo/redo across tempo changes. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
