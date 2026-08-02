# Liberu Livewire 4 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Livewire 4` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching module's public contracts.

| Application | Implementations | Standard |
|---|---:|---|
| [Accounting](../projects/accounting/livewire/README.md) | 105 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Automation](../projects/automation/livewire/README.md) | 11 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Billing](../projects/billing/livewire/README.md) | 16 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Browser-Game](../projects/browser-game/livewire/README.md) | 15 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Cms](../projects/cms/livewire/README.md) | 81 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Control-Panel](../projects/control-panel/livewire/README.md) | 15 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Crm](../projects/crm/livewire/README.md) | 95 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Ecommerce](../projects/ecommerce/livewire/README.md) | 105 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Genealogy](../projects/genealogy/livewire/README.md) | 14 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Maintenance](../projects/maintenance/livewire/README.md) | 14 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Real-Estate](../projects/real-estate/livewire/README.md) | 15 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Sap](../projects/sap/livewire/README.md) | 16 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |
| [Social-Network](../projects/social-network/livewire/README.md) | 15 | [architecture/LIVEWIRE.md](../architecture/LIVEWIRE.md) |

The package naming rule is `module-{independent-module-name}-livewire`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.
