# Procurement: core composition design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/procurement.md) and [API plan](../api/procurement.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#procurement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse supplier/master-data contracts, Maintenance purchasing where compatible, and Accounting receipt/payable contracts. Enterprise owns cross-entity sourcing, approval and matching orchestration only where those are genuine gaps.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** requisition form, approval queue, purchase order timeline, receipt capture, three-way matching exceptions.

**Business lifecycle:** draft → submitted → approved → ordered → partially_received → received → matched → closed; rejected and cancelled are explicit branches.

Separate requester, approver, receiver, and payment authority as policy requires. Enforce budget/approval thresholds, quantity and price tolerances, approved supplier status, and partial receipt accounting.

The illustrated `record-receipt` command takes `order_reference`, `receipt_reference`, `received_at`, `lines`, with a documented record-version precondition and scoped operation identity. It starts from `ordered` and reaches `partially_received` only after its defined business outcome. The [API example](../api/procurement.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/procurement.request.schema.json).

Validate the receiving actor/location, order line, units and quantity/tolerance policy. The owning stock/receipt service records physical movements; reject duplicate receipt identities.

Link the receipt and outstanding quantities. A partial receipt does not close the order or release an unmatched supplier invoice for payment.

## Layer implementation

Use an explicit application use case for each reviewed transition. Inputs are authenticated actor/service context, authorized tenant/entity/subject references, expected subject version, scoped operation identity and a typed command DTO. Browser/request fields do not replace this trusted context.

The public result distinguishes validation/permission/stale-state rejection, a committed local decision and an accepted asynchronous operation. Publish only permitted DTO fields and evidence references; Eloquent models and upstream private tables are not the cross-module contract.

**Domain context fields:** `legal_entity_id`, `supplier_reference`, `requester_id`, `cost_center_id`, `currency`, `lines`, `budget_reference`, `approval_policy_version`, `required_by`. These are design inputs/references, not a mandate to duplicate complete upstream records. Preserve owner identifiers and immutable decision/source snapshots where needed.

Store enterprise-owned orchestration changes transactionally and record outbox work with them. The shared operation journal owns delivery state; the business owner owns the actual transition. Use the owner concurrency contract for upstream writes and reconcile its acknowledgement before advancing a final outcome.

Physical stock owners record inventory movements; Accounting owns payable and journal results. Match order, receipt, and supplier invoice references without creating another payable ledger.

Migrations apply only to newly owned operation/projection state. Plan backfills, indexes, constraints, retention/holds and recovery without renaming or deleting another owner's records. Financial corrections use the owner reversal workflow; identity/access changes retain their revocation acknowledgements.

## Authorization, recovery and operations

Requesters manage own drafts; approvers act within delegated limits; receivers record quantities; AP handles invoice disputes.

Hold unmatched or over-tolerance invoices with actionable discrepancies. A supplier timeout leaves an order handoff pending; query/retry by identity before issuing another order.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A requester cannot approve their own requisition under separation policy; partial receipts do not close the order; an over-tolerance invoice remains held.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `record-receipt` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `partially_received` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
