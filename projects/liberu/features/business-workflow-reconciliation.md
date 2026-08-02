# Liberu: Business Workflow Reconciliation

## Canonical independent feature specification

**Domain module:** `liberu-business-workflow-reconciliation`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; it does not replace Billing, Control Panel, CRM, Ecommerce, Accounting, Automation, or Maintenance workflows
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Business Workflow Reconciliation tracks the shared state of composed workflows such as hosting order-to-provisioning, lead-to-revenue, procure-to-pay, and incident-to-resolution. Owning products remain authoritative for each local state and action.

## New capabilities

- **Workflow run registry:** correlate cross-product steps, contracts, events, approvals, actors, and tenant context.
- **State mapping:** declare the expected relationship between source states without copying source records.
- **Reconciliation rules:** detect missing, duplicate, out-of-order, stale, unauthorized, or contradictory transitions.
- **Recovery coordination:** expose retry, replay, compensation, escalation, and manual resolution with idempotency protection.
- **Audit timeline:** provide a permission-filtered evidence trail with correlation IDs, timestamps, contract versions, and responsible owners.

## Boundaries and verification

This module coordinates and reports; it does not mutate another module's private data or bypass its actions. Test duplicate/out-of-order events, partial failure, provider outage, timeout, replay, compensation, wrong-tenant access, manual resolution, and audit redaction.

## Canonical independent feature specification

**Domain module:** `liberu-business-workflow-reconciliation`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; it does not replace Billing, Control Panel, CRM, Ecommerce, Accounting, Automation, or Maintenance workflows
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Business Workflow Reconciliation tracks the shared state of composed workflows such as hosting order-to-provisioning, lead-to-revenue, procure-to-pay, and incident-to-resolution. Owning products remain authoritative for each local state and action.

## New capabilities

- **Workflow run registry:** correlate cross-product steps, contracts, events, approvals, actors, and tenant context.
- **State mapping:** declare the expected relationship between source states without copying source records.
- **Reconciliation rules:** detect missing, duplicate, out-of-order, stale, unauthorized, or contradictory transitions.
- **Recovery coordination:** expose retry, replay, compensation, escalation, and manual resolution with idempotency protection.
- **Audit timeline:** provide a permission-filtered evidence trail with correlation IDs, timestamps, contract versions, and responsible owners.

## Boundaries and verification

This module coordinates and reports; it does not mutate another module's private data or bypass its actions. Test duplicate/out-of-order events, partial failure, provider outage, timeout, replay, compensation, wrong-tenant access, manual resolution, and audit redaction.

## Canonical independent feature specification

**Domain module:** `liberu-business-workflow-reconciliation`  
**Application:** Liberu Business Platform  
**Status:** New cross-product capability; it does not replace Billing, Control Panel, CRM, Ecommerce, Accounting, Automation, or Maintenance workflows  
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Business Workflow Reconciliation tracks the shared state of composed workflows such as hosting order-to-provisioning, lead-to-revenue, procure-to-pay, and incident-to-resolution. Owning products remain authoritative for each local state and action.

## New capabilities

- **Workflow run registry:** correlate cross-product steps, contracts, events, approvals, actors, and tenant context.
- **State mapping:** declare the expected relationship between source states without copying source records.
- **Reconciliation rules:** detect missing, duplicate, out-of-order, stale, unauthorized, or contradictory transitions.
- **Recovery coordination:** expose retry, replay, compensation, escalation, and manual resolution with idempotency protection.
- **Audit timeline:** provide a permission-filtered evidence trail with correlation IDs, timestamps, contract versions, and responsible owners.

## Boundaries and verification

This module coordinates and reports; it does not mutate another module's private data or bypass its actions. Test duplicate/out-of-order events, partial failure, provider outage, timeout, replay, compensation, wrong-tenant access, manual resolution, and audit redaction.
