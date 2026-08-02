# Liberu Livewire 4 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Livewire 4` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching module's public contracts.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-livewire` as a Livewire 4 adapter over the matching core package. Components coordinate validated state, actions, queries, authorization, loading, pagination, events, and errors; they do not contain domain invariants, direct private-table queries, or provider integrations. Use Laravel 13/PHP 8.5 typed properties and methods, Form Requests or dedicated validators, policies, locked/validated component state, and explicit tenant/team context.

Keep browser-facing state minimal and non-sensitive, translate core events into user feedback, make retries and queued work observable, and provide accessible keyboard/focus/error/empty states with localization and timezone/currency formatting. Test component behavior, validation, authorization, tenancy, events, loading, failure, idempotency, and core action contracts; never treat a rendered snapshot as proof of domain correctness.

| Application                                                        | Implementations | Standard                                                |
| ------------------------------------------------------------------ | --------------: | ------------------------------------------------------- |
| [Accounting](../../projects/accounting/livewire/README.md)         |             105 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Automation](../../projects/automation/livewire/README.md)         |              11 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Billing](../../projects/billing/livewire/README.md)               |              16 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Browser Game](../../projects/browser-game/livewire/README.md)     |              15 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [CMS](../../projects/cms/livewire/README.md)                       |              81 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Control Panel](../../projects/control-panel/livewire/README.md)   |              15 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [CRM](../../projects/crm/livewire/README.md)                       |              95 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Ecommerce](../../projects/ecommerce/livewire/README.md)           |             105 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Genealogy](../../projects/genealogy/livewire/README.md)           |              14 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Maintenance](../../projects/maintenance/livewire/README.md)       |              14 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Real Estate](../../projects/real-estate/livewire/README.md)       |              15 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [SAP](../../projects/sap/livewire/README.md)                       |              16 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |
| [Social Network](../../projects/social-network/livewire/README.md) |              15 | [architecture/LIVEWIRE.md](../../standards/LIVEWIRE.md) |

The package naming rule is `module-{independent-module-name}-livewire`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.
