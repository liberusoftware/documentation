# Liberu Filament 5 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Filament 5` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching module's public contracts.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-filament` as a Filament 5 adapter over the matching Laravel 13/PHP 8.5 core package. Put resources, pages, widgets, schemas, tables, filters, actions, policies, navigation, and notifications in the presentation package; keep domain rules, transactions, persistence, authorization decisions, and lifecycle transitions in core actions and policies. Every panel surface must respect tenant/team scope, field sensitivity, audit requirements, and the module's public contracts.

Use typed form state and validation, explicit authorization on records and actions, accessible labels and failure states, localized dates/numbers/currency, safe destructive-action confirmation, pagination, query limits, and queued exports or bulk work. Test resources, schemas, actions, policies, tenancy, validation, loading/error/empty states, accessibility-critical behavior, and the core contract without coupling core code to Filament.

| Project | Specification documents | Standard |
| --- | ---: | --- |
| [Accounting](../../projects/accounting/filament/README.md) | 241 | [FILAMENT](../../standards/FILAMENT.md) |
| [Automation](../../projects/automation/filament/README.md) | 57 | [FILAMENT](../../standards/FILAMENT.md) |
| [Billing](../../projects/billing/filament/README.md) | 81 | [FILAMENT](../../standards/FILAMENT.md) |
| [Boilerplate](../../projects/boilerplate/filament/README.md) | 43 | [FILAMENT](../../standards/FILAMENT.md) |
| [Browser Game](../../projects/browser-game/filament/README.md) | 61 | [FILAMENT](../../standards/FILAMENT.md) |
| [CMS](../../projects/cms/filament/README.md) | 252 | [FILAMENT](../../standards/FILAMENT.md) |
| [Control Panel](../../projects/control-panel/filament/README.md) | 61 | [FILAMENT](../../standards/FILAMENT.md) |
| [CRM](../../projects/crm/filament/README.md) | 218 | [FILAMENT](../../standards/FILAMENT.md) |
| [Ecommerce](../../projects/ecommerce/filament/README.md) | 107 | [FILAMENT](../../standards/FILAMENT.md) |
| [Genealogy](../../projects/genealogy/filament/README.md) | 62 | [FILAMENT](../../standards/FILAMENT.md) |
| [Liberu platform](../../projects/liberu/filament/README.md) | 4 | [FILAMENT](../../standards/FILAMENT.md) |
| [Maintenance](../../projects/maintenance/filament/README.md) | 60 | [FILAMENT](../../standards/FILAMENT.md) |
| [Real Estate](../../projects/real-estate/filament/README.md) | 70 | [FILAMENT](../../standards/FILAMENT.md) |
| [SAP enterprise suite](../../projects/sap/filament/README.md) | 16 | [FILAMENT](../../standards/FILAMENT.md) |
| [Social Network](../../projects/social-network/filament/README.md) | 59 | [FILAMENT](../../standards/FILAMENT.md) |

The package naming rule is `module-{independent-module-name}-filament`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.

## Availability and package identities

Counts above describe Markdown specifications, not released packages or implemented features. The [source inventory](../../architecture/SOURCE-INVENTORY.md) records observed manifests and source locations. Repository slugs, design identifiers, and Composer/npm package identities can differ; install using the actual manifest name. Shared capabilities use the [canonical owner](../../architecture/SHARED-MODULES.md) rather than a separate implementation in each project.
