# Liberu Maintenance

## Product Scope

**Purpose:** Asset, work order, preventative maintenance, inspection, field service, inventory, contract, and compliance management.
**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); field, customer, provider, and device APIs follow [API.md](../../architecture/API.md); office, engineer, and customer experiences follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines maintenance behavior only.

## Outcomes

- Preserve the complete service history, condition, cost, and compliance status of every maintained asset.
- Plan and dispatch preventative and reactive work with parts, skills, SLA, and safety constraints.
- Let engineers work reliably on mobile devices and in intermittent connectivity.

## Module plan

| Module                   | Responsibilities                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------- |
| Maintenance Core         | Organizations, service settings, statuses, numbering, priorities, and shared events                |
| Customers and Sites      | Customers, contacts, sites, locations, access details, hazards, and service windows                |
| Assets                   | Hierarchies, categories, specifications, meters, warranties, condition, QR/barcodes, and history   |
| Work Orders              | Requests, triage, jobs, tasks, status machine, dependencies, notes, evidence, and completion       |
| Scheduling               | Calendars, skills, territories, shifts, availability, travel, dispatch, and conflict handling      |
| Preventative Maintenance | Plans, triggers, frequencies, meter rules, forecasts, generation, and optimization                 |
| Inspections              | Templates, conditional checklists, readings, failures, signatures, certificates, and follow-up     |
| Inventory                | Parts, warehouses/vans, stock ledger, reservations, issues/returns, transfers, reorder, and counts |
| Procurement              | Suppliers, requests, approvals, purchase orders, receipts, returns, and cost allocation            |
| Labor and Time           | Engineer skills, attendance, time entries, rates, expenses, and approval                           |
| Commercial               | Quotes, contracts, covered assets/services, rates, renewals, SLA, and billable lines               |
| Compliance               | Requirements, permits, risk assessments, incidents, corrective actions, evidence, and expiry       |
| Portals                  | Customer requests/approvals/status and engineer schedule/work/offline capture                      |
| Reporting                | Backlog, response, first-time fix, downtime, cost, utilization, stock, SLA, and compliance metrics |

## Required workflows

1. **Reactive job:** request → triage/priority/SLA → plan → dispatch → travel/work/parts → evidence/sign-off → review → billing.
2. **Preventative job:** due forecast → generate → group/plan → assign → perform checklist/readings → create failures/follow-ups → reset schedule.
3. **Inspection failure:** capture result → assess criticality → make safe → notify/escalate → corrective work → verify and close.
4. **Parts:** reserve → issue to job/van → consume/return → update ledger/cost → reorder/procure → reconcile count.
5. **Offline engineer:** securely sync assignment → capture work locally → resolve version conflicts → upload evidence → confirm server acceptance.

## Product requirements

- Support multi-site asset hierarchies, components, warranties, meters, maintenance strategies, and full lifecycle history.
- Enforce valid work-order transitions, mandatory safety/evidence/signature fields, and immutable completion history.
- Schedule by skills, certification, territory, availability, duration, travel, priority, parts, and customer windows.
- Calculate SLA clocks using calendars, pauses, priorities, contract terms, and auditable exceptions.
- Use stock ledgers and preserve part/labor/expense cost snapshots on jobs.
- Provide accessible desktop and mobile interfaces with camera, signature, QR/barcode, maps, and offline queues.

## Integrations

Accounting/Billing, CRM, calendars, maps/routing, email/SMS, IoT/meter feeds, procurement, document storage, identity, and external contractors integrate through events and replaceable drivers.

## Quality and control gates

- Test scheduling conflicts, SLA boundaries, recurrence, meter rollover, offline conflict resolution, stock concurrency, job reopen, and tenant/site isolation.
- Protect site access, safety, customer, location, and engineer data; retain compliance evidence under explicit policies.
- Validate QR/barcode authorization and prevent identifiers from granting access by themselves.
- Alert on overdue critical work, certification/contract expiry, SLA risk, stock shortage, failed sync, and compliance gaps.

## Delivery phases

1. Core, Customers/Sites, Assets, Work Orders, Scheduling, engineer portal, notifications, and basic reporting.
2. Preventative Maintenance, Inspections, parts/inventory, time, documents/media, QR/barcodes, and customer portal.
3. Contracts/SLA, quotes/billing, procurement, compliance, offline mode, and integration depth.
4. IoT/predictive inputs, optimization, contractor network, and advanced analytics.

## Definition of done

Reactive and planned work is schedulable, executable online/offline, safety-controlled, evidenced, costed, SLA-traceable, and billable; asset and stock histories reconcile. Each module becomes a GitHub epic.

