# People: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **onboarding/offboarding checklist, assignment history, scoped people directory, delegated approvals, outstanding access recovery** for the intended business tasks. Reuse foundation identity/team lifecycle, CRM skills/resource-planning where appropriate, and Accounting payroll integration. People records, employment policy, and sensitive HR data need a separately verified owner.

Business lifecycle: proposed → approved → scheduled → active → ended; withdrawn and suspended preserve effective-date history.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `active` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `end` action using `effective_until`, `offboarding_case_reference`, `access_recovery_policy_version`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require authorized HR context, consistent assignment dates and the applicable offboarding policy. Restrict employment, compensation and other sensitive fields independently of ordinary team membership.
5. Submit once and retain the displayed operation/result reference. End the effective assignment and expose outstanding access/equipment recovery obligations. The employment outcome does not claim all downstream access was successfully revoked.
6. Confirm the authoritative outcome and any remaining obligations. `ended` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

HR manages employment; line managers see approved limited fields; payroll and health-related data use separate restricted policies.

A failed access revocation remains an escalated outstanding obligation. Employment end does not silently claim all downstream access is removed.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/people.md), [API example](../../../../projects/sap/api/people.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
