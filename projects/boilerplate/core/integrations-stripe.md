# Boilerplate: Integrations Stripe Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-stripe`](../../../modules/source/liberusoftware--integrations-stripe.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-stripe` (`module-integrations-stripe`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Stripe billing and subscription integration service extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations Stripe**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/IntegrationsStripeServiceProvider.php` | `public function register(): void` |
| `src/Services/StripeService.php` | `public function __construct()`<br>`public function createSubscription(Team $team, string $paymentMethodId, string $plan = 'monthly'): TeamSubscription`<br>`public function updatePaymentMethod(Team $team, string $paymentMethodId): void`<br>`public function resolvePriceId(string $plan, array $planConfig): string`<br>`public function cancelSubscription(TeamSubscription $subscription): void`<br>`public function updateSubscriptionQuantity(TeamSubscription $subscription, int $quantity): void` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-stripe` via Composer and enable `integrations-stripe` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
