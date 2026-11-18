# Liberu Music: Offline Storage and Synchronization — API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sync-offline). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-sync-offline-api`. Depends on the [core contract](../core/sync-offline.md).

## Proposed contract scope

Expose authorized metadata, capability discovery and command/job status for local journals, pinned assets, resumable transfer, revision reconciliation and storage quotas. The first consumer journey is: pin a session, edit offline, reconnect and resolve divergent revisions. Exact routes and payloads remain to be reviewed in OpenAPI before implementation.

Use workspace-scoped resource identifiers, explicit units, revision preconditions for edits, idempotency keys for retryable commands and paginated collections. Return validation, denied, not-found, revision-conflict, quota and unsupported-capability outcomes. Long processing returns a cancellable job reference with progress and a terminal result. Asset transfer uses short-lived scoped URLs, checksums and resumable upload contracts.

Project updates use ordered revision events with reconnect cursors; consumers resync after a sequence gap. Local transport/MIDI/sample scheduling stays on the engine clock. Remote transport requests require a separately authenticated, paired session with expiry and acknowledgment; network arrival is never a sample-accurate timestamp.

## Contract verification

Test expired credentials, interrupted uploads, full disk and divergent offline revisions. Test revoked access, wrong workspace, stale revisions, duplicate requests and interrupted event streams. Revalidate this invariant in the authoritative owner: a successful local save remains recoverable while remote synchronization is pending. Follow [API architecture](../../../architecture/API.md).

<!-- layer-implementation-plan:start -->
## Product API backend and feature-to-operation plan

This API contract is composed into [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) ([Laravel API backends](../../../guides/LARAVEL-API-BACKENDS.md)) to serve [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react), [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue), [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react), [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter), [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile), and [`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop).

| Feature / aspect | HTTP query and command contract | DTO projection, concurrency & error semantics |
| --- | --- | --- |
| **Local journals** | Expose workspace-scoped read query and explicit command endpoint for `local journals` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Pinned assets** | Expose workspace-scoped read query and explicit command endpoint for `pinned assets` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Resumable transfer** | Expose workspace-scoped read query and explicit command endpoint for `resumable transfer` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Revision reconciliation** | Expose workspace-scoped read query and explicit command endpoint for `revision reconciliation` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Storage quotas** | Expose workspace-scoped read query and explicit command endpoint for `storage quotas` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
<!-- layer-implementation-plan:end -->
