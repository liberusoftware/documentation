# Billing Flutter + Dart implementations

**Scope:** [Billing](../BILLING.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Billing project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

| Module                                | Package                                | Core                               | API                              |
| ------------------------------------- | -------------------------------------- | ---------------------------------- | -------------------------------- |
| [Billing Core](billing-core.md)       | module-billing-billing-core-flutter    | [Core](../core/billing-core.md)    | [API](../api/billing-core.md)    |
| [Catalog](catalog.md)                 | module-billing-catalog-flutter         | [Core](../core/catalog.md)         | [API](../api/catalog.md)         |
| [Collections](collections.md)         | module-billing-collections-flutter     | [Core](../core/collections.md)     | [API](../api/collections.md)     |
| [Communications](communications.md)   | module-billing-communications-flutter  | [Core](../core/communications.md)  | [API](../api/communications.md)  |
| [Customer Portal](customer-portal.md) | module-billing-customer-portal-flutter | [Core](../core/customer-portal.md) | [API](../api/customer-portal.md) |
| [Domains](domains.md)                 | module-billing-domains-flutter         | [Core](../core/domains.md)         | [API](../api/domains.md)         |
| [Hosting](hosting.md)                 | module-billing-hosting-flutter         | [Core](../core/hosting.md)         | [API](../api/hosting.md)         |
| [Invoicing](invoicing.md)             | module-billing-invoicing-flutter       | [Core](../core/invoicing.md)       | [API](../api/invoicing.md)       |
| [Isp](isp.md)                         | module-billing-isp-flutter             | [Core](../core/isp.md)             | [API](../api/isp.md)             |
| [Orders](orders.md)                   | module-billing-orders-flutter          | [Core](../core/orders.md)          | [API](../api/orders.md)          |
| [Payments](payments.md)               | module-billing-payments-flutter        | [Core](../core/payments.md)        | [API](../api/payments.md)        |
| [Pricing](pricing.md)                 | module-billing-pricing-flutter         | [Core](../core/pricing.md)         | [API](../api/pricing.md)         |
| [Provisioning](provisioning.md)       | module-billing-provisioning-flutter    | [Core](../core/provisioning.md)    | [API](../api/provisioning.md)    |
| [Reporting](reporting.md)             | module-billing-reporting-flutter       | [Core](../core/reporting.md)       | [API](../api/reporting.md)       |
| [Subscriptions](subscriptions.md)     | module-billing-subscriptions-flutter   | [Core](../core/subscriptions.md)   | [API](../api/subscriptions.md)   |
| [Usage](usage.md)                     | module-billing-usage-flutter           | [Core](../core/usage.md)           | [API](../api/usage.md)           |
