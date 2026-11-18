# Boilerplate: Identity Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#identity). Observed identity: [`liberusoftware/identity-core-filament`](../../../modules/source/liberusoftware--identity-core-filament.md). This retained spelling maps to `identity-core`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-identity-filament`
**Matching core package:** [`module-identity`](../core/identity.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Registration, authentication, logout, password recovery, verification, identity linking, and security events.

## Adapter implementation plan

This package presents the Identity core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Identity core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-identity-core-filament`](https://github.com/liberusoftware/module-identity-core-filament) (`liberusoftware/identity-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/identity.md) · [API plan](../api/identity.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Registration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Authentication** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `authentication`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Logout** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `logout`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Password recovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `password recovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Identity linking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `identity linking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Security events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `security events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [IdentityFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/IdentityFilamentPlugin.php) · [IdentityFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/IdentityFilamentServiceProvider.php) · [UserResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/Resources/UserResource.php) · [CreateUser.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/Resources/UserResource/Pages/CreateUser.php) · [EditUser.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/Resources/UserResource/Pages/EditUser.php) · [ListUsers.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/Resources/UserResource/Pages/ListUsers.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [InvitationValidator.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core/src/Contracts/InvitationValidator.php) | `public function valid(string $email, ?string $token): bool` |
| [RegistrationPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core/src/Contracts/RegistrationPolicy.php) | `public function permitsSelfRegistration(): bool`<br>`public function requiresInvitation(): bool` |
<!-- layer-implementation-plan:end -->
