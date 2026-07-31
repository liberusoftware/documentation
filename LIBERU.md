# Liberu Platform

## Product and Architecture Scope

**Status:** Canonical platform overview
**Target stack:** Laravel 13, PHP 8.5, Filament 5, Livewire 4
**Architecture references:** [MODULES.md](MODULES.md) and [THEMES.md](THEMES.md)

## Purpose

Liberu is a family of independently deployable, open-source Laravel products built on one shared module and theme architecture. Products may run alone or be composed into a unified platform without forking their upstream repositories.

This document defines platform intent, product boundaries, shared capabilities, integration rules, and delivery order. `MODULES.md` is the source of truth for backend and application module architecture. `THEMES.md` is the source of truth for presentation packages and frontend assets. Product-specific behavior belongs in the relevant scope document.

## Product portfolio

| Scope | Product responsibility |
|---|---|
| `BOILERPLATE.md` | Canonical reusable application foundation for every Liberu Laravel repository |
| `ACCOUNTING.md` | Ledger, receivables, payables, banking, tax, assets, expenses, payroll accounting, and reporting |
| `AUTOMATION.md` | Provider-neutral AI, workflow automation, voice, image, and video services |
| `BILLING.md` | Catalog, ordering, subscriptions, invoicing, payments, service provisioning, domains, and ISP operations |
| `BROWSER-GAME.md` | Persistent browser game, progression, world, economy, social play, and live operations |
| `CMS.md` | Content modeling, publishing, media, navigation, SEO, forms, and headless delivery |
| `CONTROL-PANEL.md` | Hosting, server, container, Kubernetes, DNS, mail, database, backup, and security operations |
| `CRM.md` | Contacts, sales, communications, marketing, support, projects, and customer engagement |
| `ECOMMERCE.md` | Products, inventory, cart, checkout, orders, payments, shipping, tax, and promotions |
| `GENEALOGY.md` | People, relationships, trees, evidence, research, DNA, GEDCOM, and collaboration |
| `MAINTENANCE.md` | Assets, work orders, scheduling, inspections, inventory, field service, and compliance |
| `REAL-ESTATE.md` | Properties, applicants, sales, lettings, viewings, offers, progression, and portals |
| `SAP.md` | Enterprise resource planning and cross-functional business operations |
| `SOCIAL-NETWORK.md` | Profiles, graph, feed, communities, messaging, moderation, and federation |

## Platform principles

- **Composable:** every product is assembled from explicit modules with declared dependencies.
- **Independent:** a product can be installed and upgraded without the full platform.
- **Shared contracts:** identity, tenancy, money, audit, files, notifications, and integrations use common interfaces.
- **Clear ownership:** one module owns each authoritative record; other modules reference it by stable identifier.
- **Event-driven integration:** modules publish versioned domain events and avoid direct access to another module's tables.
- **Provider-neutral:** external services are accessed through contracts and replaceable drivers.
- **Secure by default:** least privilege, tenant isolation, auditable changes, encrypted secrets, and explicit approval for high-risk actions.
- **Accessible and localizable:** user interfaces target WCAG 2.2 AA and support translation, locale, currency, and timezone differences.
- **Observable:** critical workflows expose structured logs, metrics, traces, health checks, and actionable failures.

## Shared application foundation

`BOILERPLATE.md` exclusively defines reusable application-foundation features. Every product selects relevant boilerplate modules and must not reimplement or fork them. Product scopes define domain modules, permissions, translations, and monetary rules only where those extend the shared contracts.

## Shared platform capabilities

All products consume these capabilities from the boilerplate where applicable:

| Capability | Responsibility |
|---|---|
| Platform Core | Module registry, lifecycle, configuration, health, feature flags, and shared primitives |
| Identity | Authentication, SSO, sessions, MFA, service identities, and account recovery |
| Organizations | Tenants, teams, divisions, memberships, invitations, and data scoping |
| Authorization | Roles, permissions, policies, contextual access, and privileged approvals |
| Audit | Immutable activity history, actor/context capture, retention, and export |
| Files and Media | Storage abstraction, metadata, transformations, access rules, and retention |
| Notifications | Templates, preferences, delivery channels, retries, and delivery status |
| Search | Indexing contracts, tenant-aware queries, filters, and result authorization |
| Workflow | State machines, approvals, scheduled actions, queues, retries, and compensation |
| Integration Hub | Credentials, provider drivers, webhooks, rate limits, synchronization, and reconciliation |
| Reporting | Saved reports, dashboards, exports, scheduled delivery, and governed metrics |
| Localization | Languages, locales, timezones, currencies, address formats, and tax identifiers |

