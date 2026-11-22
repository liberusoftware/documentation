# Boilerplate: Integrations SSO Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-sso`](../../../modules/source/liberusoftware--integrations-sso.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-sso` (`module-integrations-sso`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** OIDC and SAML 2.0 SSO connections, metadata, ACS/SLO controllers, JIT user provisioning, enforcement middleware, SSRF guards, and Filament resources extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations SSO**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/Actions/Sso/ProvisionSsoUser.php` | `public function __construct(private TeamManagementService $teams)`<br>`public function __invoke(Team $team, string $email, ?string $name): User` |
| `src/Filament/App/Resources/SamlConnectionResource.php` | `public function canCreate(): bool`<br>`public function getCreateAuthorizationResponse(): Response`<br>`public function form(Schema $schema): Schema`<br>`public function table(Table $table): Table`<br>`public function getPages(): array` |
| `src/Filament/App/Resources/SsoConnectionResource.php` | `public function canCreate(): bool`<br>`public function getCreateAuthorizationResponse(): Response`<br>`public function form(Schema $schema): Schema`<br>`public function table(Table $table): Table`<br>`public function getPages(): array` |
| `src/Http/Controllers/SamlLoginController.php` | `public function redirect(Team $team): RedirectResponse`<br>`public function acs(Team $team, Request $request): RedirectResponse`<br>`public function sls(Team $team, Request $request): RedirectResponse` |
| `src/Http/Controllers/SamlMetadataController.php` | `public function __invoke(Team $team): Response` |
| `src/Http/Controllers/SsoLoginController.php` | `public function redirect(Team $team, OidcClient $oidc): RedirectResponse`<br>`public function callback(Team $team, Request $request, OidcClient $oidc): RedirectResponse` |
| `src/Http/Middleware/EnsureSsoWhenRequired.php` | `public function handle(Request $request, Closure $next): Response` |
| `src/IntegrationsSsoServiceProvider.php` | `public function register(): void` |
| `src/Listeners/BuildSamlLogoutRedirect.php` | `public function __construct(private SsoLogoutState $state)`<br>`public function handle(Logout $event): void` |
| `src/Listeners/BuildSsoLogoutRedirect.php` | `public function __construct(private SsoLogoutState $state)`<br>`public function handle(Logout $event): void` |
| `src/Listeners/LogSsoLogout.php` | `public function __construct(protected AuditLogService $auditLogService)`<br>`public function handle(Logout $event): void` |
| `src/Models/SamlConnection.php` | `public function roleForGroups(array $groups): ?Role` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-sso` via Composer and enable `integrations-sso` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
