# Enterprise foundation: Nuxt design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/enterprise-foundation.md) and [API plan](../api/enterprise-foundation.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#enterprise-foundation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse foundation identity, teams, policies, audit, files, and localization. Enterprise owns legal-entity mappings, stewardship, and effective-dated master-data approval, not another user directory.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** stewardship queue, before/after comparison, entity hierarchy, effective-date preview, consumer adoption status.

**Business lifecycle:** draft → submitted → approved → scheduled → applied; rejected and superseded are explicit outcomes.

Resolve legal entity membership separately from organizational reporting hierarchy. Reject overlapping effective versions, invalid parent cycles, duplicate authoritative identifiers, and approval by the proposer where segregation is required.

The illustrated `approve` command takes `decision_evidence_ids`, `effective_from`, with a documented record-version precondition and scoped operation identity. It starts from `submitted` and reaches `approved` only after its defined business outcome. The [API example](../api/enterprise-foundation.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/enterprise-foundation.request.schema.json).

Require accessible evidence, a valid effective interval and an independent approver when the policy requires separation. Reject an overlapping approved version rather than replacing it.

Record the approved master-data version and decision evidence. Application to consumers is a separately observable handoff, not proof that all consumers have adopted it.

## Layer implementation

The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.

The proposed API family is `/api/v1/enterprise/master-data-changes`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `approve` rather than a generic status update.

Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.

The command form preserves `decision_evidence_ids`, `effective_from`, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.

## Authorization, recovery and operations

Proposer edits drafts; steward reviews; independent approver authorizes; integration identity applies only approved versions.

A rejected consumer update leaves the change in an actionable partial-application state. Correct the mapping and retry the same handoff identity; do not create a second master record.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A user with access to one subsidiary cannot approve another subsidiary change; concurrent approved changes to one effective interval conflict.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `approve` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `approved` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
