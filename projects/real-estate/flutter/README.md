# Real Estate Flutter + Dart implementations

**Scope:** [Real Estate](../REAL-ESTATE.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Real Estate project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 15 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                            | Package                                          | Core                                     | API                                    |
| ------------------------------------------------- | ------------------------------------------------ | ---------------------------------------- | -------------------------------------- |
| [Instructions](instructions.md)                   | module-real-estate-instructions-flutter          | [Core](../core/instructions.md)          | [API](../api/instructions.md)          |
| [Lettings](lettings.md)                           | module-real-estate-lettings-flutter              | [Core](../core/lettings.md)              | [API](../api/lettings.md)              |
| [Listings](listings.md)                           | module-real-estate-listings-flutter              | [Core](../core/listings.md)              | [API](../api/listings.md)              |
| [Marketing](marketing.md)                         | module-real-estate-marketing-flutter             | [Core](../core/marketing.md)             | [API](../api/marketing.md)             |
| [Matching](matching.md)                           | module-real-estate-matching-flutter              | [Core](../core/matching.md)              | [API](../api/matching.md)              |
| [Media And Documents](media-and-documents.md)     | module-real-estate-media-and-documents-flutter   | [Core](../core/media-and-documents.md)   | [API](../api/media-and-documents.md)   |
| [Offers](offers.md)                               | module-real-estate-offers-flutter                | [Core](../core/offers.md)                | [API](../api/offers.md)                |
| [Parties](parties.md)                             | module-real-estate-parties-flutter               | [Core](../core/parties.md)               | [API](../api/parties.md)               |
| [Portals And Reporting](portals-and-reporting.md) | module-real-estate-portals-and-reporting-flutter | [Core](../core/portals-and-reporting.md) | [API](../api/portals-and-reporting.md) |
| [Properties](properties.md)                       | module-real-estate-properties-flutter            | [Core](../core/properties.md)            | [API](../api/properties.md)            |
| [Property Management](property-management.md)     | module-real-estate-property-management-flutter   | [Core](../core/property-management.md)   | [API](../api/property-management.md)   |
| [Real Estate Core](real-estate-core.md)           | module-real-estate-real-estate-core-flutter      | [Core](../core/real-estate-core.md)      | [API](../api/real-estate-core.md)      |
| [Sales Progression](sales-progression.md)         | module-real-estate-sales-progression-flutter     | [Core](../core/sales-progression.md)     | [API](../api/sales-progression.md)     |
| [Valuations](valuations.md)                       | module-real-estate-valuations-flutter            | [Core](../core/valuations.md)            | [API](../api/valuations.md)            |
| [Viewings](viewings.md)                           | module-real-estate-viewings-flutter              | [Core](../core/viewings.md)              | [API](../api/viewings.md)              |
