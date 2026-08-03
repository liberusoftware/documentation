# Genealogy Flutter + Dart implementations

**Scope:** [Genealogy](../GENEALOGY.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Genealogy project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 14 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                              | Package                                 | Core                              | API                             |
| ----------------------------------- | --------------------------------------- | --------------------------------- | ------------------------------- |
| [Collaboration](collaboration.md)   | module-genealogy-collaboration-flutter  | [Core](../core/collaboration.md)  | [API](../api/collaboration.md)  |
| [Discovery](discovery.md)           | module-genealogy-discovery-flutter      | [Core](../core/discovery.md)      | [API](../api/discovery.md)      |
| [Dna](dna.md)                       | module-genealogy-dna-flutter            | [Core](../core/dna.md)            | [API](../api/dna.md)            |
| [Evidence](evidence.md)             | module-genealogy-evidence-flutter       | [Core](../core/evidence.md)       | [API](../api/evidence.md)       |
| [Genealogy Core](genealogy-core.md) | module-genealogy-genealogy-core-flutter | [Core](../core/genealogy-core.md) | [API](../api/genealogy-core.md) |
| [Import Export](import-export.md)   | module-genealogy-import-export-flutter  | [Core](../core/import-export.md)  | [API](../api/import-export.md)  |
| [Media](media.md)                   | module-genealogy-media-flutter          | [Core](../core/media.md)          | [API](../api/media.md)          |
| [People](people.md)                 | module-genealogy-people-flutter         | [Core](../core/people.md)         | [API](../api/people.md)         |
| [Places](places.md)                 | module-genealogy-places-flutter         | [Core](../core/places.md)         | [API](../api/places.md)         |
| [Relationships](relationships.md)   | module-genealogy-relationships-flutter  | [Core](../core/relationships.md)  | [API](../api/relationships.md)  |
| [Reports](reports.md)               | module-genealogy-reports-flutter        | [Core](../core/reports.md)        | [API](../api/reports.md)        |
| [Research](research.md)             | module-genealogy-research-flutter       | [Core](../core/research.md)       | [API](../api/research.md)       |
| [Timeline](timeline.md)             | module-genealogy-timeline-flutter       | [Core](../core/timeline.md)       | [API](../api/timeline.md)       |
| [Tree Viewer](tree-viewer.md)       | module-genealogy-tree-viewer-flutter    | [Core](../core/tree-viewer.md)    | [API](../api/tree-viewer.md)    |
