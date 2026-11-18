# Liberu Music: Clip Launcher and Scenes — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#clip-launcher). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-clip-launcher`

## 1. Purpose

The Clip Launcher and Scenes module owns Quantized clip launch, scenes, follow actions and recording performances into the arrangement. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Quantized clip launch:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for quantized clip launch.
- **Scenes:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for scenes.
- **Follow actions:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for follow actions.
- **Recording performances into the arrangement:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for recording performances into the arrangement.

## Ownership and workflow

Quantized clip launch, scenes, follow actions and recording performances into the arrangement.

**Required journey:** Launch a scene, override one clip and capture the performance to the timeline.

**Invariant:** Launch decisions execute on the engine clock at the chosen musical boundary.

**Dependencies:** audio-engine, arrangement, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify quantized launches during tempo changes and reject invalid follow-action cycles. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/clip-launcher.md), [API plan](../api/clip-launcher.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Quantized clip launch** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `quantized clip launch`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Scenes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `scenes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Follow actions** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `follow actions`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Recording performances into the arrangement** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `recording performances into the arrangement`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/clip-launcher.md) | [Source map](../SOURCE-MAPPING.md#clip-launcher) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/clip-launcher.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/clip-launcher.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-clip-launcher-filament`](https://github.com/liberusoftware/module-music-clip-launcher-filament) (`liberusoftware/music-clip-launcher-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/clip-launcher.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/clip-launcher.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-clip-launcher-react-inertia`](https://github.com/liberusoftware/module-music-clip-launcher-react-inertia) (`@liberusoftware/module-music-clip-launcher-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/clip-launcher.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-clip-launcher-vue-inertia`](https://github.com/liberusoftware/module-music-clip-launcher-vue-inertia) (`@liberusoftware/module-music-clip-launcher-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/clip-launcher.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-clip-launcher-nuxt`](https://github.com/liberusoftware/module-music-clip-launcher-nuxt) (`@liberusoftware/module-music-clip-launcher-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/clip-launcher.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-clip-launcher-nextjs`](https://github.com/liberusoftware/module-music-clip-launcher-nextjs) (`@liberusoftware/module-music-clip-launcher-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/clip-launcher.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-clip-launcher-react-native`](https://github.com/liberusoftware/module-music-clip-launcher-react-native) (`@liberusoftware/module-music-clip-launcher-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/clip-launcher.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-clip-launcher-flutter`](https://github.com/liberusoftware/module-music-clip-launcher-flutter) (`module_music_clip_launcher_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/clip-launcher.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-clip-launcher-dart-mobile`](https://github.com/liberusoftware/module-music-clip-launcher-dart-mobile) (`module_music_clip_launcher_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-clip-launcher-dart-desktop`](https://github.com/liberusoftware/module-music-clip-launcher-dart-desktop) (`module_music_clip_launcher_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
