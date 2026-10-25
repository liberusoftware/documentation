# Product and engineering: core composition design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/product-and-engineering.md) and [API plan](../api/product-and-engineering.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#product-and-engineering). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Keep repositories, CI execution, and issue records in their owning engineering systems. Reuse CRM product/support context and licensing/billing contracts; enterprise owns governed release evidence and product outcome links.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** release checklist, requirement/test traceability, artifact comparison, rollout timeline, support readiness.

**Business lifecycle:** draft → evidence_pending → review_ready → approved → rolling_out → released; rejected and rolled_back retain artifact references.

Bind approval to immutable artifact and evidence versions. Invalidate readiness when the artifact changes. Do not infer deployment success from a green build or modify source repositories through a reporting projection.

The illustrated `approve` command takes `artifact_digest`, `test_evidence_ids`, `vulnerability_review_id`, `rollout_plan_id`, with a documented record-version precondition and scoped operation identity. It starts from `review_ready` and reaches `approved` only after its defined business outcome. The [API example](../api/product-and-engineering.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/product-and-engineering.request.schema.json).

Bind approval to the immutable artifact, required test/security evidence and rollout readiness. Changed or expired evidence invalidates the review instead of carrying approval to another artifact.

Record release authorization for this artifact. Actual deployment, rollout results and rollback evidence remain separately reported operations.

## Layer implementation

Use an explicit application use case for each reviewed transition. Inputs are authenticated actor/service context, authorized tenant/entity/subject references, expected subject version, scoped operation identity and a typed command DTO. Browser/request fields do not replace this trusted context.

The public result distinguishes validation/permission/stale-state rejection, a committed local decision and an accepted asynchronous operation. Publish only permitted DTO fields and evidence references; Eloquent models and upstream private tables are not the cross-module contract.

**Domain context fields:** `product_reference`, `release_version`, `artifact_digest`, `requirement_snapshot_id`, `test_evidence_ids`, `vulnerability_review_id`, `rollout_plan_id`, `support_readiness_id`. These are design inputs/references, not a mandate to duplicate complete upstream records. Preserve owner identifiers and immutable decision/source snapshots where needed.

Store enterprise-owned orchestration changes transactionally and record outbox work with them. The shared operation journal owns delivery state; the business owner owns the actual transition. Use the owner concurrency contract for upstream writes and reconcile its acknowledgement before advancing a final outcome.

Ingest signed/verified build and deployment events from approved connectors; publish released product/version references to licensing, support and service catalog consumers.

Migrations apply only to newly owned operation/projection state. Plan backfills, indexes, constraints, retention/holds and recovery without renaming or deleting another owner's records. Financial corrections use the owner reversal workflow; identity/access changes retain their revocation acknowledgements.

## Authorization, recovery and operations

Engineers submit evidence; product/security owners approve their controls; release managers authorize deployment under policy.

Missing, expired, or mismatched evidence blocks approval. Preserve rollout failures and rollback outcomes against the original release digest for support and audit.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- An artifact digest change invalidates approval; duplicate CI notifications do not create duplicate releases; rollback preserves the original release record.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `approve` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `approved` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
