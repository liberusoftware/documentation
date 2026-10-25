# Finance: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **posting exception inbox, journal evidence, source-to-ledger reconciliation, close checklist, consolidation status** for the intended business tasks. Accounting owns ledger accounts, journal posting, periods, reconciliation, close, and consolidation. The enterprise workspace coordinates source operations and unresolved handoffs.

Business lifecycle: received → validated → pending_approval → posted; validation_failed and rejected preserve the source reference; posted corrections use a linked reversal.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `pending_approval` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `post` action using `approval_reference`, `source_operation_key`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Validate the approved source version, entity/ledger/period, balanced totals, dimensions, exchange-rate reference and source operation uniqueness through Accounting.
5. Submit once and retain the displayed operation/result reference. Complete only after Accounting returns the durable journal reference and reconciled control totals. A queued request cannot be displayed as a posted journal.
6. Confirm the authoritative outcome and any remaining obligations. `posted` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Preparers submit; independent approvers authorize journals and reopening; read access is scoped by ledger and legal entity.

For a timeout after posting, query by source operation identity before retrying. Reconcile the returned journal and control totals; a posted journal is never silently edited or deleted.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/finance.md), [API example](../../../../projects/sap/api/finance.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
