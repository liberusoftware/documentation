# Product and engineering: Flutter design

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

Use Dart DTOs and explicit widget/navigation state for a focused mobile queue/detail/evidence and `approve` review workflow. The host Flutter application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

Resolve the selected entity and permitted subject through the reviewed API. The command body uses `artifact_digest`, `test_evidence_ids`, `vulnerability_review_id`, `rollout_plan_id`; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.

Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.

For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.

Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.

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
