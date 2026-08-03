# Maintenance React Native + Expo implementations

**Scope:** [Maintenance](../MAINTENANCE.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [React Native technology](../../../technologies/REACT-NATIVE.md) · [React Native standard](../../../standards/REACT-NATIVE.md)

This index defines the optional React Native + Expo adapter boundary for the Maintenance project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 14 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                  | Package                                                  | Core                                        | API                                       |
| ------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------- | ----------------------------------------- |
| [Assets](assets.md)                                     | module-maintenance-assets-react-native                   | [Core](../core/assets.md)                   | [API](../api/assets.md)                   |
| [Commercial](commercial.md)                             | module-maintenance-commercial-react-native               | [Core](../core/commercial.md)               | [API](../api/commercial.md)               |
| [Compliance](compliance.md)                             | module-maintenance-compliance-react-native               | [Core](../core/compliance.md)               | [API](../api/compliance.md)               |
| [Customers And Sites](customers-and-sites.md)           | module-maintenance-customers-and-sites-react-native      | [Core](../core/customers-and-sites.md)      | [API](../api/customers-and-sites.md)      |
| [Inspections](inspections.md)                           | module-maintenance-inspections-react-native              | [Core](../core/inspections.md)              | [API](../api/inspections.md)              |
| [Inventory](inventory.md)                               | module-maintenance-inventory-react-native                | [Core](../core/inventory.md)                | [API](../api/inventory.md)                |
| [Labor And Time](labor-and-time.md)                     | module-maintenance-labor-and-time-react-native           | [Core](../core/labor-and-time.md)           | [API](../api/labor-and-time.md)           |
| [Maintenance Core](maintenance-core.md)                 | module-maintenance-maintenance-core-react-native         | [Core](../core/maintenance-core.md)         | [API](../api/maintenance-core.md)         |
| [Portals](portals.md)                                   | module-maintenance-portals-react-native                  | [Core](../core/portals.md)                  | [API](../api/portals.md)                  |
| [Preventative Maintenance](preventative-maintenance.md) | module-maintenance-preventative-maintenance-react-native | [Core](../core/preventative-maintenance.md) | [API](../api/preventative-maintenance.md) |
| [Procurement](procurement.md)                           | module-maintenance-procurement-react-native              | [Core](../core/procurement.md)              | [API](../api/procurement.md)              |
| [Reporting](reporting.md)                               | module-maintenance-reporting-react-native                | [Core](../core/reporting.md)                | [API](../api/reporting.md)                |
| [Scheduling](scheduling.md)                             | module-maintenance-scheduling-react-native               | [Core](../core/scheduling.md)               | [API](../api/scheduling.md)               |
| [Work Orders](work-orders.md)                           | module-maintenance-work-orders-react-native              | [Core](../core/work-orders.md)              | [API](../api/work-orders.md)              |
