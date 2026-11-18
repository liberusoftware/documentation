# Liberu Music: Automation and Modulation — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#automation-modulation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-automation-modulation`

## 1. Purpose

The Automation and Modulation module owns Parameter automation lanes, read/write/touch/latch modes, envelopes, LFOs and modulation mappings. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Parameter automation lanes:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for parameter automation lanes.
- **Read/write/touch/latch modes:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for read/write/touch/latch modes.
- **Envelopes:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for envelopes.
- **LFOs:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for lfos.
- **Modulation mappings:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for modulation mappings.

## Ownership and workflow

Parameter automation lanes, read/write/touch/latch modes, envelopes, LFOs and modulation mappings.

**Required journey:** Record a fader move, edit its curve and add a reversible modulator mapping.

**Invariant:** Automation and modulation have declared precedence and bounded parameter ranges.

**Dependencies:** audio-engine, mixer-routing. Dependencies use public contracts rather than private tables or models.

## Acceptance

Verify sample scheduling, seek/chase state and smoothing under dense automation. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/automation-modulation.md), [API plan](../api/automation-modulation.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Parameter automation lanes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `parameter automation lanes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Read/write/touch/latch modes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `read/write/touch/latch modes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Envelopes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `envelopes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **LFOs** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `lfos`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Modulation mappings** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `modulation mappings`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/automation-modulation.md) | [Source map](../SOURCE-MAPPING.md#automation-modulation) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/automation-modulation.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/automation-modulation.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-automation-modulation-filament`](https://github.com/liberusoftware/module-music-automation-modulation-filament) (`liberusoftware/music-automation-modulation-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/automation-modulation.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/automation-modulation.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-automation-modulation-react-inertia`](https://github.com/liberusoftware/module-music-automation-modulation-react-inertia) (`@liberusoftware/module-music-automation-modulation-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/automation-modulation.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-automation-modulation-vue-inertia`](https://github.com/liberusoftware/module-music-automation-modulation-vue-inertia) (`@liberusoftware/module-music-automation-modulation-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/automation-modulation.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-automation-modulation-nuxt`](https://github.com/liberusoftware/module-music-automation-modulation-nuxt) (`@liberusoftware/module-music-automation-modulation-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/automation-modulation.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-automation-modulation-nextjs`](https://github.com/liberusoftware/module-music-automation-modulation-nextjs) (`@liberusoftware/module-music-automation-modulation-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/automation-modulation.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-automation-modulation-react-native`](https://github.com/liberusoftware/module-music-automation-modulation-react-native) (`@liberusoftware/module-music-automation-modulation-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/automation-modulation.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-automation-modulation-flutter`](https://github.com/liberusoftware/module-music-automation-modulation-flutter) (`module_music_automation_modulation_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/automation-modulation.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-automation-modulation-dart-mobile`](https://github.com/liberusoftware/module-music-automation-modulation-dart-mobile) (`module_music_automation_modulation_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-automation-modulation-dart-desktop`](https://github.com/liberusoftware/module-music-automation-modulation-dart-desktop) (`module_music_automation_modulation_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
