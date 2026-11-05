# Liberu Vue 3 + Inertia 3 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `Vue 3 + Inertia 3` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own Vue pages, components, composables, typed adapters, forms, and Inertia navigation over the matching API contract.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-vue-inertia` as the Vue 3/Inertia 3 adapter over the matching Laravel core and API contracts. Keep business rules, authorization, validation, persistence, and transactions in the server-side core; use typed pages, composables, forms, components, and navigation only to present public resources and invoke documented actions.

Use strict TypeScript contracts, CSRF/authentication, explicit error and validation mapping, tenant-safe requests, accessible keyboard/focus/label behavior, localized dates/numbers/currency, and resilient loading/empty/offline states. Test composables, page props, forms, authorization outcomes, API errors, accessibility-critical flows, and representative user journeys without duplicating core tests.

| Project | Specification documents | Standard |
| --- | ---: | --- |
| [Accounting](../../projects/accounting/vue/README.md) | 241 | [VUE](../../standards/VUE.md) |
| [Automation](../../projects/automation/vue/README.md) | 57 | [VUE](../../standards/VUE.md) |
| [Billing](../../projects/billing/vue/README.md) | 81 | [VUE](../../standards/VUE.md) |
| [Boilerplate](../../projects/boilerplate/vue/README.md) | 43 | [VUE](../../standards/VUE.md) |
| [Browser Game](../../projects/browser-game/vue/README.md) | 61 | [VUE](../../standards/VUE.md) |
| [CMS](../../projects/cms/vue/README.md) | 252 | [VUE](../../standards/VUE.md) |
| [Control Panel](../../projects/control-panel/vue/README.md) | 61 | [VUE](../../standards/VUE.md) |
| [CRM](../../projects/crm/vue/README.md) | 218 | [VUE](../../standards/VUE.md) |
| [Ecommerce](../../projects/ecommerce/vue/README.md) | 107 | [VUE](../../standards/VUE.md) |
| [Genealogy](../../projects/genealogy/vue/README.md) | 62 | [VUE](../../standards/VUE.md) |
| [Liberu platform](../../projects/liberu/vue/README.md) | 4 | [VUE](../../standards/VUE.md) |
| [Maintenance](../../projects/maintenance/vue/README.md) | 60 | [VUE](../../standards/VUE.md) |
| [Real Estate](../../projects/real-estate/vue/README.md) | 70 | [VUE](../../standards/VUE.md) |
| [SAP enterprise suite](../../projects/sap/vue/README.md) | 16 | [VUE](../../standards/VUE.md) |
| [Social Network](../../projects/social-network/vue/README.md) | 59 | [VUE](../../standards/VUE.md) |

The package naming rule is `module-{independent-module-name}-vue-inertia`. Applications compose only packages required by enabled modules. See [Vue + Inertia architecture](../../standards/VUE.md), [technology map](../../TECHNOLOGIES.md), and [theme architecture](../../standards/THEMES.md).

## Availability and package identities

Counts above describe Markdown specifications, not released packages or implemented features. The [source inventory](../../architecture/SOURCE-INVENTORY.md) records observed manifests and source locations. Repository slugs, design identifiers, and Composer/npm package identities can differ; install using the actual manifest name. Shared capabilities use the [canonical owner](../../architecture/SHARED-MODULES.md) rather than a separate implementation in each project.

## Build the application and adapter

Follow the [implementation runbook](../../guides/presentation/INERTIA.md) for a skeleton, concrete integration steps, package builds and releases. Begin with the [shared architecture/foundation setup](../../guides/presentation/README.md); the module plans above do not imply registry availability.

## Liberu Music planned modules

See the [22 Music Vue + Inertia plans](../../projects/music/vue/README.md) and [DAW scope](../../projects/music/MUSIC.md). These are proposed adapters and domain boundaries, not verified package releases.
