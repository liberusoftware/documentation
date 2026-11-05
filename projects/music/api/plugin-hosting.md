# Liberu Music: Plugin Hosting and Isolation — API

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-plugin-hosting-api`. Depends on the [core contract](../core/plugin-hosting.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for plugin discovery, scanning, process isolation, state snapshots, compatibility and missing-plugin recovery. The first consumer journey is: scan an approved directory, load a plugin, save state and recover a crashed instance. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Crash a scanner/worker and reopen a session with the plugin absent. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: untrusted plugin scans never run in the main application process. Follow [API architecture](../../../architecture/API.md).
