# Liberu Vue 3 + Inertia 3 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Vue 3 + Inertia 3` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own Vue pages, components, composables, typed adapters, forms, and Inertia navigation over the matching API contract.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-vue-inertia` as the Vue 3/Inertia 3 adapter over the matching Laravel core and API contracts. Keep business rules, authorization, validation, persistence, and transactions in the server-side core; use typed pages, composables, forms, components, and navigation only to present public resources and invoke documented actions.

Use strict TypeScript contracts, CSRF/authentication, explicit error and validation mapping, tenant-safe requests, accessible keyboard/focus/label behavior, localized dates/numbers/currency, and resilient loading/empty/offline states. Test composables, page props, forms, authorization outcomes, API errors, accessibility-critical flows, and representative user journeys without duplicating core tests.

| Application                                                    | Implementations | Scope index                                              |
| -------------------------------------------------------------- | --------------: | -------------------------------------------------------- |
| [Accounting](../../projects/accounting/vue/README.md)          |             105 | [Vue scope](../../projects/accounting/vue/README.md)     |
| [Automation](../../projects/automation/vue/README.md)          |              11 | [Vue scope](../../projects/automation/vue/README.md)     |
| [Billing](../../projects/billing/vue/README.md)                |              16 | [Vue scope](../../projects/billing/vue/README.md)        |
| [Browser Game](../../projects/browser-game/vue/README.md)      |              15 | [Vue scope](../../projects/browser-game/vue/README.md)   |
| [CMS](../../projects/cms/vue/README.md)                        |              81 | [Vue scope](../../projects/cms/vue/README.md)            |
| [Control Panel](../../projects/control-panel/vue/README.md)    |              15 | [Vue scope](../../projects/control-panel/vue/README.md)  |
| [CRM](../../projects/crm/vue/README.md)                        |              95 | [Vue scope](../../projects/crm/vue/README.md)            |
| [Ecommerce](../../projects/ecommerce/vue/README.md)            |             105 | [Vue scope](../../projects/ecommerce/vue/README.md)      |
| [Genealogy](../../projects/genealogy/vue/README.md)            |              14 | [Vue scope](../../projects/genealogy/vue/README.md)      |
| [Maintenance](../../projects/maintenance/vue/README.md)        |              14 | [Vue scope](../../projects/maintenance/vue/README.md)    |
| [Real Estate](../../projects/real-estate/vue/README.md)        |              15 | [Vue scope](../../projects/real-estate/vue/README.md)    |
| [SAP-style Enterprise Suite](../../projects/sap/vue/README.md) |              16 | [Vue scope](../../projects/sap/vue/README.md)            |
| [Social Network](../../projects/social-network/vue/README.md)  |              15 | [Vue scope](../../projects/social-network/vue/README.md) |

The package naming rule is `module-{independent-module-name}-vue-inertia`. Applications compose only packages required by enabled modules. See [Vue + Inertia architecture](../../standards/VUE.md), [technology map](../../TECHNOLOGIES.md), and [theme architecture](../../standards/THEMES.md).
