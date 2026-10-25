# Sales and CRM: Nuxt design

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

The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.

The proposed API family is `/api/v1/enterprise/commercial-handoffs`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `submit` rather than a generic status update.

Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.

The command form preserves `quote_version`, `target_order_owner`, `acceptance_evidence_id`, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.

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
