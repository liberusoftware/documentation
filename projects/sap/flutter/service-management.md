# Service management: Flutter design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/service-management.md) and [API plan](../api/service-management.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#service-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse CRM case management, knowledge, SLA/entitlements, and Control Panel monitoring. Enterprise adds cross-product service context, major-incident coordination, and controlled change orchestration where missing.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** triage inbox, incident timeline, sla clock explanation, service impact map, change/knowledge links.

**Business lifecycle:** new → triaged → assigned → investigating → resolved → closed; reopened incidents retain the prior resolution.

Version the priority and SLA basis, define pause conditions and business calendars, and preserve customer-visible communication separately from internal technical notes. Change approval is distinct from incident urgency.

The illustrated `resolve` command takes `resolution_code`, `resolution_summary`, `evidence_references`, `change_reference`, with a documented record-version precondition and scoped operation identity. It starts from `investigating` and reaches `resolved` only after its defined business outcome. The [API example](../api/service-management.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/service-management.request.schema.json).

Require resolution authority and evidence for the selected service/entitlement. Keep customer-visible resolution text separate from restricted internal notes; validate any linked change authority.

Record the resolution and SLA outcome. Closure and any later reopening preserve the earlier resolution evidence and are separate lifecycle actions.

## Layer implementation

Use Dart DTOs and explicit widget/navigation state for a focused mobile queue/detail/evidence and `resolve` review workflow. The host Flutter application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

Resolve the selected entity and permitted subject through the reviewed API. The command body uses `resolution_code`, `resolution_summary`, `evidence_references`, `change_reference`; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.

Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.

For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.

Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.

## Authorization, recovery and operations

Agents see entitled customer records; incident commanders coordinate; change approvers authorize production changes independently.

Deduplicate repeated alerts into an incident correlation policy. Escalate missed acknowledgements and failed automation visibly; a failed run never marks the incident resolved automatically.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A pause reason affects only permitted SLA clocks; repeated alerts follow correlation policy; restricted internal notes never appear in customer/mobile projections.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `resolve` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `resolved` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
