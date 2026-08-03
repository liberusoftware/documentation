# Getting started

This guide gives you the shortest safe path through the Liberu documentation repository. It is for developers, architects, and contributors choosing an application solution, selecting modules, and deciding how a Laravel application is presented.

## Start here

1. Read the [technology and solution map](TECHNOLOGIES.md) to choose a solution and delivery technology.
2. Open the application scope and identify the feature or module you need.
3. Read the matching feature specification, then its [core implementation plan](modules/core/README.md), API contract, and selected presentation adapter.
4. Choose an [adoption profile](architecture/ADOPTION.md) that matches the user's scale and recovery needs.
5. Apply the package, theme, security, tenancy, and testing rules before implementation.
6. Verify the result with the repository checks and document any new public contract.

## Core links

- [Liberu architecture](projects/LIBERU.md) — ecosystem boundaries and application composition.
- [Modules](architecture/MODULES.md) — package ownership, dependencies, lifecycle, and installation.
- [Core module implementations](modules/core/README.md) — domain-driven package plans for every project module.
- [Adoption profiles](architecture/ADOPTION.md) — practical personal, SME, and enterprise deployment choices.
- [Technologies](TECHNOLOGIES.md) — solution catalogue, GitHub repositories, and adapter selection.
- [Themes](standards/THEMES.md) — shared tokens, theme manifests, inheritance, and all framework adapters.
- [API](architecture/API.md) — contracts, authentication, tenancy, errors, pagination, and versioning.
- [Testing](standards/TESTING.md) — required suites, quality gates, coverage, and CI evidence.
- [Documentation](standards/DOCUMENTATION.md) — writing, ownership, links, examples, and review standards.
- [Installation](INSTALL.md) — local Laravel setup and verification.
- [Deployment](deployment/README.md) — Docker, Kubernetes, queues, workers, and production operations.

## Read by task

