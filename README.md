# Liberu Documentation

## Architecture, application scopes, feature specifications, and API contracts

This repository is the canonical documentation hub for the Liberu ecosystem. It defines how independently versioned Laravel modules, presentation packages, themes, APIs, applications, testing, and operations fit together.

Start with [Liberu architecture](architecture/LIBERU.md) for the portfolio view or [Module architecture](architecture/MODULES.md) when implementing a package.

## Architecture standards

| Standard | Purpose |
|---|---|
| [Liberu](architecture/LIBERU.md) | Ecosystem composition, application boundaries, and portfolio adoption |
| [Modules](architecture/MODULES.md) | Independent Composer packages, dependency direction, lifecycle, and implementation process |
| [Boilerplate](projects/boilerplate/BOILERPLATE.md) | Shared Laravel application foundation and cross-repository services |
| [Themes](architecture/THEMES.md) | Theme packaging, inheritance, assets, accessibility, and visual integration |
| [Filament](architecture/FILAMENT.md) | One-to-one Filament presentation modules, panels, plugins, resources, pages, and widgets |
| [Livewire](architecture/LIVEWIRE.md) | Livewire 4 component packaging, state, security, registration, and interaction |
| [Nuxt](architecture/NUXT.md) | Nuxt 4 API-consuming presentation packages, SSR, routing, typed clients, and deployment |
| [React + Inertia](architecture/REACT.md) | React 19.2 and Inertia 3 API-consuming presentation packages, pages, forms, hooks, SSR, and deployment |
| [API](architecture/API.md) | One-to-one API presentation modules, contracts, security, versioning, and composition |
| [Testing](architecture/TESTING.md) | Pest/PHPUnit suites, ownership, coverage, compatibility, and CI evidence |
| [CI](architecture/CI.md) | GitHub Actions workflows, required checks, release gates, environments, and deployment automation |
| [Documentation](architecture/DOCUMENTATION.md) | Documentation structure, quality, validation, and maintenance |
| [Repository README standard](architecture/REPOSITORIES.md) | Required landing-page content for Liberu repositories |
| [Jetstream](architecture/JETSTREAM.md) | Authentication, security features, and Jetstream team integration |
| [Socialstream](architecture/SOCIALSTREAM.md) | OAuth provider integration for Jetstream and Filament |
| [Policy and permissions](architecture/POLICY.md) | Laravel policies, Spatie Permission, and Filament Shield boundaries |
| [Teams](architecture/TEAMS.md) | Team context, membership, invitations, and authorization rules |
| [Tenancy](architecture/TENANCY.md) | Tenant boundaries, team isolation, context lifecycle, jobs, APIs, and verification |
| [Settings](architecture/SETTINGS.md) | Typed, encrypted, multi-scope settings with optional API and presentation adapters |
| [PSR standards](architecture/PSR.md) | PHP-FIG interoperability, coding, autoloading, HTTP, cache, events, and clock standards |
| [Installation](architecture/INSTALL.md) | Supported prerequisites and local installation workflow |
| [Deployment](deployment/README.md) | Standalone, Docker Compose, and Kubernetes deployment paths |
| [Contributing](architecture/CONTRIBUTING.md) | Contribution workflow and engineering quality gates |
| [Security](architecture/SECURITY.md) | Vulnerability reporting and security response process |

## Detailed module documentation

The generated documentation hierarchy expands every independent module listed by an application scope:

- [Feature specifications](features/README.md) — 517 detailed module documents covering full scope, implementation, security, operations, and verification.
- [API module specifications](api/README.md) — 517 matching `module-{independent-module-name}-api` documents covering contracts, audiences, implementation, and API verification.
- [Filament 5 implementations](filament/README.md) — 517 matching `module-{independent-module-name}-filament` presentation implementations with panel/resource/page/widget mappings.
- [Livewire 4 implementations](livewire/README.md) — 517 matching `module-{independent-module-name}-livewire` presentation implementations with component/state/interaction mappings.
- [Nuxt 4 implementations](nuxt/README.md) — 517 matching `module-{independent-module-name}-nuxt` presentation implementations consuming the corresponding API modules.
- [React 19.2 + Inertia 3 implementations](react/README.md) — 517 matching `module-{independent-module-name}-react-inertia` presentation implementations consuming the corresponding API modules.

Every feature and API document links back to its authoritative application scope. Feature packages remain presentation-neutral; Filament, Livewire, and API behavior belongs in matching optional presentation packages.

## Application scopes

