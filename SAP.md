# Liberu Enterprise Resource Planning

## Product Scope

**Purpose:** SAP-style modular ERP for multi-company software, hosting, managed-service, consulting, SaaS, and hybrid enterprises.
**Architecture:** This product composes modules under [MODULES.md](MODULES.md); enterprise APIs, integrations, and events follow [API.md](API.md); all experiences follow [THEMES.md](THEMES.md). [LIBERU.md](LIBERU.md) remains the platform overview.

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md); this scope composes enterprise domain behavior only.

## Outcomes

- Provide traceable enterprise operations from strategy and demand through delivery, finance, people, assets, risk, and reporting.
- Maintain governed master data and one authoritative owner for each business record.
- Support legal entities, business units, divisions, branches, cost/profit centers, projects, currencies, locales, and intercompany operations.

## Module plan

| Domain | Modules and responsibilities |
|---|---|
| Enterprise Foundation | Organization hierarchy, legal entities, master data, dimensions, workflow, approvals, documents, audit, and localization |
| Finance | General ledger, receivables, payables, banking, tax, assets, budgets, treasury, consolidation, close, and statements |
| Controlling | Cost/profit centers, internal orders, allocation, planning, variance, unit economics, and profitability |
| Sales and CRM | Accounts, leads, opportunities, quotes, contracts, orders, customer success, communications, and forecasts |
| Revenue Operations | Catalog, pricing, subscriptions, usage, licensing, billing, payments, collections, and revenue schedules |
| Procurement | Requisitions, sourcing, suppliers, approvals, purchase orders, receipts, invoices, contracts, and spend analysis |
| Inventory and Logistics | Items, warehouses, stock ledger, lots/serials, transfers, reservations, fulfillment, and valuation |
| Projects and Services | Portfolios, projects, resources, skills, time, expenses, milestones, risks, delivery, and profitability |
| Service Management | Catalog, requests, incidents, problems, changes, knowledge, CMDB, SLA, and field service |
| Hosting and Cloud | Services, subscriptions, provisioning, infrastructure inventory, domains/DNS, capacity, usage, and operations |
| Product and Engineering | Products, roadmaps, requirements, releases, licenses, repositories, issues, CI/CD links, and support feedback |
| People | Workforce records, recruitment, onboarding, skills, absence, performance, learning, compensation, and payroll interfaces |
| Assets and Facilities | Asset lifecycle, maintenance, leases, locations, facilities, energy, safety, and disposal |
| Governance, Risk and Compliance | Policies, controls, risks, audits, evidence, incidents, privacy, security, continuity, and regulatory obligations |
| Partners and Portals | Suppliers, resellers, partners, customers, employees, delegated self-service, documents, and collaboration |
| Data and Intelligence | Governed metrics, semantic models, reports, planning, forecasts, data quality, lineage, exports, and AI assistance |

## Enterprise model and master data

- Model enterprise → legal entity → business unit/division/department/team, plus branch, location, cost center, profit center, project, warehouse, data center, and cloud region.
- Govern customers, suppliers, people, products/services, items, assets, contracts, accounts, currencies, tax identifiers, addresses, and organizational dimensions.
- Support draft/review/approve/effective/retired lifecycle, duplicate detection, survivorship, stewardship, change history, and cross-module stable identifiers.
- Support intercompany sale/purchase/service, transfer pricing, settlement, matching, elimination, and consolidated reporting.

## Required end-to-end workflows

1. **Lead to cash:** lead → opportunity → quote → contract → order/subscription → delivery/provisioning → invoice → payment → accounting/revenue.
2. **Source to pay:** demand → requisition → budget/approval → sourcing/order → receipt → invoice match → payment → accounting/supplier performance.
3. **Project to profit:** scope → plan/resource → deliver/time/expense → milestone acceptance → bill/revenue → cost allocation → profitability.
4. **Incident to improvement:** alert/request → incident → SLA/escalation → resolution → problem/change → knowledge/control improvement.
5. **Hire to retire:** requisition → recruit → onboard → assign equipment/access → develop/compensate → offboard → revoke/recover/archive.
6. **Record to report:** operational postings → subledger reconciliation → allocations/adjustments → entity close → intercompany elimination → consolidation → statements.
7. **Asset lifecycle:** request → procure/build → receive/capitalize → assign/operate/maintain → impair/transfer → dispose → financial and compliance closure.

Each workflow defines accountable owner, master/source records, states, approvals, controls, segregation of duties, events, accounting impact, SLA, exceptions, compensation, and metrics.

## Product requirements

- Compose existing Liberu product modules instead of reproducing CRM, Billing, Accounting, Control Panel, Ecommerce, or Maintenance logic.
- Provide configurable state machines, approvals, delegation, escalation, business calendars, effective dating, and immutable decision evidence.
- Use governed read models for cross-domain reporting; operational modules retain write ownership.
- Support multi-company/currency/language/timezone, regional policy packs, document numbering, and local statutory extensions.
- Provide versioned APIs/events, bulk import/export with dry run, integration monitoring, replay, and reconciliation.
- Offer role-specific workspaces for executives, finance, sales, procurement, service, projects, HR, engineers, partners, and customers.
- Make automation and AI advisory by default, permission-bounded, explainable, costed, and approval-gated for material decisions.

## Integrations

Banks, payment/tax/payroll providers, e-invoicing networks, procurement catalogs, logistics, identity, e-signature, telephony, marketplaces, GitHub/CI, infrastructure clouds, monitoring, office suites, and data platforms integrate through the Integration Hub with scoped credentials and reconciliation.

## Quality, control, and operations gates

- Establish control matrices for financial close, payments, procurement, master data, payroll interfaces, infrastructure actions, privacy, and access.
- Test cross-module contract versions, tenant/entity isolation, intercompany balance, monetary precision, approval races, duplicate events, period locks, and provider outages.
- Maintain data lineage from reports to governed sources and reconcile every financial/operational subledger.
- Define SLOs, continuity tiers, backups, restore drills, disaster recovery, regional retention, legal holds, and audit exports.
- Require threat models and segregation of duties for privileged workflows; log break-glass use and review it promptly.

## Delivery phases

1. Enterprise Foundation, organization/master data, Identity, Authorization, Workflow, Audit, documents, and Integration Hub.
2. Finance/Controlling plus CRM-to-order-to-billing/accounting vertical slice.
3. Procurement, inventory, projects/services, service management, and asset/maintenance vertical slices.
4. People, partners/portals, hosting/cloud and engineering integration, consolidation, and GRC.
5. Advanced planning, semantic reporting, optimization, regional packs, and governed AI assistance.

Every phase delivers complete workflows, controls, reconciliations, reports, migration, telemetry, and runbooks—not isolated menus.

## Definition of done

The ERP is ready when master data has clear ownership; end-to-end workflows reconcile operational, financial, and provider state; entity and role controls hold; reports have lineage; failures recover safely; and each domain/module can be planned as a GitHub epic with measurable acceptance criteria.