## Product Scope

**Purpose:** Asset, work order, preventative maintenance, inspection, field service, inventory, contract, and compliance management.
**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); field, customer, provider, and device APIs follow [API.md](../../architecture/API.md); office, engineer, and customer experiences follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines maintenance behavior only.

## Outcomes

- Preserve the complete service history, condition, cost, and compliance status of every maintained asset.
- Plan and dispatch preventative and reactive work with parts, skills, SLA, and safety constraints.
- Let engineers work reliably on mobile devices and in intermittent connectivity.

## Module plan

| Module                   | Responsibilities                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------- |
| Maintenance Core         | Organizations, service settings, statuses, numbering, priorities, and shared events                |
| Customers and Sites      | Customers, contacts, sites, locations, access details, hazards, and service windows                |
| Assets                   | Hierarchies, categories, specifications, meters, warranties, condition, QR/barcodes, and history   |
| Work Orders              | Requests, triage, jobs, tasks, status machine, dependencies, notes, evidence, and completion       |
| Scheduling               | Calendars, skills, territories, shifts, availability, travel, dispatch, and conflict handling      |
| Preventative Maintenance | Plans, triggers, frequencies, meter rules, forecasts, generation, and optimization                 |
| Inspections              | Templates, conditional checklists, readings, failures, signatures, certificates, and follow-up     |
| Inventory                | Parts, warehouses/vans, stock ledger, reservations, issues/returns, transfers, reorder, and counts |
| Procurement              | Suppliers, requests, approvals, purchase orders, receipts, returns, and cost allocation            |
| Labor and Time           | Engineer skills, attendance, time entries, rates, expenses, and approval                           |
| Commercial               | Quotes, contracts, covered assets/services, rates, renewals, SLA, and billable lines               |
| Compliance               | Requirements, permits, risk assessments, incidents, corrective actions, evidence, and expiry       |
| Portals                  | Customer requests/approvals/status and engineer schedule/work/offline capture                      |
| Reporting                | Backlog, response, first-time fix, downtime, cost, utilization, stock, SLA, and compliance metrics |

## Required workflows

1. **Reactive job:** request → triage/priority/SLA → plan → dispatch → travel/work/parts → evidence/sign-off → review → billing.
2. **Preventative job:** due forecast → generate → group/plan → assign → perform checklist/readings → create failures/follow-ups → reset schedule.
3. **Inspection failure:** capture result → assess criticality → make safe → notify/escalate → corrective work → verify and close.
4. **Parts:** reserve → issue to job/van → consume/return → update ledger/cost → reorder/procure → reconcile count.
5. **Offline engineer:** securely sync assignment → capture work locally → resolve version conflicts → upload evidence → confirm server acceptance.

## Product requirements

- Support multi-site asset hierarchies, components, warranties, meters, maintenance strategies, and full lifecycle history.
- Enforce valid work-order transitions, mandatory safety/evidence/signature fields, and immutable completion history.
- Schedule by skills, certification, territory, availability, duration, travel, priority, parts, and customer windows.
- Calculate SLA clocks using calendars, pauses, priorities, contract terms, and auditable exceptions.
- Use stock ledgers and preserve part/labor/expense cost snapshots on jobs.
- Provide accessible desktop and mobile interfaces with camera, signature, QR/barcode, maps, and offline queues.

## Integrations

Accounting/Billing, CRM, calendars, maps/routing, email/SMS, IoT/meter feeds, procurement, document storage, identity, and external contractors integrate through events and replaceable drivers.

## Quality and control gates

- Test scheduling conflicts, SLA boundaries, recurrence, meter rollover, offline conflict resolution, stock concurrency, job reopen, and tenant/site isolation.
- Protect site access, safety, customer, location, and engineer data; retain compliance evidence under explicit policies.
- Validate QR/barcode authorization and prevent identifiers from granting access by themselves.
- Alert on overdue critical work, certification/contract expiry, SLA risk, stock shortage, failed sync, and compliance gaps.

## Delivery phases

1. Core, Customers/Sites, Assets, Work Orders, Scheduling, engineer portal, notifications, and basic reporting.
2. Preventative Maintenance, Inspections, parts/inventory, time, documents/media, QR/barcodes, and customer portal.
3. Contracts/SLA, quotes/billing, procurement, compliance, offline mode, and integration depth.
4. IoT/predictive inputs, optimization, contractor network, and advanced analytics.

## Definition of done

Reactive and planned work is schedulable, executable online/offline, safety-controlled, evidenced, costed, SLA-traceable, and billable; asset and stock histories reconcile. Each module becomes a GitHub epic.
