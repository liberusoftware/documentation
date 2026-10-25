# Partners and portals: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **partner onboarding, delegation review, customer/supplier self-service workspace, access history, revocation status** for the intended business tasks. Reuse foundation identity/policy, CRM partner/account relationships, and product-owned self-service APIs. Enterprise owns scoped delegation and cross-product portal composition, not copied customer/supplier ledgers.

Business lifecycle: requested → reviewed → active → expired; rejected and revoked are terminal outcomes for the grant version.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `active` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `revoke` action using `reason`, `revocation_evidence_reference`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require authority over the exact principal/resource scope. A partner relationship alone does not grant revocation or delegation rights across other organizations.
5. Submit once and retain the displayed operation/result reference. Record revocation and track downstream acknowledgements/session-cache invalidation. Keep delayed revocations visible until protected operations enforce the change.
6. Confirm the authoritative outcome and any remaining obligations. `revoked` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Sponsors request limited rights; designated owners approve; external users cannot expand scope or grant rights they do not hold.

A stale portal session must fail the next protected operation after revocation. Surface delayed downstream revocations as outstanding obligations rather than hiding them.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/partners-and-portals.md), [API example](../../../../projects/sap/api/partners-and-portals.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
