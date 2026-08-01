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
| [API](API.md) | One-to-one API presentation modules, contracts, security, versioning, and composition |
| [Testing](TESTING.md) | Pest/PHPUnit suites, ownership, coverage, compatibility, and CI evidence |
| [Documentation](DOCUMENTATION.md) | Documentation structure, quality, validation, and maintenance |
| [Repository README standard](REPOSITORIES.md) | Required landing-page content for Liberu repositories |

## Detailed module documentation

The generated documentation hierarchy expands every independent module listed by an application scope:

- [Feature specifications](features/README.md) — 517 detailed module documents covering full scope, implementation, security, operations, and verification.
- [API module specifications](api/README.md) — 517 matching `module-{independent-module-name}-api` documents covering contracts, audiences, implementation, and API verification.

Every feature and API document links back to its authoritative application scope. Feature packages remain presentation-neutral; Filament, Livewire, and API behavior belongs in matching optional presentation packages.

## Application scopes

| Application | Detailed features | API modules |
|---|---|---|
| [Accounting](ACCOUNTING.md) | [105 modules](features/accounting/README.md) | [105 API modules](api/accounting/README.md) |
| [Automation](AUTOMATION.md) | [11 modules](features/automation/README.md) | [11 API modules](api/automation/README.md) |
| [Billing](BILLING.md) | [16 modules](features/billing/README.md) | [16 API modules](api/billing/README.md) |
| [Browser Game](BROWSER-GAME.md) | [15 modules](features/browser-game/README.md) | [15 API modules](api/browser-game/README.md) |
| [CMS](CMS.md) | [81 modules](features/cms/README.md) | [81 API modules](api/cms/README.md) |
| [Control Panel](CONTROL-PANEL.md) | [15 modules](features/control-panel/README.md) | [15 API modules](api/control-panel/README.md) |
| [CRM](CRM.md) | [95 modules](features/crm/README.md) | [95 API modules](api/crm/README.md) |
| [Ecommerce](ECOMMERCE.md) | [105 modules](features/ecommerce/README.md) | [105 API modules](api/ecommerce/README.md) |
| [Genealogy](GENEALOGY.md) | [14 modules](features/genealogy/README.md) | [14 API modules](api/genealogy/README.md) |
| [Maintenance](MAINTENANCE.md) | [14 modules](features/maintenance/README.md) | [14 API modules](api/maintenance/README.md) |
| [Real Estate](REAL-ESTATE.md) | [15 modules](features/real-estate/README.md) | [15 API modules](api/real-estate/README.md) |
| [SAP-style Enterprise Suite](SAP.md) | [16 domains](features/sap/README.md) | [16 API modules](api/sap/README.md) |
| [Social Network](SOCIAL-NETWORK.md) | [15 modules](features/social-network/README.md) | [15 API modules](api/social-network/README.md) |

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
