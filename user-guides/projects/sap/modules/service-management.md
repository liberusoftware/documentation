# Service management: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **triage inbox, incident timeline, sla clock explanation, service impact map, change/knowledge links** for the intended business tasks. Reuse CRM case management, knowledge, SLA/entitlements, and Control Panel monitoring. Enterprise adds cross-product service context, major-incident coordination, and controlled change orchestration where missing.

Business lifecycle: new → triaged → assigned → investigating → resolved → closed; reopened incidents retain the prior resolution.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `investigating` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `resolve` action using `resolution_code`, `resolution_summary`, `evidence_references`, `change_reference`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Require resolution authority and evidence for the selected service/entitlement. Keep customer-visible resolution text separate from restricted internal notes; validate any linked change authority.
5. Submit once and retain the displayed operation/result reference. Record the resolution and SLA outcome. Closure and any later reopening preserve the earlier resolution evidence and are separate lifecycle actions.
6. Confirm the authoritative outcome and any remaining obligations. `resolved` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Agents see entitled customer records; incident commanders coordinate; change approvers authorize production changes independently.

Deduplicate repeated alerts into an incident correlation policy. Escalate missed acknowledgements and failed automation visibly; a failed run never marks the incident resolved automatically.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/service-management.md), [API example](../../../../projects/sap/api/service-management.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
