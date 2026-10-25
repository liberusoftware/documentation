# Data and intelligence: Vue + Inertia design

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

The Laravel host owns Inertia routes/controllers and passes authorized serializable page props to typed Vue components/composables. Compose a queue, subject/evidence detail and `run` form for the domain workspace. Props include the record/version, permitted actions, safe draft defaults and operation reference, not an unrestricted model snapshot.

An Inertia visit expects an Inertia page/redirect lifecycle. Use the Laravel controller's reviewed public application boundary or a deliberate API adapter and then return the appropriate Inertia response. Do not point an Inertia page visit at a bare REST JSON endpoint and assume it is an Inertia page.

Keep `report_definition_version`, `legal_entity_scope`, `parameter_snapshot`, `source_watermarks` in a typed command draft and map actual server field errors to the form. Preserve navigation/filter state where safe, focus the actionable error summary, and reload/review a stale record before resubmission. Laravel reauthorizes every command independently of client visibility.

Share framework-independent Vue primitives with Nuxt where the contracts fit. Keep Inertia navigation/forms/page props in its wrapper and Nuxt server/browser transport, routing and runtime configuration in its adapter.

The Vue UI displays business and operation states separately. A queued response preserves a pending status and authorized progress link; it does not manufacture the eventual domain outcome in local state.

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
