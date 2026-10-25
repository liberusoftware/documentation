# Governance, risk and compliance: React Native design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/governance-risk-and-compliance.md) and [API plan](../api/governance-risk-and-compliance.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#governance-risk-and-compliance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse foundation audit, documents, policy and notification contracts. Enterprise owns control/risk relationships, assessments, evidence review and remediation oversight without overwriting source audit events.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** control library, risk register, evidence request inbox, finding/remediation timeline, audit-ready export preview.

**Business lifecycle:** planned → evidence_requested → under_review → accepted → closed; deficient and reopened preserve reviewer findings.

Version controls and frameworks, separate control operator from independent reviewer, retain immutable evidence references, and restrict sensitive findings. A policy document alone is not proof of effective operation.

The illustrated `record-finding` command takes `control_reference`, `finding_summary`, `evidence_references`, `remediation_owner_reference`, `due_at`, with a documented record-version precondition and scoped operation identity. It starts from `under_review` and reaches `deficient` only after its defined business outcome. The [API example](../api/governance-risk-and-compliance.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/governance-risk-and-compliance.request.schema.json).

Require independent review authority, accessible immutable evidence and a valid remediation owner. Preserve control/framework version and legal-hold/retention obligations.

Record the finding and linked remediation obligation without changing the original source audit evidence. Remediation acceptance is a distinct reviewed action.

## Layer implementation

Use TypeScript DTOs and typed navigation for a focused mobile queue/detail/evidence and `record-finding` review workflow. The host React Native application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

Resolve the selected entity and permitted subject through the reviewed API. The command body uses `control_reference`, `finding_summary`, `evidence_references`, `remediation_owner_reference`, `due_at`; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.

Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.

For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.

Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.

## Authorization, recovery and operations

Control owners submit; independent reviewers assess; auditors receive scoped read/export access; legal holds require designated authority.

Expired or unavailable evidence reopens the review obligation. Retries preserve evidence provenance and do not replace the original assessment result invisibly.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- The operator cannot approve their own independent assessment; evidence access is rechecked on download; retention jobs preserve held records.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `record-finding` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `deficient` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
