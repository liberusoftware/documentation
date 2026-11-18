# Boilerplate: Passkeys and WebAuthn Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-passkeys-livewire`  
**Matching domain module:** `passkeys`  
**Matching core package:** [`module-passkeys`](../core/passkeys.md) (`liberusoftware/passkeys`)  
**Application:** Boilerplate  
**Source feature:** [Passkeys and WebAuthn](../features/passkeys.md) · [PASSKEYS.md](../../../architecture/PASSKEYS.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [PASSKEYS.md](../../../architecture/PASSKEYS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions (`PasskeyCeremonyServiceContract, PasskeyRegistrarContract, PasskeyAssertionVerifierContract, PasskeyCredentialRepositoryContract, StepUpAuthenticationContract`) and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity.

## 2. Module-specific interactions

- **WebAuthn registration ceremonies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Discoverable credentials and passwordless sign-in:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cryptographic step-up authentication:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attestation and signature-counter clone detection:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Passkey lifecycle, naming, and revocation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Account recovery and security audit evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-passkeys-livewire` component namespace and service provider according to [LIVEWIRE.md](../../../standards/LIVEWIRE.md).
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use `#[Locked]` and typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `webauthn-registration-ceremonies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `discoverable-credentials-and-passwordless-sign-in`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cryptographic-step-up-authentication`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attestation-and-signature-counter-clone-detection`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `passkey-lifecycle-naming-and-revocation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `account-recovery-and-security-audit-evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/passkeys.md) · [API plan](../api/passkeys.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **WebAuthn registration ceremonies** | Expose a focused Livewire 4 component and namespaced Blade default view for `webauthn registration ceremonies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Discoverable credentials and passwordless sign-in** | Expose a focused Livewire 4 component and namespaced Blade default view for `discoverable credentials and passwordless sign-in` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cryptographic step-up authentication** | Expose a focused Livewire 4 component and namespaced Blade default view for `cryptographic step-up authentication` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attestation and signature-counter clone detection** | Expose a focused Livewire 4 component and namespaced Blade default view for `attestation and signature-counter clone detection` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Passkey lifecycle, naming, and revocation** | Expose a focused Livewire 4 component and namespaced Blade default view for `passkey lifecycle, naming, and revocation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Account recovery and security audit evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `account recovery and security audit evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
