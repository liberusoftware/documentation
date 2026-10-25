# Data and intelligence: core composition design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/data-and-intelligence.md) and [API plan](../api/data-and-intelligence.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#data-and-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Operational products own transactional records and domain metrics. Enterprise owns governed semantic definitions, cross-product projections, lineage and report delivery where needed.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** report catalogue, filter/freshness preview, run progress, lineage drill-down, governed metric explanations.

**Business lifecycle:** requested → authorized → queued → running → ready → expired; failed and cancelled preserve execution evidence.

Apply row/field policy to every source and output; record freshness and lineage. Define currency/timezone and period semantics. Published metrics need an accountable definition owner; AI suggestions do not become authoritative transactions.

The illustrated `run` command takes `report_definition_version`, `legal_entity_scope`, `parameter_snapshot`, `source_watermarks`, with a documented record-version precondition and scoped operation identity. It starts from `authorized` and reaches `ready` only after its defined business outcome. The [API example](../api/data-and-intelligence.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/data-and-intelligence.request.schema.json).

Authorize every source, row/field and selected entity, then record metric versions and freshness policy. Reject or visibly qualify an incomplete source snapshot according to the report definition.

Produce a permission-scoped report artifact with expiry and lineage. Recheck authorization on download, even if the report was authorized when queued.

## Layer implementation

Use an explicit application use case for each reviewed transition. Inputs are authenticated actor/service context, authorized tenant/entity/subject references, expected subject version, scoped operation identity and a typed command DTO. Browser/request fields do not replace this trusted context.

The public result distinguishes validation/permission/stale-state rejection, a committed local decision and an accepted asynchronous operation. Publish only permitted DTO fields and evidence references; Eloquent models and upstream private tables are not the cross-module contract.

**Domain context fields:** `report_definition_version`, `legal_entity_scope`, `parameter_snapshot`, `source_watermarks`, `metric_definition_versions`, `requested_by`, `output_policy`, `expires_at`. These are design inputs/references, not a mandate to duplicate complete upstream records. Preserve owner identifiers and immutable decision/source snapshots where needed.

Store enterprise-owned orchestration changes transactionally and record outbox work with them. The shared operation journal owns delivery state; the business owner owns the actual transition. Use the owner concurrency contract for upstream writes and reconcile its acknowledgement before advancing a final outcome.

Build projections from published APIs/events or approved analytical feeds, with source watermarks and reconciliation. Keep report execution read-only against transactional domains.

Migrations apply only to newly owned operation/projection state. Plan backfills, indexes, constraints, retention/holds and recovery without renaming or deleting another owner's records. Financial corrections use the owner reversal workflow; identity/access changes retain their revocation acknowledgements.

## Authorization, recovery and operations

Authors define reports within approved sources; data owners approve sensitive fields; viewers can run/export only their permitted entity and purpose scope.

A stale or incomplete feed must be visible in output metadata and may block governed reports. Retry failed partitions with the same run identity; recheck authorization at download time.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A report cannot leak a hidden entity through totals or cache reuse; revoked access blocks download; source totals and declared watermark reconciliation agree.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `run` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `ready` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
