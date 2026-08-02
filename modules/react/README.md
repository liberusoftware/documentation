# Liberu React 19.2 + Inertia 3 Implementations

## Canonical one-to-one presentation indexes

Each document specifies the `React 19.2 + Inertia 3` implementation package matching exactly one independent domain module. Feature specifications remain framework-neutral; these packages own presentation adapters and depend on the matching module's public contracts.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-react-inertia` as the React 19.2/Inertia 3 presentation adapter over the matching Laravel core and API contracts. Keep domain decisions, authorization, validation, persistence, and transactions server-side; pages, components, typed props, forms, navigation, optimistic UI, and error rendering consume documented actions and resources rather than private models or ad hoc endpoints.

Use strict TypeScript types generated or checked against the API contract, CSRF/authentication and authorization-aware requests, accessible components, progressive loading, resilient empty/error/offline states, localized formatting, and safe handling of sensitive data. Test page props, forms, navigation, authorization outcomes, validation, API error mapping, accessibility, and representative end-to-end workflows while keeping core behavior covered by the core repository.

| Application                                                     | Implementations | Standard                                          |
| --------------------------------------------------------------- | --------------: | ------------------------------------------------- |
| [Accounting](../../projects/accounting/react/README.md)         |             105 | [architecture/REACT.md](../../standards/REACT.md) |
| [Automation](../../projects/automation/react/README.md)         |              11 | [architecture/REACT.md](../../standards/REACT.md) |
| [Billing](../../projects/billing/react/README.md)               |              16 | [architecture/REACT.md](../../standards/REACT.md) |
| [Browser Game](../../projects/browser-game/react/README.md)     |              15 | [architecture/REACT.md](../../standards/REACT.md) |
| [CMS](../../projects/cms/react/README.md)                       |              81 | [architecture/REACT.md](../../standards/REACT.md) |
| [Control Panel](../../projects/control-panel/react/README.md)   |              15 | [architecture/REACT.md](../../standards/REACT.md) |
| [CRM](../../projects/crm/react/README.md)                       |              95 | [architecture/REACT.md](../../standards/REACT.md) |
| [Ecommerce](../../projects/ecommerce/react/README.md)           |             105 | [architecture/REACT.md](../../standards/REACT.md) |
| [Genealogy](../../projects/genealogy/react/README.md)           |              14 | [architecture/REACT.md](../../standards/REACT.md) |
| [Maintenance](../../projects/maintenance/react/README.md)       |              14 | [architecture/REACT.md](../../standards/REACT.md) |
| [Real Estate](../../projects/real-estate/react/README.md)       |              15 | [architecture/REACT.md](../../standards/REACT.md) |
| [SAP](../../projects/sap/react/README.md)                       |              16 | [architecture/REACT.md](../../standards/REACT.md) |
| [Social Network](../../projects/social-network/react/README.md) |              15 | [architecture/REACT.md](../../standards/REACT.md) |

The package naming rule is `module-{independent-module-name}-react-inertia`. Applications compose only the packages required by enabled modules, and themes style supported React/Inertia extension points without taking ownership of functional components.
