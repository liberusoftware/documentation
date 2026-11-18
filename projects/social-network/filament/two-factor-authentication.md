# Social Network: Two Factor Authentication Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#two-factor-authentication). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-two-factor-authentication-filament`  
**Matching domain module:** `two-factor-authentication`  
**Application:** Social Network  
**Source feature:** [Two Factor Authentication](../features/two-factor-authentication.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `two-factor-authentication` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **TOTP enrollment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recovery codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Enforcement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trusted devices:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recovery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audit:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-two-factor-authentication-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `totp-enrollment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recovery-codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `enforcement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trusted-devices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recovery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audit`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `two-factor-authentication` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
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
