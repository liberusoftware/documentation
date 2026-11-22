# liberusoftware/integrations-stripe: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Stripe billing and subscription integration service.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-stripe` |
| Version | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-stripe` |
| Providers | `[]` |
| Capabilities | `integrations.stripe` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\Stripe\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/IntegrationsStripeServiceProvider.php` | `public function register(): void` |
| `src/Services/StripeService.php` | `public function __construct()`<br>`public function createSubscription(Team $team, string $paymentMethodId, string $plan = 'monthly'): TeamSubscription`<br>`public function updatePaymentMethod(Team $team, string $paymentMethodId): void`<br>`public function resolvePriceId(string $plan, array $planConfig): string`<br>`public function cancelSubscription(TeamSubscription $subscription): void`<br>`public function updateSubscriptionQuantity(TeamSubscription $subscription, int $quantity): void` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
