# Liberu Music: Mixer and Routing — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mixer-routing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-mixer-routing`

## 1. Purpose

The Mixer and Routing module owns Channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Channels:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for channels.
- **Buses:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for buses.
- **Sends:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for sends.
- **Sidechains:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for sidechains.
- **Pan:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for pan.
- **Gain:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for gain.
- **Groups:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for groups.
- **Solo/mute:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for solo/mute.
- **Routing snapshots:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for routing snapshots.

## Ownership and workflow

Channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots.

**Required journey:** Route tracks through a bus, add a sidechain and save a mix snapshot.

**Invariant:** Routing cycles are rejected unless an explicitly supported delayed feedback node exists.

**Dependencies:** audio-engine, projects. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify routing cycle detection, solo behavior, channel layouts and delay compensation. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/mixer-routing.md), [API plan](../api/mixer-routing.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Channels** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `channels`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Buses** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `buses`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Sends** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `sends`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Sidechains** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `sidechains`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Pan** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `pan`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Gain** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `gain`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Groups** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `groups`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Solo/mute** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `solo/mute`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Routing snapshots** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `routing snapshots`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/mixer-routing.md) | [Source map](../SOURCE-MAPPING.md#mixer-routing) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/mixer-routing.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/mixer-routing.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-mixer-routing-filament`](https://github.com/liberusoftware/module-music-mixer-routing-filament) (`liberusoftware/music-mixer-routing-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/mixer-routing.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/mixer-routing.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-mixer-routing-react-inertia`](https://github.com/liberusoftware/module-music-mixer-routing-react-inertia) (`@liberusoftware/module-music-mixer-routing-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/mixer-routing.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-mixer-routing-vue-inertia`](https://github.com/liberusoftware/module-music-mixer-routing-vue-inertia) (`@liberusoftware/module-music-mixer-routing-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/mixer-routing.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-mixer-routing-nuxt`](https://github.com/liberusoftware/module-music-mixer-routing-nuxt) (`@liberusoftware/module-music-mixer-routing-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/mixer-routing.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-mixer-routing-nextjs`](https://github.com/liberusoftware/module-music-mixer-routing-nextjs) (`@liberusoftware/module-music-mixer-routing-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/mixer-routing.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-mixer-routing-react-native`](https://github.com/liberusoftware/module-music-mixer-routing-react-native) (`@liberusoftware/module-music-mixer-routing-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/mixer-routing.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-mixer-routing-flutter`](https://github.com/liberusoftware/module-music-mixer-routing-flutter) (`module_music_mixer_routing_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/mixer-routing.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-mixer-routing-dart-mobile`](https://github.com/liberusoftware/module-music-mixer-routing-dart-mobile) (`module_music_mixer_routing_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-mixer-routing-dart-desktop`](https://github.com/liberusoftware/module-music-mixer-routing-dart-desktop) (`module_music_mixer_routing_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
