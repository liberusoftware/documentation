# Boilerplate: Roles and Permissions Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#roles-and-permissions). Observed identity: [`liberusoftware/roles-permissions-filament`](../../../modules/source/liberusoftware--roles-permissions-filament.md). This retained spelling maps to `roles-permissions`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-roles-and-permissions-filament`
**Matching core package:** [`module-roles-and-permissions`](../core/roles-and-permissions.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Permission definitions, assignments, contextual scope, policies, caches, safeguards, and audit.

## Adapter implementation plan

This package presents the Roles and Permissions core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Roles and Permissions core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-roles-permissions-filament`](https://github.com/liberusoftware/module-roles-permissions-filament) (`liberusoftware/roles-permissions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/roles-and-permissions.md) · [API plan](../api/roles-and-permissions.md) | Domain actions, queries, policies, and persistence |

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
