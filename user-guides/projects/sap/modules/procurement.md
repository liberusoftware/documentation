# Procurement: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **requisition form, approval queue, purchase order timeline, receipt capture, three-way matching exceptions** for the intended business tasks. Reuse supplier/master-data contracts, Maintenance purchasing where compatible, and Accounting receipt/payable contracts. Enterprise owns cross-entity sourcing, approval and matching orchestration only where those are genuine gaps.

Business lifecycle: draft → submitted → approved → ordered → partially_received → received → matched → closed; rejected and cancelled are explicit branches.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `ordered` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `record-receipt` action using `order_reference`, `receipt_reference`, `received_at`, `lines`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Validate the receiving actor/location, order line, units and quantity/tolerance policy. The owning stock/receipt service records physical movements; reject duplicate receipt identities.
5. Submit once and retain the displayed operation/result reference. Link the receipt and outstanding quantities. A partial receipt does not close the order or release an unmatched supplier invoice for payment.
6. Confirm the authoritative outcome and any remaining obligations. `partially_received` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Requesters manage own drafts; approvers act within delegated limits; receivers record quantities; AP handles invoice disputes.

Hold unmatched or over-tolerance invoices with actionable discrepancies. A supplier timeout leaves an order handoff pending; query/retry by identity before issuing another order.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/procurement.md), [API example](../../../../projects/sap/api/procurement.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