| If you are…                        | Start with                                                | Then read                                                                                                                                                                        |
| ---------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New to the repository              | [Technology map](TECHNOLOGIES.md)                         | [Architecture index](architecture/README.md), [Standards index](standards/README.md), [Installation](INSTALL.md)                                                                 |
| Designing a domain module          | [Feature specifications](features/README.md)              | [Core module plans](modules/core/README.md), [Modules architecture](architecture/MODULES.md), [DDD](standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [Testing](standards/TESTING.md) |
| Adding an API                      | [API module index](modules/api/README.md)                 | [API architecture](architecture/API.md), [API standard](standards/API.md), [Policies](architecture/POLICY.md), [Security](architecture/SECURITY.md)                              |
| Building a UI                      | [Presentation indexes](#choose-a-presentation-technology) | [Views](standards/VIEWS.md), [Themes](standards/THEMES.md), [Accessibility and testing](standards/TESTING.md)                                                                    |
| Supporting teams or tenants        | [Tenancy](architecture/TENANCY.md)                        | [Teams](architecture/TEAMS.md), [Policies](architecture/POLICY.md), [Settings](architecture/SETTINGS.md)                                                                         |
| Operating a small deployment       | [Adoption profiles](architecture/ADOPTION.md)             | [Database](standards/DATABASE.md), [Queues](standards/QUEUES.md), [Deployment](deployment/README.md), [Testing](standards/TESTING.md)                                            |
| Operating an enterprise deployment | [Modules architecture](architecture/MODULES.md)           | [Security](architecture/SECURITY.md), [CI](standards/CI.md), [Repositories](architecture/REPOSITORIES.md), [Deployment](deployment/README.md)                                    |
| Contributing documentation or code | [Contributing](standards/CONTRIBUTING.md)                 | [Guidelines](standards/GUIDELINES.md), [Documentation](standards/DOCUMENTATION.md), [Testing](standards/TESTING.md)                                                              |

## Choose a presentation technology

| Need                                                  | Read                                                                                               |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Laravel application foundation and domain composition | [Liberu](projects/LIBERU.md) · [Modules](architecture/MODULES.md)                                  |
| Administrative panels                                 | [Filament architecture](standards/FILAMENT.md) · [Filament indexes](modules/filament/README.md)    |
| Server-driven interactive UI                          | [Livewire architecture](standards/LIVEWIRE.md) · [Livewire indexes](modules/livewire/README.md)    |
| React application UI over Laravel routes              | [React + Inertia](standards/REACT.md) · [React indexes](modules/react/README.md)                   |
| Vue application UI over Laravel routes                | [Vue + Inertia](standards/VUE.md) · [Vue indexes](modules/vue/README.md)                           |
| Vue SSR/API-consuming application                     | [Nuxt](standards/NUXT.md) · [Nuxt indexes](modules/nuxt/README.md)                                 |
| iOS/Android client with React skills                  | [React Native](standards/REACT-NATIVE.md) · [React Native indexes](modules/react-native/README.md) |
| iOS/Android client with Dart/Flutter skills           | [Flutter](standards/FLUTTER.md) · [Flutter indexes](modules/flutter/README.md)                     |

Use one matching presentation package per domain module. Presentation packages consume the module API/public contracts; they do not duplicate authorization, persistence, or domain rules. For mobile-specific offline, device-security, and release decisions, read [mobile architecture](architecture/MOBILE.md) and [mobile standards](standards/MOBILE.md).

## Application and module indexes

The links below include every `README.md` index currently under `projects/`. Application scope documents are linked from [README.md](README.md) and [TECHNOLOGIES.md](TECHNOLOGIES.md).

### Accounting

- [API modules](projects/accounting/api/README.md)
- [Feature specifications](projects/accounting/features/README.md)
- [Filament 5](projects/accounting/filament/README.md)
- [Livewire 4](projects/accounting/livewire/README.md)
- [Nuxt 4](projects/accounting/nuxt/README.md)
- [React + Inertia](projects/accounting/react/README.md)
- [Vue + Inertia](projects/accounting/vue/README.md)

### Automation

- [API modules](projects/automation/api/README.md)
- [Feature specifications](projects/automation/features/README.md)
- [Filament 5](projects/automation/filament/README.md)
- [Livewire 4](projects/automation/livewire/README.md)
- [Nuxt 4](projects/automation/nuxt/README.md)
- [React + Inertia](projects/automation/react/README.md)
- [Vue + Inertia](projects/automation/vue/README.md)

### Billing

- [API modules](projects/billing/api/README.md)
- [Feature specifications](projects/billing/features/README.md)
- [Filament 5](projects/billing/filament/README.md)
- [Livewire 4](projects/billing/livewire/README.md)
- [Nuxt 4](projects/billing/nuxt/README.md)
- [React + Inertia](projects/billing/react/README.md)
- [Vue + Inertia](projects/billing/vue/README.md)

### Browser Game

- [API modules](projects/browser-game/api/README.md)
- [Feature specifications](projects/browser-game/features/README.md)
- [Filament 5](projects/browser-game/filament/README.md)
- [Livewire 4](projects/browser-game/livewire/README.md)
- [Nuxt 4](projects/browser-game/nuxt/README.md)
- [React + Inertia](projects/browser-game/react/README.md)
- [Vue + Inertia](projects/browser-game/vue/README.md)

### Cms

- [API modules](projects/cms/api/README.md)
- [Feature specifications](projects/cms/features/README.md)
- [Filament 5](projects/cms/filament/README.md)
- [Livewire 4](projects/cms/livewire/README.md)
- [Nuxt 4](projects/cms/nuxt/README.md)
- [React + Inertia](projects/cms/react/README.md)
- [Vue + Inertia](projects/cms/vue/README.md)

### Control Panel

- [API modules](projects/control-panel/api/README.md)
- [Feature specifications](projects/control-panel/features/README.md)
- [Filament 5](projects/control-panel/filament/README.md)
- [Livewire 4](projects/control-panel/livewire/README.md)
- [Nuxt 4](projects/control-panel/nuxt/README.md)
- [React + Inertia](projects/control-panel/react/README.md)
- [Vue + Inertia](projects/control-panel/vue/README.md)

### Crm

- [API modules](projects/crm/api/README.md)
- [Feature specifications](projects/crm/features/README.md)
- [Filament 5](projects/crm/filament/README.md)
- [Livewire 4](projects/crm/livewire/README.md)
- [Nuxt 4](projects/crm/nuxt/README.md)
- [React + Inertia](projects/crm/react/README.md)
- [Vue + Inertia](projects/crm/vue/README.md)

### Ecommerce

- [API modules](projects/ecommerce/api/README.md)
- [Feature specifications](projects/ecommerce/features/README.md)
- [Filament 5](projects/ecommerce/filament/README.md)
- [Livewire 4](projects/ecommerce/livewire/README.md)
- [Nuxt 4](projects/ecommerce/nuxt/README.md)
- [React + Inertia](projects/ecommerce/react/README.md)
- [Vue + Inertia](projects/ecommerce/vue/README.md)

### Genealogy

- [API modules](projects/genealogy/api/README.md)
- [Feature specifications](projects/genealogy/features/README.md)
- [Filament 5](projects/genealogy/filament/README.md)
- [Livewire 4](projects/genealogy/livewire/README.md)
- [Nuxt 4](projects/genealogy/nuxt/README.md)
- [React + Inertia](projects/genealogy/react/README.md)
- [Vue + Inertia](projects/genealogy/vue/README.md)

### Maintenance

- [API modules](projects/maintenance/api/README.md)
- [Feature specifications](projects/maintenance/features/README.md)
- [Filament 5](projects/maintenance/filament/README.md)
- [Livewire 4](projects/maintenance/livewire/README.md)
- [Nuxt 4](projects/maintenance/nuxt/README.md)
- [React + Inertia](projects/maintenance/react/README.md)
- [Vue + Inertia](projects/maintenance/vue/README.md)

### Liberu platform

- [Platform scope](projects/LIBERU.md)
- [Feature specifications](projects/liberu/features/README.md)
- [Core modules](projects/liberu/core/README.md)
- [API modules](projects/liberu/api/README.md)
- [Filament 5](projects/liberu/filament/README.md)
- [Livewire 4](projects/liberu/livewire/README.md)
- [Nuxt 4](projects/liberu/nuxt/README.md)
- [React + Inertia](projects/liberu/react/README.md)
- [Vue + Inertia](projects/liberu/vue/README.md)

### SAP-style Enterprise Suite

- [Platform scope](projects/sap/SAP.md)
- [Feature specifications](projects/sap/features/README.md)
- [Core modules](projects/sap/core/README.md)
- [API modules](projects/sap/api/README.md)
- [Filament 5](projects/sap/filament/README.md)
- [Livewire 4](projects/sap/livewire/README.md)
- [Nuxt 4](projects/sap/nuxt/README.md)
- [React + Inertia](projects/sap/react/README.md)
- [Vue + Inertia](projects/sap/vue/README.md)

### Real Estate

- [API modules](projects/real-estate/api/README.md)
- [Feature specifications](projects/real-estate/features/README.md)
- [Filament 5](projects/real-estate/filament/README.md)
- [Livewire 4](projects/real-estate/livewire/README.md)
- [Nuxt 4](projects/real-estate/nuxt/README.md)
- [React + Inertia](projects/real-estate/react/README.md)
- [Vue + Inertia](projects/real-estate/vue/README.md)

### Sap

- [API modules](projects/sap/api/README.md)
- [Feature specifications](projects/sap/features/README.md)
- [Filament 5](projects/sap/filament/README.md)
- [Livewire 4](projects/sap/livewire/README.md)
- [Nuxt 4](projects/sap/nuxt/README.md)
- [React + Inertia](projects/sap/react/README.md)
- [Vue + Inertia](projects/sap/vue/README.md)

### Social Network

- [API modules](projects/social-network/api/README.md)
- [Feature specifications](projects/social-network/features/README.md)
- [Filament 5](projects/social-network/filament/README.md)
- [Livewire 4](projects/social-network/livewire/README.md)
- [Nuxt 4](projects/social-network/nuxt/README.md)
- [React + Inertia](projects/social-network/react/README.md)
- [Vue + Inertia](projects/social-network/vue/README.md)

## Next steps

- For security-sensitive changes, follow [SECURITY.md](architecture/SECURITY.md) and the private reporting process.
- For tenancy and team-aware features, read [TENANCY.md](architecture/TENANCY.md), [TEAMS.md](architecture/TEAMS.md), and [POLICY.md](architecture/POLICY.md).
- For persistence and asynchronous work, read [DATABASE.md](standards/DATABASE.md), [MODELS.md](standards/MODELS.md), [JOBS.md](standards/JOBS.md), and [QUEUES.md](standards/QUEUES.md).
- For public boundaries, read [CONTRACTS.md](standards/CONTRACTS.md), [CONTROLLERS.md](standards/CONTROLLERS.md), and [API.md](standards/API.md).
- For a new package or presentation adapter, use the relevant issue mapping in its architecture standard and update documentation in the same change.
