# Control Panel Control Core: shared Next.js adapter

<!-- nextjs-plan:generated -->

**Status:** proposed consumer/alias reference. This document preserves the existing module scope; it does not create another npm package or certify source compatibility.

## Shared implementation home

Use [Control Core: Next.js presentation plan](control-core.md) for adapter group `liberusoftware/module-control-panel-control-core`. Its component, API, validation, cache and recovery contracts belong to that shared plan.

The local [domain specification](../features/control-panel-control-core.md) remains the application scope. Enable only the UI needed by this consumer and keep product-specific policy in documented extension points. Review the source variants and API contract before adopting a common adapter release.

A directory alias or alternate design spelling is not a separate authoritative record owner. The application owns its routes, navigation and session integration; the shared adapter owns reusable components and transport boundaries.

See the [project source map](../SOURCE-MAPPING.md#control-panel-control-core), [reuse guide](../../../architecture/SHARED-MODULES.md), and [npm lifecycle guide](../../../guides/NPM.md).
