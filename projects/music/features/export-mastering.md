# Liberu Music: Export, Mastering and Delivery — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#export-mastering). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-export-mastering`

## 1. Purpose

The Export, Mastering and Delivery module owns Offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Offline bounce:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for offline bounce.
- **Stems:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for stems.
- **Freeze/flatten:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for freeze/flatten.
- **Dithering:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for dithering.
- **Loudness/true-peak analysis:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for loudness/true-peak analysis.
- **Delivery manifests:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for delivery manifests.

## Ownership and workflow

Offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests.

**Required journey:** Export a mix and stems, inspect loudness and verify delivery checksums.

**Invariant:** A render records source revision, graph/plugin versions, format and processing settings.

**Dependencies:** audio-engine, mixer-routing, media-library. Dependencies use public contracts rather than private tables or models.

## Acceptance

Compare realtime/offline output within declared tolerances and test clipping, tails and cancellation. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/export-mastering.md), [API plan](../api/export-mastering.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Offline bounce** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `offline bounce`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Stems** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `stems`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Freeze/flatten** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `freeze/flatten`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Dithering** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `dithering`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Loudness/true-peak analysis** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `loudness/true-peak analysis`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Delivery manifests** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `delivery manifests`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/export-mastering.md) | [Source map](../SOURCE-MAPPING.md#export-mastering) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/export-mastering.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/export-mastering.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-export-mastering-filament`](https://github.com/liberusoftware/module-music-export-mastering-filament) (`liberusoftware/music-export-mastering-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/export-mastering.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/export-mastering.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-export-mastering-react-inertia`](https://github.com/liberusoftware/module-music-export-mastering-react-inertia) (`@liberusoftware/module-music-export-mastering-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/export-mastering.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-export-mastering-vue-inertia`](https://github.com/liberusoftware/module-music-export-mastering-vue-inertia) (`@liberusoftware/module-music-export-mastering-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/export-mastering.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-export-mastering-nuxt`](https://github.com/liberusoftware/module-music-export-mastering-nuxt) (`@liberusoftware/module-music-export-mastering-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/export-mastering.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-export-mastering-nextjs`](https://github.com/liberusoftware/module-music-export-mastering-nextjs) (`@liberusoftware/module-music-export-mastering-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/export-mastering.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-export-mastering-react-native`](https://github.com/liberusoftware/module-music-export-mastering-react-native) (`@liberusoftware/module-music-export-mastering-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/export-mastering.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-export-mastering-flutter`](https://github.com/liberusoftware/module-music-export-mastering-flutter) (`module_music_export_mastering_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/export-mastering.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-export-mastering-dart-mobile`](https://github.com/liberusoftware/module-music-export-mastering-dart-mobile) (`module_music_export_mastering_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-export-mastering-dart-desktop`](https://github.com/liberusoftware/module-music-export-mastering-dart-desktop) (`module_music_export_mastering_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
