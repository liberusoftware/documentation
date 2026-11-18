# Liberu Music: Media Library and Content — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#media-library). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-media-library`

## 1. Purpose

The Media Library and Content module owns Content-addressed audio assets, waveform peaks, metadata, tags, search, packs and rights provenance. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Content-addressed audio assets:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for content-addressed audio assets.
- **Waveform peaks:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for waveform peaks.
- **Metadata:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for metadata.
- **Tags:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for tags.
- **Search:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for search.
- **Packs:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for packs.
- **Rights provenance:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for rights provenance.

## Ownership and workflow

Content-addressed audio assets, waveform peaks, metadata, tags, search, packs and rights provenance.

**Required journey:** Import recordings, index peaks, find samples and resolve a missing asset.

**Invariant:** Only verified complete assets become available to a session revision.

**Dependencies:** foundation files, search and import/export. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify checksums, resumable upload, duplicate detection and referenced-asset retention. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/media-library.md), [API plan](../api/media-library.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Content-addressed audio assets** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `content-addressed audio assets`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Waveform peaks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `waveform peaks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Metadata** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `metadata`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Tags** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `tags`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Search** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `search`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Packs** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `packs`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Rights provenance** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `rights provenance`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/media-library.md) | [Source map](../SOURCE-MAPPING.md#media-library) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/media-library.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/media-library.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-media-library-filament`](https://github.com/liberusoftware/module-music-media-library-filament) (`liberusoftware/music-media-library-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/media-library.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/media-library.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-media-library-react-inertia`](https://github.com/liberusoftware/module-music-media-library-react-inertia) (`@liberusoftware/module-music-media-library-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/media-library.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-media-library-vue-inertia`](https://github.com/liberusoftware/module-music-media-library-vue-inertia) (`@liberusoftware/module-music-media-library-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/media-library.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-media-library-nuxt`](https://github.com/liberusoftware/module-music-media-library-nuxt) (`@liberusoftware/module-music-media-library-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/media-library.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-media-library-nextjs`](https://github.com/liberusoftware/module-music-media-library-nextjs) (`@liberusoftware/module-music-media-library-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/media-library.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-media-library-react-native`](https://github.com/liberusoftware/module-music-media-library-react-native) (`@liberusoftware/module-music-media-library-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/media-library.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-media-library-flutter`](https://github.com/liberusoftware/module-music-media-library-flutter) (`module_music_media_library_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/media-library.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-media-library-dart-mobile`](https://github.com/liberusoftware/module-music-media-library-dart-mobile) (`module_music_media_library_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-media-library-dart-desktop`](https://github.com/liberusoftware/module-music-media-library-dart-desktop) (`module_music_media_library_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
