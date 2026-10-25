# Projects and services: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **delivery board, timesheet/expense approval, milestone evidence, billing readiness, margin drill-down** for the intended business tasks. Reuse CRM project/resource planning, Maintenance labor/time, Billing project charging, and Accounting cost dimensions where contracts fit. Enterprise coordinates accepted delivery and profitability views.

Business lifecycle: planned → in_progress → submitted → accepted → billing_requested → billed → reconciled; disputed and rework preserve the submission history.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `accepted` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `request-billing` action using `contract_version`, `time_expense_snapshot_id`, `billing_rule_version`, `customer_acceptance_id`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require accepted scope, approved time/expenses, valid billing terms and customer/delegate evidence. Preserve the accepted snapshot across retries.
5. Submit once and retain the displayed operation/result reference. Link the Billing invoice reference and reconcile its basis. A billing request can pass through billing_requested before confirmed invoicing.
6. Confirm the authoritative outcome and any remaining obligations. `billed` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Project staff submit work; project/customer delegates accept deliverables; billing and finance retain their separate authorities.

A rejected milestone returns to rework as a new submission version. If billing times out, reconcile by milestone operation identity before sending again.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/projects-and-services.md), [API example](../../../../projects/sap/api/projects-and-services.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
