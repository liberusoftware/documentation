# Liberu Music: Offline Storage and Synchronization — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sync-offline). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-sync-offline`

## 1. Purpose

The Offline Storage and Synchronization module owns Local journals, pinned assets, resumable transfer, revision reconciliation and storage quotas. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Local journals:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for local journals.
- **Pinned assets:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for pinned assets.
- **Resumable transfer:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for resumable transfer.
- **Revision reconciliation:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for revision reconciliation.
- **Storage quotas:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for storage quotas.

## Ownership and workflow

Local journals, pinned assets, resumable transfer, revision reconciliation and storage quotas.

**Required journey:** Pin a session, edit offline, reconnect and resolve divergent revisions.

**Invariant:** A successful local save remains recoverable while remote synchronization is pending.

**Dependencies:** projects, media-library, collaboration. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test expired credentials, interrupted uploads, full disk and divergent offline revisions. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/sync-offline.md), [API plan](../api/sync-offline.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Local journals** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `local journals`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Pinned assets** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `pinned assets`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Resumable transfer** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `resumable transfer`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Revision reconciliation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `revision reconciliation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Storage quotas** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `storage quotas`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/sync-offline.md) | [Source map](../SOURCE-MAPPING.md#sync-offline) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/sync-offline.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/sync-offline.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-sync-offline-filament`](https://github.com/liberusoftware/module-music-sync-offline-filament) (`liberusoftware/music-sync-offline-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/sync-offline.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/sync-offline.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-sync-offline-react-inertia`](https://github.com/liberusoftware/module-music-sync-offline-react-inertia) (`@liberusoftware/module-music-sync-offline-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/sync-offline.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-sync-offline-vue-inertia`](https://github.com/liberusoftware/module-music-sync-offline-vue-inertia) (`@liberusoftware/module-music-sync-offline-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/sync-offline.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-sync-offline-nuxt`](https://github.com/liberusoftware/module-music-sync-offline-nuxt) (`@liberusoftware/module-music-sync-offline-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/sync-offline.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-sync-offline-nextjs`](https://github.com/liberusoftware/module-music-sync-offline-nextjs) (`@liberusoftware/module-music-sync-offline-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/sync-offline.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-sync-offline-react-native`](https://github.com/liberusoftware/module-music-sync-offline-react-native) (`@liberusoftware/module-music-sync-offline-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/sync-offline.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-sync-offline-flutter`](https://github.com/liberusoftware/module-music-sync-offline-flutter) (`module_music_sync_offline_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/sync-offline.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-sync-offline-dart-mobile`](https://github.com/liberusoftware/module-music-sync-offline-dart-mobile) (`module_music_sync_offline_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-sync-offline-dart-desktop`](https://github.com/liberusoftware/module-music-sync-offline-dart-desktop) (`module_music_sync_offline_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
