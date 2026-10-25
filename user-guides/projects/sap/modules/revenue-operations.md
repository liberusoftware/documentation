# Revenue operations: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **usage completeness dashboard, rating explanation, invoice preview, dispute timeline, settlement reconciliation** for the intended business tasks. Billing owns subscriptions, usage rating, invoices, and collections; Accounting owns financial recognition and postings. Enterprise coordinates source usage completeness and cross-entity revenue evidence.

Business lifecycle: collecting → validated → rated → approved → invoiced → reconciled; disputed settlements retain the original calculation.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `approved` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `finalize` action using `usage_window`, `source_event_watermark`, `pricing_version`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require a closed reviewed usage window, deduplicated source events, explicit units/timezone and the approved rating/pricing snapshot. Late usage follows the correction policy.
5. Submit once and retain the displayed operation/result reference. Billing owns invoice finalization and returns its reference. Financial revenue recognition remains Accounting-owned and is not implied by invoicing.
6. Confirm the authoritative outcome and any remaining obligations. `invoiced` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Meter operators submit scoped usage; billing specialists approve adjustments; finance owns recognition policy and postings.

Late or corrected usage creates an adjustment referencing the original settlement. Preserve invoice finality and route disputes through Billing correction workflows.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/revenue-operations.md), [API example](../../../../projects/sap/api/revenue-operations.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
