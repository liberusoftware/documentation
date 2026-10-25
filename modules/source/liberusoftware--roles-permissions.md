# liberusoftware/roles-permissions: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Contextual roles, permissions, policies, and authorization safeguards.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/composer.json) | `39a49babafc0` | [Variant 3](#variant-3) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/roles-permissions/composer.json) | `68e5f07a6704` | [Variant 3](#variant-3) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/roles-permissions/composer.json) | `4743bdfebd1c` | [Variant 3](#variant-3) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/roles-permissions/composer.json) | `3ade34046c3d` | [Variant 3](#variant-3) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/roles-permissions/composer.json) | `790fdffebd3a` | [Variant 3](#variant-3) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/roles-permissions/composer.json) | `1797f25d705f` | [Variant 3](#variant-3) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/composer.json) | `63aad94e94c0` | [Variant 2](#variant-2) | 2 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/roles-permissions/composer.json) | `b12a8c841c6a` | [Variant 3](#variant-3) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/roles-permissions/composer.json) | `577e93db23cc` | [Variant 3](#variant-3) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/roles-permissions/composer.json) | `c267d625e264` | [Variant 3](#variant-3) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/roles-permissions/composer.json) | `08bbc484b50f` | [Variant 3](#variant-3) | 1 |

Physical source locations: **12**. Reference variants: **3**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: real-estate-laravel, `roles-permissions`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/roles-permissions` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `roles-permissions` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\RolesPermissions\\RolesPermissionsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/composer.json) · [module.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/module.json).

**Declared capabilities:** foundation.authorization

**Declared features:** Contextual role assignments, Module-owned permissions, Policies, Cache invalidation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-permission` | `^8.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\RolesPermissions\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/PrivilegedActor.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Contracts/PrivilegedActor.php) | `public function authorizationIdentifier(): int\|string`<br>`public function authorizationType(): string`<br>`public function hasRoleInAnyTeam(string\|array $roles): bool`<br>`public function isSuperAdmin(): bool` |
| [src/Policies/RolePolicy.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Policies/RolePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Role $role): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Role $role): bool`<br>`public function delete(AuthUser $authUser, Role $role): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Role $role): bool`<br>`public function forceDelete(AuthUser $authUser, Role $role): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Role $role): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [src/Services/AnyTeamRoleLookup.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/AnyTeamRoleLookup.php) | `public function hasRoleInAnyTeam(PrivilegedActor $actor, string\|array $roles): bool` |
| [src/Services/BreakGlass.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/BreakGlass.php) | `public function grant(string\|int $actorId, string $permission, string $reason, \DateTimeImmutable $expiresAt, bool $stronglyAuthenticated): int`<br>`public function active(string\|int $actorId, string $permission): bool` |
| [src/Services/SeparationOfDuty.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/SeparationOfDuty.php) | `public function permits(string\|int $requester, string\|int $approver, bool $material = true): bool` |

Other non-legacy PHP sources: [src/Models/Permission.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Models/Permission.php) · [src/Models/Role.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Models/Role.php) · [src/Registry/PermissionRegistry.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Registry/PermissionRegistry.php) · [src/RolesPermissionsServiceProvider.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/RolesPermissionsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_06_29_124225_create_permission_tables.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/database/migrations/2026_06_29_124225_create_permission_tables.php)
- [database/migrations/2026_08_01_062000_create_break_glass_grants_table.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/database/migrations/2026_08_01_062000_create_break_glass_grants_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: crm-laravel, `roles-permissions`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/roles-permissions` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `roles-permissions` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\RolesPermissions\\RolesPermissionsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/module.json).

**Declared capabilities:** foundation.authorization

