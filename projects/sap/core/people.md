# People: core composition design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/people.md) and [API plan](../api/people.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#people). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse foundation identity/team lifecycle, CRM skills/resource-planning where appropriate, and Accounting payroll integration. People records, employment policy, and sensitive HR data need a separately verified owner.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** onboarding/offboarding checklist, assignment history, scoped people directory, delegated approvals, outstanding access recovery.

**Business lifecycle:** proposed → approved → scheduled → active → ended; withdrawn and suspended preserve effective-date history.

Separate a login identity from employment and compensation records. Enforce effective-date consistency, delegated HR access, minimal data sharing, and policy-defined retention. Do not expose compensation in generic team membership DTOs.

The illustrated `end` command takes `effective_until`, `offboarding_case_reference`, `access_recovery_policy_version`, with a documented record-version precondition and scoped operation identity. It starts from `active` and reaches `ended` only after its defined business outcome. The [API example](../api/people.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/people.request.schema.json).

Require authorized HR context, consistent assignment dates and the applicable offboarding policy. Restrict employment, compensation and other sensitive fields independently of ordinary team membership.

End the effective assignment and expose outstanding access/equipment recovery obligations. The employment outcome does not claim all downstream access was successfully revoked.

## Layer implementation

Use an explicit application use case for each reviewed transition. Inputs are authenticated actor/service context, authorized tenant/entity/subject references, expected subject version, scoped operation identity and a typed command DTO. Browser/request fields do not replace this trusted context.

The public result distinguishes validation/permission/stale-state rejection, a committed local decision and an accepted asynchronous operation. Publish only permitted DTO fields and evidence references; Eloquent models and upstream private tables are not the cross-module contract.

**Domain context fields:** `person_reference`, `legal_entity_id`, `position_reference`, `manager_reference`, `effective_from`, `effective_until`, `employment_policy_version`, `access_profile_reference`. These are design inputs/references, not a mandate to duplicate complete upstream records. Preserve owner identifiers and immutable decision/source snapshots where needed.

Store enterprise-owned orchestration changes transactionally and record outbox work with them. The shared operation journal owns delivery state; the business owner owns the actual transition. Use the owner concurrency contract for upstream writes and reconcile its acknowledgement before advancing a final outcome.

Approved assignments trigger access/equipment requests through foundation and asset owners. Offboarding tracks revocation/recovery acknowledgements; payroll receives only approved interface data.

Migrations apply only to newly owned operation/projection state. Plan backfills, indexes, constraints, retention/holds and recovery without renaming or deleting another owner's records. Financial corrections use the owner reversal workflow; identity/access changes retain their revocation acknowledgements.

## Authorization, recovery and operations

HR manages employment; line managers see approved limited fields; payroll and health-related data use separate restricted policies.

A failed access revocation remains an escalated outstanding obligation. Employment end does not silently claim all downstream access is removed.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A manager cannot retrieve another entity compensation data; overlapping assignments obey policy; ending employment exposes incomplete revocations until acknowledged.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `end` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `ended` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
