# Liberu Music: Collaboration and Review — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-collaboration`. See [domain specification](../features/collaboration.md).

## Public application boundary

Own project membership integration, revision sharing, comments, review markers, locks and conflict branches. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Concurrent musical edits preserve both revisions; sharing never grants access to unrelated assets.

**Dependencies:** projects, media-library, foundation teams and notifications. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Test wrong-tenant assets, revoked shares and concurrent edits after offline work. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
