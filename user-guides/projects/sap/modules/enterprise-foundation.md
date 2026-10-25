# Enterprise foundation: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **stewardship queue, before/after comparison, entity hierarchy, effective-date preview, consumer adoption status** for the intended business tasks. Reuse foundation identity, teams, policies, audit, files, and localization. Enterprise owns legal-entity mappings, stewardship, and effective-dated master-data approval, not another user directory.

Business lifecycle: draft → submitted → approved → scheduled → applied; rejected and superseded are explicit outcomes.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `submitted` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `approve` action using `decision_evidence_ids`, `effective_from`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require accessible evidence, a valid effective interval and an independent approver when the policy requires separation. Reject an overlapping approved version rather than replacing it.
5. Submit once and retain the displayed operation/result reference. Record the approved master-data version and decision evidence. Application to consumers is a separately observable handoff, not proof that all consumers have adopted it.
6. Confirm the authoritative outcome and any remaining obligations. `approved` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Proposer edits drafts; steward reviews; independent approver authorizes; integration identity applies only approved versions.

A rejected consumer update leaves the change in an actionable partial-application state. Correct the mapping and retry the same handoff identity; do not create a second master record.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/enterprise-foundation.md), [API example](../../../../projects/sap/api/enterprise-foundation.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
