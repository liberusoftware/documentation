# Controlling: Nuxt design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/controlling.md) and [API plan](../api/controlling.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#controlling). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse Accounting dimensions, budgets, periods, and posted balances. Enterprise controlling owns documented allocation rules, scenario versions, and cross-unit profitability projections where missing.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** rule editor, driver completeness report, allocation preview, variance drill-down, run reconciliation.

**Business lifecycle:** draft → simulated → approved → executing → reconciled; failed and cancelled runs retain their input snapshots.

Freeze source balances and drivers for a run. Require complete allocation weights, defined zero-driver behavior, conserved totals after rounding, and a clear distinction between simulations and posted adjustments.

The illustrated `simulate` command takes `rule_version`, `source_balance_snapshot_id`, `driver_snapshot_id`, `scenario_id`, with a documented record-version precondition and scoped operation identity. It starts from `draft` and reaches `simulated` only after its defined business outcome. The [API example](../api/controlling.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/controlling.request.schema.json).

Require compatible immutable snapshots and complete allocation drivers. Define zero-driver and rounding-residual behavior; a simulation never posts ledger adjustments.

Publish scenario outputs, residuals and source lineage. Approval and actual posting remain separate actions under the owning policy.

## Layer implementation

The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.

The proposed API family is `/api/v1/enterprise/allocation-runs`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `simulate` rather than a generic status update.

Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.

The command form preserves `rule_version`, `source_balance_snapshot_id`, `driver_snapshot_id`, `scenario_id`, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.

## Authorization, recovery and operations

Analysts simulate; controllers approve rules; posting authority remains with Accounting and the relevant entities.

Partition runs by durable operation IDs. Resume incomplete partitions without reposting completed ones; route unexplained residuals to reconciliation rather than absorbing them silently.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- Zero or missing drivers produce a defined error; rerunning an execution key does not duplicate allocations; rounded destinations reconcile to the source total.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `simulate` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `simulated` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
