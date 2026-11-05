# Liberu Music: Collaboration and Review — API

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-collaboration-api`. Depends on the [core contract](../core/collaboration.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for project membership integration, revision sharing, comments, review markers, locks and conflict branches. The first consumer journey is: invite a collaborator, share a checkpoint, annotate a mix and resolve an edit conflict. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Test wrong-tenant assets, revoked shares and concurrent edits after offline work. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: concurrent musical edits preserve both revisions; sharing never grants access to unrelated assets. Follow [API architecture](../../../architecture/API.md).
