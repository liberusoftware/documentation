# Liberu Business Platform

## Composition and Implementation Scope

**Status:** Canonical Liberu deployment plan
**Target stack:** Laravel 13, PHP 8.5, Filament 5, Livewire 4
**Architecture:** [MODULES.md](../architecture/MODULES.md) · [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) · [THEMES.md](../standards/THEMES.md) · [API.md](../architecture/API.md)

## 1. Purpose

This document defines how Liberu composes existing product packages to run its software, hosting, services, and group operations. It does not redefine module features. The linked product scope owns each module's requirements, data, workflows, tests, and definition of done.

Liberu's deployment must provide:

- four branded public sites with one governed content and identity platform;
- open-source product, documentation, release, and community operations;
- hosting/service discovery, sales, ordering, payment, provisioning, renewal, and support;
- consulting lead, proposal, contract, project, time, expense, billing, and profitability workflows;
- finance, purchasing, payroll accounting, cash, tax, close, and management reporting;
- staff, contractor, partner, affiliate, customer, and supplier collaboration;
- secure automation and AI with approvals, cost controls, and recoverable execution;
- governed infrastructure, assets, maintenance, compliance, risk, and business continuity.

## 2. Scope precedence

| Concern | Source of truth |
|---|---|
| Composer packages, module boundaries, dependencies, adapters, lifecycle | [MODULES.md](../architecture/MODULES.md) |
| Shared application foundation | [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) |
| Blade, Livewire, layouts, components, CSS, JavaScript, and media | [THEMES.md](../standards/THEMES.md) |
| Module, application, connector, marketplace, and webhook APIs | [API.md](../architecture/API.md) |
| Product behavior | The corresponding product `.md` scope listed below |
| Liberu-specific composition, rollout, and cross-product acceptance | This document |

If this document lists a module, its linked scope supplies the implementation detail. Do not copy that module into a platform-specific package.

## 3. Business structure and experience surfaces

| Brand/division | Primary surface | Business purpose |
|---|---|---|
| Liberu Software | `liberusoftware.com` | Products, repositories, documentation, releases, roadmap, support, sponsorship, and software services |
| Liberu Hosting | `liberuhosting.com` | Hosting/domain catalog, checkout, service portal, provisioning, usage, incidents, and renewals |
| Liberu Services | `liberuservices.com` | Consulting, enquiries, bookings, proposals, contracts, projects, client collaboration, and case studies |
| Liberu Group | `liberugroup.com` | Corporate information, brands, leadership, governance, careers, partners, press, and policies |

One organization model represents legal entities, brands, divisions, departments, teams, cost/profit centers, projects, sites, and infrastructure locations. A single identity may hold different roles and visibility in each context.

## 4. Required package composition

Module names below are installation targets. Responsibilities remain in the linked scopes.

### 4.1 Application foundation

Source: [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md)

| Delivery | Modules |
|---|---|
| Required | Application Core; Module Manager; Identity; Two-Factor Authentication; Sessions and Devices; Profiles; Organizations and Teams; Roles and Permissions; Localization; Currency Context; Settings; Audit; Notifications; Files and Media; Scheduler and Queues; Observability; Developer Experience |
| Required for integration | API Access; Webhooks; Integrations; Import and Export; Feature Flags; Search |
| Required for measurement | Analytics Core; Google Analytics; Meta Server-Side Tracking |
| Optional | Jetstream Bridge; Activity and Comments |

### 4.2 Public sites and content operations

Source: [projects/cms/CMS.md](../projects/cms/CMS.md)

| Delivery | Modules |
|---|---|
| Required | CMS Core; Content Entities; Field System; Metadata; Taxonomy; Pages; Editorial Content; Structured Collections; Rich Text Editor; Block Editor; Revisions; Editorial Workflow; Publishing; Content Calendar; Media Library; Image Processing; Digital Asset Management; Navigation; Regions and Widgets; SEO; Redirects; Sitemaps; Content Search; Theme Integration; Web Delivery; Form Builder; Form Operations |
| Multi-brand and developer content | Multisite; Site Factory; Localization; Translation Management; Content Access; Content Governance; Configuration Management; Headless API; Syndication and Feeds; Static Publishing; Knowledge Base; Events Content; Analytics Integration |
| Operational | Backup and Restore; Cache and Performance; Content Integrity; Security Operations; Extension Manager; Site Recipes; Integration Directory |
| Later | Layout Builder; Views and Query Builder; Personalization; Experimentation; Recommendations; CMS Copilot; Content Intelligence |

