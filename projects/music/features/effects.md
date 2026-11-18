# Liberu Music: Audio Effects and Amp Processing — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#effects). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-effects`

## 1. Purpose

The Audio Effects and Amp Processing module owns EQ, dynamics, delay, reverb, modulation effects and independently designed amp/cabinet processing. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **EQ:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for eq.
- **Dynamics:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for dynamics.
- **Delay:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for delay.
- **Reverb:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for reverb.
- **Modulation effects:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for modulation effects.
- **Independently designed amp/cabinet processing:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for independently designed amp/cabinet processing.

## Ownership and workflow

EQ, dynamics, delay, reverb, modulation effects and independently designed amp/cabinet processing.

**Required journey:** Build an effects chain, automate controls and compare latency-aligned bypass.

**Invariant:** Parameter changes are smoothed and bypass preserves reported latency.

**Dependencies:** audio-engine, presets. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test impulses, silence, finite outputs, parameter smoothing and CPU limits. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/effects.md), [API plan](../api/effects.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **EQ** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `eq`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Dynamics** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `dynamics`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Delay** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `delay`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Reverb** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `reverb`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Modulation effects** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `modulation effects`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Independently designed amp/cabinet processing** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `independently designed amp/cabinet processing`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/effects.md) | [Source map](../SOURCE-MAPPING.md#effects) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/effects.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/effects.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-effects-filament`](https://github.com/liberusoftware/module-music-effects-filament) (`liberusoftware/music-effects-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/effects.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/effects.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-effects-react-inertia`](https://github.com/liberusoftware/module-music-effects-react-inertia) (`@liberusoftware/module-music-effects-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/effects.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-effects-vue-inertia`](https://github.com/liberusoftware/module-music-effects-vue-inertia) (`@liberusoftware/module-music-effects-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/effects.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-effects-nuxt`](https://github.com/liberusoftware/module-music-effects-nuxt) (`@liberusoftware/module-music-effects-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/effects.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-effects-nextjs`](https://github.com/liberusoftware/module-music-effects-nextjs) (`@liberusoftware/module-music-effects-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/effects.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-effects-react-native`](https://github.com/liberusoftware/module-music-effects-react-native) (`@liberusoftware/module-music-effects-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/effects.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-effects-flutter`](https://github.com/liberusoftware/module-music-effects-flutter) (`module_music_effects_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/effects.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-effects-dart-mobile`](https://github.com/liberusoftware/module-music-effects-dart-mobile) (`module_music_effects_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-effects-dart-desktop`](https://github.com/liberusoftware/module-music-effects-dart-desktop) (`module_music_effects_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
