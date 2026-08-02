# Liberu React 19.2 + Inertia 3 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `React 19.2 + Inertia 3` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own presentation adapters and depend on the matching module's public contracts.

| Application | Implementations | Standard |
|---|---:|---|
| [Accounting](../projects/accounting/react/README.md) | 105 | [architecture/REACT.md](../architecture/REACT.md) |
| [Automation](../projects/automation/react/README.md) | 11 | [architecture/REACT.md](../architecture/REACT.md) |
| [Billing](../projects/billing/react/README.md) | 16 | [architecture/REACT.md](../architecture/REACT.md) |
| [Browser-Game](../projects/browser-game/react/README.md) | 15 | [architecture/REACT.md](../architecture/REACT.md) |
| [Cms](../projects/cms/react/README.md) | 81 | [architecture/REACT.md](../architecture/REACT.md) |
| [Control-Panel](../projects/control-panel/react/README.md) | 15 | [architecture/REACT.md](../architecture/REACT.md) |
| [Crm](../projects/crm/react/README.md) | 95 | [architecture/REACT.md](../architecture/REACT.md) |
| [Ecommerce](../projects/ecommerce/react/README.md) | 105 | [architecture/REACT.md](../architecture/REACT.md) |
| [Genealogy](../projects/genealogy/react/README.md) | 14 | [architecture/REACT.md](../architecture/REACT.md) |
| [Maintenance](../projects/maintenance/react/README.md) | 14 | [architecture/REACT.md](../architecture/REACT.md) |
| [Real-Estate](../projects/real-estate/react/README.md) | 15 | [architecture/REACT.md](../architecture/REACT.md) |
| [Sap](../projects/sap/react/README.md) | 16 | [architecture/REACT.md](../architecture/REACT.md) |
| [Social-Network](../projects/social-network/react/README.md) | 15 | [architecture/REACT.md](../architecture/REACT.md) |

The package naming rule is `module-{independent-module-name}-react-inertia`. Applications compose only the packages required by enabled modules, and themes style supported React/Inertia extension points without taking ownership of functional components.
