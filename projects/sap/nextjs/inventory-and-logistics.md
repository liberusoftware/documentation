# Inventory and logistics: Next.js presentation plan

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inventory-and-logistics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status:** proposed `module-sap-inventory-and-logistics-nextjs` adapter. Confirm actual package identities and release availability before installation.

## Workspace and routes

Compose **availability inquiry, transfer planning, pick/dispatch scanning, receipt discrepancy capture, lot traceability** from the [detailed domain design](../design/inventory-and-logistics.md). The application owns a list route, detail route and appropriate command forms for `stock-transfers`. Their public URL shape is an application decision, separate from API paths. Reuse existing product UI components and API adapters where their contracts fit.

## Reads and commands

The server integration resolves session and authorized tenant/entity scope, queries the owning API, validates its DTO, and sends only permitted serializable fields to UI components. Reads expose workflow state/version, source references and permitted actions. Command wrappers support `reserve, dispatch, receive, reconcile, cancel` only after their API contracts are implemented and reviewed.

Warehouse staff act only on assigned locations; supervisors approve adjustments and discrepancy resolution; valuation authority is separate.

Preserve the record version and operation identity across retries. Return field errors and conflict/review guidance instead of overwriting newer data. Keep credentials in server-only integration. Every server action or route handler authenticates and authorizes its request, and Laravel independently authorizes the domain command.

## Components and failure states

Separate the work queue, record summary, evidence panel, state timeline and command form into documented component boundaries. Framework-independent React primitives may also serve Inertia; navigation, session, form transport and cache invalidation remain adapter-specific. The [Next.js standard](../../../standards/NEXTJS.md) defines the server/client and cache boundaries.

Record short/over/damaged receipt discrepancies separately. Retry a scanner submission under its original movement identity; do not repair discrepancies by editing stock balances directly.

Show loading, empty, forbidden, validation, conflict, pending-operation and recoverable-error states. Refetch after confirmed state changes and recheck evidence download access. Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware policy exists.

## Verification and release

Concurrent reservations cannot oversell controlled stock; duplicate scans do not double-receive; source plus transit plus destination quantities reconcile.

Also verify session expiry, cross-tenant cache isolation, secret exclusion from browser bundles, keyboard/focus behavior and failure recovery. Build and test the packed adapter in a clean consuming application, then release through the [npm lifecycle guide](../../../guides/NPM.md). Deploy compatible owning API changes before the dependent frontend.
