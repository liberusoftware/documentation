# Liberu Music: Controllers and Hardware Integration — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#controllers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-controllers`

## 1. Purpose

The Controllers and Hardware Integration module owns MIDI port mapping, controller learn, control surfaces, feedback and external clock synchronization. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **MIDI port mapping:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for midi port mapping.
- **Controller learn:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for controller learn.
- **Control surfaces:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for control surfaces.
- **Feedback:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for feedback.
- **External clock synchronization:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for external clock synchronization.

## Ownership and workflow

MIDI port mapping, controller learn, control surfaces, feedback and external clock synchronization.

**Required journey:** Learn a control, map transport, reconnect hardware and reconcile feedback.

**Invariant:** Lost devices release held notes and stale remote sessions cannot control transport.

**Dependencies:** audio-devices, midi-sequencing, audio-engine. Dependencies use public contracts rather than private tables or models.

## Acceptance

Check disconnect, MIDI feedback loops, clock jitter and reconnect mappings. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/controllers.md), [API plan](../api/controllers.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **MIDI port mapping** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `midi port mapping`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Controller learn** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `controller learn`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Control surfaces** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `control surfaces`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Feedback** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `feedback`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **External clock synchronization** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `external clock synchronization`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/controllers.md) | [Source map](../SOURCE-MAPPING.md#controllers) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/controllers.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/controllers.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-controllers-filament`](https://github.com/liberusoftware/module-music-controllers-filament) (`liberusoftware/music-controllers-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/controllers.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/controllers.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-controllers-react-inertia`](https://github.com/liberusoftware/module-music-controllers-react-inertia) (`@liberusoftware/module-music-controllers-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/controllers.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-controllers-vue-inertia`](https://github.com/liberusoftware/module-music-controllers-vue-inertia) (`@liberusoftware/module-music-controllers-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/controllers.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-controllers-nuxt`](https://github.com/liberusoftware/module-music-controllers-nuxt) (`@liberusoftware/module-music-controllers-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/controllers.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-controllers-nextjs`](https://github.com/liberusoftware/module-music-controllers-nextjs) (`@liberusoftware/module-music-controllers-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/controllers.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-controllers-react-native`](https://github.com/liberusoftware/module-music-controllers-react-native) (`@liberusoftware/module-music-controllers-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/controllers.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-controllers-flutter`](https://github.com/liberusoftware/module-music-controllers-flutter) (`module_music_controllers_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/controllers.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-controllers-dart-mobile`](https://github.com/liberusoftware/module-music-controllers-dart-mobile) (`module_music_controllers_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-controllers-dart-desktop`](https://github.com/liberusoftware/module-music-controllers-dart-desktop) (`module_music_controllers_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
