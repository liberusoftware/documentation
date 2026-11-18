# Browser Game: Social Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social). Observed identity: [`liberusoftware/module-browser-game-social-livewire`](../../../modules/source/liberusoftware--module-browser-game-social-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-social-livewire`  
**Matching domain module:** `browser-game-social`  
**Application:** Browser Game  
**Source feature:** [Social](../features/social.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Friends:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Parties:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Chat:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mail:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Guilds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Alliances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Permissions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Activity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reporting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-social-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-browser-game-social::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `friends`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `parties`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `chat`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mail`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `guilds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `alliances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `permissions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `activity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reporting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-social` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/social.md) · [API plan](../api/social.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Friends** | Expose a focused Livewire 4 component and namespaced Blade default view for `friends` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Parties** | Expose a focused Livewire 4 component and namespaced Blade default view for `parties` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Chat** | Expose a focused Livewire 4 component and namespaced Blade default view for `chat` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mail** | Expose a focused Livewire 4 component and namespaced Blade default view for `mail` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Guilds** | Expose a focused Livewire 4 component and namespaced Blade default view for `guilds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Alliances** | Expose a focused Livewire 4 component and namespaced Blade default view for `alliances` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Permissions** | Expose a focused Livewire 4 component and namespaced Blade default view for `permissions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Activity** | Expose a focused Livewire 4 component and namespaced Blade default view for `activity` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reporting** | Expose a focused Livewire 4 component and namespaced Blade default view for `reporting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SocialCatalog.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-livewire/src/Livewire/SocialCatalog.php) · [SocialLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-livewire/src/SocialLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SocialQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Queries/SocialQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SocialActivity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialActivity.php) | No literal fillable array detected; inspect the model and API schema. |
| [SocialMembership.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialMembership.php) | No literal fillable array detected; inspect the model and API schema. |
| [SocialRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
