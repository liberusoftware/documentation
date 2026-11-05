# Liberu Music: MIDI and Expressive Editing — API

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-midi-sequencing-api`. Depends on the [core contract](../core/midi-sequencing.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export. The first consumer journey is: record a MIDI phrase, quantize selected notes and edit per-note expression. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Round-trip supported MIDI events and test note-off cleanup after stop or device loss. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: notes and expression retain stable identifiers and explicit time units. Follow [API architecture](../../../architecture/API.md).
