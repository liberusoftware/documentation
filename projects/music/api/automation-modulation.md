# Liberu Music: Automation and Modulation — API

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-automation-modulation-api`. Depends on the [core contract](../core/automation-modulation.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for parameter automation lanes, read/write/touch/latch modes, envelopes, LFOs and modulation mappings. The first consumer journey is: record a fader move, edit its curve and add a reversible modulator mapping. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Verify sample scheduling, seek/chase state and smoothing under dense automation. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: automation and modulation have declared precedence and bounded parameter ranges. Follow [API architecture](../../../architecture/API.md).