### 4.3 Customer, sales, marketing, support, and delivery

Source: [projects/crm/CRM.md](../projects/crm/CRM.md)

| Delivery | Modules |
|---|---|
| Customer foundation | CRM Core; Customer Data Model; Data Operations; Consent and Preferences; Territories and Ownership; CRM Search; CRM Documents; Collaboration |
| Demand and sales | Lead Capture; Web Intent; Enrichment; Lead Qualification; Routing; Sales Pipelines; Sales Workspace; Activities; Scheduling; Sales Engagement; Email Productivity; Playbooks and Enablement; Forecasting; Revenue Intelligence; Account Planning |
| Commercial | CRM Product Workspace; CPQ; Proposals and Quotes; Contracts; Orders and Payments Workspace; Revenue Lifecycle |
| Marketing | Segmentation; Campaigns; Journey Orchestration; Email Marketing; Mobile Messaging; Advertising; Account-Based Marketing; Attribution; Events and Webinars; Landing Pages and Funnels; Conversion Optimization |
| Communications and service | Unified Conversations; Channel Gateway; Telephony; AI Reception and Conversation; Case Management; Omnichannel Service; SLA and Entitlements; Knowledge; Customer Self-Service; Feedback and Voice of Customer; Reputation Management; Service Analytics |
| Customer growth | Customer Success; Communities; Learning and Courses; Memberships; Referrals; Affiliate Management; Advocacy |
| Delivery and partners | Projects; Resource Planning; Work Management; Business Process Management; Partner Relationship Management; Deal Registration; Channel Sales; Client Onboarding |
| Later/optional | Prospecting; Dialer and Outreach; Contact Center; Quotas and Incentives; Loyalty; Marketing Development Funds; Agency Workspace; White Label; SaaS Packaging; Templates and Snapshots; CRM Copilot; Predictive Models |

### 4.4 Hosting, domains, subscriptions, and customer billing

Source: [projects/billing/BILLING.md](../projects/billing/BILLING.md)

| Delivery | Modules |
|---|---|
| Required | Billing Core; Catalog; Pricing; Orders; Subscriptions; Usage; Invoicing; Payments; Collections; Provisioning; Hosting; Domains; Customer Portal; Reporting |
| Where required | ISP; Communications |

Billing owns commercial service state. It invokes Control Panel provisioning through contracts/events and sends governed postings to Accounting.

### 4.5 Infrastructure and hosting operations

Source: [projects/control-panel/CONTROL-PANEL.md](../projects/control-panel/CONTROL-PANEL.md)

| Delivery | Modules |
|---|---|
| Required | Control Core; OS Adapters; Accounts; Web Hosting; Mail; Databases; DNS; Files; Certificates; Backups; Security; Monitoring; API and Automation |
| Platform expansion | Containers; Kubernetes |

Only Control Panel packages execute infrastructure changes. Billing, CRM, and portals submit authorized requests and consume operation status.

### 4.6 Finance and accounting

Source: [projects/accounting/ACCOUNTING.md](../projects/accounting/ACCOUNTING.md)

| Delivery | Modules |
|---|---|
| Foundation | Accounting Core; Financial Master Data; Chart of Accounts; General Ledger; Dimensions and Tracking; Accounting Periods; Accounting Policies |
| Income and cash | Sales Invoicing; Credit Notes and Adjustments; Customer Payments; Accounts Receivable; Collections; Bank Accounts; Bank Feeds; Bank Rules; Bank Reconciliation; Payment Reconciliation; Cash Position; Cash-Flow Forecasting |
| Spend and purchasing | Purchase Requisitions; Purchase Orders; Goods and Service Receipts; Supplier Bills; Three-Way Matching; Accounts Payable; Bill Payments; Document Capture; Receipt Management; Employee Expenses; Corporate Cards; Mileage; Time Tracking; Reimbursements |
| Compliance and assets | Tax Core; VAT; Tax Returns; E-Invoicing; Contractor Compliance; Fixed Assets; Depreciation; Asset Events; Inventory Accounting |
| Projects and workforce | Projects and Jobs; Project Costing; Project Billing; Project Profitability; Payroll Integration; Payroll Journals; Payroll Liabilities; Payroll Payments; Workforce Costing |
| Planning and control | Financial Statements; Operational Reports; Custom Report Builder; Dashboards; Budgets; Forecasts; Management Reporting; Close Management; Account Reconciliations; Journal Approvals; Accounting Review; Accountant Workspace; Year End; Audit Support |
| As organization grows | Multi-Currency; Multi-Entity; Intercompany; Consolidation; Regional Packs; Accounting Automation Pack; Business Insights |

