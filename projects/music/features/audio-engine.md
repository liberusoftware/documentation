# Liberu Music: Audio Engine and Transport — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#audio-engine). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-audio-engine`

## 1. Purpose

The Audio Engine and Transport module owns Native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Native audio graph:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for native audio graph.
- **Sample clock:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for sample clock.
- **Play/stop/seek:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for play/stop/seek.
- **Buffers:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for buffers.
- **Latency compensation:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for latency compensation.
- **Offline graph rendering:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for offline graph rendering.

## Ownership and workflow

Native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering.

**Required journey:** Load a graph snapshot, start playback, seek and safely stop.

**Invariant:** Audio callbacks never wait for network, database, allocation or UI locks.

**Dependencies:** projects. Dependencies use public contracts rather than private tables or models.

## Acceptance

Measure callback deadlines, underruns, seek accuracy and latency compensation on reference hardware. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/audio-engine.md), [API plan](../api/audio-engine.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Native audio graph** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `native audio graph`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Sample clock** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `sample clock`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Play/stop/seek** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `play/stop/seek`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Buffers** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `buffers`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Latency compensation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `latency compensation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Offline graph rendering** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `offline graph rendering`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/audio-engine.md) | [Source map](../SOURCE-MAPPING.md#audio-engine) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/audio-engine.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/audio-engine.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-audio-engine-filament`](https://github.com/liberusoftware/module-music-audio-engine-filament) (`liberusoftware/music-audio-engine-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/audio-engine.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/audio-engine.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-audio-engine-react-inertia`](https://github.com/liberusoftware/module-music-audio-engine-react-inertia) (`@liberusoftware/module-music-audio-engine-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/audio-engine.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-audio-engine-vue-inertia`](https://github.com/liberusoftware/module-music-audio-engine-vue-inertia) (`@liberusoftware/module-music-audio-engine-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/audio-engine.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-audio-engine-nuxt`](https://github.com/liberusoftware/module-music-audio-engine-nuxt) (`@liberusoftware/module-music-audio-engine-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/audio-engine.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-audio-engine-nextjs`](https://github.com/liberusoftware/module-music-audio-engine-nextjs) (`@liberusoftware/module-music-audio-engine-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/audio-engine.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-audio-engine-react-native`](https://github.com/liberusoftware/module-music-audio-engine-react-native) (`@liberusoftware/module-music-audio-engine-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/audio-engine.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-audio-engine-flutter`](https://github.com/liberusoftware/module-music-audio-engine-flutter) (`module_music_audio_engine_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/audio-engine.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-audio-engine-dart-mobile`](https://github.com/liberusoftware/module-music-audio-engine-dart-mobile) (`module_music_audio_engine_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-audio-engine-dart-desktop`](https://github.com/liberusoftware/module-music-audio-engine-dart-desktop) (`module_music_audio_engine_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
