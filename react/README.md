# Liberu React 19.2 + Inertia 3 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `React 19.2 + Inertia 3` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own presentation adapters and depend on the matching module's public contracts.

| Application | Implementations | Standard |
|---|---:|---|
| [Accounting](accounting/README.md) | 105 | [../REACT.md](../REACT.md) |
| [Automation](automation/README.md) | 11 | [../REACT.md](../REACT.md) |
| [Billing](billing/README.md) | 16 | [../REACT.md](../REACT.md) |
| [Browser-Game](browser-game/README.md) | 15 | [../REACT.md](../REACT.md) |
| [Cms](cms/README.md) | 81 | [../REACT.md](../REACT.md) |
| [Control-Panel](control-panel/README.md) | 15 | [../REACT.md](../REACT.md) |
| [Crm](crm/README.md) | 95 | [../REACT.md](../REACT.md) |
| [Ecommerce](ecommerce/README.md) | 105 | [../REACT.md](../REACT.md) |
| [Genealogy](genealogy/README.md) | 14 | [../REACT.md](../REACT.md) |
| [Maintenance](maintenance/README.md) | 14 | [../REACT.md](../REACT.md) |
| [Real-Estate](real-estate/README.md) | 15 | [../REACT.md](../REACT.md) |
| [Sap](sap/README.md) | 16 | [../REACT.md](../REACT.md) |
| [Social-Network](social-network/README.md) | 15 | [../REACT.md](../REACT.md) |

The package naming rule is `module-{independent-module-name}-react-inertia`. Applications compose only the packages required by enabled modules, and themes style supported React/Inertia extension points without taking ownership of functional components.
