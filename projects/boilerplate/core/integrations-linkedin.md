# Boilerplate: Integrations LinkedIn Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-linkedin`](../../../modules/source/liberusoftware--integrations-linkedin.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-linkedin` (`module-integrations-linkedin`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** LinkedIn organic publishing and LinkedIn Ads integration services extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations LinkedIn**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/IntegrationsLinkedinServiceProvider.php` | `public function register(): void` |
| `src/Services/LinkedInAdsService.php` | `public function __construct(protected AdvertisingAccount $account)`<br>`public function getCampaigns()`<br>`public function createAndSchedulePost($organizationId, array $postData)` |
| `src/Services/LinkedInService.php` | `public function getProfile(ConnectedAccount $account)`<br>`public function sharePost(ConnectedAccount $account, $content)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-linkedin` via Composer and enable `integrations-linkedin` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
