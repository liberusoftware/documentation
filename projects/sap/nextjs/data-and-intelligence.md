# Data and intelligence: Next.js presentation plan

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#data-and-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status:** proposed `module-sap-data-and-intelligence-nextjs` adapter. Confirm actual package identities and release availability before installation.

## Workspace and routes

Compose **report catalogue, filter/freshness preview, run progress, lineage drill-down, governed metric explanations** from the [detailed domain design](../design/data-and-intelligence.md). The application owns a list route, detail route and appropriate command forms for `report-runs`. Their public URL shape is an application decision, separate from API paths. Reuse existing product UI components and API adapters where their contracts fit.

## Reads and commands

The server integration resolves session and authorized tenant/entity scope, queries the owning API, validates its DTO, and sends only permitted serializable fields to UI components. Reads expose workflow state/version, source references and permitted actions. Command wrappers support `validate, run, cancel, refresh, download` only after their API contracts are implemented and reviewed.

Authors define reports within approved sources; data owners approve sensitive fields; viewers can run/export only their permitted entity and purpose scope.

Preserve the record version and operation identity across retries. Return field errors and conflict/review guidance instead of overwriting newer data. Keep credentials in server-only integration. Every server action or route handler authenticates and authorizes its request, and Laravel independently authorizes the domain command.

## Components and failure states

Separate the work queue, record summary, evidence panel, state timeline and command form into documented component boundaries. Framework-independent React primitives may also serve Inertia; navigation, session, form transport and cache invalidation remain adapter-specific. The [Next.js standard](../../../standards/NEXTJS.md) defines the server/client and cache boundaries.

A stale or incomplete feed must be visible in output metadata and may block governed reports. Retry failed partitions with the same run identity; recheck authorization at download time.

Show loading, empty, forbidden, validation, conflict, pending-operation and recoverable-error states. Refetch after confirmed state changes and recheck evidence download access. Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware policy exists.

## Verification and release

A report cannot leak a hidden entity through totals or cache reuse; revoked access blocks download; source totals and declared watermark reconciliation agree.

Also verify session expiry, cross-tenant cache isolation, secret exclusion from browser bundles, keyboard/focus behavior and failure recovery. Build and test the packed adapter in a clean consuming application, then release through the [npm lifecycle guide](../../../guides/NPM.md). Deploy compatible owning API changes before the dependent frontend.
