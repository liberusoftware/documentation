# Controlling: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **rule editor, driver completeness report, allocation preview, variance drill-down, run reconciliation** for the intended business tasks. Reuse Accounting dimensions, budgets, periods, and posted balances. Enterprise controlling owns documented allocation rules, scenario versions, and cross-unit profitability projections where missing.

Business lifecycle: draft → simulated → approved → executing → reconciled; failed and cancelled runs retain their input snapshots.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `draft` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `simulate` action using `rule_version`, `source_balance_snapshot_id`, `driver_snapshot_id`, `scenario_id`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require compatible immutable snapshots and complete allocation drivers. Define zero-driver and rounding-residual behavior; a simulation never posts ledger adjustments.
5. Submit once and retain the displayed operation/result reference. Publish scenario outputs, residuals and source lineage. Approval and actual posting remain separate actions under the owning policy.
6. Confirm the authoritative outcome and any remaining obligations. `simulated` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Analysts simulate; controllers approve rules; posting authority remains with Accounting and the relevant entities.

Partition runs by durable operation IDs. Resume incomplete partitions without reposting completed ones; route unexplained residuals to reconciliation rather than absorbing them silently.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/controlling.md), [API example](../../../../projects/sap/api/controlling.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