### 4.7 Storefront and digital commerce

Source: [projects/ecommerce/ECOMMERCE.md](../projects/ecommerce/ECOMMERCE.md)

| Delivery | Modules |
|---|---|
| Required for software, merchandise, and digital sales | Commerce Core; Product Information Management; Catalog; Product Types; Pricing; Promotions; Availability; Inventory Ledger; Cart; Checkout; Orders; Payments; Tax; Shipping; Fulfillment; Digital Fulfillment; Returns; Refunds; Commerce Customers; Customer Accounts; Attribution and Analytics |
| Useful extensions | Bundles and Kits; Gift Cards and Store Credit; Search and Discovery; Recommendations; Reviews and Ratings; Loyalty; Referrals; Subscription Commerce; Membership Commerce; Bookings and Appointments; Markets; Sales Channels |
| Optional | Point of Sale; Marketplace Channels; Seller Marketplace; App Marketplace |

For hosting subscriptions, Billing remains authoritative; Ecommerce supplies storefront/cart/checkout experience and hands off the accepted order.

### 4.8 Automation and AI

Source: [projects/automation/AUTOMATION.md](../projects/automation/AUTOMATION.md)

| Delivery | Modules |
|---|---|
| Required | Automation Core; Rules; Approvals; AI Gateway; Prompt Registry; Data Processing; Connectors; Evaluation |
| Channel/content expansion | Voice; Image; Video |

AI may draft, classify, summarize, recommend, or perform approved low-risk actions. Financial disbursement, contracts, bulk outreach, publication, access changes, and infrastructure destruction retain explicit policy and human approval.

### 4.9 Internal assets, facilities, and field work

Source: [projects/maintenance/MAINTENANCE.md](../projects/maintenance/MAINTENANCE.md)

| Delivery | Modules |
|---|---|
| Required for managed infrastructure and offices | Maintenance Core; Customers and Sites; Assets; Work Orders; Scheduling; Preventative Maintenance; Inspections; Inventory; Procurement; Labor and Time; Commercial; Compliance; Portals; Reporting |

Use these packages for physical servers, networking equipment, offices, tools, vehicles, and customer-site maintenance. Control Panel remains authoritative for digital infrastructure operations.

### 4.10 Enterprise people, governance, and portfolio operations

Source: [projects/sap/SAP.md](../projects/sap/SAP.md)

| Delivery | Modules/domains |
|---|---|
| Required as the business grows | People; Procurement; Product and Engineering; Governance, Risk and Compliance; Data and Intelligence; Partners and Portals |
| Compose from specialist products | Finance; Controlling; Sales and CRM; Revenue Operations; Projects and Services; Service Management; Hosting and Cloud; Assets and Facilities |

The second row is a cross-functional ERP composition, not authorization to duplicate Accounting, CRM, Billing, Control Panel, or Maintenance records.

### 4.11 Specialist products

The browser game, genealogy, real-estate, and social-network scopes are independent products. Do not install their packages in the internal Liberu business application unless a documented business requirement exists. A public customer/community feature should prefer CRM Communities before adopting the full Social Network product.

## 5. Authoritative records

| Record | Owning product/module family | Consumers |
|---|---|---|
| Login, person identity, organization/team membership | Boilerplate | Every application |
| CRM contact/account relationship and consent | CRM | CMS, Billing, Ecommerce, Support, Automation |
| Public/editorial content and media | CMS | CRM campaigns, storefronts, public sites |
| Product/service commercial definition | Billing for services; Ecommerce for goods/storefront assortment | CRM sales workspace, CMS presentation |
| Subscription, service entitlement, invoice, payment allocation | Billing | CRM, Control Panel, Accounting, portals |
| Ecommerce order and fulfillment | Ecommerce | CRM, Accounting, support |
| Provisioned hosting/infrastructure observed state | Control Panel | Billing, CRM, support, monitoring |
| Journal, subledger, tax, bank, close, financial report | Accounting | Management, ERP reporting |
| Project/customer delivery state | CRM Projects initially; specialist project package when extracted | Billing, Accounting, customer portal |
| Physical asset and maintenance history | Maintenance | Accounting assets, service/support |
| Employee/contractor workforce record | SAP People | Boilerplate identity, CRM projects, Accounting payroll integration |
| AI prompt/run/evaluation/cost | Automation | Finance, management, originating product |

