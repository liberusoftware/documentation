# Liberu platform Flutter + Dart implementations

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

The following 3 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                                  | Package                                                | Core                                                | API                                               |
| ----------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------- | ------------------------------------------------- |
| [Business Workflow Reconciliation](business-workflow-reconciliation.md) | module-liberu-business-workflow-reconciliation-flutter | [Core](../core/business-workflow-reconciliation.md) | [API](../api/business-workflow-reconciliation.md) |
| [Executive Insights](executive-insights.md)                             | module-liberu-executive-insights-flutter               | [Core](../core/executive-insights.md)               | [API](../api/executive-insights.md)               |
| [Platform Orchestration](platform-orchestration.md)                     | module-liberu-platform-orchestration-flutter           | [Core](../core/platform-orchestration.md)           | [API](../api/platform-orchestration.md)           |
