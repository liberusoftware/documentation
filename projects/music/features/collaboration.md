# Liberu Music: Collaboration and Review — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Project membership integration, revision sharing, comments, review markers, locks and conflict branches.

**Required journey:** Invite a collaborator, share a checkpoint, annotate a mix and resolve an edit conflict.

**Invariant:** Concurrent musical edits preserve both revisions; sharing never grants access to unrelated assets.

**Dependencies:** projects, media-library, foundation teams and notifications. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test wrong-tenant assets, revoked shares and concurrent edits after offline work. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/collaboration.md), [API plan](../api/collaboration.md) and [surface support](../PRESENTATION.md).
