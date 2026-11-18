# Governance, risk and compliance: Flutter design

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

Use Dart DTOs and explicit widget/navigation state for a focused mobile queue/detail/evidence and `record-finding` review workflow. The host Flutter application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

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

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `governance-risk-and-compliance`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-enterprise-sap-mobile-flutter`](https://github.com/liberusoftware/project-enterprise-sap-mobile-flutter) | [`module-sap-governance-risk-and-compliance-flutter`](https://github.com/liberusoftware/module-sap-governance-risk-and-compliance-flutter) (`module_sap_governance_risk_and_compliance_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-enterprise-sap-dart-mobile`](https://github.com/liberusoftware/project-enterprise-sap-dart-mobile) | [`module-sap-governance-risk-and-compliance-dart-mobile`](https://github.com/liberusoftware/module-sap-governance-risk-and-compliance-dart-mobile) (`module_sap_governance_risk_and_compliance_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-enterprise-sap-dart-desktop`](https://github.com/liberusoftware/project-enterprise-sap-dart-desktop) | [`module-sap-governance-risk-and-compliance-dart-desktop`](https://github.com/liberusoftware/module-sap-governance-risk-and-compliance-dart-desktop) (`module_sap_governance_risk_and_compliance_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | [API plan](../api/governance-risk-and-compliance.md) · [Core plan](../core/governance-risk-and-compliance.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Policies** | Adaptive mobile cards/sheets for `policies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `policies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Controls** | Adaptive mobile cards/sheets for `controls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `controls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Risks** | Adaptive mobile cards/sheets for `risks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `risks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Audits** | Adaptive mobile cards/sheets for `audits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `audits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Evidence** | Adaptive mobile cards/sheets for `evidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `evidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Incidents** | Adaptive mobile cards/sheets for `incidents` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `incidents` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Privacy** | Adaptive mobile cards/sheets for `privacy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `privacy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Security** | Adaptive mobile cards/sheets for `security` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `security` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Continuity** | Adaptive mobile cards/sheets for `continuity` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `continuity` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Regulatory obligations** | Adaptive mobile cards/sheets for `regulatory obligations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `regulatory obligations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-enterprise-sap-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
