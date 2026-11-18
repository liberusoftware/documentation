# Real Estate: Identity Core Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#identity-core). Observed identity: [`liberusoftware/identity-core-livewire`](../../../modules/source/liberusoftware--identity-core-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-real-estate-identity-core-livewire`  
**Matching domain module:** `identity-core`  
**Application:** Real Estate  
**Source feature:** [Identity Core](../features/identity-core.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Registration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Authentication:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Logout:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Password recovery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Verification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Identity linking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Security events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-real-estate-identity-core-livewire` component namespace and service provider; use explicit aliases such as `<livewire:realestateIdentityCore::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `registration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `authentication`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `logout`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `password-recovery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `verification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `identity-linking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `security-events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `identity-core` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/identity-core.md) · [API plan](../api/identity-core.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Registration** | Expose a focused Livewire 4 component and namespaced Blade default view for `registration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Authentication** | Expose a focused Livewire 4 component and namespaced Blade default view for `authentication` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Logout** | Expose a focused Livewire 4 component and namespaced Blade default view for `logout` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Password recovery** | Expose a focused Livewire 4 component and namespaced Blade default view for `password recovery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Verification** | Expose a focused Livewire 4 component and namespaced Blade default view for `verification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Identity linking** | Expose a focused Livewire 4 component and namespaced Blade default view for `identity linking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Security events** | Expose a focused Livewire 4 component and namespaced Blade default view for `security events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Overview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-core-livewire/src/Livewire/Overview.php) · [IdentityCoreLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-core-livewire/src/IdentityCoreLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [InvitationValidator.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core/src/Contracts/InvitationValidator.php) | `public function valid(string $email, ?string $token): bool` |
| [RegistrationPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core/src/Contracts/RegistrationPolicy.php) | `public function permitsSelfRegistration(): bool`<br>`public function requiresInvitation(): bool` |
<!-- layer-implementation-plan:end -->
