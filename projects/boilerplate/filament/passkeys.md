# Boilerplate: Passkeys and WebAuthn Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#passkeys). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-passkeys-filament`  
**Matching domain module:** `passkeys`  
**Matching core package:** [`module-passkeys`](../core/passkeys.md) (`liberusoftware/passkeys`)  
**Application:** Boilerplate  
**Source feature:** [Passkeys and WebAuthn](../features/passkeys.md) · [PASSKEYS.md](../../../architecture/PASSKEYS.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [PASSKEYS.md](../../../architecture/PASSKEYS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `passkeys` public contract boundary (`PasskeyCeremonyServiceContract, PasskeyRegistrarContract, PasskeyAssertionVerifierContract, PasskeyCredentialRepositoryContract, StepUpAuthenticationContract`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **WebAuthn registration ceremonies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Discoverable credentials and passwordless sign-in:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cryptographic step-up authentication:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attestation and signature-counter clone detection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Passkey lifecycle, naming, and revocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account recovery and security audit evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-passkeys-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `webauthn-registration-ceremonies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `discoverable-credentials-and-passwordless-sign-in`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cryptographic-step-up-authentication`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attestation-and-signature-counter-clone-detection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `passkey-lifecycle-naming-and-revocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-recovery-and-security-audit-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-passkeys-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/passkeys.md) · [API plan](../api/passkeys.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **WebAuthn registration ceremonies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `webauthn registration ceremonies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Discoverable credentials and passwordless sign-in** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `discoverable credentials and passwordless sign-in`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cryptographic step-up authentication** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cryptographic step-up authentication`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attestation and signature-counter clone detection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attestation and signature-counter clone detection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Passkey lifecycle, naming, and revocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `passkey lifecycle, naming, and revocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Account recovery and security audit evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account recovery and security audit evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
