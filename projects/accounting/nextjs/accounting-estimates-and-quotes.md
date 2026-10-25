# Accounting Estimates And Quotes: shared Next.js adapter

<!-- nextjs-plan:generated -->

**Status:** proposed consumer/alias reference. This document preserves the existing module scope; it does not create another npm package or certify source compatibility.

## Shared implementation home

Use [Estimates and Quotes: Next.js presentation plan](estimates-and-quotes.md) for adapter group `liberusoftware/module-accounting-estimates-and-quotes`. Its component, API, validation, cache and recovery contracts belong to that shared plan.

The local [domain specification](../features/accounting-estimates-and-quotes.md) remains the application scope. Enable only the UI needed by this consumer and keep product-specific policy in documented extension points. Review the source variants and API contract before adopting a common adapter release.

A directory alias or alternate design spelling is not a separate authoritative record owner. The application owns its routes, navigation and session integration; the shared adapter owns reusable components and transport boundaries.

See the [project source map](../SOURCE-MAPPING.md#accounting-estimates-and-quotes), [reuse guide](../../../architecture/SHARED-MODULES.md), and [npm lifecycle guide](../../../guides/NPM.md).
