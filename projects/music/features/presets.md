# Liberu Music: Presets, Racks and Templates — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#presets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-presets`

## 1. Purpose

The Presets, Racks and Templates module owns Versioned instrument/effect presets, device racks, macros and reusable session templates. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Versioned instrument/effect presets:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for versioned instrument/effect presets.
- **Device racks:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for device racks.
- **Macros:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for macros.
- **Reusable session templates:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for reusable session templates.

## Ownership and workflow

Versioned instrument/effect presets, device racks, macros and reusable session templates.

**Required journey:** Save a rack with macro mappings, share it and preview migration before loading.

**Invariant:** Preset loading validates schema and dependencies before changing the active graph.

**Dependencies:** projects, media-library. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test version migration, unavailable devices and safe restoration after failed load. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/presets.md), [API plan](../api/presets.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Versioned instrument/effect presets** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `versioned instrument/effect presets`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Device racks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `device racks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Macros** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `macros`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Reusable session templates** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `reusable session templates`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/presets.md) | [Source map](../SOURCE-MAPPING.md#presets) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/presets.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/presets.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-presets-filament`](https://github.com/liberusoftware/module-music-presets-filament) (`liberusoftware/music-presets-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/presets.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/presets.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-presets-react-inertia`](https://github.com/liberusoftware/module-music-presets-react-inertia) (`@liberusoftware/module-music-presets-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/presets.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-presets-vue-inertia`](https://github.com/liberusoftware/module-music-presets-vue-inertia) (`@liberusoftware/module-music-presets-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/presets.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-presets-nuxt`](https://github.com/liberusoftware/module-music-presets-nuxt) (`@liberusoftware/module-music-presets-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/presets.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-presets-nextjs`](https://github.com/liberusoftware/module-music-presets-nextjs) (`@liberusoftware/module-music-presets-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/presets.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-presets-react-native`](https://github.com/liberusoftware/module-music-presets-react-native) (`@liberusoftware/module-music-presets-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/presets.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-presets-flutter`](https://github.com/liberusoftware/module-music-presets-flutter) (`module_music_presets_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/presets.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-presets-dart-mobile`](https://github.com/liberusoftware/module-music-presets-dart-mobile) (`module_music_presets_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-presets-dart-desktop`](https://github.com/liberusoftware/module-music-presets-dart-desktop) (`module_music_presets_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
