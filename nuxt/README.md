# Liberu Nuxt 4 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Nuxt 4` implementation package matching exactly one matching API module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching API contracts.

| Application | Implementations | Standard |
|---|---:|---|
| [Accounting](accounting/README.md) | 105 | [../NUXT.md](../NUXT.md) |
| [Automation](automation/README.md) | 11 | [../NUXT.md](../NUXT.md) |
| [Billing](billing/README.md) | 16 | [../NUXT.md](../NUXT.md) |
| [Browser-Game](browser-game/README.md) | 15 | [../NUXT.md](../NUXT.md) |
| [Cms](cms/README.md) | 81 | [../NUXT.md](../NUXT.md) |
| [Control-Panel](control-panel/README.md) | 15 | [../NUXT.md](../NUXT.md) |
| [Crm](crm/README.md) | 95 | [../NUXT.md](../NUXT.md) |
| [Ecommerce](ecommerce/README.md) | 105 | [../NUXT.md](../NUXT.md) |
| [Genealogy](genealogy/README.md) | 14 | [../NUXT.md](../NUXT.md) |
| [Maintenance](maintenance/README.md) | 14 | [../NUXT.md](../NUXT.md) |
| [Real-Estate](real-estate/README.md) | 15 | [../NUXT.md](../NUXT.md) |
| [Sap](sap/README.md) | 16 | [../NUXT.md](../NUXT.md) |
| [Social-Network](social-network/README.md) | 15 | [../NUXT.md](../NUXT.md) |

The package naming rule is `module-{independent-module-name}-nuxt`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.
