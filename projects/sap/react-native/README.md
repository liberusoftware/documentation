# SAP-style Enterprise Suite React Native + Expo implementations

<!-- catalogue-status:start -->
This index preserves **16 module documents/spellings**. Counts are specifications, not released packages or deployed features. Exact source identities and aliases are in the [source map](../SOURCE-MAPPING.md); [shared ownership](../../../architecture/SHARED-MODULES.md) and [Next.js adapter homes](../../../modules/nextjs/OWNERSHIP.md) prevent alternate spellings from becoming competing implementations.
<!-- catalogue-status:end -->

**Scope:** [SAP-style Enterprise Suite](../SAP.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [React Native technology](../../../technologies/REACT-NATIVE.md) · [React Native standard](../../../standards/REACT-NATIVE.md)

This index defines the optional React Native + Expo adapter boundary for the SAP-style Enterprise Suite project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 16 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module document | Source/target reference | Related plans |
| --- | --- | --- |
| [React Native design](assets-and-facilities.md) | [Target/source map](../SOURCE-MAPPING.md#assets-and-facilities) | [core](../core/assets-and-facilities.md) · [api](../api/assets-and-facilities.md) · [nextjs](../nextjs/assets-and-facilities.md) |
| [React Native design](controlling.md) | [Target/source map](../SOURCE-MAPPING.md#controlling) | [core](../core/controlling.md) · [api](../api/controlling.md) · [nextjs](../nextjs/controlling.md) |
| [React Native design](data-and-intelligence.md) | [Target/source map](../SOURCE-MAPPING.md#data-and-intelligence) | [core](../core/data-and-intelligence.md) · [api](../api/data-and-intelligence.md) · [nextjs](../nextjs/data-and-intelligence.md) |
| [React Native design](enterprise-foundation.md) | [Target/source map](../SOURCE-MAPPING.md#enterprise-foundation) | [core](../core/enterprise-foundation.md) · [api](../api/enterprise-foundation.md) · [nextjs](../nextjs/enterprise-foundation.md) |
| [React Native design](finance.md) | [Target/source map](../SOURCE-MAPPING.md#finance) | [core](../core/finance.md) · [api](../api/finance.md) · [nextjs](../nextjs/finance.md) |
| [React Native design](governance-risk-and-compliance.md) | [Target/source map](../SOURCE-MAPPING.md#governance-risk-and-compliance) | [core](../core/governance-risk-and-compliance.md) · [api](../api/governance-risk-and-compliance.md) · [nextjs](../nextjs/governance-risk-and-compliance.md) |
| [React Native design](hosting-and-cloud.md) | [Target/source map](../SOURCE-MAPPING.md#hosting-and-cloud) | [core](../core/hosting-and-cloud.md) · [api](../api/hosting-and-cloud.md) · [nextjs](../nextjs/hosting-and-cloud.md) |
| [React Native design](inventory-and-logistics.md) | [Target/source map](../SOURCE-MAPPING.md#inventory-and-logistics) | [core](../core/inventory-and-logistics.md) · [api](../api/inventory-and-logistics.md) · [nextjs](../nextjs/inventory-and-logistics.md) |
| [React Native design](partners-and-portals.md) | [Target/source map](../SOURCE-MAPPING.md#partners-and-portals) | [core](../core/partners-and-portals.md) · [api](../api/partners-and-portals.md) · [nextjs](../nextjs/partners-and-portals.md) |
| [React Native design](people.md) | [Target/source map](../SOURCE-MAPPING.md#people) | [core](../core/people.md) · [api](../api/people.md) · [nextjs](../nextjs/people.md) |
| [React Native design](procurement.md) | [Target/source map](../SOURCE-MAPPING.md#procurement) | [core](../core/procurement.md) · [api](../api/procurement.md) · [nextjs](../nextjs/procurement.md) |
| [React Native design](product-and-engineering.md) | [Target/source map](../SOURCE-MAPPING.md#product-and-engineering) | [core](../core/product-and-engineering.md) · [api](../api/product-and-engineering.md) · [nextjs](../nextjs/product-and-engineering.md) |
| [React Native design](projects-and-services.md) | [Target/source map](../SOURCE-MAPPING.md#projects-and-services) | [core](../core/projects-and-services.md) · [api](../api/projects-and-services.md) · [nextjs](../nextjs/projects-and-services.md) |
| [React Native design](revenue-operations.md) | [Target/source map](../SOURCE-MAPPING.md#revenue-operations) | [core](../core/revenue-operations.md) · [api](../api/revenue-operations.md) · [nextjs](../nextjs/revenue-operations.md) |
| [React Native design](sales-and-crm.md) | [Target/source map](../SOURCE-MAPPING.md#sales-and-crm) | [core](../core/sales-and-crm.md) · [api](../api/sales-and-crm.md) · [nextjs](../nextjs/sales-and-crm.md) |
| [React Native design](service-management.md) | [Target/source map](../SOURCE-MAPPING.md#service-management) | [core](../core/service-management.md) · [api](../api/service-management.md) · [nextjs](../nextjs/service-management.md) |