## Composition and deployment

- Applications select modules through configuration and lock dependency versions through Composer.
- A module may expose web, API, console, queue, scheduled, Filament, Livewire, and Blade surfaces.
- Themes are selected independently of functional modules and may target a public site, portal, or admin panel.
- Deployments may be single-tenant or multi-tenant; tenancy behavior must be explicit and consistently tested.
- Long-running and failure-prone work must use queues with idempotency and retry policies.
- Backward-incompatible contracts, events, routes, or data changes require a documented migration path.

## Shared identity and data ownership

- A person or organization has one canonical identity and stable platform identifier.
- Product modules own domain extensions, not copies of core identity data.
- Data exchanged between modules uses documented DTOs, commands, queries, or events.
- Cross-product reporting consumes governed read models rather than coupling transactional schemas.
- Privacy requests, retention rules, consent, and legal holds propagate across participating modules.

## Primary platform workflows

1. **Lead to revenue:** CRM lead → opportunity → proposal → contract → order/subscription → invoice → payment → accounting entry.
2. **Service lifecycle:** paid order → provisioning request → control-panel operation → service activation → usage/status sync → renewal or suspension.
3. **Commerce lifecycle:** catalog → cart → checkout → payment authorization → fulfillment → refund/return → accounting reconciliation.
4. **Project delivery:** won work → project → tasks or GitHub issues → time/cost capture → billing → profitability reporting.
5. **Customer support:** channel message → identity resolution → triage → ticket → SLA workflow → resolution → knowledge feedback.
6. **Content to campaign:** CMS content → approval → publication → social/email campaign → engagement → CRM attribution.

Every workflow must define its record owner, state transitions, events, failure recovery, permissions, audit trail, and operational metrics.

## Domains and experience surfaces

| Domain | Primary experience |
|---|---|
| `liberusoftware.com` | Open-source products, documentation, releases, and software services |
| `liberuhosting.com` | Hosting catalog, checkout, customer portal, and service management |
| `liberuservices.com` | Consulting, enquiries, proposals, bookings, and project delivery |
| `liberugroup.com` | Corporate information, brands, leadership, and press |

Host resolution selects site, brand, locale, theme, navigation, and enabled features. It must not bypass tenant authorization or create separate identity records.

## Quality and governance gates

- Automated unit, feature, integration, architecture, accessibility, and authorization tests.
- Static analysis, formatting, dependency audit, secret scanning, and migration validation in CI.
- API and event contract tests for cross-module integrations.
- Performance budgets and representative load tests for critical paths.
- Backup, restore, disaster-recovery, and upgrade rehearsals for stateful products.
- Data classification, retention, export, deletion, and consent behavior documented per module.
- Human approval for financial disbursements, contractual commitments, destructive infrastructure actions, and externally published AI output unless policy explicitly permits automation.

## Delivery sequence

1. **Foundation:** core module manager, identity, organizations, authorization, audit, theme engine, CI conventions.
2. **Digital presence:** CMS, media, search, forms, multi-site routing, public themes.
3. **Revenue:** CRM, catalog, ecommerce/billing, payments, customer portal.
4. **Operations:** provisioning, control panel, support, projects, maintenance workflows.
5. **Finance:** accounting integration, reconciliation, tax, expenses, payroll interfaces, reporting.
6. **Automation:** provider drivers, AI gateway, approval policies, omnichannel workflows, content automation.
7. **Expansion:** specialist products, federation, marketplaces, advanced analytics, and regional capabilities.

Each phase must deliver usable vertical workflows, migration/upgrade documentation, telemetry, and operational runbooks rather than isolated screens.

## Scope document convention

Each product scope defines: module ownership, required capabilities, key workflows, integration contracts, non-functional requirements, dependencies, phases, and acceptance gates. Requirements use stable module names and imperative language so a follow-up process can convert each module or phase into a GitHub epic and its capability bullets into child issues.

## Out of scope for this overview

Detailed database schemas, UI mockups, provider selection, estimates, and repository-specific migration steps belong in implementation issues or architecture decisions. If a product document conflicts with `MODULES.md` or `THEMES.md` on architecture, those canonical documents take precedence.
