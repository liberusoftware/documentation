# Liberu Music: Plugin Hosting and Isolation — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#plugin-hosting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-plugin-hosting`

## 1. Purpose

The Plugin Hosting and Isolation module owns Plugin discovery, scanning, process isolation, state snapshots, compatibility and missing-plugin recovery. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Plugin discovery:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for plugin discovery.
- **Scanning:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for scanning.
- **Process isolation:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for process isolation.
- **State snapshots:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for state snapshots.
- **Compatibility:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for compatibility.
- **Missing-plugin recovery:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for missing-plugin recovery.

## Ownership and workflow

Plugin discovery, scanning, process isolation, state snapshots, compatibility and missing-plugin recovery.

**Required journey:** Scan an approved directory, load a plugin, save state and recover a crashed instance.

**Invariant:** Untrusted plugin scans never run in the main application process.

**Dependencies:** audio-engine, presets. Dependencies use public contracts rather than private tables or models.

## Acceptance

Crash a scanner/worker and reopen a session with the plugin absent. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/plugin-hosting.md), [API plan](../api/plugin-hosting.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Plugin discovery** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `plugin discovery`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Scanning** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `scanning`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Process isolation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `process isolation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **State snapshots** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `state snapshots`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Compatibility** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `compatibility`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Missing-plugin recovery** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `missing-plugin recovery`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/plugin-hosting.md) | [Source map](../SOURCE-MAPPING.md#plugin-hosting) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/plugin-hosting.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/plugin-hosting.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-plugin-hosting-filament`](https://github.com/liberusoftware/module-music-plugin-hosting-filament) (`liberusoftware/music-plugin-hosting-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/plugin-hosting.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/plugin-hosting.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-plugin-hosting-react-inertia`](https://github.com/liberusoftware/module-music-plugin-hosting-react-inertia) (`@liberusoftware/module-music-plugin-hosting-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/plugin-hosting.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-plugin-hosting-vue-inertia`](https://github.com/liberusoftware/module-music-plugin-hosting-vue-inertia) (`@liberusoftware/module-music-plugin-hosting-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/plugin-hosting.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-plugin-hosting-nuxt`](https://github.com/liberusoftware/module-music-plugin-hosting-nuxt) (`@liberusoftware/module-music-plugin-hosting-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/plugin-hosting.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-plugin-hosting-nextjs`](https://github.com/liberusoftware/module-music-plugin-hosting-nextjs) (`@liberusoftware/module-music-plugin-hosting-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/plugin-hosting.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-plugin-hosting-react-native`](https://github.com/liberusoftware/module-music-plugin-hosting-react-native) (`@liberusoftware/module-music-plugin-hosting-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/plugin-hosting.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-plugin-hosting-flutter`](https://github.com/liberusoftware/module-music-plugin-hosting-flutter) (`module_music_plugin_hosting_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/plugin-hosting.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-plugin-hosting-dart-mobile`](https://github.com/liberusoftware/module-music-plugin-hosting-dart-mobile) (`module_music_plugin_hosting_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-plugin-hosting-dart-desktop`](https://github.com/liberusoftware/module-music-plugin-hosting-dart-desktop) (`module_music_plugin_hosting_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
