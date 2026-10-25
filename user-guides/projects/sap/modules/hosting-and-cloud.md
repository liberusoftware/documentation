# Hosting and cloud: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **service request wizard, capacity preview, approval summary, provisioning progress, drift and failed-resource reconciliation** for the intended business tasks. Billing owns commercial subscriptions and provisioning demand; Control Panel owns infrastructure lifecycle and adapters. Enterprise coordinates approval, tenancy, capacity and reconciliation.

Business lifecycle: requested → validated → approved → queued → provisioning → active; failed, compensating, suspended and retired remain observable.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `approved` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `provision` action using `service_template_version`, `region`, `capacity_request`, `approved_change_reference`, `target_platform`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Validate entitlement, allowed region, capacity, approved template and change authority. Payloads contain secret references only where required, never provider credentials.
5. Submit once and retain the displayed operation/result reference. Control Panel returns an observed resource reference and outcome. Partial creation retains created-resource and compensation evidence until reconciled.
6. Confirm the authoritative outcome and any remaining obligations. `active` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Customers request entitled services; operators act on scoped infrastructure; approvers authorize high-impact or high-cost changes.

On partial infrastructure creation, record every created resource and compensation result. Query provider/control-plane state before retry; a new retry must not allocate another billable resource unintentionally.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/hosting-and-cloud.md), [API example](../../../../projects/sap/api/hosting-and-cloud.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
