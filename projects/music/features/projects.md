# Liberu Music: Projects and Sessions — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#projects). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-projects`

## 1. Purpose

The Projects and Sessions module owns Project documents, tracks, folders, templates, revision history, autosave and portable session manifests. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Project documents:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for project documents.
- **Tracks:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for tracks.
- **Folders:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for folders.
- **Templates:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for templates.
- **Revision history:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for revision history.
- **Autosave:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for autosave.
- **Portable session manifests:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for portable session manifests.

## Ownership and workflow

Project documents, tracks, folders, templates, revision history, autosave and portable session manifests.

**Required journey:** Create a session, add tracks, save a checkpoint and recover an interrupted edit.

**Invariant:** Every saved revision resolves immutable media references and a declared schema version.

**Dependencies:** foundation identity, files and settings. Dependencies use public contracts rather than private tables or models.

## Acceptance

Recover an autosave and reopen a portable session without missing references. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/projects.md), [API plan](../api/projects.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Project documents** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `project documents`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Tracks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `tracks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Folders** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `folders`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Templates** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `templates`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Revision history** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `revision history`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Autosave** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `autosave`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Portable session manifests** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `portable session manifests`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/projects.md) | [Source map](../SOURCE-MAPPING.md#projects) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/projects.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/projects.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-projects-filament`](https://github.com/liberusoftware/module-music-projects-filament) (`liberusoftware/music-projects-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/projects.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/projects.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-projects-react-inertia`](https://github.com/liberusoftware/module-music-projects-react-inertia) (`@liberusoftware/module-music-projects-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/projects.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-projects-vue-inertia`](https://github.com/liberusoftware/module-music-projects-vue-inertia) (`@liberusoftware/module-music-projects-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/projects.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-projects-nuxt`](https://github.com/liberusoftware/module-music-projects-nuxt) (`@liberusoftware/module-music-projects-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/projects.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-projects-nextjs`](https://github.com/liberusoftware/module-music-projects-nextjs) (`@liberusoftware/module-music-projects-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/projects.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-projects-react-native`](https://github.com/liberusoftware/module-music-projects-react-native) (`@liberusoftware/module-music-projects-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/projects.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-projects-flutter`](https://github.com/liberusoftware/module-music-projects-flutter) (`module_music_projects_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/projects.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-projects-dart-mobile`](https://github.com/liberusoftware/module-music-projects-dart-mobile) (`module_music_projects_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-projects-dart-desktop`](https://github.com/liberusoftware/module-music-projects-dart-desktop) (`module_music_projects_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
