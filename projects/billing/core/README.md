# Billing Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Billing domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                                | Core package                   | Domain specification                      |
| ------------------------------------- | ------------------------------ | ----------------------------------------- |
| [Billing Core](billing-core.md)       | module-billing-billing-core    | [Feature](../features/billing-core.md)    |
| [Catalog](catalog.md)                 | module-billing-catalog         | [Feature](../features/catalog.md)         |
| [Collections](collections.md)         | module-billing-collections     | [Feature](../features/collections.md)     |
| [Communications](communications.md)   | module-billing-communications  | [Feature](../features/communications.md)  |
| [Customer Portal](customer-portal.md) | module-billing-customer-portal | [Feature](../features/customer-portal.md) |
| [Domains](domains.md)                 | module-billing-domains         | [Feature](../features/domains.md)         |
| [Hosting](hosting.md)                 | module-billing-hosting         | [Feature](../features/hosting.md)         |
| [Invoicing](invoicing.md)             | module-billing-invoicing       | [Feature](../features/invoicing.md)       |
| [Isp](isp.md)                         | module-billing-isp             | [Feature](../features/isp.md)             |
| [Orders](orders.md)                   | module-billing-orders          | [Feature](../features/orders.md)          |
| [Payments](payments.md)               | module-billing-payments        | [Feature](../features/payments.md)        |
| [Pricing](pricing.md)                 | module-billing-pricing         | [Feature](../features/pricing.md)         |
| [Provisioning](provisioning.md)       | module-billing-provisioning    | [Feature](../features/provisioning.md)    |
| [Reporting](reporting.md)             | module-billing-reporting       | [Feature](../features/reporting.md)       |
| [Subscriptions](subscriptions.md)     | module-billing-subscriptions   | [Feature](../features/subscriptions.md)   |
| [Usage](usage.md)                     | module-billing-usage           | [Feature](../features/usage.md)           |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
