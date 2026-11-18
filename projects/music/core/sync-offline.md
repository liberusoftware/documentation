# Liberu Music: Offline Storage and Synchronization — Core

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sync-offline). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-sync-offline`. See [domain specification](../features/sync-offline.md).

## Public application boundary

Own local journals, pinned assets, resumable transfer, revision reconciliation and storage quotas. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** A successful local save remains recoverable while remote synchronization is pending.

**Dependencies:** projects, media-library, collaboration. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Test expired credentials, interrupted uploads, full disk and divergent offline revisions. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Local journals** | Model `local journals` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Pinned assets** | Model `pinned assets` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Resumable transfer** | Model `resumable transfer` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Revision reconciliation** | Model `revision reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Storage quotas** | Model `storage quotas` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/sync-offline.md) · [Filament 5](../filament/sync-offline.md) · [Livewire 4](../livewire/sync-offline.md) · [React + Inertia](../react/sync-offline.md) · [Vue + Inertia](../vue/sync-offline.md) · [Nuxt 4](../nuxt/sync-offline.md) · [Next.js](../nextjs/sync-offline.md) · [React Native](../react-native/sync-offline.md) · [Flutter & Dart](../flutter/sync-offline.md)
<!-- core-implementation-plan:end -->
