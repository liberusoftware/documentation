# Assets and facilities: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **asset/custody search, handover checklist, inspection evidence, discrepancy queue, operational-to-financial reconciliation** for the intended business tasks. Maintenance owns operational assets, inspections and work orders; Accounting owns capitalization, depreciation and disposal postings. Enterprise coordinates custody, locations, facilities and cross-domain evidence.

Business lifecycle: draft → approved → in_transit → accepted → reconciled; rejected and lost_or_damaged preserve custody evidence.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `in_transit` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `accept` action using `to_custodian_reference`, `location_reference`, `condition_snapshot_id`, `acceptance_evidence_id`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Validate the receiving custodian, authorized location, required inspection and current custody version. Conflicting concurrent acceptance must not create two current custodians.
5. Submit once and retain the displayed operation/result reference. Record the accepted custody transition. Damage/discrepancy and financial capitalization/disposal stay with their respective owner workflows.
6. Confirm the authoritative outcome and any remaining obligations. `accepted` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Custodians acknowledge receipt; asset managers approve changes; finance authorizes capitalization/disposal financial effects.

Unaccepted or damaged handovers stay in a discrepancy queue. Never complete offboarding by deleting an assigned asset or clearing its custody history.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/assets-and-facilities.md), [API example](../../../../projects/sap/api/assets-and-facilities.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