| Application | Domain modules | API modules | Filament 5 | Livewire 4 | React + Inertia |
|---|---:|---:|---:|---:|---:|
| [Accounting](projects/accounting/ACCOUNTING.md) | [105](projects/accounting/features/README.md) | [105](projects/accounting/api/README.md) | [105](projects/accounting/filament/README.md) | [105](projects/accounting/livewire/README.md) | [105](projects/accounting/react/README.md) |
| [Automation](projects/automation/AUTOMATION.md) | [11](projects/automation/features/README.md) | [11](projects/automation/api/README.md) | [11](projects/automation/filament/README.md) | [11](projects/automation/livewire/README.md) | [11](projects/automation/react/README.md) |
| [Billing](projects/billing/BILLING.md) | [16](projects/billing/features/README.md) | [16](projects/billing/api/README.md) | [16](projects/billing/filament/README.md) | [16](projects/billing/livewire/README.md) | [16](projects/billing/react/README.md) |
| [Browser Game](projects/browser-game/BROWSER-GAME.md) | [15](projects/browser-game/features/README.md) | [15](projects/browser-game/api/README.md) | [15](projects/browser-game/filament/README.md) | [15](projects/browser-game/livewire/README.md) | [15](projects/browser-game/react/README.md) |
| [CMS](projects/cms/CMS.md) | [81](projects/cms/features/README.md) | [81](projects/cms/api/README.md) | [81](projects/cms/filament/README.md) | [81](projects/cms/livewire/README.md) | [81](projects/cms/react/README.md) |
| [Control Panel](projects/control-panel/CONTROL-PANEL.md) | [15](projects/control-panel/features/README.md) | [15](projects/control-panel/api/README.md) | [15](projects/control-panel/filament/README.md) | [15](projects/control-panel/livewire/README.md) | [15](projects/control-panel/react/README.md) |
| [CRM](projects/crm/CRM.md) | [95](projects/crm/features/README.md) | [95](projects/crm/api/README.md) | [95](projects/crm/filament/README.md) | [95](projects/crm/livewire/README.md) | [95](projects/crm/react/README.md) |
| [Ecommerce](projects/ecommerce/ECOMMERCE.md) | [105](projects/ecommerce/features/README.md) | [105](projects/ecommerce/api/README.md) | [105](projects/ecommerce/filament/README.md) | [105](projects/ecommerce/livewire/README.md) | [105](projects/ecommerce/react/README.md) |
| [Genealogy](projects/genealogy/GENEALOGY.md) | [14](projects/genealogy/features/README.md) | [14](projects/genealogy/api/README.md) | [14](projects/genealogy/filament/README.md) | [14](projects/genealogy/livewire/README.md) | [14](projects/genealogy/react/README.md) |
| [Maintenance](projects/maintenance/MAINTENANCE.md) | [14](projects/maintenance/features/README.md) | [14](projects/maintenance/api/README.md) | [14](projects/maintenance/filament/README.md) | [14](projects/maintenance/livewire/README.md) | [14](projects/maintenance/react/README.md) |
| [Real Estate](projects/real-estate/REAL-ESTATE.md) | [15](projects/real-estate/features/README.md) | [15](projects/real-estate/api/README.md) | [15](projects/real-estate/filament/README.md) | [15](projects/real-estate/livewire/README.md) | [15](projects/real-estate/react/README.md) |
| [SAP-style Enterprise Suite](projects/sap/SAP.md) | [16](projects/sap/features/README.md) | [16](projects/sap/api/README.md) | [16](projects/sap/filament/README.md) | [16](projects/sap/livewire/README.md) | [16](projects/sap/react/README.md) |
| [Social Network](projects/social-network/SOCIAL-NETWORK.md) | [15](projects/social-network/features/README.md) | [15](projects/social-network/api/README.md) | [15](projects/social-network/filament/README.md) | [15](projects/social-network/livewire/README.md) | [15](projects/social-network/react/README.md) |

## Supporting specifications

- [Maintenance](projects/maintenance/MAINTENANCE.md) defines field-service and asset-maintenance scope.
- [Real Estate](projects/real-estate/REAL-ESTATE.md) defines agency, property, sales, and lettings scope.
- [Browser Game](projects/browser-game/BROWSER-GAME.md), [Genealogy](projects/genealogy/GENEALOGY.md), and [Social Network](projects/social-network/SOCIAL-NETWORK.md) are independent application scopes.
- [Control Panel](projects/control-panel/CONTROL-PANEL.md) covers infrastructure and hosting operations.

## How to use this repository

1. Select the application scope and identify the independent module.
2. Use its document under `features/` as the detailed capability and implementation specification.
3. Apply `MODULES.md` for package boundaries and lifecycle.
4. Add only the required one-to-one presentation packages using `FILAMENT.md`, `LIVEWIRE.md`, and `API.md`.
5. Implement and verify the package using `TESTING.md`, `DOCUMENTATION.md`, and the module's definition of done.

Changes to package boundaries, public contracts, ownership, or cross-repository policy require corresponding documentation updates and an architecture decision record where specified by the relevant standard.

## Project governance

- [License](LICENSE.md)
- [Contributing](architecture/CONTRIBUTING.md)
- [Security policy](architecture/SECURITY.md)
