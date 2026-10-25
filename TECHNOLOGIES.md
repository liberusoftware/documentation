# Liberu technology and solution map

This is the root catalogue for the solutions Liberu offers, the technology used to deliver each solution, and the documentation/repository that owns it. Choose the solution scope first, then select the presentation adapter required by the application surface.

## Solution portfolio

These are documented application solutions and target scopes. Source availability varies by project; the [commit-pinned source inventory](architecture/SOURCE-INVENTORY.md) identifies the 14 application repositories cloned from `liberusoftware` and their observed source locations. Documentation coverage does not prove that every package or adapter is released.

| Solution                   | What it provides                                                                                   | Application repository                                                                                      | Scope documentation                                         |
| -------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Boilerplate                | Shared Laravel foundation, identity, teams, settings, tenancy, policies, queues, and observability | [liberusoftware/boilerplate-laravel](https://github.com/liberusoftware/boilerplate-laravel) | [Boilerplate](projects/boilerplate/BOILERPLATE.md)          |
| CMS                        | Structured content, publishing, media, multisite, headless delivery, and site factory capabilities | [liberusoftware/cms-laravel](https://github.com/liberusoftware/cms-laravel) | [CMS](projects/cms/CMS.md)                                  |
| CRM                        | Customer data, sales, marketing, service, customer success, and relationship workspaces            | [liberusoftware/crm-laravel](https://github.com/liberusoftware/crm-laravel) | [CRM](projects/crm/CRM.md)                                  |
| Billing                    | Products, subscriptions, invoicing, payments, provisioning, hosting, and customer portals          | [liberusoftware/billing-laravel](https://github.com/liberusoftware/billing-laravel) | [Billing](projects/billing/BILLING.md)                      |
| Accounting                 | Ledgers, banking, tax, expenses, close management, reporting, and financial operations             | [liberusoftware/accounting-erp-laravel](https://github.com/liberusoftware/accounting-erp-laravel) | [Accounting](projects/accounting/ACCOUNTING.md)             |
| Ecommerce                  | Catalog, checkout, orders, fulfillment, returns, B2B, marketplaces, and omnichannel commerce       | [liberusoftware/ecommerce-laravel](https://github.com/liberusoftware/ecommerce-laravel) | [Ecommerce](projects/ecommerce/ECOMMERCE.md)                |
| Control Panel              | Hosting, infrastructure, DNS, mail, databases, containers, backups, and security operations        | [liberusoftware/control-panel-laravel](https://github.com/liberusoftware/control-panel-laravel) | [Control Panel](projects/control-panel/CONTROL-PANEL.md)    |
| Automation                 | Governed workflows, provider-neutral AI, approvals, evaluation, media generation, and connectors   | [liberusoftware/automation-laravel](https://github.com/liberusoftware/automation-laravel) | [Automation](projects/automation/AUTOMATION.md)             |
| Browser Game               | Accounts, characters, worlds, quests, combat, economy, competition, and live operations            | [liberusoftware/browser-game-laravel](https://github.com/liberusoftware/browser-game-laravel) | [Browser Game](projects/browser-game/BROWSER-GAME.md)       |
| Genealogy                  | People, relationships, evidence, DNA, places, research, media, and tree exploration                | [liberusoftware/genealogy-laravel](https://github.com/liberusoftware/genealogy-laravel) | [Genealogy](projects/genealogy/GENEALOGY.md)                |
| Maintenance                | Assets, work orders, inspections, scheduling, inventory, compliance, labor, and portals            | [liberusoftware/maintenance-laravel](https://github.com/liberusoftware/maintenance-laravel) | [Maintenance](projects/maintenance/MAINTENANCE.md)          |
| Real Estate                | Properties, parties, listings, viewings, valuations, offers, sales progression, and lettings       | [liberusoftware/real-estate-laravel](https://github.com/liberusoftware/real-estate-laravel) | [Real Estate](projects/real-estate/REAL-ESTATE.md)          |
| SAP-style Enterprise Suite | Finance, controlling, procurement, inventory, projects, service, people, assets, and governance    | [liberusoftware/enterprise-sap-laravel](https://github.com/liberusoftware/enterprise-sap-laravel) | [SAP](projects/sap/SAP.md)                                  |
| Social Network             | Profiles, graph, publishing, feeds, communities, messaging, moderation, federation, and analytics  | [liberusoftware/social-network-laravel](https://github.com/liberusoftware/social-network-laravel) | [Social Network](projects/social-network/SOCIAL-NETWORK.md) |

The [projects index](projects/README.md) provides the complete local scope directory. Application links above identify the repositories observed in the requested `liberusoftware` organization scan. The enterprise source host is `liberusoftware/enterprise-sap-laravel`; its foundation implementation is distinct from the full target domain scope. The [repository standard](architecture/REPOSITORIES.md) governs repository documentation; actual source locations are recorded in the inventory.

## Delivery technologies

| Technology solution    | Best fit                                                                                        | Repository/documentation links                                                                                                                                                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Laravel + PHP          | Application composition, domain integration, HTTP, queues, authorization, persistence, and APIs | [Laravel GitHub](https://github.com/laravel/laravel) · [Modules](architecture/MODULES.md) · [Liberu architecture](projects/LIBERU.md)                                                                      |
| Filament 5             | Administrative panels, resources, pages, widgets, tables, forms, and operational dashboards     | [Filament GitHub](https://github.com/filamentphp/filament) · [Filament architecture](standards/FILAMENT.md) · [Filament indexes](modules/filament/README.md)                                               |
| Livewire 4             | Server-driven interactive Laravel UI and presentation-state components                          | [Livewire GitHub](https://github.com/livewire/livewire) · [Livewire architecture](standards/LIVEWIRE.md) · [Livewire indexes](modules/livewire/README.md)                                                  |
| React 19.2 + Inertia 3 | Rich Laravel-driven application shells with React components, typed hooks, forms, and SSR       | [React GitHub](https://github.com/facebook/react) · [Inertia GitHub](https://github.com/inertiajs/inertia) · [React architecture](standards/REACT.md) · [React indexes](modules/react/README.md)           |
| Vue 3 + Inertia 3      | Rich Laravel-driven application shells with Vue SFCs, typed composables, forms, and SSR         | [Vue GitHub](https://github.com/vuejs/core) · [Inertia GitHub](https://github.com/inertiajs/inertia) · [Vue/Inertia architecture](standards/VUE.md) · [Vue indexes](modules/vue/README.md)                 |
| Nuxt 4                 | Vue SSR/API-consuming applications, public sites, file-based routing, and deliberate BFF layers | [Nuxt GitHub](https://github.com/nuxt/nuxt) · [Nuxt architecture](standards/NUXT.md) · [Nuxt indexes](modules/nuxt/README.md)                                                                              |
| Next.js | Independently deployed React web applications consuming Laravel APIs | [Next.js standard](standards/NEXTJS.md) · [Next.js module plans](modules/nextjs/README.md) |
| Vite                   | Shared asset compilation for Laravel, React/Inertia, Vue/Inertia, and theme adapters            | [Vite GitHub](https://github.com/vitejs/vite) · [Theme architecture](standards/THEMES.md)                                                                                                                  |
| React Native + Expo    | iOS, Android, and optional web clients consuming Liberu APIs                                    | [React Native docs](https://reactnative.dev/docs/getting-started) · [Expo docs](https://docs.expo.dev/) · [Mobile architecture](architecture/MOBILE.md) · [Mobile modules](modules/react-native/README.md) |
| Flutter + Dart         | iOS, Android, and optional desktop/web clients consuming Liberu APIs                            | [Flutter docs](https://docs.flutter.dev/) · [Dart docs](https://dart.dev/) · [Mobile architecture](architecture/MOBILE.md) · [Flutter modules](modules/flutter/README.md)                                  |

## Package and scope matrix

Technology adapters are optional. These are design identifier patterns; actual installable identities come from package manifests, and an enterprise workspace may compose several existing adapters:

```text
module-{module}-api
module-{module}-filament
module-{module}-livewire
module-{module}-react-inertia
module-{module}-vue-inertia
module-{module}-nuxt
module-{module}-nextjs
```

The current catalogue contains 1,380 feature documents across 15 scopes, plus 12 retained foundation design aliases. Core and adapter folders each preserve 1,392 documented spellings. The source maps explain the aliases and observed identities; these counts do not prove implementation or release availability. Next.js provides 1,392 module documents organized into [617 shared adapter plan groups](modules/nextjs/OWNERSHIP.md), so alternate spellings and consumers do not automatically become separate packages.

| Adapter index | Scope |
| --- | --- |
| Core | [Domain implementation specifications](modules/core/README.md) |
| API | [HTTP contract specifications](modules/api/README.md) |
| Filament | [Administrative presentation specifications](modules/filament/README.md) |
| Livewire | [Server-driven presentation specifications](modules/livewire/README.md) |
| React + Inertia | [React presentation specifications](modules/react/README.md) |
| Vue + Inertia | [Vue presentation specifications](modules/vue/README.md) |
| Next.js | [Proposed API-consuming React adapters](modules/nextjs/README.md) |
| Nuxt | [API-consuming Vue presentation specifications](modules/nuxt/README.md) |
| React Native | [Mobile React Native specifications](modules/react-native/README.md) |
| Flutter | [Mobile Flutter specifications](modules/flutter/README.md) |

## Shared design and architecture rules

- Domain modules own business rules, persistence, policies, contracts, events, jobs, and recovery semantics.
- Presentation packages consume only the matching module contract and never access private Laravel models or another module's internals.
- Laravel owns authoritative business authorization, validation, and tenant policy. Independently deployed Next.js/Nuxt applications also authorize their own entry points and manage their routing and session integration.
- Themes use one technology-neutral identity, manifest, token vocabulary, accessibility contract, and extension-point model. Framework-specific theme adapters are optional; see [THEMES.md](standards/THEMES.md).
- The same feature must preserve permissions, tenancy, localization, loading/error/empty states, and API semantics across every adapter.

## Choosing a solution path

1. Choose the application solution and read its scope document.
2. Select the independent feature under `projects/{solution}/features/`.
3. Add the matching API and only the presentation adapters required by the surface.
4. Select a compatible theme and technology adapter using [THEMES.md](standards/THEMES.md).
5. Verify contracts, accessibility, security, compatibility, and deployment using [TESTING.md](standards/TESTING.md).

External technology links identify the upstream projects Liberu builds on; Liberu application and package repositories remain the authoritative sources for Liberu-specific behavior.

## Package development and updates

Use the [Composer lifecycle guide](guides/COMPOSER.md) for PHP modules and the [npm lifecycle guide](guides/NPM.md) for JavaScript packages. Both cover project clones, local development, dependency updates, and publishing. Choose reuse candidates through the [shared module source comparison](architecture/SHARED-MODULE-COMPARISON.md).
