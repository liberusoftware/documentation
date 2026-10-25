# Module Cms Static Publishing: shared Next.js adapter

<!-- nextjs-plan:generated -->

**Status:** proposed consumer/alias reference. This document preserves the existing module scope; it does not create another npm package or certify source compatibility.

## Shared implementation home

Use [Static Publishing: Next.js presentation plan](static-publishing.md) for adapter group `liberusoftware/module-cms-static-publishing`. Its component, API, validation, cache and recovery contracts belong to that shared plan.

The local [domain specification](../features/module-cms-static-publishing.md) remains the application scope. Enable only the UI needed by this consumer and keep product-specific policy in documented extension points. Review the source variants and API contract before adopting a common adapter release.

A directory alias or alternate design spelling is not a separate authoritative record owner. The application owns its routes, navigation and session integration; the shared adapter owns reusable components and transport boundaries.

See the [project source map](../SOURCE-MAPPING.md#module-cms-static-publishing), [reuse guide](../../../architecture/SHARED-MODULES.md), and [npm lifecycle guide](../../../guides/NPM.md).
