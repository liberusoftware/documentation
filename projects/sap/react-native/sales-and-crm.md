# Sales and CRM: React Native design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/sales-and-crm.md) and [API plan](../api/sales-and-crm.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-and-crm). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

CRM owns customer relationships, opportunities, quotes, and contracts. Billing or Ecommerce owns the accepted commercial order according to the deployment; enterprise owns the governed handoff.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** opportunity-to-order workspace, accepted quote comparison, approval evidence, handoff exception queue.

**Business lifecycle:** prepared → approved → submitted → accepted; rejected and needs_review retain downstream reasons.

An accepted quote snapshot cannot be silently changed during handoff. Resolve the authoritative customer and order owner, approved pricing/tax treatment, and seller entity before submission.

The illustrated `submit` command takes `quote_version`, `target_order_owner`, `acceptance_evidence_id`, with a documented record-version precondition and scoped operation identity. It starts from `approved` and reaches `accepted` only after its defined business outcome. The [API example](../api/sales-and-crm.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/sales-and-crm.request.schema.json).

Require a current accepted quote snapshot, authorized seller entity, resolvable customer/product mappings and a reviewed target order owner. Revalidate expired or superseded commercial terms.

Link the accepted downstream order/subscription reference. A timeout remains pending until queried or reconciled using the original handoff identity.

## Layer implementation

Use TypeScript DTOs and typed navigation for a focused mobile queue/detail/evidence and `submit` review workflow. The host React Native application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

Resolve the selected entity and permitted subject through the reviewed API. The command body uses `quote_version`, `target_order_owner`, `acceptance_evidence_id`; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.

Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.

For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.

Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.

## Authorization, recovery and operations

Account teams propose; commercial approvers authorize within value/entity limits; destination services independently authorize acceptance.

If quote validity expires or the destination rejects a product mapping, request review and prepare a new version. Retry a network failure under the original handoff identity.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- An expired or superseded quote cannot be accepted; a retry returns the same downstream order; unauthorized customer details are absent from projections.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `submit` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `accepted` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `sales-and-crm`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-enterprise-sap-mobile-react`](https://github.com/liberusoftware/project-enterprise-sap-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/sales-and-crm.md)) |
| Capability React Native module skeleton | [`module-sap-sales-and-crm-react-native`](https://github.com/liberusoftware/module-sap-sales-and-crm-react-native) (`@liberusoftware/module-sap-sales-and-crm-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Accounts** | Progressive mobile list/detail/sheet flow for `accounts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Leads** | Progressive mobile list/detail/sheet flow for `leads` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Opportunities** | Progressive mobile list/detail/sheet flow for `opportunities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quotes** | Progressive mobile list/detail/sheet flow for `quotes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contracts** | Progressive mobile list/detail/sheet flow for `contracts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Orders** | Progressive mobile list/detail/sheet flow for `orders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Customer success** | Progressive mobile list/detail/sheet flow for `customer success` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Communications** | Progressive mobile list/detail/sheet flow for `communications` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Forecasts** | Progressive mobile list/detail/sheet flow for `forecasts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
