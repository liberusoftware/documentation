# liberusoftware/module-billing-subscriptions: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral subscription lifecycle for Liberu Billing.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-subscriptions](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-billing-subscriptions`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-subscriptions` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-subscriptions` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Billing\\Subscriptions\\SubscriptionsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/module.json).

**Declared capabilities:** billing.subscriptions

**Declared features:** Activation, Renewal, Trials, Configurable periods, Plan changes, Pause, Cancellation, Expiry, Entitlements

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Subscriptions\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ActivateSubscription.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ActivateSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Subscription` |
| [src/Actions/CancelSubscription.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/CancelSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [src/Actions/ChangeSubscriptionPlan.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ChangeSubscriptionPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, ?int $pricingPlanId): Subscription` |
| [src/Actions/ExpireSubscriptions.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ExpireSubscriptions.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(?int $teamId = null, ?CarbonInterface $asOf = null): int` |
| [src/Actions/PauseSubscription.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/PauseSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [src/Actions/RenewSubscription.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/RenewSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, ?int $periodDays = null): Subscription` |
| [src/Actions/ResumeSubscription.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ResumeSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [src/Actions/UpdateEntitlementState.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/UpdateEntitlementState.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, array $entitlements): Subscription` |
| [src/Policies/SubscriptionPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Policies/SubscriptionPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Subscription $subscription): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Subscription $subscription): bool` |
| [src/Queries/ListSubscriptions.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Queries/ListSubscriptions.php) | `public function execute(?int $teamId, int $perPage = 25, ?int $customerId = null, ?SubscriptionStatus $status = null): LengthAwarePaginator` |
| [src/Support/CustomerReference.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Support/CustomerReference.php) | `public static function assertBelongsToTeam(DatabaseManager $database, mixed $customerId, mixed $teamId): ?int` |

Other non-legacy PHP sources: [src/Enums/SubscriptionStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Enums/SubscriptionStatus.php) · [src/Events/SubscriptionActivated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Events/SubscriptionActivated.php) · [src/Events/SubscriptionCancelled.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Events/SubscriptionCancelled.php) · [src/Events/SubscriptionEntitlementsUpdated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Events/SubscriptionEntitlementsUpdated.php) · [src/Events/SubscriptionExpired.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Events/SubscriptionExpired.php) · [src/Events/SubscriptionPaused.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Events/SubscriptionPaused.php) · [src/Events/SubscriptionPlanChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Events/SubscriptionPlanChanged.php) · [src/Events/SubscriptionRenewed.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Events/SubscriptionRenewed.php) · [src/Events/SubscriptionResumed.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Events/SubscriptionResumed.php) · [src/Models/Subscription.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Models/Subscription.php) · [src/SubscriptionsServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/SubscriptionsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_030000_create_billing_subscriptions_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/database/migrations/2026_08_24_030000_create_billing_subscriptions_table.php)
- [database/migrations/2026_08_25_010000_add_id_protection_to_billing_subscriptions.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/database/migrations/2026_08_25_010000_add_id_protection_to_billing_subscriptions.php)
- [database/migrations/2026_08_29_210000_add_period_days_to_billing_subscriptions.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/database/migrations/2026_08_29_210000_add_period_days_to_billing_subscriptions.php)

[src/Enums/SubscriptionStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Enums/SubscriptionStatus.php): `Trialing = 'trialing'`, `Active = 'active'`, `Paused = 'paused'`, `Cancelled = 'cancelled'`, `Expired = 'expired'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
