# Liberu: Platform Orchestration

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#platform-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent feature specification

**Domain module:** `module-liberu-platform-orchestration`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; does not replace Module Manager or any product module
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Platform Orchestration coordinates application manifests, enabled/installed/entitled states, cross-product capability declarations, workflow ownership, release gates, and safe composition. It does not own product records, package internals, authorization policy, or business workflows already owned by another project.

## New capabilities

- **Composition manifest:** declare applications, selected modules, adapters, themes, compatibility ranges, and deliberate exclusions.
- **Capability graph:** resolve required/optional capabilities and report missing, conflicting, or unsupported combinations before activation.
- **Lifecycle coordination:** distinguish install, enable, entitlement, activation, migration, disable, upgrade, and uninstall states.
- **Release gates:** collect compatibility, migration, security, test, and operator sign-off evidence for a composed release.
- **Ownership registry:** identify the authoritative module and escalation owner for cross-product workflows without copying its data.

## Boundaries and verification

The module stores only platform composition metadata and evidence. It consumes package manifests and public contracts, never private tables. Test collision detection, dependency cycles, capability resolution, authorization, tenant isolation, migration rehearsal, rollback, and safe failure when an optional module is unavailable.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Composition manifest** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `composition manifest`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Capability graph** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `capability graph`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Lifecycle coordination** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `lifecycle coordination`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Release gates** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `release gates`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Ownership registry** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `ownership registry`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/platform-orchestration.md) | [Source map](../SOURCE-MAPPING.md#platform-orchestration) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/platform-orchestration.md) | [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/platform-orchestration.md) | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) · [`module-planned-liberu-platform-orchestration-081c1f70-filament`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-filament) (`liberusoftware/planned-liberu-platform-orchestration-081c1f70-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/platform-orchestration.md) | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/platform-orchestration.md) | [`project-liberu-official-laravel-inertia-react`](https://github.com/liberusoftware/project-liberu-official-laravel-inertia-react) · [`module-planned-liberu-platform-orchestration-081c1f70-react-inertia`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-react-inertia) (`@liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/platform-orchestration.md) | [`project-liberu-official-laravel-inertia-vue`](https://github.com/liberusoftware/project-liberu-official-laravel-inertia-vue) · [`module-planned-liberu-platform-orchestration-081c1f70-vue-inertia`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-vue-inertia) (`@liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/platform-orchestration.md) | [`project-liberu-official-nuxt-vue`](https://github.com/liberusoftware/project-liberu-official-nuxt-vue) · [`module-planned-liberu-platform-orchestration-081c1f70-nuxt`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-nuxt) (`@liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-nuxt`) | Standalone Vue SSR client consuming `project-liberu-official-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/platform-orchestration.md) | [`project-liberu-official-next-react`](https://github.com/liberusoftware/project-liberu-official-next-react) · [`module-planned-liberu-platform-orchestration-081c1f70-nextjs`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-nextjs) (`@liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-nextjs`) | App Router Server/Client components consuming `project-liberu-official-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/platform-orchestration.md) | [`project-liberu-official-mobile-react`](https://github.com/liberusoftware/project-liberu-official-mobile-react) · [`module-planned-liberu-platform-orchestration-081c1f70-react-native`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-react-native) (`@liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/platform-orchestration.md) | [`project-liberu-official-mobile-flutter`](https://github.com/liberusoftware/project-liberu-official-mobile-flutter) · [`module-planned-liberu-platform-orchestration-081c1f70-flutter`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-flutter) (`module_planned_liberu_platform_orchestration_081c1f70_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/platform-orchestration.md) | [`project-liberu-official-dart-mobile`](https://github.com/liberusoftware/project-liberu-official-dart-mobile) · [`module-planned-liberu-platform-orchestration-081c1f70-dart-mobile`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-dart-mobile) (`module_planned_liberu_platform_orchestration_081c1f70_dart_mobile`)<br>[`project-liberu-official-dart-desktop`](https://github.com/liberusoftware/project-liberu-official-dart-desktop) · [`module-planned-liberu-platform-orchestration-081c1f70-dart-desktop`](https://github.com/liberusoftware/module-planned-liberu-platform-orchestration-081c1f70-dart-desktop) (`module_planned_liberu_platform_orchestration_081c1f70_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
