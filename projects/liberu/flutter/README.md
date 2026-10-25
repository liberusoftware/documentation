# Liberu platform Flutter + Dart implementations

<!-- catalogue-status:start -->
This index preserves **4 module documents/spellings**. Counts are specifications, not released packages or deployed features. Exact source identities and aliases are in the [source map](../SOURCE-MAPPING.md); [shared ownership](../../../architecture/SHARED-MODULES.md) and [Next.js adapter homes](../../../modules/nextjs/OWNERSHIP.md) prevent alternate spellings from becoming competing implementations.
<!-- catalogue-status:end -->

**Scope:** [Liberu platform](../../LIBERU.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Liberu platform project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-flutter`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [Flutter + Dart module standard](../../../modules/flutter/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 4 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module document | Source/target reference | Related plans |
| --- | --- | --- |
| [Business Workflow Reconciliation Flutter + Dart](business-workflow-reconciliation.md) | [Target/source map](../SOURCE-MAPPING.md#business-workflow-reconciliation) | [core](../core/business-workflow-reconciliation.md) · [api](../api/business-workflow-reconciliation.md) · [nextjs](../nextjs/business-workflow-reconciliation.md) |
| [Executive Insights Flutter + Dart](executive-insights.md) | [Target/source map](../SOURCE-MAPPING.md#executive-insights) | [core](../core/executive-insights.md) · [api](../api/executive-insights.md) · [nextjs](../nextjs/executive-insights.md) |
| [Platform Orchestration Flutter + Dart](platform-orchestration.md) | [Target/source map](../SOURCE-MAPPING.md#platform-orchestration) | [core](../core/platform-orchestration.md) · [api](../api/platform-orchestration.md) · [nextjs](../nextjs/platform-orchestration.md) |
| [Revenue and Care Orchestration Flutter + Dart](revenue-and-care-orchestration.md) | [Target/source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration) | [core](../core/revenue-and-care-orchestration.md) · [api](../api/revenue-and-care-orchestration.md) · [nextjs](../nextjs/revenue-and-care-orchestration.md) |
