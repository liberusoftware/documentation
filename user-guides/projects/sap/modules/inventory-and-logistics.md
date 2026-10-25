# Inventory and logistics: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **availability inquiry, transfer planning, pick/dispatch scanning, receipt discrepancy capture, lot traceability** for the intended business tasks. Review Ecommerce inventory/reservation and Maintenance stock contracts before adding another physical ledger. Accounting retains valuation and financial posting ownership.

Business lifecycle: requested → reserved → dispatched → partially_received → received → reconciled; cancelled and discrepancy require explicit handling.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `dispatched` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `receive` action using `receipt_reference`, `destination_location_id`, `received_at`, `lines`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require authorized destination custody, correct units and lot/serial policy, and conserved dispatched/received/in-transit quantities. Validate the movement identity at the selected stock owner.
5. Submit once and retain the displayed operation/result reference. Record received quantities and discrepancies separately. Financial valuation is a linked Accounting event, not a direct write from the receiving UI.
6. Confirm the authoritative outcome and any remaining obligations. `partially_received` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Warehouse staff act only on assigned locations; supervisors approve adjustments and discrepancy resolution; valuation authority is separate.

Record short/over/damaged receipt discrepancies separately. Retry a scanner submission under its original movement identity; do not repair discrepancies by editing stock balances directly.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/inventory-and-logistics.md), [API example](../../../../projects/sap/api/inventory-and-logistics.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
