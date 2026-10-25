# Product and engineering: Next.js presentation plan

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#product-and-engineering). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status:** proposed `module-sap-product-and-engineering-nextjs` adapter. Confirm actual package identities and release availability before installation.

## Workspace and routes

Compose **release checklist, requirement/test traceability, artifact comparison, rollout timeline, support readiness** from the [detailed domain design](../design/product-and-engineering.md). The application owns a list route, detail route and appropriate command forms for `release-reviews`. Their public URL shape is an application decision, separate from API paths. Reuse existing product UI components and API adapters where their contracts fit.

## Reads and commands

The server integration resolves session and authorized tenant/entity scope, queries the owning API, validates its DTO, and sends only permitted serializable fields to UI components. Reads expose workflow state/version, source references and permitted actions. Command wrappers support `collect-evidence, review, approve, begin-rollout, record-outcome, record-rollback` only after their API contracts are implemented and reviewed.

Engineers submit evidence; product/security owners approve their controls; release managers authorize deployment under policy.

Preserve the record version and operation identity across retries. Return field errors and conflict/review guidance instead of overwriting newer data. Keep credentials in server-only integration. Every server action or route handler authenticates and authorizes its request, and Laravel independently authorizes the domain command.

## Components and failure states

Separate the work queue, record summary, evidence panel, state timeline and command form into documented component boundaries. Framework-independent React primitives may also serve Inertia; navigation, session, form transport and cache invalidation remain adapter-specific. The [Next.js standard](../../../standards/NEXTJS.md) defines the server/client and cache boundaries.

Missing, expired, or mismatched evidence blocks approval. Preserve rollout failures and rollback outcomes against the original release digest for support and audit.

Show loading, empty, forbidden, validation, conflict, pending-operation and recoverable-error states. Refetch after confirmed state changes and recheck evidence download access. Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware policy exists.

## Verification and release

An artifact digest change invalidates approval; duplicate CI notifications do not create duplicate releases; rollback preserves the original release record.

Also verify session expiry, cross-tenant cache isolation, secret exclusion from browser bundles, keyboard/focus behavior and failure recovery. Build and test the packed adapter in a clean consuming application, then release through the [npm lifecycle guide](../../../guides/NPM.md). Deploy compatible owning API changes before the dependent frontend.