**Declared features:** Contextual role assignments, Module-owned permissions, Policies, Cache invalidation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-permission` | `^7.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\RolesPermissions\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/PrivilegedActor.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/Contracts/PrivilegedActor.php) | `public function authorizationIdentifier(): int\|string`<br>`public function authorizationType(): string`<br>`public function hasRoleInAnyTeam(string\|array $roles): bool`<br>`public function isSuperAdmin(): bool` |
| [src/Policies/RolePolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/Policies/RolePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Role $role): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Role $role): bool`<br>`public function delete(AuthUser $authUser, Role $role): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Role $role): bool`<br>`public function forceDelete(AuthUser $authUser, Role $role): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Role $role): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [src/Services/AnyTeamRoleLookup.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/Services/AnyTeamRoleLookup.php) | `public function hasRoleInAnyTeam(PrivilegedActor $actor, string\|array $roles): bool` |
| [src/Services/BreakGlass.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/Services/BreakGlass.php) | `public function grant(string\|int $actorId, string $permission, string $reason, \DateTimeImmutable $expiresAt, bool $stronglyAuthenticated): int`<br>`public function active(string\|int $actorId, string $permission): bool` |
| [src/Services/SeparationOfDuty.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/Services/SeparationOfDuty.php) | `public function permits(string\|int $requester, string\|int $approver, bool $material = true): bool` |

Other non-legacy PHP sources: [src/Models/Permission.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/Models/Permission.php) · [src/Models/Role.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/Models/Role.php) · [src/Registry/PermissionRegistry.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/Registry/PermissionRegistry.php) · [src/RolesPermissionsServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/src/RolesPermissionsServiceProvider.php).

**Legacy review:** 3 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2024_02_21_190705_create_permission_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/database/migrations/2024_02_21_190705_create_permission_tables.php)
- [database/migrations/2026_07_06_000003_backfill_role_assignment_teams.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/database/migrations/2026_07_06_000003_backfill_role_assignment_teams.php)
- [database/migrations/2026_07_08_060000_add_role_mappings_to_sso_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/database/migrations/2026_07_08_060000_add_role_mappings_to_sso_connections_table.php)
- [database/migrations/2026_07_10_000100_seed_role_permissions.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/database/migrations/2026_07_10_000100_seed_role_permissions.php)
- [database/migrations/2026_08_01_062000_create_break_glass_grants_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/database/migrations/2026_08_01_062000_create_break_glass_grants_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/tests/.gitkeep)
- [tests/Feature/Permissions/PermissionCatalogTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions/tests/Feature/Permissions/PermissionCatalogTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: accounting-erp-laravel, `roles-permissions`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/roles-permissions` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `roles-permissions` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\RolesPermissions\\RolesPermissionsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/module.json).

**Declared capabilities:** foundation.authorization

**Declared features:** Contextual role assignments, Module-owned permissions, Policies, Cache invalidation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-permission` | `^7.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\RolesPermissions\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/PrivilegedActor.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/Contracts/PrivilegedActor.php) | `public function authorizationIdentifier(): int\|string`<br>`public function authorizationType(): string`<br>`public function hasRoleInAnyTeam(string\|array $roles): bool`<br>`public function isSuperAdmin(): bool` |
| [src/Policies/RolePolicy.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/Policies/RolePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Role $role): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Role $role): bool`<br>`public function delete(AuthUser $authUser, Role $role): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Role $role): bool`<br>`public function forceDelete(AuthUser $authUser, Role $role): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Role $role): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [src/Services/AnyTeamRoleLookup.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/Services/AnyTeamRoleLookup.php) | `public function hasRoleInAnyTeam(PrivilegedActor $actor, string\|array $roles): bool` |
| [src/Services/BreakGlass.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/Services/BreakGlass.php) | `public function grant(string\|int $actorId, string $permission, string $reason, \DateTimeImmutable $expiresAt, bool $stronglyAuthenticated): int`<br>`public function active(string\|int $actorId, string $permission): bool` |
| [src/Services/SeparationOfDuty.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/Services/SeparationOfDuty.php) | `public function permits(string\|int $requester, string\|int $approver, bool $material = true): bool` |

Other non-legacy PHP sources: [src/Models/Permission.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/Models/Permission.php) · [src/Models/Role.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/Models/Role.php) · [src/Registry/PermissionRegistry.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/Registry/PermissionRegistry.php) · [src/RolesPermissionsServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/src/RolesPermissionsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_06_29_124225_create_permission_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/database/migrations/2026_06_29_124225_create_permission_tables.php)
- [database/migrations/2026_08_01_062000_create_break_glass_grants_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/database/migrations/2026_08_01_062000_create_break_glass_grants_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
