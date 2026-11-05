# Liberu Music: Export, Mastering and Delivery — API

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-export-mastering-api`. Depends on the [core contract](../core/export-mastering.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests. The first consumer journey is: export a mix and stems, inspect loudness and verify delivery checksums. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Compare realtime/offline output within declared tolerances and test clipping, tails and cancellation. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: a render records source revision, graph/plugin versions, format and processing settings. Follow [API architecture](../../../architecture/API.md).
