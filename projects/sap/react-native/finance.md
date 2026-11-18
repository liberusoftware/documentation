# Finance: React Native design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/finance.md) and [API plan](../api/finance.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#finance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Accounting owns ledger accounts, journal posting, periods, reconciliation, close, and consolidation. The enterprise workspace coordinates source operations and unresolved handoffs.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** posting exception inbox, journal evidence, source-to-ledger reconciliation, close checklist, consolidation status.

**Business lifecycle:** received → validated → pending_approval → posted; validation_failed and rejected preserve the source reference; posted corrections use a linked reversal.

Require balanced debit/credit totals in the posting representation, valid dimensions, open periods, approved source versions, and unique source operation identities. Preserve transaction/base-currency amounts and the selected exchange-rate reference.

The illustrated `post` command takes `approval_reference`, `source_operation_key`, with a documented record-version precondition and scoped operation identity. It starts from `pending_approval` and reaches `posted` only after its defined business outcome. The [API example](../api/finance.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/finance.request.schema.json).

Validate the approved source version, entity/ledger/period, balanced totals, dimensions, exchange-rate reference and source operation uniqueness through Accounting.

Complete only after Accounting returns the durable journal reference and reconciled control totals. A queued request cannot be displayed as a posted journal.

## Layer implementation

Use TypeScript DTOs and typed navigation for a focused mobile queue/detail/evidence and `post` review workflow. The host React Native application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.

Resolve the selected entity and permitted subject through the reviewed API. The command body uses `approval_reference`, `source_operation_key`; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.

Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.

For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.

Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.

## Authorization, recovery and operations

Preparers submit; independent approvers authorize journals and reopening; read access is scoped by ledger and legal entity.

For a timeout after posting, query by source operation identity before retrying. Reconcile the returned journal and control totals; a posted journal is never silently edited or deleted.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A duplicate invoice event creates one posting; a closed-period command is rejected; reversal preserves the original journal and audit chain.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `post` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `posted` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `finance`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-enterprise-sap-mobile-react`](https://github.com/liberusoftware/project-enterprise-sap-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/finance.md)) |
| Capability React Native module skeleton | [`module-sap-finance-react-native`](https://github.com/liberusoftware/module-sap-finance-react-native) (`@liberusoftware/module-sap-finance-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **General ledger** | Progressive mobile list/detail/sheet flow for `general ledger` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Receivables** | Progressive mobile list/detail/sheet flow for `receivables` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payables** | Progressive mobile list/detail/sheet flow for `payables` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Banking** | Progressive mobile list/detail/sheet flow for `banking` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax** | Progressive mobile list/detail/sheet flow for `tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assets** | Progressive mobile list/detail/sheet flow for `assets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Budgets** | Progressive mobile list/detail/sheet flow for `budgets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Treasury** | Progressive mobile list/detail/sheet flow for `treasury` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Consolidation** | Progressive mobile list/detail/sheet flow for `consolidation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Close** | Progressive mobile list/detail/sheet flow for `close` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Statements** | Progressive mobile list/detail/sheet flow for `statements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-enterprise-sap-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
