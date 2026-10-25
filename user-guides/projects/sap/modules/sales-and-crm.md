# Sales and CRM: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **opportunity-to-order workspace, accepted quote comparison, approval evidence, handoff exception queue** for the intended business tasks. CRM owns customer relationships, opportunities, quotes, and contracts. Billing or Ecommerce owns the accepted commercial order according to the deployment; enterprise owns the governed handoff.

Business lifecycle: prepared → approved → submitted → accepted; rejected and needs_review retain downstream reasons.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `approved` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `submit` action using `quote_version`, `target_order_owner`, `acceptance_evidence_id`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require a current accepted quote snapshot, authorized seller entity, resolvable customer/product mappings and a reviewed target order owner. Revalidate expired or superseded commercial terms.
5. Submit once and retain the displayed operation/result reference. Link the accepted downstream order/subscription reference. A timeout remains pending until queried or reconciled using the original handoff identity.
6. Confirm the authoritative outcome and any remaining obligations. `accepted` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Account teams propose; commercial approvers authorize within value/entity limits; destination services independently authorize acceptance.

If quote validity expires or the destination rejects a product mapping, request review and prepare a new version. Retry a network failure under the original handoff identity.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/sales-and-crm.md), [API example](../../../../projects/sap/api/sales-and-crm.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
