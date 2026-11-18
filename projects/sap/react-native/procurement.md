# Procurement: React Native design

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

Use TypeScript DTOs and typed navigation for a focused mobile queue/detail/evidence and `record-receipt` review workflow. The host React Native application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

Resolve the selected entity and permitted subject through the reviewed API. The command body uses `order_reference`, `receipt_reference`, `received_at`, `lines`; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.

Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.

For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.

Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.

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

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `procurement`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-enterprise-sap-mobile-react`](https://github.com/liberusoftware/project-enterprise-sap-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/procurement.md)) |
| Capability React Native module skeleton | [`module-sap-procurement-react-native`](https://github.com/liberusoftware/module-sap-procurement-react-native) (`@liberusoftware/module-sap-procurement-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Requisitions** | Progressive mobile list/detail/sheet flow for `requisitions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sourcing** | Progressive mobile list/detail/sheet flow for `sourcing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Suppliers** | Progressive mobile list/detail/sheet flow for `suppliers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Purchase orders** | Progressive mobile list/detail/sheet flow for `purchase orders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Receipts** | Progressive mobile list/detail/sheet flow for `receipts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Invoices** | Progressive mobile list/detail/sheet flow for `invoices` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contracts** | Progressive mobile list/detail/sheet flow for `contracts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Spend analysis** | Progressive mobile list/detail/sheet flow for `spend analysis` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
