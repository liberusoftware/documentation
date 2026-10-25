# Enterprise foundation: React + Inertia design

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

The Laravel host owns Inertia routes/controllers and passes authorized serializable page props to typed React components/hooks. Compose a queue, subject/evidence detail and `approve` form for the domain workspace. Props include the record/version, permitted actions, safe draft defaults and operation reference, not an unrestricted model snapshot.

An Inertia visit expects an Inertia page/redirect lifecycle. Use the Laravel controller's reviewed public application boundary or a deliberate API adapter and then return the appropriate Inertia response. Do not point an Inertia page visit at a bare REST JSON endpoint and assume it is an Inertia page.

Keep `decision_evidence_ids`, `effective_from` in a typed command draft and map actual server field errors to the form. Preserve navigation/filter state where safe, focus the actionable error summary, and reload/review a stale record before resubmission. Laravel reauthorizes every command independently of client visibility.

Share framework-independent cards, tables, labels, formatting and field primitives with the [Next.js adapter](../nextjs/enterprise-foundation.md). Keep Inertia `Link`, visits, page props, form transport and redirects in its wrapper; Next.js retains its own routing, server/client and cache boundaries.

The React UI displays business and operation states separately. A queued response preserves a pending status and authorized progress link; it does not manufacture the eventual domain outcome in local state.

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
