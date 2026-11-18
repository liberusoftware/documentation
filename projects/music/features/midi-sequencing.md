# Liberu Music: MIDI and Expressive Editing — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#midi-sequencing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-midi-sequencing`

## 1. Purpose

The MIDI and Expressive Editing module owns Piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Piano roll:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for piano roll.
- **Drum editor:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for drum editor.
- **Step entry:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for step entry.
- **Controller lanes:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for controller lanes.
- **Note expression:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for note expression.
- **MPE:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for mpe.
- **MIDI import/export:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for midi import/export.

## Ownership and workflow

Piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export.

**Required journey:** Record a MIDI phrase, quantize selected notes and edit per-note expression.

**Invariant:** Notes and expression retain stable identifiers and explicit time units.

**Dependencies:** projects, audio-engine, tempo-groove. Dependencies use public contracts rather than private tables or models.

## Acceptance

Round-trip supported MIDI events and test note-off cleanup after stop or device loss. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/midi-sequencing.md), [API plan](../api/midi-sequencing.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Piano roll** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `piano roll`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Drum editor** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `drum editor`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Step entry** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `step entry`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Controller lanes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `controller lanes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Note expression** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `note expression`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **MPE** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `mpe`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **MIDI import/export** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `midi import/export`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/midi-sequencing.md) | [Source map](../SOURCE-MAPPING.md#midi-sequencing) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/midi-sequencing.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/midi-sequencing.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-midi-sequencing-filament`](https://github.com/liberusoftware/module-music-midi-sequencing-filament) (`liberusoftware/music-midi-sequencing-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/midi-sequencing.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/midi-sequencing.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-midi-sequencing-react-inertia`](https://github.com/liberusoftware/module-music-midi-sequencing-react-inertia) (`@liberusoftware/module-music-midi-sequencing-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/midi-sequencing.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-midi-sequencing-vue-inertia`](https://github.com/liberusoftware/module-music-midi-sequencing-vue-inertia) (`@liberusoftware/module-music-midi-sequencing-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/midi-sequencing.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-midi-sequencing-nuxt`](https://github.com/liberusoftware/module-music-midi-sequencing-nuxt) (`@liberusoftware/module-music-midi-sequencing-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/midi-sequencing.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-midi-sequencing-nextjs`](https://github.com/liberusoftware/module-music-midi-sequencing-nextjs) (`@liberusoftware/module-music-midi-sequencing-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/midi-sequencing.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-midi-sequencing-react-native`](https://github.com/liberusoftware/module-music-midi-sequencing-react-native) (`@liberusoftware/module-music-midi-sequencing-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/midi-sequencing.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-midi-sequencing-flutter`](https://github.com/liberusoftware/module-music-midi-sequencing-flutter) (`module_music_midi_sequencing_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/midi-sequencing.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-midi-sequencing-dart-mobile`](https://github.com/liberusoftware/module-music-midi-sequencing-dart-mobile) (`module_music_midi_sequencing_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-midi-sequencing-dart-desktop`](https://github.com/liberusoftware/module-music-midi-sequencing-dart-desktop) (`module_music_midi_sequencing_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
