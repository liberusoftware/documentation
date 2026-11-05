# Liberu Music: Presets, Racks and Templates — API

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-presets-api`. Depends on the [core contract](../core/presets.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for versioned instrument/effect presets, device racks, macros and reusable session templates. The first consumer journey is: save a rack with macro mappings, share it and preview migration before loading. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Test version migration, unavailable devices and safe restoration after failed load. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: preset loading validates schema and dependencies before changing the active graph. Follow [API architecture](../../../architecture/API.md).
