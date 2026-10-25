# Projects and services: Filament design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/projects-and-services.md) and [API plan](../api/projects-and-services.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#projects-and-services). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse CRM project/resource planning, Maintenance labor/time, Billing project charging, and Accounting cost dimensions where contracts fit. Enterprise coordinates accepted delivery and profitability views.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** delivery board, timesheet/expense approval, milestone evidence, billing readiness, margin drill-down.

**Business lifecycle:** planned → in_progress → submitted → accepted → billing_requested → billed → reconciled; disputed and rework preserve the submission history.

Freeze the accepted scope and billing basis. Do not bill unapproved time/expenses or claim milestone acceptance without the required customer/delegate evidence. Keep cost attribution separate from access to personal labor details.

The illustrated `request-billing` command takes `contract_version`, `time_expense_snapshot_id`, `billing_rule_version`, `customer_acceptance_id`, with a documented record-version precondition and scoped operation identity. It starts from `accepted` and reaches `billed` only after its defined business outcome. The [API example](../api/projects-and-services.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/projects-and-services.request.schema.json).

Require accepted scope, approved time/expenses, valid billing terms and customer/delegate evidence. Preserve the accepted snapshot across retries.

Link the Billing invoice reference and reconcile its basis. A billing request can pass through billing_requested before confirmed invoicing.

## Layer implementation

Compose a scoped work queue and detail/evidence page for the workspace above. Recommended queue columns are subject/source reference, active legal entity, business state, operation state, responsible owner and last transition/attempt time. Filter authorized records before counts, search, exports and relationships.

Implement `request-billing` as an explicit authorized action/form using `contract_version`, `time_expense_snapshot_id`, `billing_rule_version`, `customer_acceptance_id`. Load permitted options from owning queries; keep protected IDs and final state fields outside editable form state. Validate at the form boundary for feedback and again in the public core/API command.

A generic resource save or a status dropdown must not bypass the transition use case. Resolve the current record/version and policy again when handling the action. Display a review summary/evidence when the domain approval policy requires it; do not infer approval from a hidden button or navigation permission.

Bulk operations preview eligible/skipped rows and retain each record's version and command identity. Show per-record completion/conflict/failure rather than a blanket success toast. Queue large exports/actions and preserve authorized result/evidence links.

## Authorization, recovery and operations

Project staff submit work; project/customer delegates accept deliverables; billing and finance retain their separate authorities.

A rejected milestone returns to rework as a new submission version. If billing times out, reconcile by milestone operation identity before sending again.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- Rejected time is excluded from the billable snapshot; duplicate acceptance cannot double-bill; a contract change cannot rewrite an already billed milestone.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `request-billing` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `billed` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
