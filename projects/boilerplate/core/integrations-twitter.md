# Boilerplate: Integrations Twitter Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-twitter`](../../../modules/source/liberusoftware--integrations-twitter.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-twitter` (`module-integrations-twitter`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Twitter / X social publishing integration service extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations Twitter**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/IntegrationsTwitterServiceProvider.php` | `public function register(): void` |
| `src/Services/TwitterService.php` | `public function __construct()`<br>`public function getTimeline(ConnectedAccount $account)`<br>`public function postTweet(ConnectedAccount $account, $message)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-twitter` via Composer and enable `integrations-twitter` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