Cross-product references use stable identifiers and contracts/events. No package reads or writes another package's private tables.

## 6. Required business workflows

| Workflow | Package chain | Business result |
|---|---|---|
| Open-source release | Product/Engineering → GitHub adapter → CMS Publishing → Campaigns → Analytics | Release notes, documentation, announcements, adoption, and support context stay synchronized |
| Lead to consulting revenue | CMS/Form or campaign → CRM Lead/Sales → Proposal/Contract → Project/Time/Expense → Billing → Accounting | Complete services pipeline and profitability |
| Hosting order to active service | CMS/Ecommerce storefront → Billing Order/Subscription/Payment → Provisioning → Control Panel → Customer Portal → Accounting | Paid service is provisioned, monitored, renewed, suspended, or cancelled safely |
| Support to resolution | Unified Conversations/Telephony → Case/SLA/Knowledge → Control Panel or Project work → Feedback → Customer Success | Omnichannel support with ownership, escalation, evidence, and retention signals |
| Procure to pay | Purchase Requisition → approval → Purchase Order/Receipt → Supplier Bill/Match → Bill Payment → Bank Reconciliation | Controlled company spending with supplier and cash visibility |
| Hire/onboard to offboard | People → identity/team/roles → equipment/assets → learning → time/expense/payroll integration → access and asset recovery | Staff and contractors receive and lose access/resources reliably |
| Month-end management | Billing/Ecommerce/Payroll/Maintenance events → Accounting subledgers → reconciliations/close → budget/forecast/report pack | Management sees cash, revenue, cost, tax, margin, runway, and risks |
| Partner/affiliate growth | Partner/affiliate onboarding → campaign/referral/deal registration → sale → commission approval → Accounting export | Channel growth is attributable, governed, and payable |
| Incident and continuity | Monitoring → Service incident → customer communication/status content → remediation → problem/change → GRC evidence | Operational incidents produce learning, controls, and transparent communications |

Each workflow must have one accountable owner, versioned contracts/events, idempotency keys, explicit approvals, compensation/recovery, audit, service levels, and business metrics.

## 7. Useful management capabilities

The composed platform must give leadership and operators:

- a daily workspace for leads awaiting response, sales risks, support SLA risks, failed provisioning, overdue receivables/payables, cash exceptions, incidents, and approvals;
- consolidated revenue, recurring revenue, gross margin, project profitability, cash runway, tax exposure, churn, pipeline coverage, utilization, support quality, infrastructure capacity, and AI/provider spend;
- quarterly objectives, budgets, forecasts, hiring/capacity plans, product roadmaps, risks, controls, and decision records;
- supplier, contract, subscription, certificate, domain, license, warranty, policy, training, and compliance renewal calendars;
- customer health combining service usage, incidents, support, invoices, sentiment, adoption, renewals, and expansion opportunities;
- self-service portals for customers, staff, partners, affiliates, and suppliers with only role-relevant information;
- searchable company knowledge covering products, architecture, sales playbooks, support procedures, policies, runbooks, and lessons learned;
- data-quality, integration-health, failed-job, reconciliation, audit, privacy-request, and security dashboards.

These are cross-product read models and workspaces. They do not become a new owner of source data.

## 8. Developer implementation plan

