# Liberu Music: Arrangement and Audio Editing — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#arrangement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-arrangement`

## 1. Purpose

The Arrangement and Audio Editing module owns Timeline clips, fades, splits, slip edits, crossfades, markers, warp anchors and nondestructive pitch/time changes. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Timeline clips:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for timeline clips.
- **Fades:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for fades.
- **Splits:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for splits.
- **Slip edits:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for slip edits.
- **Crossfades:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for crossfades.
- **Markers:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for markers.
- **Warp anchors:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for warp anchors.
- **Nondestructive pitch/time changes:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for nondestructive pitch/time changes.

## Ownership and workflow

Timeline clips, fades, splits, slip edits, crossfades, markers, warp anchors and nondestructive pitch/time changes.

**Required journey:** Arrange clips, trim and crossfade, stretch to tempo and undo the edit group.

**Invariant:** Edits preserve source audio and explicitly distinguish musical time from sample time.

**Dependencies:** projects, media-library, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify sample boundaries, crossfade continuity and undo/redo across tempo changes. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/arrangement.md), [API plan](../api/arrangement.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Timeline clips** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `timeline clips`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Fades** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `fades`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Splits** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `splits`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Slip edits** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `slip edits`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Crossfades** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `crossfades`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Markers** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `markers`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Warp anchors** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `warp anchors`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Nondestructive pitch/time changes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `nondestructive pitch/time changes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/arrangement.md) | [Source map](../SOURCE-MAPPING.md#arrangement) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/arrangement.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/arrangement.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-arrangement-filament`](https://github.com/liberusoftware/module-music-arrangement-filament) (`liberusoftware/music-arrangement-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/arrangement.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/arrangement.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-arrangement-react-inertia`](https://github.com/liberusoftware/module-music-arrangement-react-inertia) (`@liberusoftware/module-music-arrangement-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/arrangement.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-arrangement-vue-inertia`](https://github.com/liberusoftware/module-music-arrangement-vue-inertia) (`@liberusoftware/module-music-arrangement-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/arrangement.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-arrangement-nuxt`](https://github.com/liberusoftware/module-music-arrangement-nuxt) (`@liberusoftware/module-music-arrangement-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/arrangement.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-arrangement-nextjs`](https://github.com/liberusoftware/module-music-arrangement-nextjs) (`@liberusoftware/module-music-arrangement-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/arrangement.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-arrangement-react-native`](https://github.com/liberusoftware/module-music-arrangement-react-native) (`@liberusoftware/module-music-arrangement-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/arrangement.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-arrangement-flutter`](https://github.com/liberusoftware/module-music-arrangement-flutter) (`module_music_arrangement_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/arrangement.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-arrangement-dart-mobile`](https://github.com/liberusoftware/module-music-arrangement-dart-mobile) (`module_music_arrangement_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-arrangement-dart-desktop`](https://github.com/liberusoftware/module-music-arrangement-dart-desktop) (`module_music_arrangement_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
