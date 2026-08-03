# Real Estate React Native + Expo implementations

**Scope:** [Real Estate](../REAL-ESTATE.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [React Native technology](../../../technologies/REACT-NATIVE.md) · [React Native standard](../../../standards/REACT-NATIVE.md)

This index defines the optional React Native + Expo adapter boundary for the Real Estate project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-react-native`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [React Native + Expo module standard](../../../modules/react-native/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 15 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                            | Package                                               | Core                                     | API                                    |
| ------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------- | -------------------------------------- |
| [Instructions](instructions.md)                   | module-real-estate-instructions-react-native          | [Core](../core/instructions.md)          | [API](../api/instructions.md)          |
| [Lettings](lettings.md)                           | module-real-estate-lettings-react-native              | [Core](../core/lettings.md)              | [API](../api/lettings.md)              |
| [Listings](listings.md)                           | module-real-estate-listings-react-native              | [Core](../core/listings.md)              | [API](../api/listings.md)              |
| [Marketing](marketing.md)                         | module-real-estate-marketing-react-native             | [Core](../core/marketing.md)             | [API](../api/marketing.md)             |
| [Matching](matching.md)                           | module-real-estate-matching-react-native              | [Core](../core/matching.md)              | [API](../api/matching.md)              |
| [Media And Documents](media-and-documents.md)     | module-real-estate-media-and-documents-react-native   | [Core](../core/media-and-documents.md)   | [API](../api/media-and-documents.md)   |
| [Offers](offers.md)                               | module-real-estate-offers-react-native                | [Core](../core/offers.md)                | [API](../api/offers.md)                |
| [Parties](parties.md)                             | module-real-estate-parties-react-native               | [Core](../core/parties.md)               | [API](../api/parties.md)               |
| [Portals And Reporting](portals-and-reporting.md) | module-real-estate-portals-and-reporting-react-native | [Core](../core/portals-and-reporting.md) | [API](../api/portals-and-reporting.md) |
| [Properties](properties.md)                       | module-real-estate-properties-react-native            | [Core](../core/properties.md)            | [API](../api/properties.md)            |
| [Property Management](property-management.md)     | module-real-estate-property-management-react-native   | [Core](../core/property-management.md)   | [API](../api/property-management.md)   |
| [Real Estate Core](real-estate-core.md)           | module-real-estate-real-estate-core-react-native      | [Core](../core/real-estate-core.md)      | [API](../api/real-estate-core.md)      |
| [Sales Progression](sales-progression.md)         | module-real-estate-sales-progression-react-native     | [Core](../core/sales-progression.md)     | [API](../api/sales-progression.md)     |
| [Valuations](valuations.md)                       | module-real-estate-valuations-react-native            | [Core](../core/valuations.md)            | [API](../api/valuations.md)            |
| [Viewings](viewings.md)                           | module-real-estate-viewings-react-native              | [Core](../core/viewings.md)              | [API](../api/viewings.md)              |
