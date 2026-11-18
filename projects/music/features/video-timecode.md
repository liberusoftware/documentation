# Liberu Music: Video and Timecode — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#video-timecode). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-video-timecode`

## 1. Purpose

The Video and Timecode module owns Reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Reference video:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for reference video.
- **Frame-rate-aware timeline display:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for frame-rate-aware timeline display.
- **Timecode offsets:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for timecode offsets.
- **Audio-to-picture synchronization:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for audio-to-picture synchronization.

## Ownership and workflow

Reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization.

**Required journey:** Import a reference video, align cues and export audio against the picture revision.

**Invariant:** Frame rate, drop-frame mode and project offset are explicit metadata.

**Dependencies:** projects, audio-engine, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify supported frame-rate conversions, long-session drift and missing video recovery. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/video-timecode.md), [API plan](../api/video-timecode.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Reference video** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `reference video`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Frame-rate-aware timeline display** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `frame-rate-aware timeline display`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Timecode offsets** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `timecode offsets`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Audio-to-picture synchronization** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `audio-to-picture synchronization`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/video-timecode.md) | [Source map](../SOURCE-MAPPING.md#video-timecode) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/video-timecode.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/video-timecode.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-video-timecode-filament`](https://github.com/liberusoftware/module-music-video-timecode-filament) (`liberusoftware/music-video-timecode-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/video-timecode.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/video-timecode.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-video-timecode-react-inertia`](https://github.com/liberusoftware/module-music-video-timecode-react-inertia) (`@liberusoftware/module-music-video-timecode-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/video-timecode.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-video-timecode-vue-inertia`](https://github.com/liberusoftware/module-music-video-timecode-vue-inertia) (`@liberusoftware/module-music-video-timecode-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/video-timecode.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-video-timecode-nuxt`](https://github.com/liberusoftware/module-music-video-timecode-nuxt) (`@liberusoftware/module-music-video-timecode-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/video-timecode.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-video-timecode-nextjs`](https://github.com/liberusoftware/module-music-video-timecode-nextjs) (`@liberusoftware/module-music-video-timecode-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/video-timecode.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-video-timecode-react-native`](https://github.com/liberusoftware/module-music-video-timecode-react-native) (`@liberusoftware/module-music-video-timecode-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/video-timecode.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-video-timecode-flutter`](https://github.com/liberusoftware/module-music-video-timecode-flutter) (`module_music_video_timecode_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/video-timecode.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-video-timecode-dart-mobile`](https://github.com/liberusoftware/module-music-video-timecode-dart-mobile) (`module_music_video_timecode_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-video-timecode-dart-desktop`](https://github.com/liberusoftware/module-music-video-timecode-dart-desktop) (`module_music_video_timecode_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
