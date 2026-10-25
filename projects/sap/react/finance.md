# Finance: React + Inertia design

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

The Laravel host owns Inertia routes/controllers and passes authorized serializable page props to typed React components/hooks. Compose a queue, subject/evidence detail and `post` form for the domain workspace. Props include the record/version, permitted actions, safe draft defaults and operation reference, not an unrestricted model snapshot.

An Inertia visit expects an Inertia page/redirect lifecycle. Use the Laravel controller's reviewed public application boundary or a deliberate API adapter and then return the appropriate Inertia response. Do not point an Inertia page visit at a bare REST JSON endpoint and assume it is an Inertia page.

Keep `approval_reference`, `source_operation_key` in a typed command draft and map actual server field errors to the form. Preserve navigation/filter state where safe, focus the actionable error summary, and reload/review a stale record before resubmission. Laravel reauthorizes every command independently of client visibility.

Share framework-independent cards, tables, labels, formatting and field primitives with the [Next.js adapter](../nextjs/finance.md). Keep Inertia `Link`, visits, page props, form transport and redirects in its wrapper; Next.js retains its own routing, server/client and cache boundaries.

The React UI displays business and operation states separately. A queued response preserves a pending status and authorized progress link; it does not manufacture the eventual domain outcome in local state.

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
