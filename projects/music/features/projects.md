# Liberu Music: Projects and Sessions — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Project documents, tracks, folders, templates, revision history, autosave and portable session manifests.

**Required journey:** Create a session, add tracks, save a checkpoint and recover an interrupted edit.

**Invariant:** Every saved revision resolves immutable media references and a declared schema version.

**Dependencies:** foundation identity, files and settings. Dependencies use public contracts rather than private tables or models.

## Acceptance

Recover an autosave and reopen a portable session without missing references. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/projects.md), [API plan](../api/projects.md) and [surface support](../PRESENTATION.md).
