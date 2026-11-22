# liberusoftware/users-roles: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Shared users, role lookup, user policies, and user factories.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/users-roles` |
| Version | `1.0.3` |
| Package type | `liberu-module` |
| Module manifest name | `users-roles` |
| Providers | `["Liberu\\Foundation\\UsersRoles\\UsersRolesServiceProvider"]` |
| Capabilities | `foundation.users-roles` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/auth` | `^13.0` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |
| `spatie/laravel-permission` | `^8.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\UsersRoles\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/Concerns/HasUserRoles.php` | `public function authorizationIdentifier(): int|string`<br>`public function authorizationType(): string`<br>`public function hasRoleInAnyTeam(string|array $roles): bool`<br>`public function isSuperAdmin(): bool` |
| `src/Database/Factories/UserFactory.php` | `public function modelName(): string`<br>`public function definition(): array`<br>`public function unverified(): static` |
| `src/DatabaseServiceProvider.php` | `public function boot(): void` |
| `src/Policies/UserPolicy.php` | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser): bool`<br>`public function delete(AuthUser $authUser): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser): bool`<br>`public function forceDelete(AuthUser $authUser): bool` |
| `src/Services/UserRoleLookup.php` | `public function hasRoleInAnyTeam(Model $user, string|array $roles): bool` |
| `src/UsersRolesServiceProvider.php` | `public function boot(): void` |

## Persistence and lifecycle

- `database/migrations/0001_01_01_000000_create_users_table.php`

## Verification

Tracked files under `tests/`: **1**.

- `tests/UserRoleLookupTest.php`
