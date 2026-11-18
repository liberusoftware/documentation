# Liberu Music: Collaboration and Review — Domain specifications

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collaboration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Domain module:** `module-music-collaboration`

## 1. Purpose

The Collaboration and Review module owns Project membership integration, revision sharing, comments, review markers, locks and conflict branches. It is the authoritative domain boundary for this capability across web, mobile, and desktop DAW surfaces.

## 2. Full feature scope

- **Project membership integration:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for project membership integration.
- **Revision sharing:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for revision sharing.
- **Comments:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for comments.
- **Review markers:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for review markers.
- **Locks:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for locks.
- **Conflict branches:** implement the complete domain rules, sample/musical-time invariants, authorization, revision state, and user/operator feedback required for conflict branches.

## Ownership and workflow

Project membership integration, revision sharing, comments, review markers, locks and conflict branches.

**Required journey:** Invite a collaborator, share a checkpoint, annotate a mix and resolve an edit conflict.

**Invariant:** Concurrent musical edits preserve both revisions; sharing never grants access to unrelated assets.

**Dependencies:** projects, media-library, foundation teams and notifications. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test wrong-tenant assets, revoked shares and concurrent edits after offline work. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/collaboration.md), [API plan](../api/collaboration.md) and [surface support](../PRESENTATION.md).

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Project membership integration** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `project membership integration`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Revision sharing** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `revision sharing`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Comments** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `comments`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Review markers** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `review markers`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Locks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `locks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Conflict branches** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `conflict branches`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/collaboration.md) | [Source map](../SOURCE-MAPPING.md#collaboration) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/collaboration.md) | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/collaboration.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) · [`module-music-collaboration-filament`](https://github.com/liberusoftware/module-music-collaboration-filament) (`liberusoftware/music-collaboration-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/collaboration.md) | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/collaboration.md) | [`project-music-daw-laravel-inertia-react`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-react) · [`module-music-collaboration-react-inertia`](https://github.com/liberusoftware/module-music-collaboration-react-inertia) (`@liberusoftware/module-music-collaboration-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/collaboration.md) | [`project-music-daw-laravel-inertia-vue`](https://github.com/liberusoftware/project-music-daw-laravel-inertia-vue) · [`module-music-collaboration-vue-inertia`](https://github.com/liberusoftware/module-music-collaboration-vue-inertia) (`@liberusoftware/module-music-collaboration-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/collaboration.md) | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) · [`module-music-collaboration-nuxt`](https://github.com/liberusoftware/module-music-collaboration-nuxt) (`@liberusoftware/module-music-collaboration-nuxt`) | Standalone Vue SSR client consuming `project-music-daw-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/collaboration.md) | [`project-music-daw-next-react`](https://github.com/liberusoftware/project-music-daw-next-react) · [`module-music-collaboration-nextjs`](https://github.com/liberusoftware/module-music-collaboration-nextjs) (`@liberusoftware/module-music-collaboration-nextjs`) | App Router Server/Client components consuming `project-music-daw-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/collaboration.md) | [`project-music-daw-mobile-react`](https://github.com/liberusoftware/project-music-daw-mobile-react) · [`module-music-collaboration-react-native`](https://github.com/liberusoftware/module-music-collaboration-react-native) (`@liberusoftware/module-music-collaboration-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/collaboration.md) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) · [`module-music-collaboration-flutter`](https://github.com/liberusoftware/module-music-collaboration-flutter) (`module_music_collaboration_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/collaboration.md) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) · [`module-music-collaboration-dart-mobile`](https://github.com/liberusoftware/module-music-collaboration-dart-mobile) (`module_music_collaboration_dart_mobile`)<br>[`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) · [`module-music-collaboration-dart-desktop`](https://github.com/liberusoftware/module-music-collaboration-dart-desktop) (`module_music_collaboration_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
