# Boilerplate: Tenancy Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/tenancy`](../../../modules/source/liberusoftware--tenancy.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/tenancy` (`module-tenancy`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Shared Filament and Jetstream team tenancy with scoped runtime context, Eloquent isolation, queue context propagation, and Spatie permission team synchronization.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Tenancy**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
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

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/tenancy` via Composer and enable `tenancy` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
