# Procurement: Nuxt design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/procurement.md) and [API plan](../api/procurement.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#procurement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse supplier/master-data contracts, Maintenance purchasing where compatible, and Accounting receipt/payable contracts. Enterprise owns cross-entity sourcing, approval and matching orchestration only where those are genuine gaps.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** requisition form, approval queue, purchase order timeline, receipt capture, three-way matching exceptions.

**Business lifecycle:** draft → submitted → approved → ordered → partially_received → received → matched → closed; rejected and cancelled are explicit branches.

Separate requester, approver, receiver, and payment authority as policy requires. Enforce budget/approval thresholds, quantity and price tolerances, approved supplier status, and partial receipt accounting.

The illustrated `record-receipt` command takes `order_reference`, `receipt_reference`, `received_at`, `lines`, with a documented record-version precondition and scoped operation identity. It starts from `ordered` and reaches `partially_received` only after its defined business outcome. The [API example](../api/procurement.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/procurement.request.schema.json).

Validate the receiving actor/location, order line, units and quantity/tolerance policy. The owning stock/receipt service records physical movements; reject duplicate receipt identities.

Link the receipt and outstanding quantities. A partial receipt does not close the order or release an unmatched supplier invoice for payment.

## Layer implementation

The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.

The proposed API family is `/api/v1/enterprise/purchase-requisitions`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `record-receipt` rather than a generic status update.

Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.

The command form preserves `order_reference`, `receipt_reference`, `received_at`, `lines`, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.

## Authorization, recovery and operations

Requesters manage own drafts; approvers act within delegated limits; receivers record quantities; AP handles invoice disputes.

Hold unmatched or over-tolerance invoices with actionable discrepancies. A supplier timeout leaves an order handoff pending; query/retry by identity before issuing another order.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A requester cannot approve their own requisition under separation policy; partial receipts do not close the order; an over-tolerance invoice remains held.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `record-receipt` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `partially_received` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
