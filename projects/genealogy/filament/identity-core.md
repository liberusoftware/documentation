# Genealogy: Identity Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#identity-core). Observed identity: [`liberusoftware/identity-core-filament`](../../../modules/source/liberusoftware--identity-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-identity-core-filament`  
**Matching domain module:** `identity-core`  
**Application:** Genealogy  
**Source feature:** [Identity Core](../features/identity-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `identity-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Registration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Authentication:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Logout:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Password recovery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identity linking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Security events:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-identity-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `registration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `authentication`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `logout`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `password-recovery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identity-linking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `security-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `identity-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-identity-core-filament`](https://github.com/liberusoftware/module-identity-core-filament) (`liberusoftware/identity-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/identity-core.md) · [API plan](../api/identity-core.md) | Domain actions, queries, policies, and persistence |

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
