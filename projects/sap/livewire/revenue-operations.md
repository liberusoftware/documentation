# Revenue operations: Livewire design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/revenue-operations.md) and [API plan](../api/revenue-operations.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-operations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Billing owns subscriptions, usage rating, invoices, and collections; Accounting owns financial recognition and postings. Enterprise coordinates source usage completeness and cross-entity revenue evidence.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** usage completeness dashboard, rating explanation, invoice preview, dispute timeline, settlement reconciliation.

**Business lifecycle:** collecting → validated → rated → approved → invoiced → reconciled; disputed settlements retain the original calculation.

Deduplicate usage source identities and state the window/timezone, late-event policy, quantity units, rounding, and pricing snapshot. Distinguish commercial billing from financial revenue recognition.

The illustrated `finalize` command takes `usage_window`, `source_event_watermark`, `pricing_version`, with a documented record-version precondition and scoped operation identity. It starts from `approved` and reaches `invoiced` only after its defined business outcome. The [API example](../api/revenue-operations.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/revenue-operations.request.schema.json).

Require a closed reviewed usage window, deduplicated source events, explicit units/timezone and the approved rating/pricing snapshot. Late usage follows the correction policy.

Billing owns invoice finalization and returns its reference. Financial revenue recognition remains Accounting-owned and is not implied by invoicing.

## Layer implementation

Compose a workspace list, selected-subject detail, command form and operation-status component. Public component state contains only authorized filter values, opaque selection/version, safe command draft and operation reference; hydrated IDs are untrusted input.

The `finalize` handler resolves the authenticated actor and current scope afresh, loads the authorized subject, validates `usage_window`, `source_event_watermark`, `pricing_version`, and calls the public application/API command. Protected lifecycle/audit/owner-result fields are not mass-assigned from component state.

Keep field validation messages with the draft and announce them accessibly. Disable repeat interaction while a request is pending for usability, while relying on server command identity/concurrency rules for correctness. After a confirmed write, reload authorized state rather than applying an assumed client-side final state.

Poll only an authorized operation reference at a bounded interval; stop/recover cleanly after expiry, revocation or navigation. Avoid persisting request-specific tenant/actor data in long-lived singleton/static state. File uploads need size/type checks and authorized evidence registration before use.

## Authorization, recovery and operations

Meter operators submit scoped usage; billing specialists approve adjustments; finance owns recognition policy and postings.

Late or corrected usage creates an adjustment referencing the original settlement. Preserve invoice finality and route disputes through Billing correction workflows.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- Duplicate meter events do not increase invoice quantity; a late correction is traceable; retries cannot finalize the same invoice twice.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `finalize` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `invoiced` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
