# Data and intelligence: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **report catalogue, filter/freshness preview, run progress, lineage drill-down, governed metric explanations** for the intended business tasks. Operational products own transactional records and domain metrics. Enterprise owns governed semantic definitions, cross-product projections, lineage and report delivery where needed.

Business lifecycle: requested → authorized → queued → running → ready → expired; failed and cancelled preserve execution evidence.

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `authorized` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `run` action using `report_definition_version`, `legal_entity_scope`, `parameter_snapshot`, `source_watermarks`. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: Authorize every source, row/field and selected entity, then record metric versions and freshness policy. Reject or visibly qualify an incomplete source snapshot according to the report definition.
5. Submit once and retain the displayed operation/result reference. Produce a permission-scoped report artifact with expiry and lineage. Recheck authorization on download, even if the report was authorized when queued.
6. Confirm the authoritative outcome and any remaining obligations. `ready` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

Authors define reports within approved sources; data owners approve sensitive fields; viewers can run/export only their permitted entity and purpose scope.

A stale or incomplete feed must be visible in output metadata and may block governed reports. Retry failed partitions with the same run identity; recheck authorization at download time.

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/data-and-intelligence.md), [API example](../../../../projects/sap/api/data-and-intelligence.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
