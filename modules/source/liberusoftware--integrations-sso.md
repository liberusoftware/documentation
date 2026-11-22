# liberusoftware/integrations-sso: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

OIDC and SAML SSO connections, controllers, middleware, and JIT provisioning.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-sso` |
| Version | `1.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-sso` |
| Providers | `[]` |
| Capabilities | `integrations.sso` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `liberusoftware/roles-permissions` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\Sso\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
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
| `src/Models/SsoConnection.php` | `public function roleForGroups(array $groups): ?Role` |
| `src/Services/Sso/OidcClient.php` | `public function discover(SsoConnection $connection): array`<br>`public function authorizeUrl(SsoConnection $connection, string $redirectUri, string $state, string $nonce, string $codeChallenge): string`<br>`public function exchangeCode(SsoConnection $connection, string $code, string $redirectUri, string $codeVerifier): array`<br>`public function jwks(SsoConnection $connection): array`<br>`public function validateIdToken(SsoConnection $connection, string $idToken, string $expectedNonce): array`<br>`public function userinfo(SsoConnection $connection, string $accessToken): array` |
| `src/Services/Sso/SamlPayloadGuard.php` | `public function allows(mixed $encoded, bool $deflated = false): bool` |
| `src/Services/Sso/SamlSettings.php` | `public function for(Team $team, SamlConnection $connection): array` |
| `src/Support/SsoEnforcement.php` | `public function enforcingTeamFor(User $user): ?Team`<br>`public function loginRouteFor(Team $team): string` |
| `src/Support/SsoLogoutState.php` | `public function set(string $url): void`<br>`public function url(): ?string` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **18**.

- `tests/Feature/Saml/SamlAcsTest.php`
- `tests/Feature/Saml/SamlJitTest.php`
- `tests/Feature/Saml/SamlLoginRedirectTest.php`
- `tests/Feature/Saml/SamlSloTest.php`
- `tests/Feature/Saml/SignsSamlResponses.php`
- `tests/Feature/Sso/OidcSingleLogoutTest.php`
- `tests/Feature/Sso/SamlConfigTest.php`
- `tests/Feature/Sso/SamlValidateConnectionTest.php`
- `tests/Feature/Sso/SsoClientAuthTest.php`
- `tests/Feature/Sso/SsoEnforcementTest.php`
- `tests/Feature/Sso/SsoGroupMappingTest.php`
- `tests/Feature/Sso/SsoIdTokenTest.php`
- `tests/Feature/Sso/SsoJitProvisioningTest.php`
- `tests/Feature/Sso/SsoLoginTest.php`
- `tests/Feature/Sso/SsoLogoutAuditTest.php`
- `tests/Feature/Sso/SsoPkceTest.php`
- `tests/Feature/Sso/SsoTestConnectionTest.php`
- `tests/Unit/ServiceProviderTest.php`
