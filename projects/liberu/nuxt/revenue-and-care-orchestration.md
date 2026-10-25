# Liberu: Revenue and Care Orchestration Nuxt

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-liberu-revenue-and-care-orchestration-nuxt`

Expose public website entry points and authenticated staff/customer views over the [API](../api/revenue-and-care-orchestration.md). Keep public SSR limited to approved, cacheable content; do not leak health, consent, invoice, or infrastructure data into SSR payloads. Use mobile-first responsive components, Core Web Vitals budgets, accessible chat/support handoff, typed composables, and explicit queued/error states.
