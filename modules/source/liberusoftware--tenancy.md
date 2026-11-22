# liberusoftware/tenancy: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Shared Filament and Jetstream team tenancy with scoped runtime context and Eloquent isolation.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/tenancy` |
| Version | `1.2.3` |
| Package type | `liberu-module` |
| Module manifest name | `tenancy` |
| Providers | `["Liberu\\Foundation\\Tenancy\\TenancyServiceProvider"]` |
| Capabilities | `foundation.tenancy` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `laravel/jetstream` | `^5.5` |
| `php` | `^8.5` |
| `spatie/laravel-permission` | `^8.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Tenancy\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/Concerns/BelongsToTeam.php` | `public function team(): BelongsTo` |
| `src/Concerns/IsTenantModel.php` | `public function scopeByTeam(Builder $query, ?int $teamId): void`<br>`public function belongsToTeam(?int $teamId): bool` |
| `src/Http/Middleware/SetPermissionsTeamContext.php` | `public function handle(Request $request, Closure $next): Response`<br>`public function terminate(Request $request, Response $response): void` |
| `src/Http/Middleware/SetTenantContext.php` | `public function handle(Request $request, Closure $next): Response`<br>`public function terminate(Request $request, Response $response): void` |
| `src/Jobs/Concerns/TenantAware.php` | `public function middleware(): array` |
| `src/Jobs/Middleware/RestoreTenantContext.php` | `public function handle(object $job, callable $next): mixed` |
| `src/Listeners/SwitchTeam.php` | `public function handle(object $event): void` |
| `src/TenancyServiceProvider.php` | `public function register(): void` |
| `src/TenantContext.php` | `public function set(?int $teamId): void`<br>`public function clear(): void`<br>`public function forUser(?Authenticatable $user): ?int`<br>`public function currentId(): ?int` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **2**.

- `tests/RuntimeContractsTest.php`
- `tests/TenantContextTest.php`
