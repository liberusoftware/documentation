# Liberu technology and solution map

This is the root catalogue for the solutions Liberu offers, the technology used to deliver each solution, and the documentation/repository that owns it. Choose the solution scope first, then select the presentation adapter required by the application surface.

## Solution portfolio

These are the current application solutions. Each solution has framework-neutral feature and API scopes in this repository and an application repository for the Laravel composition root.

| Solution | What it provides | Application repository | Scope documentation |
|---|---|---|---|
| Boilerplate | Shared Laravel foundation, identity, teams, settings, tenancy, policies, queues, and observability | [liberusoftware/boilerplate-laravel](https://github.com/liberusoftware/boilerplate-laravel) | [Boilerplate](projects/boilerplate/BOILERPLATE.md) |
| CMS | Structured content, publishing, media, multisite, headless delivery, and site factory capabilities | [liberu-cms/cms-laravel](https://github.com/liberu-cms/cms-laravel) | [CMS](projects/cms/CMS.md) |
| CRM | Customer data, sales, marketing, service, customer success, and relationship workspaces | [liberu-crm/crm-laravel](https://github.com/liberu-crm/crm-laravel) | [CRM](projects/crm/CRM.md) |
| Billing | Products, subscriptions, invoicing, payments, provisioning, hosting, and customer portals | [liberu-billing/billing-laravel](https://github.com/liberu-billing/billing-laravel) | [Billing](projects/billing/BILLING.md) |
| Accounting | Ledgers, banking, tax, expenses, close management, reporting, and financial operations | [liberu-accounting/accounting-laravel](https://github.com/liberu-accounting/accounting-laravel) | [Accounting](projects/accounting/ACCOUNTING.md) |
| Ecommerce | Catalog, checkout, orders, fulfillment, returns, B2B, marketplaces, and omnichannel commerce | [liberu-ecommerce/ecommerce-laravel](https://github.com/liberu-ecommerce/ecommerce-laravel) | [Ecommerce](projects/ecommerce/ECOMMERCE.md) |
| Control Panel | Hosting, infrastructure, DNS, mail, databases, containers, backups, and security operations | [liberu-control-panel/control-panel-laravel](https://github.com/liberu-control-panel/control-panel-laravel) | [Control Panel](projects/control-panel/CONTROL-PANEL.md) |
| Automation | Governed workflows, provider-neutral AI, approvals, evaluation, media generation, and connectors | [liberu-automation/automation-laravel](https://github.com/liberu-automation/automation-laravel) | [Automation](projects/automation/AUTOMATION.md) |
| Browser Game | Accounts, characters, worlds, quests, combat, economy, competition, and live operations | [LiberuSoftware GitHub organization](https://github.com/liberusoftware) | [Browser Game](projects/browser-game/BROWSER-GAME.md) |
| Genealogy | People, relationships, evidence, DNA, places, research, media, and tree exploration | [liberusoftware/genealogy-laravel](https://github.com/liberusoftware/genealogy-laravel) | [Genealogy](projects/genealogy/GENEALOGY.md) |
| Maintenance | Assets, work orders, inspections, scheduling, inventory, compliance, labor, and portals | [LiberuSoftware GitHub organization](https://github.com/liberusoftware) | [Maintenance](projects/maintenance/MAINTENANCE.md) |
| Real Estate | Properties, parties, listings, viewings, valuations, offers, sales progression, and lettings | [LiberuSoftware GitHub organization](https://github.com/liberusoftware) | [Real Estate](projects/real-estate/REAL-ESTATE.md) |
| SAP-style Enterprise Suite | Finance, controlling, procurement, inventory, projects, service, people, assets, and governance | [LiberuSoftware GitHub organization](https://github.com/liberusoftware) | [SAP](projects/sap/SAP.md) |
| Social Network | Profiles, graph, publishing, feeds, communities, messaging, moderation, federation, and analytics | [LiberuSoftware GitHub organization](https://github.com/liberusoftware) | [Social Network](projects/social-network/SOCIAL-NETWORK.md) |

The [repository standard](architecture/REPOSITORIES.md) is the source of truth for canonical application repository names. Where a dedicated repository is not yet published, the organization link is intentional and avoids inventing a repository URL.

## Delivery technologies

| Technology solution | Best fit | Repository/documentation links |
|---|---|---|
| Laravel + PHP | Application composition, domain integration, HTTP, queues, authorization, persistence, and APIs | [Laravel GitHub](https://github.com/laravel/laravel) · [Modules](architecture/MODULES.md) · [Liberu architecture](projects/LIBERU.md) |
| Filament 5 | Administrative panels, resources, pages, widgets, tables, forms, and operational dashboards | [Filament GitHub](https://github.com/filamentphp/filament) · [Filament architecture](standards/FILAMENT.md) · [Filament indexes](modules/filament/README.md) |
| Livewire 4 | Server-driven interactive Laravel UI and presentation-state components | [Livewire GitHub](https://github.com/livewire/livewire) · [Livewire architecture](standards/LIVEWIRE.md) · [Livewire indexes](modules/livewire/README.md) |
| React 19.2 + Inertia 3 | Rich Laravel-driven application shells with React components, typed hooks, forms, and SSR | [React GitHub](https://github.com/facebook/react) · [Inertia GitHub](https://github.com/inertiajs/inertia) · [React architecture](standards/REACT.md) · [React indexes](modules/react/README.md) |
| Vue 3 + Inertia 3 | Rich Laravel-driven application shells with Vue SFCs, typed composables, forms, and SSR | [Vue GitHub](https://github.com/vuejs/core) · [Inertia GitHub](https://github.com/inertiajs/inertia) · [Vue/Inertia architecture](standards/VUE.md) · [Vue indexes](modules/vue/README.md) |
| Nuxt 4 | Vue SSR/API-consuming applications, public sites, file-based routing, and deliberate BFF layers | [Nuxt GitHub](https://github.com/nuxt/nuxt) · [Nuxt architecture](standards/NUXT.md) · [Nuxt indexes](modules/nuxt/README.md) |
| Vite | Shared asset compilation for Laravel, React/Inertia, Vue/Inertia, and theme adapters | [Vite GitHub](https://github.com/vitejs/vite) · [Theme architecture](standards/THEMES.md) |

## Package and scope matrix

Every technology adapter is optional and maps one-to-one to one domain module:

```text
module-{module}-api
module-{module}-filament
module-{module}-livewire
module-{module}-react-inertia
module-{module}-vue-inertia
module-{module}-nuxt
```

The complete Vue/Inertia matrix covers all 13 application scopes and 517 modules:

| Adapter index | Scope |
|---|---|
| React + Inertia | [517 React module implementations](modules/react/README.md) |
| Vue + Inertia | [517 Vue module implementations](modules/vue/README.md) |
| Nuxt | [517 Nuxt module implementations](modules/nuxt/README.md) |
| API | [517 API module implementations](modules/api/README.md) |
| Livewire | [517 Livewire module implementations](modules/livewire/README.md) |
| Filament | [517 Filament module implementations](modules/filament/README.md) |

## Shared design and architecture rules

- Domain modules own business rules, persistence, policies, contracts, events, jobs, and recovery semantics.
- Presentation packages consume only the matching module contract and never access private Laravel models or another module's internals.
- Laravel owns authorization, validation, team/tenant context, and composition even when the browser uses React, Vue, or Nuxt.
- Themes use one technology-neutral identity, manifest, token vocabulary, accessibility contract, and extension-point model. Framework-specific theme adapters are optional; see [THEMES.md](standards/THEMES.md).
- The same feature must preserve permissions, tenancy, localization, loading/error/empty states, and API semantics across every adapter.

## Choosing a solution path

1. Choose the application solution and read its scope document.
2. Select the independent feature under `projects/{solution}/features/`.
3. Add the matching API and only the presentation adapters required by the surface.
4. Select a compatible theme and technology adapter using [THEMES.md](standards/THEMES.md).
5. Verify contracts, accessibility, security, compatibility, and deployment using [TESTING.md](standards/TESTING.md).

External technology links identify the upstream projects Liberu builds on; Liberu application and package repositories remain the authoritative sources for Liberu-specific behavior.
