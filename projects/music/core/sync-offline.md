# Liberu Music: Offline Storage and Synchronization — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-sync-offline`. See [domain specification](../features/sync-offline.md).

## Public application boundary

Own local journals, pinned assets, resumable transfer, revision reconciliation and storage quotas. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** A successful local save remains recoverable while remote synchronization is pending.

**Dependencies:** projects, media-library, collaboration. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Test expired credentials, interrupted uploads, full disk and divergent offline revisions. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
