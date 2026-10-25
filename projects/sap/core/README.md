# Sap Core Modules

<!-- catalogue-status:start -->
This index preserves **16 module documents/spellings**. Counts are specifications, not released packages or deployed features. Exact source identities and aliases are in the [source map](../SOURCE-MAPPING.md); [shared ownership](../../../architecture/SHARED-MODULES.md) and [Next.js adapter homes](../../../modules/nextjs/OWNERSHIP.md) prevent alternate spellings from becoming competing implementations.
<!-- catalogue-status:end -->

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Sap domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module document | Source/target reference | Related plans |
| --- | --- | --- |
| [core composition design](assets-and-facilities.md) | [Target/source map](../SOURCE-MAPPING.md#assets-and-facilities) | [api](../api/assets-and-facilities.md) · [nextjs](../nextjs/assets-and-facilities.md) |
| [core composition design](controlling.md) | [Target/source map](../SOURCE-MAPPING.md#controlling) | [api](../api/controlling.md) · [nextjs](../nextjs/controlling.md) |
| [core composition design](data-and-intelligence.md) | [Target/source map](../SOURCE-MAPPING.md#data-and-intelligence) | [api](../api/data-and-intelligence.md) · [nextjs](../nextjs/data-and-intelligence.md) |
| [core composition design](enterprise-foundation.md) | [Target/source map](../SOURCE-MAPPING.md#enterprise-foundation) | [api](../api/enterprise-foundation.md) · [nextjs](../nextjs/enterprise-foundation.md) |
| [core composition design](finance.md) | [Target/source map](../SOURCE-MAPPING.md#finance) | [api](../api/finance.md) · [nextjs](../nextjs/finance.md) |
| [core composition design](governance-risk-and-compliance.md) | [Target/source map](../SOURCE-MAPPING.md#governance-risk-and-compliance) | [api](../api/governance-risk-and-compliance.md) · [nextjs](../nextjs/governance-risk-and-compliance.md) |
| [core composition design](hosting-and-cloud.md) | [Target/source map](../SOURCE-MAPPING.md#hosting-and-cloud) | [api](../api/hosting-and-cloud.md) · [nextjs](../nextjs/hosting-and-cloud.md) |
| [core composition design](inventory-and-logistics.md) | [Target/source map](../SOURCE-MAPPING.md#inventory-and-logistics) | [api](../api/inventory-and-logistics.md) · [nextjs](../nextjs/inventory-and-logistics.md) |
| [core composition design](partners-and-portals.md) | [Target/source map](../SOURCE-MAPPING.md#partners-and-portals) | [api](../api/partners-and-portals.md) · [nextjs](../nextjs/partners-and-portals.md) |
| [core composition design](people.md) | [Target/source map](../SOURCE-MAPPING.md#people) | [api](../api/people.md) · [nextjs](../nextjs/people.md) |
| [core composition design](procurement.md) | [Target/source map](../SOURCE-MAPPING.md#procurement) | [api](../api/procurement.md) · [nextjs](../nextjs/procurement.md) |
| [core composition design](product-and-engineering.md) | [Target/source map](../SOURCE-MAPPING.md#product-and-engineering) | [api](../api/product-and-engineering.md) · [nextjs](../nextjs/product-and-engineering.md) |
| [core composition design](projects-and-services.md) | [Target/source map](../SOURCE-MAPPING.md#projects-and-services) | [api](../api/projects-and-services.md) · [nextjs](../nextjs/projects-and-services.md) |
| [core composition design](revenue-operations.md) | [Target/source map](../SOURCE-MAPPING.md#revenue-operations) | [api](../api/revenue-operations.md) · [nextjs](../nextjs/revenue-operations.md) |
| [core composition design](sales-and-crm.md) | [Target/source map](../SOURCE-MAPPING.md#sales-and-crm) | [api](../api/sales-and-crm.md) · [nextjs](../nextjs/sales-and-crm.md) |
| [core composition design](service-management.md) | [Target/source map](../SOURCE-MAPPING.md#service-management) | [api](../api/service-management.md) · [nextjs](../nextjs/service-management.md) |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
