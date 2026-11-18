# Boilerplate: Passkeys and WebAuthn Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-passkeys-nuxt`
**Matching domain module:** `passkeys`
**Matching core package:** [`module-passkeys`](../core/passkeys.md) (`liberusoftware/passkeys`)
**Application:** Boilerplate
**Source feature:** [Passkeys and WebAuthn](../features/passkeys.md) · [PASSKEYS.md](../../../architecture/PASSKEYS.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [PASSKEYS.md](../../../architecture/PASSKEYS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/passkeys.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`PasskeyCeremonyServiceContract, PasskeyRegistrarContract, PasskeyAssertionVerifierContract, PasskeyCredentialRepositoryContract, StepUpAuthenticationContract`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `passkeys` public API boundary.

## 2. Module-specific surfaces

- **WebAuthn registration ceremonies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Discoverable credentials and passwordless sign-in:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cryptographic step-up authentication:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attestation and signature-counter clone detection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Passkey lifecycle, naming, and revocation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Account recovery and security audit evidence:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-passkeys-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `webauthn-registration-ceremonies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `discoverable-credentials-and-passwordless-sign-in`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cryptographic-step-up-authentication`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attestation-and-signature-counter-clone-detection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `passkey-lifecycle-naming-and-revocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `account-recovery-and-security-audit-evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/passkeys.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-passkeys-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **WebAuthn registration ceremonies** | Expose composable and Vue 3 component for `webauthn registration ceremonies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/passkeys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Discoverable credentials and passwordless sign-in** | Expose composable and Vue 3 component for `discoverable credentials and passwordless sign-in` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/passkeys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Cryptographic step-up authentication** | Expose composable and Vue 3 component for `cryptographic step-up authentication` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/passkeys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Attestation and signature-counter clone detection** | Expose composable and Vue 3 component for `attestation and signature-counter clone detection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/passkeys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Passkey lifecycle, naming, and revocation** | Expose composable and Vue 3 component for `passkey lifecycle, naming, and revocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/passkeys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Account recovery and security audit evidence** | Expose composable and Vue 3 component for `account recovery and security audit evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/passkeys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
