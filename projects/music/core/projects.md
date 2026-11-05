# Liberu Music: Projects and Sessions — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-projects`. See [domain specification](../features/projects.md).

## Public application boundary

Own project documents, tracks, folders, templates, revision history, autosave and portable session manifests. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Every saved revision resolves immutable media references and a declared schema version.

**Dependencies:** foundation identity, files and settings. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Recover an autosave and reopen a portable session without missing references. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
