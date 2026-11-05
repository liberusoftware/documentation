# Liberu React 19.2 + Inertia 3 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `React 19.2 + Inertia 3` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own presentation adapters and depend on the matching module's public contracts.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-react-inertia` as the React 19.2/Inertia 3 presentation adapter over the matching Laravel core and API contracts. Keep domain decisions, authorization, validation, persistence, and transactions server-side; pages, components, typed props, forms, navigation, optimistic UI, and error rendering consume documented actions and resources rather than private models or ad hoc endpoints.

Use strict TypeScript types generated or checked against the API contract, CSRF/authentication and authorization-aware requests, accessible components, progressive loading, resilient empty/error/offline states, localized formatting, and safe handling of sensitive data. Test page props, forms, navigation, authorization outcomes, validation, API error mapping, accessibility, and representative end-to-end workflows while keeping core behavior covered by the core repository.

| Project | Specification documents | Standard |
| --- | ---: | --- |
| [Accounting](../../projects/accounting/react/README.md) | 241 | [REACT](../../standards/REACT.md) |
| [Automation](../../projects/automation/react/README.md) | 57 | [REACT](../../standards/REACT.md) |
| [Billing](../../projects/billing/react/README.md) | 81 | [REACT](../../standards/REACT.md) |
| [Boilerplate](../../projects/boilerplate/react/README.md) | 43 | [REACT](../../standards/REACT.md) |
| [Browser Game](../../projects/browser-game/react/README.md) | 61 | [REACT](../../standards/REACT.md) |
| [CMS](../../projects/cms/react/README.md) | 252 | [REACT](../../standards/REACT.md) |
| [Control Panel](../../projects/control-panel/react/README.md) | 61 | [REACT](../../standards/REACT.md) |
| [CRM](../../projects/crm/react/README.md) | 218 | [REACT](../../standards/REACT.md) |
| [Ecommerce](../../projects/ecommerce/react/README.md) | 107 | [REACT](../../standards/REACT.md) |
| [Genealogy](../../projects/genealogy/react/README.md) | 62 | [REACT](../../standards/REACT.md) |
| [Liberu platform](../../projects/liberu/react/README.md) | 4 | [REACT](../../standards/REACT.md) |
| [Maintenance](../../projects/maintenance/react/README.md) | 60 | [REACT](../../standards/REACT.md) |
| [Real Estate](../../projects/real-estate/react/README.md) | 70 | [REACT](../../standards/REACT.md) |
| [SAP enterprise suite](../../projects/sap/react/README.md) | 16 | [REACT](../../standards/REACT.md) |
| [Social Network](../../projects/social-network/react/README.md) | 59 | [REACT](../../standards/REACT.md) |

The package naming rule is `module-{independent-module-name}-react-inertia`. Applications compose only the packages required by enabled modules, and themes style supported React/Inertia extension points without taking ownership of functional components.

## Availability and package identities

Counts above describe Markdown specifications, not released packages or implemented features. The [source inventory](../../architecture/SOURCE-INVENTORY.md) records observed manifests and source locations. Repository slugs, design identifiers, and Composer/npm package identities can differ; install using the actual manifest name. Shared capabilities use the [canonical owner](../../architecture/SHARED-MODULES.md) rather than a separate implementation in each project.

## Build the application and adapter

Follow the [implementation runbook](../../guides/presentation/INERTIA.md) for a skeleton, concrete integration steps, package builds and releases. Begin with the [shared architecture/foundation setup](../../guides/presentation/README.md); the module plans above do not imply registry availability.

## Liberu Music planned modules

See the [22 Music React + Inertia plans](../../projects/music/react/README.md) and [DAW scope](../../projects/music/MUSIC.md). These are proposed adapters and domain boundaries, not verified package releases.
