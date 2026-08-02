# Sap Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Sap domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                                                              | Core package                              | Domain specification                                     |
| ------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------- |
| [Assets And Facilities](assets-and-facilities.md)                   | module-sap-assets-and-facilities          | [Feature](../features/assets-and-facilities.md)          |
| [Controlling](controlling.md)                                       | module-sap-controlling                    | [Feature](../features/controlling.md)                    |
| [Data And Intelligence](data-and-intelligence.md)                   | module-sap-data-and-intelligence          | [Feature](../features/data-and-intelligence.md)          |
| [Enterprise Foundation](enterprise-foundation.md)                   | module-sap-enterprise-foundation          | [Feature](../features/enterprise-foundation.md)          |
| [Finance](finance.md)                                               | module-sap-finance                        | [Feature](../features/finance.md)                        |
| [Governance Risk And Compliance](governance-risk-and-compliance.md) | module-sap-governance-risk-and-compliance | [Feature](../features/governance-risk-and-compliance.md) |
| [Hosting And Cloud](hosting-and-cloud.md)                           | module-sap-hosting-and-cloud              | [Feature](../features/hosting-and-cloud.md)              |
| [Inventory And Logistics](inventory-and-logistics.md)               | module-sap-inventory-and-logistics        | [Feature](../features/inventory-and-logistics.md)        |
| [Partners And Portals](partners-and-portals.md)                     | module-sap-partners-and-portals           | [Feature](../features/partners-and-portals.md)           |
| [People](people.md)                                                 | module-sap-people                         | [Feature](../features/people.md)                         |
| [Procurement](procurement.md)                                       | module-sap-procurement                    | [Feature](../features/procurement.md)                    |
| [Product And Engineering](product-and-engineering.md)               | module-sap-product-and-engineering        | [Feature](../features/product-and-engineering.md)        |
| [Projects And Services](projects-and-services.md)                   | module-sap-projects-and-services          | [Feature](../features/projects-and-services.md)          |
| [Revenue Operations](revenue-operations.md)                         | module-sap-revenue-operations             | [Feature](../features/revenue-operations.md)             |
| [Sales And Crm](sales-and-crm.md)                                   | module-sap-sales-and-crm                  | [Feature](../features/sales-and-crm.md)                  |
| [Service Management](service-management.md)                         | module-sap-service-management             | [Feature](../features/service-management.md)             |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
