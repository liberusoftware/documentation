# Inventory and logistics: Nuxt design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/inventory-and-logistics.md) and [API plan](../api/inventory-and-logistics.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inventory-and-logistics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Review Ecommerce inventory/reservation and Maintenance stock contracts before adding another physical ledger. Accounting retains valuation and financial posting ownership.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** availability inquiry, transfer planning, pick/dispatch scanning, receipt discrepancy capture, lot traceability.

**Business lifecycle:** requested → reserved → dispatched → partially_received → received → reconciled; cancelled and discrepancy require explicit handling.

Keep quantity units explicit, conserve movement quantities, enforce lot/serial uniqueness, and distinguish available, reserved, in-transit, and quarantined stock. Cross-company movements require paired commercial/financial references.

The illustrated `receive` command takes `receipt_reference`, `destination_location_id`, `received_at`, `lines`, with a documented record-version precondition and scoped operation identity. It starts from `dispatched` and reaches `partially_received` only after its defined business outcome. The [API example](../api/inventory-and-logistics.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/inventory-and-logistics.request.schema.json).

Require authorized destination custody, correct units and lot/serial policy, and conserved dispatched/received/in-transit quantities. Validate the movement identity at the selected stock owner.

Record received quantities and discrepancies separately. Financial valuation is a linked Accounting event, not a direct write from the receiving UI.

## Layer implementation

The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.

The proposed API family is `/api/v1/enterprise/stock-transfers`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `receive` rather than a generic status update.

Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.

The command form preserves `receipt_reference`, `destination_location_id`, `received_at`, `lines`, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.

## Authorization, recovery and operations

Warehouse staff act only on assigned locations; supervisors approve adjustments and discrepancy resolution; valuation authority is separate.

Record short/over/damaged receipt discrepancies separately. Retry a scanner submission under its original movement identity; do not repair discrepancies by editing stock balances directly.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- Concurrent reservations cannot oversell controlled stock; duplicate scans do not double-receive; source plus transit plus destination quantities reconcile.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `receive` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `partially_received` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
