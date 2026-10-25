# Sales and CRM: Filament design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/sales-and-crm.md) and [API plan](../api/sales-and-crm.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-and-crm). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

CRM owns customer relationships, opportunities, quotes, and contracts. Billing or Ecommerce owns the accepted commercial order according to the deployment; enterprise owns the governed handoff.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** opportunity-to-order workspace, accepted quote comparison, approval evidence, handoff exception queue.

**Business lifecycle:** prepared → approved → submitted → accepted; rejected and needs_review retain downstream reasons.

An accepted quote snapshot cannot be silently changed during handoff. Resolve the authoritative customer and order owner, approved pricing/tax treatment, and seller entity before submission.

The illustrated `submit` command takes `quote_version`, `target_order_owner`, `acceptance_evidence_id`, with a documented record-version precondition and scoped operation identity. It starts from `approved` and reaches `accepted` only after its defined business outcome. The [API example](../api/sales-and-crm.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/sales-and-crm.request.schema.json).

Require a current accepted quote snapshot, authorized seller entity, resolvable customer/product mappings and a reviewed target order owner. Revalidate expired or superseded commercial terms.

Link the accepted downstream order/subscription reference. A timeout remains pending until queried or reconciled using the original handoff identity.

## Layer implementation

Compose a scoped work queue and detail/evidence page for the workspace above. Recommended queue columns are subject/source reference, active legal entity, business state, operation state, responsible owner and last transition/attempt time. Filter authorized records before counts, search, exports and relationships.

Implement `submit` as an explicit authorized action/form using `quote_version`, `target_order_owner`, `acceptance_evidence_id`. Load permitted options from owning queries; keep protected IDs and final state fields outside editable form state. Validate at the form boundary for feedback and again in the public core/API command.

A generic resource save or a status dropdown must not bypass the transition use case. Resolve the current record/version and policy again when handling the action. Display a review summary/evidence when the domain approval policy requires it; do not infer approval from a hidden button or navigation permission.

Bulk operations preview eligible/skipped rows and retain each record's version and command identity. Show per-record completion/conflict/failure rather than a blanket success toast. Queue large exports/actions and preserve authorized result/evidence links.

## Authorization, recovery and operations

Account teams propose; commercial approvers authorize within value/entity limits; destination services independently authorize acceptance.

If quote validity expires or the destination rejects a product mapping, request review and prepare a new version. Retry a network failure under the original handoff identity.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- An expired or superseded quote cannot be accepted; a retry returns the same downstream order; unauthorized customer details are absent from projections.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `submit` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `accepted` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
