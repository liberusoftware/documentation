# Liberu Nuxt 4 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Nuxt 4` implementation package matching exactly one matching API module. Feature specifications remain framework-neutral; these packages own only presentation adapters and depend on the matching API contracts.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-nuxt` as a Nuxt 4 SSR/API-consuming adapter over the matching API contract. Keep server-only credentials and privileged operations behind Nuxt server routes or the Laravel API; never expose secrets, private models, or unfiltered tenant data to the browser. Use typed API clients, runtime validation for external responses, route middleware, explicit pending/error states, and cache invalidation aligned with core events and API versioning.

Design for public, authenticated, and tenant-scoped users separately; apply authorization at the API boundary even when a Nuxt route is hidden. Provide accessible responsive views, localization, timezone/currency formatting, safe media handling, SEO metadata only for approved public data, and clear recovery for queued or unavailable operations. Test SSR/client boundaries, authentication, authorization, API schemas, hydration, caching, errors, accessibility, security headers, and production build behavior.

| Application                                                    | Implementations | Standard                                        |
| -------------------------------------------------------------- | --------------: | ----------------------------------------------- |
| [Accounting](../../projects/accounting/nuxt/README.md)         |             105 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Automation](../../projects/automation/nuxt/README.md)         |              11 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Billing](../../projects/billing/nuxt/README.md)               |              16 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Browser Game](../../projects/browser-game/nuxt/README.md)     |              15 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [CMS](../../projects/cms/nuxt/README.md)                       |              81 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Control Panel](../../projects/control-panel/nuxt/README.md)   |              15 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [CRM](../../projects/crm/nuxt/README.md)                       |              95 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Ecommerce](../../projects/ecommerce/nuxt/README.md)           |             105 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Genealogy](../../projects/genealogy/nuxt/README.md)           |              14 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Maintenance](../../projects/maintenance/nuxt/README.md)       |              14 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Real Estate](../../projects/real-estate/nuxt/README.md)       |              15 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [SAP](../../projects/sap/nuxt/README.md)                       |              16 | [architecture/NUXT.md](../../standards/NUXT.md) |
| [Social Network](../../projects/social-network/nuxt/README.md) |              15 | [architecture/NUXT.md](../../standards/NUXT.md) |

The package naming rule is `module-{independent-module-name}-nuxt`. Applications compose only the packages required by enabled modules, and themes style supported extension points without taking ownership of functional components.
