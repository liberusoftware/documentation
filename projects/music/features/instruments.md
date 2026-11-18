# Liberu Music: Instruments and Samplers — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#instruments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-instruments`

## 1. Purpose

The Instruments and Samplers module owns Built-in synth, drum machine, sampler, multisamples, voice allocation and portable instrument presets. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Built-in synth:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for built-in synth.
- **Drum machine:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for drum machine.
- **Sampler:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for sampler.
- **Multisamples:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for multisamples.
- **Voice allocation:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for voice allocation.
- **Portable instrument presets:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for portable instrument presets.

## Ownership and workflow

Built-in synth, drum machine, sampler, multisamples, voice allocation and portable instrument presets.

**Required journey:** Load a sampler, map zones, record a part and freeze the result.

**Invariant:** Voice limits are bounded and missing samples produce explicit recoverable state.

**Dependencies:** audio-engine, media-library, presets. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test voice stealing, sustained notes, missing samples and deterministic seeded patches. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/instruments.md), [API plan](../api/instruments.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Built-in synth** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `built-in synth`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Drum machine** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `drum machine`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Sampler** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `sampler`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Multisamples** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `multisamples`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Voice allocation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `voice allocation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Portable instrument presets** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `portable instrument presets`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/instruments.md) | [Source map](../SOURCE-MAPPING.md#instruments) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/instruments.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/instruments.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-instruments-filament`](https://github.com/liberusoftware/module-music-instruments-filament) (`liberusoftware/music-instruments-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/instruments.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/instruments.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-instruments-react-inertia`](https://github.com/liberusoftware/module-music-instruments-react-inertia) (`@liberusoftware/module-music-instruments-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/instruments.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-instruments-vue-inertia`](https://github.com/liberusoftware/module-music-instruments-vue-inertia) (`@liberusoftware/module-music-instruments-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/instruments.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-instruments-nuxt`](https://github.com/liberusoftware/module-music-instruments-nuxt) (`@liberusoftware/module-music-instruments-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/instruments.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-instruments-nextjs`](https://github.com/liberusoftware/module-music-instruments-nextjs) (`@liberusoftware/module-music-instruments-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/instruments.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-instruments-react-native`](https://github.com/liberusoftware/module-music-instruments-react-native) (`@liberusoftware/module-music-instruments-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/instruments.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-instruments-flutter`](https://github.com/liberusoftware/module-music-instruments-flutter) (`module_music_instruments_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/instruments.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-instruments-dart-mobile`](https://github.com/liberusoftware/module-music-instruments-dart-mobile) (`module_music_instruments_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-instruments-dart-desktop`](https://github.com/liberusoftware/module-music-instruments-dart-desktop) (`module_music_instruments_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
