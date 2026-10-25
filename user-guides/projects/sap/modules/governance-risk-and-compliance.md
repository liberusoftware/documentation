# Governance, risk and compliance: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **control library, risk register, evidence request inbox, finding/remediation timeline, audit-ready export preview** for the intended business tasks. Reuse foundation audit, documents, policy and notification contracts. Enterprise owns control/risk relationships, assessments, evidence review and remediation oversight without overwriting source audit events.

Business lifecycle: planned → evidence_requested → under_review → accepted → closed; deficient and reopened preserve reviewer findings.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `under_review` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `record-finding` action using `control_reference`, `finding_summary`, `evidence_references`, `remediation_owner_reference`, `due_at`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require independent review authority, accessible immutable evidence and a valid remediation owner. Preserve control/framework version and legal-hold/retention obligations.
5. Submit once and retain the displayed operation/result reference. Record the finding and linked remediation obligation without changing the original source audit evidence. Remediation acceptance is a distinct reviewed action.
6. Confirm the authoritative outcome and any remaining obligations. `deficient` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Control owners submit; independent reviewers assess; auditors receive scoped read/export access; legal holds require designated authority.

Expired or unavailable evidence reopens the review obligation. Retries preserve evidence provenance and do not replace the original assessment result invisibly.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/governance-risk-and-compliance.md), [API example](../../../../projects/sap/api/governance-risk-and-compliance.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