1. **Create the composition repository.** Start from `boilerplate-laravel`; keep root `app/` limited to composition, brand policy, deployment configuration, and application-specific adapters.
2. **Record package decisions.** Create ADRs for selected packages, excluded packages, dependency direction, authoritative records, project ownership, event transport, tenancy model, and deployment topology.
3. **Define the application manifest.** Pin Composer packages and compatibility ranges; declare enabled modules by environment/site; distinguish installed, enabled, entitled, and authorized states.
4. **Implement organization context.** Seed legal entity, four brands/divisions, teams, sites/domains, cost/profit centers, projects, and locations; add least-privilege roles and approval matrices.
5. **Implement shared identity.** Configure SSO, two-factor enforcement, sessions/devices, invitations, service identities, customer/staff separation, and cross-domain login/session policy.
6. **Establish contracts before integrations.** Define stable IDs, DTOs, commands, queries, events, idempotency, outbox/inbox, correlation, schema versions, and ownership for every workflow in section 6.
7. **Build one vertical slice first.** Deliver `liberuhosting.com` plan → checkout → payment → provisioning → active service → invoice posting → portal/support, including failure and reconciliation paths.
8. **Deliver the other brand surfaces.** Configure CMS multisite, domains, site recipes, themes, navigation, SEO, analytics/consent, forms, content workflow, and deployment/cache behavior for all four brands.
9. **Deliver services operations.** Implement lead → proposal/contract → project/resource/time/expense → billing/accounting plus client portal, GitHub/project integration, and profitability reporting.
10. **Deliver finance and internal operations.** Implement procure-to-pay, expenses/cards, bank feeds/reconciliation, payroll accounting, tax, assets/maintenance, close, budgets, forecasts, and management packs.
11. **Add communications and automation.** Connect email/calendar, telephony/SMS/WhatsApp, support channels, CRM journeys, AI gateway, prompt/evaluation registry, approval policies, and spend limits.
12. **Add people, partner, and governance workflows.** Implement workforce lifecycle, partner/affiliate processes, contract/policy renewals, risk/control registers, compliance evidence, and continuity runbooks.
13. **Build governed read models.** Create leadership and operational dashboards from events/projections; document metric ownership, formula, freshness, permissions, and drill-through.
14. **Harden operations.** Complete contract, architecture, tenant isolation, authorization, accessibility, performance, migration, provider-failure, backup/restore, disaster-recovery, and security tests.
15. **Release incrementally.** Migrate one workflow/brand/team at a time with dry run, reconciliation, training, rollback, telemetry, and sign-off; remove replaced legacy paths only after acceptance.

## 9. Implementation deliverables

For every selected package or cross-product workflow, developers must provide:

- package/manifest and version constraints;
- ADR covering ownership, dependencies, data, events, and exclusions;
- migrations, seed/configuration, permissions, policies, and approval rules;
- provider adapters with test/sandbox mode, webhooks, retries, replay, and reconciliation;
- Filament/Livewire/API surfaces and theme extension points where required;
- contract, feature, architecture, authorization, tenant, migration, failure, and accessibility tests;
- logs, metrics, health checks, alerts, dashboards, and operational runbook;
- import/cutover/rollback plan, user documentation, changelog, and acceptance evidence.

## 10. Delivery milestones

1. **Foundation and brands:** application shell, identity, organization model, module registry, four CMS sites/themes, observability, and CI/CD.
2. **Hosting revenue slice:** catalog, checkout/payment, subscription/invoice, provisioning/control panel, portal, support, and accounting posting.
3. **Services revenue slice:** CRM sales, proposals/contracts, projects/resources/time/expense, client portal, billing, and profitability.
4. **Finance and internal operations:** purchasing/AP, banking, tax, payroll accounting, assets/maintenance, close, budgets, and reports.
5. **Growth and customer success:** campaigns, journeys, attribution, partner/affiliate, knowledge/community/learning, health, renewals, and advocacy.
6. **Automation and governance:** AI/voice/content automation, approval policy, people lifecycle, risk/compliance, consolidated insights, and continuity.

Do not complete a milestone with disconnected screens. Each milestone requires at least one production-ready vertical workflow, reconciliation, telemetry, runbook, migration, and business-owner sign-off.

## 11. Platform acceptance

The Liberu business platform is ready when:

- every authoritative record has one owner and no platform package duplicates a product module;
- all selected packages install, enable, upgrade, disable, and recover according to `MODULES.md`;
- the primary workflows reconcile customer, provider, operational, and accounting state;
- brand, division, tenant, team, and role isolation hold across UI, API, jobs, search, exports, analytics, and automation;
- financial, contractual, access, publication, outreach, and infrastructure risks enforce approvals and audit;
- leadership metrics reproduce governed source data and drill through to authorized evidence;
- customer/staff/partner/supplier journeys are accessible, localized, observable, documented, and supported by runbooks;
- backups restore, provider outages degrade safely, failed workflows can be replayed, and releases can roll back.

Each composition table row maps to repository adoption issues. Each workflow maps to a cross-repository epic with child issues in the owning package repositories.
