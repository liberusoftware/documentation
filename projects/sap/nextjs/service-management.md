# Service management: Next.js presentation plan

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#service-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status:** proposed `module-sap-service-management-nextjs` adapter. Confirm actual package identities and release availability before installation.

## Workspace and routes

Compose **triage inbox, incident timeline, sla clock explanation, service impact map, change/knowledge links** from the [detailed domain design](../design/service-management.md). The application owns a list route, detail route and appropriate command forms for `service-incidents`. Their public URL shape is an application decision, separate from API paths. Reuse existing product UI components and API adapters where their contracts fit.

## Reads and commands

The server integration resolves session and authorized tenant/entity scope, queries the owning API, validates its DTO, and sends only permitted serializable fields to UI components. Reads expose workflow state/version, source references and permitted actions. Command wrappers support `triage, assign, escalate, resolve, reopen, close` only after their API contracts are implemented and reviewed.

Agents see entitled customer records; incident commanders coordinate; change approvers authorize production changes independently.

Preserve the record version and operation identity across retries. Return field errors and conflict/review guidance instead of overwriting newer data. Keep credentials in server-only integration. Every server action or route handler authenticates and authorizes its request, and Laravel independently authorizes the domain command.

## Components and failure states

Separate the work queue, record summary, evidence panel, state timeline and command form into documented component boundaries. Framework-independent React primitives may also serve Inertia; navigation, session, form transport and cache invalidation remain adapter-specific. The [Next.js standard](../../../standards/NEXTJS.md) defines the server/client and cache boundaries.

Deduplicate repeated alerts into an incident correlation policy. Escalate missed acknowledgements and failed automation visibly; a failed run never marks the incident resolved automatically.

Show loading, empty, forbidden, validation, conflict, pending-operation and recoverable-error states. Refetch after confirmed state changes and recheck evidence download access. Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware policy exists.

## Verification and release

A pause reason affects only permitted SLA clocks; repeated alerts follow correlation policy; restricted internal notes never appear in customer/mobile projections.

Also verify session expiry, cross-tenant cache isolation, secret exclusion from browser bundles, keyboard/focus behavior and failure recovery. Build and test the packed adapter in a clean consuming application, then release through the [npm lifecycle guide](../../../guides/NPM.md). Deploy compatible owning API changes before the dependent frontend.
