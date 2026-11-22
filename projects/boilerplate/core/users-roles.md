# Boilerplate: Users and Roles Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/users-roles`](../../../modules/source/liberusoftware--users-roles.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/users-roles` (`module-users-roles`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Shared user authenticatable base model, role lookup service, user policies, migrations, and user factories.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Users and Roles**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/Concerns/HasUserRoles.php` | `public function authorizationIdentifier(): int|string`<br>`public function authorizationType(): string`<br>`public function hasRoleInAnyTeam(string|array $roles): bool`<br>`public function isSuperAdmin(): bool` |
| `src/Database/Factories/UserFactory.php` | `public function modelName(): string`<br>`public function definition(): array`<br>`public function unverified(): static` |
| `src/DatabaseServiceProvider.php` | `public function boot(): void` |
| `src/Policies/UserPolicy.php` | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser): bool`<br>`public function delete(AuthUser $authUser): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser): bool`<br>`public function forceDelete(AuthUser $authUser): bool` |
| `src/Services/UserRoleLookup.php` | `public function hasRoleInAnyTeam(Model $user, string|array $roles): bool` |
| `src/UsersRolesServiceProvider.php` | `public function boot(): void` |

**Migrations:**
- `database/migrations/0001_01_01_000000_create_users_table.php`

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/users-roles` via Composer and enable `users-roles` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
