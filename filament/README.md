# Liberu Filament 5 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Filament 5` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching module's public contracts.

| Application | Implementations | Standard |
|---|---:|---|
| [Accounting](accounting/README.md) | 105 | [../FILAMENT.md](../FILAMENT.md) |
| [Automation](automation/README.md) | 11 | [../FILAMENT.md](../FILAMENT.md) |
| [Billing](billing/README.md) | 16 | [../FILAMENT.md](../FILAMENT.md) |
| [Browser-Game](browser-game/README.md) | 15 | [../FILAMENT.md](../FILAMENT.md) |
| [Cms](cms/README.md) | 81 | [../FILAMENT.md](../FILAMENT.md) |
| [Control-Panel](control-panel/README.md) | 15 | [../FILAMENT.md](../FILAMENT.md) |
| [Crm](crm/README.md) | 95 | [../FILAMENT.md](../FILAMENT.md) |
| [Ecommerce](ecommerce/README.md) | 105 | [../FILAMENT.md](../FILAMENT.md) |
| [Genealogy](genealogy/README.md) | 14 | [../FILAMENT.md](../FILAMENT.md) |
| [Maintenance](maintenance/README.md) | 14 | [../FILAMENT.md](../FILAMENT.md) |
| [Real-Estate](real-estate/README.md) | 15 | [../FILAMENT.md](../FILAMENT.md) |
| [Sap](sap/README.md) | 16 | [../FILAMENT.md](../FILAMENT.md) |
| [Social-Network](social-network/README.md) | 15 | [../FILAMENT.md](../FILAMENT.md) |

The package naming rule is `module-{independent-module-name}-filament`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.
