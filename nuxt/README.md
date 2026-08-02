# Liberu Nuxt 4 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Nuxt 4` implementation package matching exactly one matching API module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching API contracts.

| Application | Implementations | Standard |
|---|---:|---|
| [Accounting](../projects/accounting/nuxt/README.md) | 105 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Automation](../projects/automation/nuxt/README.md) | 11 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Billing](../projects/billing/nuxt/README.md) | 16 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Browser-Game](../projects/browser-game/nuxt/README.md) | 15 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Cms](../projects/cms/nuxt/README.md) | 81 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Control-Panel](../projects/control-panel/nuxt/README.md) | 15 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Crm](../projects/crm/nuxt/README.md) | 95 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Ecommerce](../projects/ecommerce/nuxt/README.md) | 105 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Genealogy](../projects/genealogy/nuxt/README.md) | 14 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Maintenance](../projects/maintenance/nuxt/README.md) | 14 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Real-Estate](../projects/real-estate/nuxt/README.md) | 15 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Sap](../projects/sap/nuxt/README.md) | 16 | [architecture/NUXT.md](../architecture/NUXT.md) |
| [Social-Network](../projects/social-network/nuxt/README.md) | 15 | [architecture/NUXT.md](../architecture/NUXT.md) |

The package naming rule is `module-{independent-module-name}-nuxt`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.
