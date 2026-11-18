# Liberu Music: Composition, Chords and Score — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#composition-score). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-composition-score`

## 1. Purpose

The Composition, Chords and Score module owns Chord tracks, scales, voicings, articulation maps and notation views with printable parts. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Chord tracks:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for chord tracks.
- **Scales:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for scales.
- **Voicings:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for voicings.
- **Articulation maps:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for articulation maps.
- **Notation views with printable parts:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for notation views with printable parts.

## Ownership and workflow

Chord tracks, scales, voicings, articulation maps and notation views with printable parts.

**Required journey:** Create a chord progression, map articulations and print a part.

**Invariant:** Score interpretation never destroys the expressive timing of the source MIDI.

**Dependencies:** midi-sequencing, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Check enharmonic spelling, meter layout and articulation fallback on unsupported instruments. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/composition-score.md), [API plan](../api/composition-score.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Chord tracks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `chord tracks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Scales** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `scales`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Voicings** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `voicings`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Articulation maps** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `articulation maps`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Notation views with printable parts** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `notation views with printable parts`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/composition-score.md) | [Source map](../SOURCE-MAPPING.md#composition-score) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/composition-score.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/composition-score.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-composition-score-filament`](https://github.com/liberusoftware/module-music-composition-score-filament) (`liberusoftware/music-composition-score-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/composition-score.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/composition-score.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-composition-score-react-inertia`](https://github.com/liberusoftware/module-music-composition-score-react-inertia) (`@liberusoftware/module-music-composition-score-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/composition-score.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-composition-score-vue-inertia`](https://github.com/liberusoftware/module-music-composition-score-vue-inertia) (`@liberusoftware/module-music-composition-score-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/composition-score.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-composition-score-nuxt`](https://github.com/liberusoftware/module-music-composition-score-nuxt) (`@liberusoftware/module-music-composition-score-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/composition-score.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-composition-score-nextjs`](https://github.com/liberusoftware/module-music-composition-score-nextjs) (`@liberusoftware/module-music-composition-score-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/composition-score.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-composition-score-react-native`](https://github.com/liberusoftware/module-music-composition-score-react-native) (`@liberusoftware/module-music-composition-score-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/composition-score.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-composition-score-flutter`](https://github.com/liberusoftware/module-music-composition-score-flutter) (`module_music_composition_score_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/composition-score.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-composition-score-dart-mobile`](https://github.com/liberusoftware/module-music-composition-score-dart-mobile) (`module_music_composition_score_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-composition-score-dart-desktop`](https://github.com/liberusoftware/module-music-composition-score-dart-desktop) (`module_music_composition_score_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
