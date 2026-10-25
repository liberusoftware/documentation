# Partners and portals: React Native design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/partners-and-portals.md) and [API plan](../api/partners-and-portals.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#partners-and-portals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse foundation identity/policy, CRM partner/account relationships, and product-owned self-service APIs. Enterprise owns scoped delegation and cross-product portal composition, not copied customer/supplier ledgers.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** partner onboarding, delegation review, customer/supplier self-service workspace, access history, revocation status.

**Business lifecycle:** requested → reviewed → active → expired; rejected and revoked are terminal outcomes for the grant version.

Bind delegation to explicit resources, operations, audience and expiry. A partner relationship is not authorization. Invitations and passwordless links need bounded lifetime and non-enumerating failure responses.

The illustrated `revoke` command takes `reason`, `revocation_evidence_reference`, with a documented record-version precondition and scoped operation identity. It starts from `active` and reaches `revoked` only after its defined business outcome. The [API example](../api/partners-and-portals.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/partners-and-portals.request.schema.json).

Require authority over the exact principal/resource scope. A partner relationship alone does not grant revocation or delegation rights across other organizations.

Record revocation and track downstream acknowledgements/session-cache invalidation. Keep delayed revocations visible until protected operations enforce the change.

## Layer implementation

Use TypeScript DTOs and typed navigation for a focused mobile queue/detail/evidence and `revoke` review workflow. The host React Native application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

Resolve the selected entity and permitted subject through the reviewed API. The command body uses `reason`, `revocation_evidence_reference`; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.

Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.

For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.

Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.

## Authorization, recovery and operations

Sponsors request limited rights; designated owners approve; external users cannot expand scope or grant rights they do not hold.

A stale portal session must fail the next protected operation after revocation. Surface delayed downstream revocations as outstanding obligations rather than hiding them.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- An expired grant cannot download a previously listed document; changing a resource ID cannot escape scope; revocation reaches active portal workflows.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `revoke` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `revoked` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
