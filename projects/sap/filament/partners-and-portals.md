# Partners and portals: Filament design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/partners-and-portals.md) and [API plan](../api/partners-and-portals.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#partners-and-portals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse foundation identity/policy, CRM partner/account relationships, and product-owned self-service APIs. Enterprise owns scoped delegation and cross-product portal composition, not copied customer/supplier ledgers.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** partner onboarding, delegation review, customer/supplier self-service workspace, access history, revocation status.

**Business lifecycle:** requested → reviewed → active → expired; rejected and revoked are terminal outcomes for the grant version.

Bind delegation to explicit resources, operations, audience and expiry. A partner relationship is not authorization. Invitations and passwordless links need bounded lifetime and non-enumerating failure responses.

The illustrated `revoke` command takes `reason`, `revocation_evidence_reference`, with a documented record-version precondition and scoped operation identity. It starts from `active` and reaches `revoked` only after its defined business outcome. The [API example](../api/partners-and-portals.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/partners-and-portals.request.schema.json).

Require authority over the exact principal/resource scope. A partner relationship alone does not grant revocation or delegation rights across other organizations.

Record revocation and track downstream acknowledgements/session-cache invalidation. Keep delayed revocations visible until protected operations enforce the change.

## Layer implementation

Compose a scoped work queue and detail/evidence page for the workspace above. Recommended queue columns are subject/source reference, active legal entity, business state, operation state, responsible owner and last transition/attempt time. Filter authorized records before counts, search, exports and relationships.

Implement `revoke` as an explicit authorized action/form using `reason`, `revocation_evidence_reference`. Load permitted options from owning queries; keep protected IDs and final state fields outside editable form state. Validate at the form boundary for feedback and again in the public core/API command.

A generic resource save or a status dropdown must not bypass the transition use case. Resolve the current record/version and policy again when handling the action. Display a review summary/evidence when the domain approval policy requires it; do not infer approval from a hidden button or navigation permission.

Bulk operations preview eligible/skipped rows and retain each record's version and command identity. Show per-record completion/conflict/failure rather than a blanket success toast. Queue large exports/actions and preserve authorized result/evidence links.

## Authorization, recovery and operations

Sponsors request limited rights; designated owners approve; external users cannot expand scope or grant rights they do not hold.

A stale portal session must fail the next protected operation after revocation. Surface delayed downstream revocations as outstanding obligations rather than hiding them.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- An expired grant cannot download a previously listed document; changing a resource ID cannot escape scope; revocation reaches active portal workflows.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `revoke` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `revoked` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
