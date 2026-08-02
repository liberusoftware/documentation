# Liberu Filament 5 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Filament 5` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching module's public contracts.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-filament` as a Filament 5 adapter over the matching Laravel 13/PHP 8.5 core package. Put resources, pages, widgets, schemas, tables, filters, actions, policies, navigation, and notifications in the presentation package; keep domain rules, transactions, persistence, authorization decisions, and lifecycle transitions in core actions and policies. Every panel surface must respect tenant/team scope, field sensitivity, audit requirements, and the module's public contracts.

Use typed form state and validation, explicit authorization on records and actions, accessible labels and failure states, localized dates/numbers/currency, safe destructive-action confirmation, pagination, query limits, and queued exports or bulk work. Test resources, schemas, actions, policies, tenancy, validation, loading/error/empty states, accessibility-critical behavior, and the core contract without coupling core code to Filament.

| Application                                                        | Implementations | Standard                                                |
| ------------------------------------------------------------------ | --------------: | ------------------------------------------------------- |
| [Accounting](../../projects/accounting/filament/README.md)         |             105 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Automation](../../projects/automation/filament/README.md)         |              11 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Billing](../../projects/billing/filament/README.md)               |              16 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Browser Game](../../projects/browser-game/filament/README.md)     |              15 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [CMS](../../projects/cms/filament/README.md)                       |              81 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Control Panel](../../projects/control-panel/filament/README.md)   |              15 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [CRM](../../projects/crm/filament/README.md)                       |              95 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Ecommerce](../../projects/ecommerce/filament/README.md)           |             105 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Genealogy](../../projects/genealogy/filament/README.md)           |              14 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Maintenance](../../projects/maintenance/filament/README.md)       |              14 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Real Estate](../../projects/real-estate/filament/README.md)       |              15 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [SAP](../../projects/sap/filament/README.md)                       |              16 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |
| [Social Network](../../projects/social-network/filament/README.md) |              15 | [architecture/FILAMENT.md](../../standards/FILAMENT.md) |

The package naming rule is `module-{independent-module-name}-filament`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.
