# Service management: Filament design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/service-management.md) and [API plan](../api/service-management.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#service-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse CRM case management, knowledge, SLA/entitlements, and Control Panel monitoring. Enterprise adds cross-product service context, major-incident coordination, and controlled change orchestration where missing.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** triage inbox, incident timeline, sla clock explanation, service impact map, change/knowledge links.

**Business lifecycle:** new → triaged → assigned → investigating → resolved → closed; reopened incidents retain the prior resolution.

Version the priority and SLA basis, define pause conditions and business calendars, and preserve customer-visible communication separately from internal technical notes. Change approval is distinct from incident urgency.

The illustrated `resolve` command takes `resolution_code`, `resolution_summary`, `evidence_references`, `change_reference`, with a documented record-version precondition and scoped operation identity. It starts from `investigating` and reaches `resolved` only after its defined business outcome. The [API example](../api/service-management.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/service-management.request.schema.json).

Require resolution authority and evidence for the selected service/entitlement. Keep customer-visible resolution text separate from restricted internal notes; validate any linked change authority.

Record the resolution and SLA outcome. Closure and any later reopening preserve the earlier resolution evidence and are separate lifecycle actions.

## Layer implementation

Compose a scoped work queue and detail/evidence page for the workspace above. Recommended queue columns are subject/source reference, active legal entity, business state, operation state, responsible owner and last transition/attempt time. Filter authorized records before counts, search, exports and relationships.

Implement `resolve` as an explicit authorized action/form using `resolution_code`, `resolution_summary`, `evidence_references`, `change_reference`. Load permitted options from owning queries; keep protected IDs and final state fields outside editable form state. Validate at the form boundary for feedback and again in the public core/API command.

A generic resource save or a status dropdown must not bypass the transition use case. Resolve the current record/version and policy again when handling the action. Display a review summary/evidence when the domain approval policy requires it; do not infer approval from a hidden button or navigation permission.

Bulk operations preview eligible/skipped rows and retain each record's version and command identity. Show per-record completion/conflict/failure rather than a blanket success toast. Queue large exports/actions and preserve authorized result/evidence links.

## Authorization, recovery and operations

Agents see entitled customer records; incident commanders coordinate; change approvers authorize production changes independently.

Deduplicate repeated alerts into an incident correlation policy. Escalate missed acknowledgements and failed automation visibly; a failed run never marks the incident resolved automatically.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A pause reason affects only permitted SLA clocks; repeated alerts follow correlation policy; restricted internal notes never appear in customer/mobile projections.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `resolve` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `resolved` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
