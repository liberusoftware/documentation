# Boilerplate: Roles Permissions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#roles-permissions). Observed identity: [`liberusoftware/roles-permissions-filament`](../../../modules/source/liberusoftware--roles-permissions-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-boilerplate-roles-permissions-filament`  
**Matching domain module:** `roles-permissions`  
**Application:** Boilerplate  
**Source feature:** [Roles Permissions](../features/roles-permissions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `roles-permissions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Permission definitions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assignments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contextual scope:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Policies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Caches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Safeguards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audit:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-boilerplate-roles-permissions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `permission-definitions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assignments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contextual-scope`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `policies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `caches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `safeguards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audit`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `roles-permissions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-roles-permissions-filament`](https://github.com/liberusoftware/module-roles-permissions-filament) (`liberusoftware/roles-permissions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/roles-permissions.md) · [API plan](../api/roles-permissions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Permission definitions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permission definitions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assignments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assignments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contextual scope** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contextual scope`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Policies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `policies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Caches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `caches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Safeguards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `safeguards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audit** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audit`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [RolesPermissionsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions-filament/src/RolesPermissionsFilamentPlugin.php) · [RolesPermissionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions-filament/src/RolesPermissionsFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PrivilegedActor.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Contracts/PrivilegedActor.php) | `public function authorizationIdentifier(): int\|string`<br>`public function authorizationType(): string`<br>`public function hasRoleInAnyTeam(string\|array $roles): bool`<br>`public function isSuperAdmin(): bool` |
| [RolePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Policies/RolePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Role $role): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Role $role): bool`<br>`public function delete(AuthUser $authUser, Role $role): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Role $role): bool`<br>`public function forceDelete(AuthUser $authUser, Role $role): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Role $role): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [AnyTeamRoleLookup.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/AnyTeamRoleLookup.php) | `public function hasRoleInAnyTeam(PrivilegedActor $actor, string\|array $roles): bool` |
| [BreakGlass.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/BreakGlass.php) | `public function grant(string\|int $actorId, string $permission, string $reason, \DateTimeImmutable $expiresAt, bool $stronglyAuthenticated): int`<br>`public function active(string\|int $actorId, string $permission): bool` |
| [SeparationOfDuty.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/SeparationOfDuty.php) | `public function permits(string\|int $requester, string\|int $approver, bool $material = true): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Permission.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/roles-permissions/src/Models/Permission.php) | No literal fillable array detected; inspect the model and API schema. |
| [Role.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/roles-permissions/src/Models/Role.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
