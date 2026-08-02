# Liberu Documentation

## Architecture, application scopes, feature specifications, and API contracts

This repository is the canonical documentation hub for the Liberu ecosystem. It defines how independently versioned Laravel modules, presentation packages, themes, APIs, applications, testing, and operations fit together.

Start with [Liberu architecture](LIBERU.md) for the portfolio view or [Module architecture](MODULES.md) when implementing a package.

## Architecture standards

| Standard | Purpose |
|---|---|
| [Liberu](LIBERU.md) | Ecosystem composition, application boundaries, and portfolio adoption |
| [Modules](MODULES.md) | Independent Composer packages, dependency direction, lifecycle, and implementation process |
| [Boilerplate](BOILERPLATE.md) | Shared Laravel application foundation and cross-repository services |
| [Themes](THEMES.md) | Theme packaging, inheritance, assets, accessibility, and visual integration |
| [Filament](FILAMENT.md) | One-to-one Filament presentation modules, panels, plugins, resources, pages, and widgets |
| [Livewire](LIVEWIRE.md) | Livewire 4 component packaging, state, security, registration, and interaction |
| [Nuxt](NUXT.md) | Nuxt 4 API-consuming presentation packages, SSR, routing, typed clients, and deployment |
| [React + Inertia](REACT.md) | React 19.2 and Inertia 3 API-consuming presentation packages, pages, forms, hooks, SSR, and deployment |
| [API](API.md) | One-to-one API presentation modules, contracts, security, versioning, and composition |
| [Testing](TESTING.md) | Pest/PHPUnit suites, ownership, coverage, compatibility, and CI evidence |
| [CI](CI.md) | GitHub Actions workflows, required checks, release gates, environments, and deployment automation |
| [Documentation](DOCUMENTATION.md) | Documentation structure, quality, validation, and maintenance |
| [Repository README standard](REPOSITORIES.md) | Required landing-page content for Liberu repositories |
| [Jetstream](JETSTREAM.md) | Authentication, security features, and Jetstream team integration |
| [Socialstream](SOCIALSTREAM.md) | OAuth provider integration for Jetstream and Filament |
| [Policy and permissions](POLICY.md) | Laravel policies, Spatie Permission, and Filament Shield boundaries |
| [Teams](TEAMS.md) | Team context, membership, invitations, and authorization rules |
| [Tenancy](TENANCY.md) | Tenant boundaries, team isolation, context lifecycle, jobs, APIs, and verification |
| [Settings](SETTINGS.md) | Typed, encrypted, multi-scope settings with optional API and presentation adapters |
| [PSR standards](PSR.md) | PHP-FIG interoperability, coding, autoloading, HTTP, cache, events, and clock standards |
| [Installation](INSTALL.md) | Supported prerequisites and local installation workflow |
| [Deployment](deployment/README.md) | Standalone, Docker Compose, and Kubernetes deployment paths |
| [Contributing](CONTRIBUTING.md) | Contribution workflow and engineering quality gates |
| [Security](SECURITY.md) | Vulnerability reporting and security response process |

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
| [Accounting](ACCOUNTING.md) | [105](features/accounting/README.md) | [105](api/accounting/README.md) | [105](filament/accounting/README.md) | [105](livewire/accounting/README.md) | [105](react/accounting/README.md) |
| [Automation](AUTOMATION.md) | [11](features/automation/README.md) | [11](api/automation/README.md) | [11](filament/automation/README.md) | [11](livewire/automation/README.md) | [11](react/automation/README.md) |
| [Billing](BILLING.md) | [16](features/billing/README.md) | [16](api/billing/README.md) | [16](filament/billing/README.md) | [16](livewire/billing/README.md) | [16](react/billing/README.md) |
| [Browser Game](BROWSER-GAME.md) | [15](features/browser-game/README.md) | [15](api/browser-game/README.md) | [15](filament/browser-game/README.md) | [15](livewire/browser-game/README.md) | [15](react/browser-game/README.md) |
| [CMS](CMS.md) | [81](features/cms/README.md) | [81](api/cms/README.md) | [81](filament/cms/README.md) | [81](livewire/cms/README.md) | [81](react/cms/README.md) |
| [Control Panel](CONTROL-PANEL.md) | [15](features/control-panel/README.md) | [15](api/control-panel/README.md) | [15](filament/control-panel/README.md) | [15](livewire/control-panel/README.md) | [15](react/control-panel/README.md) |
| [CRM](CRM.md) | [95](features/crm/README.md) | [95](api/crm/README.md) | [95](filament/crm/README.md) | [95](livewire/crm/README.md) | [95](react/crm/README.md) |
| [Ecommerce](ECOMMERCE.md) | [105](features/ecommerce/README.md) | [105](api/ecommerce/README.md) | [105](filament/ecommerce/README.md) | [105](livewire/ecommerce/README.md) | [105](react/ecommerce/README.md) |
| [Genealogy](GENEALOGY.md) | [14](features/genealogy/README.md) | [14](api/genealogy/README.md) | [14](filament/genealogy/README.md) | [14](livewire/genealogy/README.md) | [14](react/genealogy/README.md) |
| [Maintenance](MAINTENANCE.md) | [14](features/maintenance/README.md) | [14](api/maintenance/README.md) | [14](filament/maintenance/README.md) | [14](livewire/maintenance/README.md) | [14](react/maintenance/README.md) |
| [Real Estate](REAL-ESTATE.md) | [15](features/real-estate/README.md) | [15](api/real-estate/README.md) | [15](filament/real-estate/README.md) | [15](livewire/real-estate/README.md) | [15](react/real-estate/README.md) |
| [SAP-style Enterprise Suite](SAP.md) | [16](features/sap/README.md) | [16](api/sap/README.md) | [16](filament/sap/README.md) | [16](livewire/sap/README.md) | [16](react/sap/README.md) |
| [Social Network](SOCIAL-NETWORK.md) | [15](features/social-network/README.md) | [15](api/social-network/README.md) | [15](filament/social-network/README.md) | [15](livewire/social-network/README.md) | [15](react/social-network/README.md) |

## Supporting specifications

- [Maintenance](MAINTENANCE.md) defines field-service and asset-maintenance scope.
- [Real Estate](REAL-ESTATE.md) defines agency, property, sales, and lettings scope.
- [Browser Game](BROWSER-GAME.md), [Genealogy](GENEALOGY.md), and [Social Network](SOCIAL-NETWORK.md) are independent application scopes.
- [Control Panel](CONTROL-PANEL.md) covers infrastructure and hosting operations.

## How to use this repository

1. Select the application scope and identify the independent module.
2. Use its document under `features/` as the detailed capability and implementation specification.
3. Apply `MODULES.md` for package boundaries and lifecycle.
4. Add only the required one-to-one presentation packages using `FILAMENT.md`, `LIVEWIRE.md`, and `API.md`.
5. Implement and verify the package using `TESTING.md`, `DOCUMENTATION.md`, and the module's definition of done.

Changes to package boundaries, public contracts, ownership, or cross-repository policy require corresponding documentation updates and an architecture decision record where specified by the relevant standard.

## Project governance

- [License](LICENSE.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
