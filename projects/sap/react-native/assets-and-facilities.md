# Assets and facilities: React Native design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/assets-and-facilities.md) and [API plan](../api/assets-and-facilities.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#assets-and-facilities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Maintenance owns operational assets, inspections and work orders; Accounting owns capitalization, depreciation and disposal postings. Enterprise coordinates custody, locations, facilities and cross-domain evidence.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** asset/custody search, handover checklist, inspection evidence, discrepancy queue, operational-to-financial reconciliation.

**Business lifecycle:** draft → approved → in_transit → accepted → reconciled; rejected and lost_or_damaged preserve custody evidence.

Keep physical asset identity distinct from its financial record. Require explicit custody acceptance, valid location/entity mappings, inspection evidence where needed, and a separate disposal authorization.

The illustrated `accept` command takes `to_custodian_reference`, `location_reference`, `condition_snapshot_id`, `acceptance_evidence_id`, with a documented record-version precondition and scoped operation identity. It starts from `in_transit` and reaches `accepted` only after its defined business outcome. The [API example](../api/assets-and-facilities.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/assets-and-facilities.request.schema.json).

Validate the receiving custodian, authorized location, required inspection and current custody version. Conflicting concurrent acceptance must not create two current custodians.

Record the accepted custody transition. Damage/discrepancy and financial capitalization/disposal stay with their respective owner workflows.

## Layer implementation

Use TypeScript DTOs and typed navigation for a focused mobile queue/detail/evidence and `accept` review workflow. The host React Native application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

Resolve the selected entity and permitted subject through the reviewed API. The command body uses `to_custodian_reference`, `location_reference`, `condition_snapshot_id`, `acceptance_evidence_id`; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.

Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.

For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.

Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.

## Authorization, recovery and operations

Custodians acknowledge receipt; asset managers approve changes; finance authorizes capitalization/disposal financial effects.

Unaccepted or damaged handovers stay in a discrepancy queue. Never complete offboarding by deleting an assigned asset or clearing its custody history.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- The same asset cannot be concurrently accepted by two custodians; damaged receipts remain unresolved; disposal retains financial and custody references.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `accept` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `accepted` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
