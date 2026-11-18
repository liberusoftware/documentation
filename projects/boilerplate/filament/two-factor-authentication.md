# Boilerplate: Two-Factor Authentication Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#two-factor-authentication). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-two-factor-authentication-filament`
**Matching core package:** [`module-two-factor-authentication`](../core/two-factor-authentication.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** TOTP enrollment, recovery codes, enforcement, trusted devices, recovery, and audit.

## Adapter implementation plan

This package presents the Two-Factor Authentication core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Two-Factor Authentication core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-two-factor-authentication-filament`](https://github.com/liberusoftware/module-two-factor-authentication-filament) (`liberusoftware/two-factor-authentication-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/two-factor-authentication.md) · [API plan](../api/two-factor-authentication.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **TOTP enrollment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `totp enrollment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recovery codes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recovery codes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Enforcement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `enforcement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trusted devices** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trusted devices`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audit** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audit`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TwoFactorRecovery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/src/Contracts/TwoFactorRecovery.php) | `public function recover(Authenticatable $subject, Authenticatable $administrator, string $reason): void` |
<!-- layer-implementation-plan:end -->
