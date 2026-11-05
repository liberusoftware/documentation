# Liberu Music: Audio Engine and Transport — API

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-audio-engine-api`. Depends on the [core contract](../core/audio-engine.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering. The first consumer journey is: load a graph snapshot, start playback, seek and safely stop. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Measure callback deadlines, underruns, seek accuracy and latency compensation on reference hardware. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: audio callbacks never wait for network, database, allocation or UI locks. Follow [API architecture](../../../architecture/API.md).
