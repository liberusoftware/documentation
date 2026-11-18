# Liberu Music: Live Performance and Setlists — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#live-performance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-live-performance`

## 1. Purpose

The Live Performance and Setlists module owns Setlists, cue preparation, preloaded projects, scene transitions and performance recovery. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Setlists:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for setlists.
- **Cue preparation:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for cue preparation.
- **Preloaded projects:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for preloaded projects.
- **Scene transitions:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for scene transitions.
- **Performance recovery:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for performance recovery.

## Ownership and workflow

Setlists, cue preparation, preloaded projects, scene transitions and performance recovery.

**Required journey:** Prepare a set, preload the next song and recover a failed device during rehearsal.

**Invariant:** Set changes are preflighted for missing assets and bounded CPU/memory use.

**Dependencies:** clip-launcher, controllers, audio-engine. Dependencies use public contracts rather than private tables or models.

## Acceptance

Measure transition gaps and peak memory; rehearse missing-media and device-failure paths. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/live-performance.md), [API plan](../api/live-performance.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Setlists** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `setlists`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Cue preparation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `cue preparation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Preloaded projects** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `preloaded projects`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Scene transitions** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `scene transitions`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Performance recovery** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `performance recovery`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/live-performance.md) | [Source map](../SOURCE-MAPPING.md#live-performance) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/live-performance.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/live-performance.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-live-performance-filament`](https://github.com/liberusoftware/module-music-live-performance-filament) (`liberusoftware/music-live-performance-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/live-performance.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/live-performance.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-live-performance-react-inertia`](https://github.com/liberusoftware/module-music-live-performance-react-inertia) (`@liberusoftware/module-music-live-performance-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/live-performance.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-live-performance-vue-inertia`](https://github.com/liberusoftware/module-music-live-performance-vue-inertia) (`@liberusoftware/module-music-live-performance-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/live-performance.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-live-performance-nuxt`](https://github.com/liberusoftware/module-music-live-performance-nuxt) (`@liberusoftware/module-music-live-performance-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/live-performance.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-live-performance-nextjs`](https://github.com/liberusoftware/module-music-live-performance-nextjs) (`@liberusoftware/module-music-live-performance-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/live-performance.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-live-performance-react-native`](https://github.com/liberusoftware/module-music-live-performance-react-native) (`@liberusoftware/module-music-live-performance-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/live-performance.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-live-performance-flutter`](https://github.com/liberusoftware/module-music-live-performance-flutter) (`module_music_live_performance_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/live-performance.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-live-performance-dart-mobile`](https://github.com/liberusoftware/module-music-live-performance-dart-mobile) (`module_music_live_performance_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-live-performance-dart-desktop`](https://github.com/liberusoftware/module-music-live-performance-dart-desktop) (`module_music_live_performance_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
