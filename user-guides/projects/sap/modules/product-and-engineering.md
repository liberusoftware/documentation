# Product and engineering: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **release checklist, requirement/test traceability, artifact comparison, rollout timeline, support readiness** for the intended business tasks. Keep repositories, CI execution, and issue records in their owning engineering systems. Reuse CRM product/support context and licensing/billing contracts; enterprise owns governed release evidence and product outcome links.

Business lifecycle: draft → evidence_pending → review_ready → approved → rolling_out → released; rejected and rolled_back retain artifact references.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `review_ready` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `approve` action using `artifact_digest`, `test_evidence_ids`, `vulnerability_review_id`, `rollout_plan_id`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Bind approval to the immutable artifact, required test/security evidence and rollout readiness. Changed or expired evidence invalidates the review instead of carrying approval to another artifact.
5. Submit once and retain the displayed operation/result reference. Record release authorization for this artifact. Actual deployment, rollout results and rollback evidence remain separately reported operations.
6. Confirm the authoritative outcome and any remaining obligations. `approved` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Engineers submit evidence; product/security owners approve their controls; release managers authorize deployment under policy.

Missing, expired, or mismatched evidence blocks approval. Preserve rollout failures and rollback outcomes against the original release digest for support and audit.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/product-and-engineering.md), [API example](../../../../projects/sap/api/product-and-engineering.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
