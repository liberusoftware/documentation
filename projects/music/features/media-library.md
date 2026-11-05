# Liberu Music: Media Library and Content — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Content-addressed audio assets, waveform peaks, metadata, tags, search, packs and rights provenance.

**Required journey:** Import recordings, index peaks, find samples and resolve a missing asset.

**Invariant:** Only verified complete assets become available to a session revision.

**Dependencies:** foundation files, search and import/export. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify checksums, resumable upload, duplicate detection and referenced-asset retention. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/media-library.md), [API plan](../api/media-library.md) and [surface support](../PRESENTATION.md).
