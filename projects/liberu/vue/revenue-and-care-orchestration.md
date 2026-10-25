# Liberu: Revenue and Care Orchestration Vue + Inertia

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-liberu-revenue-and-care-orchestration-vue-inertia`

Provide typed Vue pages/composables for health constellation, care queue, outreach eligibility, recovery handoff, and AI approval using the [API](../api/revenue-and-care-orchestration.md). Design for one-handed mobile use, resilient loading/empty/denied/offline/conflict states, accessible forms, localized time, and server-side authorization. Never implement a client-side force-contact path.

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->
