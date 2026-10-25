# Liberu Livewire 4 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Livewire 4` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching module's public contracts.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-livewire` as a Livewire 4 adapter over the matching core package. Components coordinate validated state, actions, queries, authorization, loading, pagination, events, and errors; they do not contain domain invariants, direct private-table queries, or provider integrations. Use Laravel 13/PHP 8.5 typed properties and methods, Form Requests or dedicated validators, policies, locked/validated component state, and explicit tenant/team context.

Keep browser-facing state minimal and non-sensitive, translate core events into user feedback, make retries and queued work observable, and provide accessible keyboard/focus/error/empty states with localization and timezone/currency formatting. Test component behavior, validation, authorization, tenancy, events, loading, failure, idempotency, and core action contracts; never treat a rendered snapshot as proof of domain correctness.

| Project | Specification documents | Standard |
| --- | ---: | --- |
| [Accounting](../../projects/accounting/livewire/README.md) | 241 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Automation](../../projects/automation/livewire/README.md) | 57 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Billing](../../projects/billing/livewire/README.md) | 81 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Boilerplate](../../projects/boilerplate/livewire/README.md) | 43 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Browser Game](../../projects/browser-game/livewire/README.md) | 61 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [CMS](../../projects/cms/livewire/README.md) | 252 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Control Panel](../../projects/control-panel/livewire/README.md) | 61 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [CRM](../../projects/crm/livewire/README.md) | 218 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Ecommerce](../../projects/ecommerce/livewire/README.md) | 107 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Genealogy](../../projects/genealogy/livewire/README.md) | 62 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Liberu platform](../../projects/liberu/livewire/README.md) | 4 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Maintenance](../../projects/maintenance/livewire/README.md) | 60 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Real Estate](../../projects/real-estate/livewire/README.md) | 70 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [SAP enterprise suite](../../projects/sap/livewire/README.md) | 16 | [LIVEWIRE](../../standards/LIVEWIRE.md) |
| [Social Network](../../projects/social-network/livewire/README.md) | 59 | [LIVEWIRE](../../standards/LIVEWIRE.md) |

The package naming rule is `module-{independent-module-name}-livewire`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.

## Availability and package identities

Counts above describe Markdown specifications, not released packages or implemented features. The [source inventory](../../architecture/SOURCE-INVENTORY.md) records observed manifests and source locations. Repository slugs, design identifiers, and Composer/npm package identities can differ; install using the actual manifest name. Shared capabilities use the [canonical owner](../../architecture/SHARED-MODULES.md) rather than a separate implementation in each project.
