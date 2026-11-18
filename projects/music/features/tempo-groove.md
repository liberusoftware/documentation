# Liberu Music: Tempo, Meter and Groove — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#tempo-groove). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-tempo-groove`

## 1. Purpose

The Tempo, Meter and Groove module owns Tempo maps, meter changes, groove templates, swing, metronome and musical/sample-time conversion. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Tempo maps:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for tempo maps.
- **Meter changes:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for meter changes.
- **Groove templates:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for groove templates.
- **Swing:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for swing.
- **Metronome:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for metronome.
- **Musical/sample-time conversion:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for musical/sample-time conversion.

## Ownership and workflow

Tempo maps, meter changes, groove templates, swing, metronome and musical/sample-time conversion.

**Required journey:** Set a tempo ramp, change meter and apply reversible groove quantization.

**Invariant:** Time conversion is deterministic at tempo and meter boundaries.

**Dependencies:** projects. Dependencies use public contracts rather than private tables or models.

## Acceptance

Check conversion round trips, ramp integration and metronome alignment. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/tempo-groove.md), [API plan](../api/tempo-groove.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Tempo maps** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `tempo maps`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Meter changes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `meter changes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Groove templates** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `groove templates`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Swing** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `swing`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Metronome** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `metronome`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Musical/sample-time conversion** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `musical/sample-time conversion`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/tempo-groove.md) | [Source map](../SOURCE-MAPPING.md#tempo-groove) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/tempo-groove.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/tempo-groove.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-tempo-groove-filament`](https://github.com/liberusoftware/module-music-tempo-groove-filament) (`liberusoftware/music-tempo-groove-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/tempo-groove.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/tempo-groove.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-tempo-groove-react-inertia`](https://github.com/liberusoftware/module-music-tempo-groove-react-inertia) (`@liberusoftware/module-music-tempo-groove-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/tempo-groove.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-tempo-groove-vue-inertia`](https://github.com/liberusoftware/module-music-tempo-groove-vue-inertia) (`@liberusoftware/module-music-tempo-groove-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/tempo-groove.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-tempo-groove-nuxt`](https://github.com/liberusoftware/module-music-tempo-groove-nuxt) (`@liberusoftware/module-music-tempo-groove-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/tempo-groove.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-tempo-groove-nextjs`](https://github.com/liberusoftware/module-music-tempo-groove-nextjs) (`@liberusoftware/module-music-tempo-groove-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/tempo-groove.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-tempo-groove-react-native`](https://github.com/liberusoftware/module-music-tempo-groove-react-native) (`@liberusoftware/module-music-tempo-groove-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/tempo-groove.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-tempo-groove-flutter`](https://github.com/liberusoftware/module-music-tempo-groove-flutter) (`module_music_tempo_groove_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/tempo-groove.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-tempo-groove-dart-mobile`](https://github.com/liberusoftware/module-music-tempo-groove-dart-mobile) (`module_music_tempo_groove_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-tempo-groove-dart-desktop`](https://github.com/liberusoftware/module-music-tempo-groove-dart-desktop) (`module_music_tempo_groove_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
