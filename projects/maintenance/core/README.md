# Maintenance Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Maintenance domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                                                  | Core package                                | Domain specification                               |
| ------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------- |
| [Assets](assets.md)                                     | module-maintenance-assets                   | [Feature](../features/assets.md)                   |
| [Commercial](commercial.md)                             | module-maintenance-commercial               | [Feature](../features/commercial.md)               |
| [Compliance](compliance.md)                             | module-maintenance-compliance               | [Feature](../features/compliance.md)               |
| [Customers And Sites](customers-and-sites.md)           | module-maintenance-customers-and-sites      | [Feature](../features/customers-and-sites.md)      |
| [Inspections](inspections.md)                           | module-maintenance-inspections              | [Feature](../features/inspections.md)              |
| [Inventory](inventory.md)                               | module-maintenance-inventory                | [Feature](../features/inventory.md)                |
| [Labor And Time](labor-and-time.md)                     | module-maintenance-labor-and-time           | [Feature](../features/labor-and-time.md)           |
| [Maintenance Core](maintenance-core.md)                 | module-maintenance-maintenance-core         | [Feature](../features/maintenance-core.md)         |
| [Portals](portals.md)                                   | module-maintenance-portals                  | [Feature](../features/portals.md)                  |
| [Preventative Maintenance](preventative-maintenance.md) | module-maintenance-preventative-maintenance | [Feature](../features/preventative-maintenance.md) |
| [Procurement](procurement.md)                           | module-maintenance-procurement              | [Feature](../features/procurement.md)              |
| [Reporting](reporting.md)                               | module-maintenance-reporting                | [Feature](../features/reporting.md)                |
| [Scheduling](scheduling.md)                             | module-maintenance-scheduling               | [Feature](../features/scheduling.md)               |
| [Work Orders](work-orders.md)                           | module-maintenance-work-orders              | [Feature](../features/work-orders.md)              |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
