# Ecommerce: Catering

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catering). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

Catering owns meals, recipes and yields, staff-managed catering packages, event-specific menu revisions, and event/service requirements. Staff can quote a frozen menu and convert an accepted, availability-confirmed event to an order without copying generic commerce behavior.

The [core specification](../core/catering.md) is authoritative for lifecycle, ownership, dependencies, open decisions and acceptance evidence. The [delivery map](../CATERING.md) links the API, all web surfaces, mobile and desktop. Recipes/preparation/costs are staff-only; customer screens show a deliberately limited projection. No implementation or schema is authorized until the core boundary decisions are resolved.

**Domain module:** `module-ecommerce-catering`

## 1. Purpose

The Catering module owns meals, recipes and yields, staff-managed catering packages, event-specific menu revisions, and event/service requirements, enabling reproducible quotations and idempotent order conversion within Ecommerce.

## 2. Full feature scope

- **Meals and ingredient composition:** implement the complete lifecycle, validation, permissions, privacy projection, and recovery required for staff-managed sellable meals, ingredient references, quantities, and unit validation.
- **Recipes and preparation yields:** implement the complete lifecycle, validation, permissions, privacy projection, and recovery required for staff-only preparation instructions, yield ratios, and cost boundaries excluded from customer projections.
- **Staff-managed catering packages:** implement the complete lifecycle, validation, permissions, privacy projection, and recovery required for curated package templates, component quantities, and dietary disclosures.
- **Event requirements and venue context:** implement the complete lifecycle, validation, permissions, privacy projection, and recovery required for event date, time, IANA timezone, venue, guest counts, and service needs.
- **Immutable menu revisions:** implement the complete lifecycle, validation, permissions, privacy projection, and recovery required for versioned menu selections that freeze commercial and preparation context per revision.
- **Reproducible quotation context:** implement the complete lifecycle, validation, permissions, privacy projection, and recovery required for immutable quote snapshots, currency, expiry, and atomic revision acceptance.
- **Availability confirmation and order conversion:** implement the complete lifecycle, validation, permissions, privacy projection, and recovery required for separate booking availability checks and idempotent accepted-quote-to-order conversion.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Meals and ingredient composition** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `meals and ingredient composition`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Recipes and preparation yields** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `recipes and preparation yields`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Staff-managed catering packages** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `staff-managed catering packages`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Event requirements and venue context** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `event requirements and venue context`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Immutable menu revisions** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `immutable menu revisions`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Reproducible quotation context** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `reproducible quotation context`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Availability confirmation and order conversion** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `availability confirmation and order conversion`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/catering.md) | [Source map](../SOURCE-MAPPING.md#catering) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/catering.md) | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/catering.md) | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) · `module-ecommerce-catering-filament` | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/catering.md) | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/catering.md) | [`project-ecommerce-laravel-inertia-react`](https://github.com/liberusoftware/project-ecommerce-laravel-inertia-react) · `module-ecommerce-catering-react-inertia` | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/catering.md) | [`project-ecommerce-laravel-inertia-vue`](https://github.com/liberusoftware/project-ecommerce-laravel-inertia-vue) · `module-ecommerce-catering-vue-inertia` | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/catering.md) | [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue) · `module-ecommerce-catering-nuxt` | Standalone Vue SSR client consuming `project-ecommerce-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/catering.md) | [`project-ecommerce-next-react`](https://github.com/liberusoftware/project-ecommerce-next-react) · `module-ecommerce-catering-nextjs` | App Router Server/Client components consuming `project-ecommerce-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/catering.md) | [`project-ecommerce-mobile-react`](https://github.com/liberusoftware/project-ecommerce-mobile-react) · `module-ecommerce-catering-react-native` | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/catering.md) | [`project-ecommerce-mobile-flutter`](https://github.com/liberusoftware/project-ecommerce-mobile-flutter) · `module-ecommerce-catering-flutter` | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/catering.md) | [`project-ecommerce-dart-mobile`](https://github.com/liberusoftware/project-ecommerce-dart-mobile) · `module-ecommerce-catering-dart-mobile`<br>[`project-ecommerce-dart-desktop`](https://github.com/liberusoftware/project-ecommerce-dart-desktop) · `module-ecommerce-catering-dart-desktop` | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
