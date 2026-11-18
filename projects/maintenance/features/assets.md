# Maintenance: Assets

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#assets). Observed identity: [`liberusoftware/module-maintenance-assets`](../../../modules/source/liberusoftware--module-maintenance-assets.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-maintenance-assets`
**Application:** Maintenance
**Capability group:** Module plan
**Source scope:** [MAINTENANCE.md](../MAINTENANCE.md)
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Assets module owns Hierarchies, categories, specifications, meters, warranties, condition, QR/barcodes, and history. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Hierarchies:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Categories:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Specifications:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Meters:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Warranties:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Condition:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **QR/barcodes:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **History:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

## 3. Ownership and boundaries

- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.
- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.
- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.
- Never depend on an application's `App\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.
- Keep Filament, Livewire, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.

## 4. Implementation strategy

### Domain model

- Define aggregates, entities, value objects, enums, invariants, lifecycle states, and transition rules using the terminology in this specification.
- Make invalid states unrepresentable where practical and enforce remaining invariants at every mutation boundary.
- Use opaque stable identifiers and explicit actor, tenant, locale, timezone, and currency context where relevant.

### Application layer

- Implement one application action per mutation/use case and purpose-built queries for reads.
- Authorize before accessing or mutating protected data; navigation or UI visibility never substitutes for a policy.
- Execute local invariant changes transactionally, dispatch events after commit, and make retryable commands idempotent.
- Model long-running or cross-module work through queued jobs, outbox/inbox delivery, sagas, compensation, and operator-visible recovery.

### Persistence and integrations

- Store only module-owned data in module-owned tables with documented indexes, constraints, retention, export, deletion, and migration behavior.
- Integrate other capabilities through contracts/events and external systems through independent provider adapters with timeouts, retries, rate limits, reconciliation, and sandbox support.
- Treat imports, webhooks, provider callbacks, files, and generated content as untrusted inputs with provenance and deduplication.

### Presentation

- Provide matching optional presentation packages only when required: `module-maintenance-assets-filament`, `module-maintenance-assets-livewire`, and `module-maintenance-assets-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval f…70722 tokens truncated…tional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-maintenance-procurement` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Suppliers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Purchase orders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Receipts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Returns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost allocation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-procurement-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `suppliers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `purchase-orders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `receipts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `returns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-allocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `module-maintenance-procurement` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Hierarchies** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `hierarchies`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Categories** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `categories`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Specifications** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `specifications`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Meters** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `meters`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Warranties** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `warranties`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Condition** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `condition`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **QR/barcodes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `qr/barcodes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **History** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `history`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/assets.md) | [Source map](../SOURCE-MAPPING.md#assets) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/assets.md) | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/assets.md) | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) · [`module-maintenance-assets-filament`](https://github.com/liberusoftware/module-maintenance-assets-filament) (`liberusoftware/maintenance-assets-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/assets.md) | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/assets.md) | [`project-maintenance-laravel-inertia-react`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-react) · [`module-maintenance-assets-react-inertia`](https://github.com/liberusoftware/module-maintenance-assets-react-inertia) (`@liberusoftware/module-maintenance-assets-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/assets.md) | [`project-maintenance-laravel-inertia-vue`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-vue) · [`module-maintenance-assets-vue-inertia`](https://github.com/liberusoftware/module-maintenance-assets-vue-inertia) (`@liberusoftware/module-maintenance-assets-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/assets.md) | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) · [`module-maintenance-assets-nuxt`](https://github.com/liberusoftware/module-maintenance-assets-nuxt) (`@liberusoftware/module-maintenance-assets-nuxt`) | Standalone Vue SSR client consuming `project-maintenance-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/assets.md) | [`project-maintenance-next-react`](https://github.com/liberusoftware/project-maintenance-next-react) · [`module-maintenance-assets-nextjs`](https://github.com/liberusoftware/module-maintenance-assets-nextjs) (`@liberusoftware/module-maintenance-assets-nextjs`) | App Router Server/Client components consuming `project-maintenance-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/assets.md) | [`project-maintenance-mobile-react`](https://github.com/liberusoftware/project-maintenance-mobile-react) · [`module-maintenance-assets-react-native`](https://github.com/liberusoftware/module-maintenance-assets-react-native) (`@liberusoftware/module-maintenance-assets-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/assets.md) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) · [`module-maintenance-assets-flutter`](https://github.com/liberusoftware/module-maintenance-assets-flutter) (`module_maintenance_assets_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/assets.md) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) · [`module-maintenance-assets-dart-mobile`](https://github.com/liberusoftware/module-maintenance-assets-dart-mobile) (`module_maintenance_assets_dart_mobile`)<br>[`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) · [`module-maintenance-assets-dart-desktop`](https://github.com/liberusoftware/module-maintenance-assets-dart-desktop) (`module_maintenance_assets_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
