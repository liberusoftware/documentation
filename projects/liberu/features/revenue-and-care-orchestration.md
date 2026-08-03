# Liberu: Revenue and Care Orchestration

**Domain module:** `module-liberu-revenue-and-care-orchestration`
**Status:** Liberu-specific cross-product capability
**Architecture:** [LIBERU](../../LIBERU.md) · [CRM](../../crm/CRM.md) · [Modules](../../../architecture/MODULES.md)

## Purpose

This module turns authoritative CRM, CMS, Billing, Control Panel, Ecommerce, Maintenance, Projects, and Automation events into explainable customer-health projections and safe next actions. It coordinates the Liberu hosting and professional-services journey without duplicating customer, case, invoice, subscription, infrastructure, project, or AI records.

## Business capabilities

- Customer health constellation with source, confidence, owner, expiry, and drill-through evidence.
- Revenue-aware service recovery for incidents, provisioning failures, entitlement gaps, renewal risk, and overdue commercial actions.
- Contact-protection ledger that blocks automated outreach until `next_contact_at`, conversion, explicit reply/request, or approved exception.
- Cross-brand consent and quiet-hour evaluation for Liberu websites, campaigns, sales, support, and success.
- Approval-gated AI recommendations for triage, summaries, drafts, next-best action, and recovery plays.
- Mobile-ready daily queues for sales, support, on-call, and managers.

## Invariants and events

Health signals are immutable observations and can expire; projections never overwrite source records. An outreach decision must cite the policy version and reason. Service recovery must retain the source incident/job ID and owning module. AI output is advisory until an authorized action accepts it. Publish `HealthSignalObserved`, `CareRiskDetected`, `OutreachDeferred`, `RecoveryCaseRequested`, and `AiRecommendationAccepted` after commit through the outbox.

## Non-goals

CRM remains authoritative for people, relationships, cases, activities, consent, and dialer behavior. Billing/Ecommerce remain authoritative for money and orders. Control Panel remains authoritative for infrastructure. Automation remains authoritative for the generic workflow and AI runtime.

## Acceptance

Test cross-module correlation, stale signals, duplicate/replayed events, consent withdrawal, outreach cooling-off, incident-to-case handoff, tenant/brand isolation, AI approval, provider outage, offline mobile recovery, and explainable audit trails.
