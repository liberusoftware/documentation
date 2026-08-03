# SAP-style Enterprise Suite Flutter + Dart implementations

**Scope:** [SAP-style Enterprise Suite](../SAP.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the SAP-style Enterprise Suite project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 16 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                              | Package                                           | Core                                              | API                                             |
| ------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------- |
| [Assets And Facilities](assets-and-facilities.md)                   | module-sap-assets-and-facilities-flutter          | [Core](../core/assets-and-facilities.md)          | [API](../api/assets-and-facilities.md)          |
| [Controlling](controlling.md)                                       | module-sap-controlling-flutter                    | [Core](../core/controlling.md)                    | [API](../api/controlling.md)                    |
| [Data And Intelligence](data-and-intelligence.md)                   | module-sap-data-and-intelligence-flutter          | [Core](../core/data-and-intelligence.md)          | [API](../api/data-and-intelligence.md)          |
| [Enterprise Foundation](enterprise-foundation.md)                   | module-sap-enterprise-foundation-flutter          | [Core](../core/enterprise-foundation.md)          | [API](../api/enterprise-foundation.md)          |
| [Finance](finance.md)                                               | module-sap-finance-flutter                        | [Core](../core/finance.md)                        | [API](../api/finance.md)                        |
| [Governance Risk And Compliance](governance-risk-and-compliance.md) | module-sap-governance-risk-and-compliance-flutter | [Core](../core/governance-risk-and-compliance.md) | [API](../api/governance-risk-and-compliance.md) |
| [Hosting And Cloud](hosting-and-cloud.md)                           | module-sap-hosting-and-cloud-flutter              | [Core](../core/hosting-and-cloud.md)              | [API](../api/hosting-and-cloud.md)              |
| [Inventory And Logistics](inventory-and-logistics.md)               | module-sap-inventory-and-logistics-flutter        | [Core](../core/inventory-and-logistics.md)        | [API](../api/inventory-and-logistics.md)        |
| [Partners And Portals](partners-and-portals.md)                     | module-sap-partners-and-portals-flutter           | [Core](../core/partners-and-portals.md)           | [API](../api/partners-and-portals.md)           |
| [People](people.md)                                                 | module-sap-people-flutter                         | [Core](../core/people.md)                         | [API](../api/people.md)                         |
| [Procurement](procurement.md)                                       | module-sap-procurement-flutter                    | [Core](../core/procurement.md)                    | [API](../api/procurement.md)                    |
| [Product And Engineering](product-and-engineering.md)               | module-sap-product-and-engineering-flutter        | [Core](../core/product-and-engineering.md)        | [API](../api/product-and-engineering.md)        |
| [Projects And Services](projects-and-services.md)                   | module-sap-projects-and-services-flutter          | [Core](../core/projects-and-services.md)          | [API](../api/projects-and-services.md)          |
| [Revenue Operations](revenue-operations.md)                         | module-sap-revenue-operations-flutter             | [Core](../core/revenue-operations.md)             | [API](../api/revenue-operations.md)             |
| [Sales And Crm](sales-and-crm.md)                                   | module-sap-sales-and-crm-flutter                  | [Core](../core/sales-and-crm.md)                  | [API](../api/sales-and-crm.md)                  |
| [Service Management](service-management.md)                         | module-sap-service-management-flutter             | [Core](../core/service-management.md)             | [API](../api/service-management.md)             |
