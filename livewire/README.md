# Liberu Livewire 4 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Livewire 4` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching module's public contracts.

| Application | Implementations | Standard |
|---|---:|---|
| [Accounting](accounting/README.md) | 105 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Automation](automation/README.md) | 11 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Billing](billing/README.md) | 16 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Browser-Game](browser-game/README.md) | 15 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Cms](cms/README.md) | 81 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Control-Panel](control-panel/README.md) | 15 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Crm](crm/README.md) | 95 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Ecommerce](ecommerce/README.md) | 105 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Genealogy](genealogy/README.md) | 14 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Maintenance](maintenance/README.md) | 14 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Real-Estate](real-estate/README.md) | 15 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Sap](sap/README.md) | 16 | [../LIVEWIRE.md](../LIVEWIRE.md) |
| [Social-Network](social-network/README.md) | 15 | [../LIVEWIRE.md](../LIVEWIRE.md) |

The package naming rule is `module-{independent-module-name}-livewire`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.
