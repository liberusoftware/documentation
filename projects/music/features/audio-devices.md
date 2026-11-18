# Liberu Music: Audio Devices and Monitoring — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#audio-devices). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-audio-devices`

## 1. Purpose

The Audio Devices and Monitoring module owns Device discovery, input/output channel mapping, sample rates, buffer sizes and direct/software monitoring. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Device discovery:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for device discovery.
- **Input/output channel mapping:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for input/output channel mapping.
- **Sample rates:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for sample rates.
- **Buffer sizes:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for buffer sizes.
- **Direct/software monitoring:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for direct/software monitoring.

## Ownership and workflow

Device discovery, input/output channel mapping, sample rates, buffer sizes and direct/software monitoring.

**Required journey:** Select an interface, map inputs, check levels and recover from disconnect.

**Invariant:** A device change must never silently arm a different input or enable a feedback path.

**Dependencies:** audio-engine. Dependencies use public contracts rather than private tables or models.

## Acceptance

Unplug an active interface, deny microphone permission and verify safe recovery. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/audio-devices.md), [API plan](../api/audio-devices.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Device discovery** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `device discovery`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Input/output channel mapping** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `input/output channel mapping`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Sample rates** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `sample rates`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Buffer sizes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `buffer sizes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Direct/software monitoring** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `direct/software monitoring`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/audio-devices.md) | [Source map](../SOURCE-MAPPING.md#audio-devices) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/audio-devices.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/audio-devices.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-audio-devices-filament`](https://github.com/liberusoftware/module-music-audio-devices-filament) (`liberusoftware/music-audio-devices-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/audio-devices.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/audio-devices.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-audio-devices-react-inertia`](https://github.com/liberusoftware/module-music-audio-devices-react-inertia) (`@liberusoftware/module-music-audio-devices-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/audio-devices.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-audio-devices-vue-inertia`](https://github.com/liberusoftware/module-music-audio-devices-vue-inertia) (`@liberusoftware/module-music-audio-devices-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/audio-devices.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-audio-devices-nuxt`](https://github.com/liberusoftware/module-music-audio-devices-nuxt) (`@liberusoftware/module-music-audio-devices-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/audio-devices.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-audio-devices-nextjs`](https://github.com/liberusoftware/module-music-audio-devices-nextjs) (`@liberusoftware/module-music-audio-devices-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/audio-devices.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-audio-devices-react-native`](https://github.com/liberusoftware/module-music-audio-devices-react-native) (`@liberusoftware/module-music-audio-devices-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/audio-devices.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-audio-devices-flutter`](https://github.com/liberusoftware/module-music-audio-devices-flutter) (`module_music_audio_devices_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/audio-devices.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-audio-devices-dart-mobile`](https://github.com/liberusoftware/module-music-audio-devices-dart-mobile) (`module_music_audio_devices_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-audio-devices-dart-desktop`](https://github.com/liberusoftware/module-music-audio-devices-dart-desktop) (`module_music_audio_devices_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
