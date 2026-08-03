# Ecommerce Flutter + Dart implementations

**Scope:** [Ecommerce](../ECOMMERCE.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Ecommerce project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 105 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                              | Package                                                 | Core                                              | API                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------- |
| [Abandoned Checkout](abandoned-checkout.md)                         | module-ecommerce-abandoned-checkout-flutter             | [Core](../core/abandoned-checkout.md)             | [API](../api/abandoned-checkout.md)             |
| [App Marketplace](app-marketplace.md)                               | module-ecommerce-app-marketplace-flutter                | [Core](../core/app-marketplace.md)                | [API](../api/app-marketplace.md)                |
| [Attribution And Analytics](attribution-and-analytics.md)           | module-ecommerce-attribution-and-analytics-flutter      | [Core](../core/attribution-and-analytics.md)      | [API](../api/attribution-and-analytics.md)      |
| [Availability](availability.md)                                     | module-ecommerce-availability-flutter                   | [Core](../core/availability.md)                   | [API](../api/availability.md)                   |
| [B2b Purchasing Rules](b2b-purchasing-rules.md)                     | module-ecommerce-b2b-purchasing-rules-flutter           | [Core](../core/b2b-purchasing-rules.md)           | [API](../api/b2b-purchasing-rules.md)           |
| [B2b Self Service](b2b-self-service.md)                             | module-ecommerce-b2b-self-service-flutter               | [Core](../core/b2b-self-service.md)               | [API](../api/b2b-self-service.md)               |
| [Back In Stock And Price Alerts](back-in-stock-and-price-alerts.md) | module-ecommerce-back-in-stock-and-price-alerts-flutter | [Core](../core/back-in-stock-and-price-alerts.md) | [API](../api/back-in-stock-and-price-alerts.md) |
| [Bookings And Appointments](bookings-and-appointments.md)           | module-ecommerce-bookings-and-appointments-flutter      | [Core](../core/bookings-and-appointments.md)      | [API](../api/bookings-and-appointments.md)      |
| [Bundles And Kits](bundles-and-kits.md)                             | module-ecommerce-bundles-and-kits-flutter               | [Core](../core/bundles-and-kits.md)               | [API](../api/bundles-and-kits.md)               |
| [Carrier Operations](carrier-operations.md)                         | module-ecommerce-carrier-operations-flutter             | [Core](../core/carrier-operations.md)             | [API](../api/carrier-operations.md)             |
| [Cart](cart.md)                                                     | module-ecommerce-cart-flutter                           | [Core](../core/cart.md)                           | [API](../api/cart.md)                           |
| [Cash Management](cash-management.md)                               | module-ecommerce-cash-management-flutter                | [Core](../core/cash-management.md)                | [API](../api/cash-management.md)                |
| [Catalog Import And Export](catalog-import-and-export.md)           | module-ecommerce-catalog-import-and-export-flutter      | [Core](../core/catalog-import-and-export.md)      | [API](../api/catalog-import-and-export.md)      |
| [Catalog Staging](catalog-staging.md)                               | module-ecommerce-catalog-staging-flutter                | [Core](../core/catalog-staging.md)                | [API](../api/catalog-staging.md)                |
| [Catalog](catalog.md)                                               | module-ecommerce-catalog-flutter                        | [Core](../core/catalog.md)                        | [API](../api/catalog.md)                        |
| [Categories And Navigation](categories-and-navigation.md)           | module-ecommerce-categories-and-navigation-flutter      | [Core](../core/categories-and-navigation.md)      | [API](../api/categories-and-navigation.md)      |
| [Checkout Extensibility](checkout-extensibility.md)                 | module-ecommerce-checkout-extensibility-flutter         | [Core](../core/checkout-extensibility.md)         | [API](../api/checkout-extensibility.md)         |
| [Checkout](checkout.md)                                             | module-ecommerce-checkout-flutter                       | [Core](../core/checkout.md)                       | [API](../api/checkout.md)                       |
| [Commerce Automation Pack](commerce-automation-pack.md)             | module-ecommerce-commerce-automation-pack-flutter       | [Core](../core/commerce-automation-pack.md)       | [API](../api/commerce-automation-pack.md)       |
| [Commerce Copilot](commerce-copilot.md)                             | module-ecommerce-commerce-copilot-flutter               | [Core](../core/commerce-copilot.md)               | [API](../api/commerce-copilot.md)               |
| [Commerce Core](commerce-core.md)                                   | module-ecommerce-commerce-core-flutter                  | [Core](../core/commerce-core.md)                  | [API](../api/commerce-core.md)                  |
| [Commerce Customers](commerce-customers.md)                         | module-ecommerce-commerce-customers-flutter             | [Core](../core/commerce-customers.md)             | [API](../api/commerce-customers.md)             |
| [Commerce Extensions](commerce-extensions.md)                       | module-ecommerce-commerce-extensions-flutter            | [Core](../core/commerce-extensions.md)            | [API](../api/commerce-extensions.md)            |
| [Commerce Functions](commerce-functions.md)                         | module-ecommerce-commerce-functions-flutter             | [Core](../core/commerce-functions.md)             | [API](../api/commerce-functions.md)             |
| [Commissions And Settlements](commissions-and-settlements.md)       | module-ecommerce-commissions-and-settlements-flutter    | [Core](../core/commissions-and-settlements.md)    | [API](../api/commissions-and-settlements.md)    |
| [Companies](companies.md)                                           | module-ecommerce-companies-flutter                      | [Core](../core/companies.md)                      | [API](../api/companies.md)                      |
| [Cross Border](cross-border.md)                                     | module-ecommerce-cross-border-flutter                   | [Core](../core/cross-border.md)                   | [API](../api/cross-border.md)                   |
| [Customer Accounts](customer-accounts.md)                           | module-ecommerce-customer-accounts-flutter              | [Core](../core/customer-accounts.md)              | [API](../api/customer-accounts.md)              |
| [Customer Service Workspace](customer-service-workspace.md)         | module-ecommerce-customer-service-workspace-flutter     | [Core](../core/customer-service-workspace.md)     | [API](../api/customer-service-workspace.md)     |
| [Delivery Promises](delivery-promises.md)                           | module-ecommerce-delivery-promises-flutter              | [Core](../core/delivery-promises.md)              | [API](../api/delivery-promises.md)              |
| [Digital Assets](digital-assets.md)                                 | module-ecommerce-digital-assets-flutter                 | [Core](../core/digital-assets.md)                 | [API](../api/digital-assets.md)                 |
| [Digital Fulfillment](digital-fulfillment.md)                       | module-ecommerce-digital-fulfillment-flutter            | [Core](../core/digital-fulfillment.md)            | [API](../api/digital-fulfillment.md)            |
| [Donations](donations.md)                                           | module-ecommerce-donations-flutter                      | [Core](../core/donations.md)                      | [API](../api/donations.md)                      |
| [Draft And Assisted Orders](draft-and-assisted-orders.md)           | module-ecommerce-draft-and-assisted-orders-flutter      | [Core](../core/draft-and-assisted-orders.md)      | [API](../api/draft-and-assisted-orders.md)      |
| [Dropshipping](dropshipping.md)                                     | module-ecommerce-dropshipping-flutter                   | [Core](../core/dropshipping.md)                   | [API](../api/dropshipping.md)                   |
| [Exchanges](exchanges.md)                                           | module-ecommerce-exchanges-flutter                      | [Core](../core/exchanges.md)                      | [API](../api/exchanges.md)                      |
| [Express Checkout](express-checkout.md)                             | module-ecommerce-express-checkout-flutter               | [Core](../core/express-checkout.md)               | [API](../api/express-checkout.md)               |
| [Feed Management](feed-management.md)                               | module-ecommerce-feed-management-flutter                | [Core](../core/feed-management.md)                | [API](../api/feed-management.md)                |
| [Fraud And Risk](fraud-and-risk.md)                                 | module-ecommerce-fraud-and-risk-flutter                 | [Core](../core/fraud-and-risk.md)                 | [API](../api/fraud-and-risk.md)                 |
| [Fraud Intelligence](fraud-intelligence.md)                         | module-ecommerce-fraud-intelligence-flutter             | [Core](../core/fraud-intelligence.md)             | [API](../api/fraud-intelligence.md)             |
| [Fulfillment](fulfillment.md)                                       | module-ecommerce-fulfillment-flutter                    | [Core](../core/fulfillment.md)                    | [API](../api/fulfillment.md)                    |
| [Gift Cards And Store Credit](gift-cards-and-store-credit.md)       | module-ecommerce-gift-cards-and-store-credit-flutter    | [Core](../core/gift-cards-and-store-credit.md)    | [API](../api/gift-cards-and-store-credit.md)    |
| [Inventory Counting](inventory-counting.md)                         | module-ecommerce-inventory-counting-flutter             | [Core](../core/inventory-counting.md)             | [API](../api/inventory-counting.md)             |
| [Inventory Ledger](inventory-ledger.md)                             | module-ecommerce-inventory-ledger-flutter               | [Core](../core/inventory-ledger.md)               | [API](../api/inventory-ledger.md)               |
| [Invoices And Documents](invoices-and-documents.md)                 | module-ecommerce-invoices-and-documents-flutter         | [Core](../core/invoices-and-documents.md)         | [API](../api/invoices-and-documents.md)         |
| [Localization](localization.md)                                     | module-ecommerce-localization-flutter                   | [Core](../core/localization.md)                   | [API](../api/localization.md)                   |
| [Lots And Serials](lots-and-serials.md)                             | module-ecommerce-lots-and-serials-flutter               | [Core](../core/lots-and-serials.md)               | [API](../api/lots-and-serials.md)               |
| [Loyalty](loyalty.md)                                               | module-ecommerce-loyalty-flutter                        | [Core](../core/loyalty.md)                        | [API](../api/loyalty.md)                        |
| [Marketplace Channels](marketplace-channels.md)                     | module-ecommerce-marketplace-channels-flutter           | [Core](../core/marketplace-channels.md)           | [API](../api/marketplace-channels.md)           |
| [Marketplace Orders](marketplace-orders.md)                         | module-ecommerce-marketplace-orders-flutter             | [Core](../core/marketplace-orders.md)             | [API](../api/marketplace-orders.md)             |
| [Markets](markets.md)                                               | module-ecommerce-markets-flutter                        | [Core](../core/markets.md)                        | [API](../api/markets.md)                        |
| [Membership Commerce](membership-commerce.md)                       | module-ecommerce-membership-commerce-flutter            | [Core](../core/membership-commerce.md)            | [API](../api/membership-commerce.md)            |
| [Merchandising Intelligence](merchandising-intelligence.md)         | module-ecommerce-merchandising-intelligence-flutter     | [Core](../core/merchandising-intelligence.md)     | [API](../api/merchandising-intelligence.md)     |
| [Merchandising](merchandising.md)                                   | module-ecommerce-merchandising-flutter                  | [Core](../core/merchandising.md)                  | [API](../api/merchandising.md)                  |
| [Migration Framework](migration-framework.md)                       | module-ecommerce-migration-framework-flutter            | [Core](../core/migration-framework.md)            | [API](../api/migration-framework.md)            |
| [Multi Source Inventory](multi-source-inventory.md)                 | module-ecommerce-multi-source-inventory-flutter         | [Core](../core/multi-source-inventory.md)         | [API](../api/multi-source-inventory.md)         |
| [Multi Tender Payments](multi-tender-payments.md)                   | module-ecommerce-multi-tender-payments-flutter          | [Core](../core/multi-tender-payments.md)          | [API](../api/multi-tender-payments.md)          |
| [Negotiated Quotes](negotiated-quotes.md)                           | module-ecommerce-negotiated-quotes-flutter              | [Core](../core/negotiated-quotes.md)              | [API](../api/negotiated-quotes.md)              |
| [Offline Pos](offline-pos.md)                                       | module-ecommerce-offline-pos-flutter                    | [Core](../core/offline-pos.md)                    | [API](../api/offline-pos.md)                    |
| [Options And Customization](options-and-customization.md)           | module-ecommerce-options-and-customization-flutter      | [Core](../core/options-and-customization.md)      | [API](../api/options-and-customization.md)      |
| [Order Editing](order-editing.md)                                   | module-ecommerce-order-editing-flutter                  | [Core](../core/order-editing.md)                  | [API](../api/order-editing.md)                  |
| [Order Orchestration](order-orchestration.md)                       | module-ecommerce-order-orchestration-flutter            | [Core](../core/order-orchestration.md)            | [API](../api/order-orchestration.md)            |
| [Order Tracking](order-tracking.md)                                 | module-ecommerce-order-tracking-flutter                 | [Core](../core/order-tracking.md)                 | [API](../api/order-tracking.md)                 |
| [Orders](orders.md)                                                 | module-ecommerce-orders-flutter                         | [Core](../core/orders.md)                         | [API](../api/orders.md)                         |
| [Payment Operations](payment-operations.md)                         | module-ecommerce-payment-operations-flutter             | [Core](../core/payment-operations.md)             | [API](../api/payment-operations.md)             |
| [Payments](payments.md)                                             | module-ecommerce-payments-flutter                       | [Core](../core/payments.md)                       | [API](../api/payments.md)                       |
| [Personalization](personalization.md)                               | module-ecommerce-personalization-flutter                | [Core](../core/personalization.md)                | [API](../api/personalization.md)                |
| [Pickup And Local Delivery](pickup-and-local-delivery.md)           | module-ecommerce-pickup-and-local-delivery-flutter      | [Core](../core/pickup-and-local-delivery.md)      | [API](../api/pickup-and-local-delivery.md)      |
| [Point Of Sale](point-of-sale.md)                                   | module-ecommerce-point-of-sale-flutter                  | [Core](../core/point-of-sale.md)                  | [API](../api/point-of-sale.md)                  |
| [Pos Devices](pos-devices.md)                                       | module-ecommerce-pos-devices-flutter                    | [Core](../core/pos-devices.md)                    | [API](../api/pos-devices.md)                    |
| [Post Purchase Experience](post-purchase-experience.md)             | module-ecommerce-post-purchase-experience-flutter       | [Core](../core/post-purchase-experience.md)       | [API](../api/post-purchase-experience.md)       |
| [Pricing Rules](pricing-rules.md)                                   | module-ecommerce-pricing-rules-flutter                  | [Core](../core/pricing-rules.md)                  | [API](../api/pricing-rules.md)                  |
| [Pricing](pricing.md)                                               | module-ecommerce-pricing-flutter                        | [Core](../core/pricing.md)                        | [API](../api/pricing.md)                        |
| [Product Comparison](product-comparison.md)                         | module-ecommerce-product-comparison-flutter             | [Core](../core/product-comparison.md)             | [API](../api/product-comparison.md)             |
| [Product Information Management](product-information-management.md) | module-ecommerce-product-information-management-flutter | [Core](../core/product-information-management.md) | [API](../api/product-information-management.md) |
| [Product Types](product-types.md)                                   | module-ecommerce-product-types-flutter                  | [Core](../core/product-types.md)                  | [API](../api/product-types.md)                  |
| [Promotions](promotions.md)                                         | module-ecommerce-promotions-flutter                     | [Core](../core/promotions.md)                     | [API](../api/promotions.md)                     |
| [Purchase Orders](purchase-orders.md)                               | module-ecommerce-purchase-orders-flutter                | [Core](../core/purchase-orders.md)                | [API](../api/purchase-orders.md)                |
| [Quick Order](quick-order.md)                                       | module-ecommerce-quick-order-flutter                    | [Core](../core/quick-order.md)                    | [API](../api/quick-order.md)                    |
| [Recommendations](recommendations.md)                               | module-ecommerce-recommendations-flutter                | [Core](../core/recommendations.md)                | [API](../api/recommendations.md)                |
| [Recurring Orders](recurring-orders.md)                             | module-ecommerce-recurring-orders-flutter               | [Core](../core/recurring-orders.md)               | [API](../api/recurring-orders.md)               |
| [Referrals](referrals.md)                                           | module-ecommerce-referrals-flutter                      | [Core](../core/referrals.md)                      | [API](../api/referrals.md)                      |
| [Refunds](refunds.md)                                               | module-ecommerce-refunds-flutter                        | [Core](../core/refunds.md)                        | [API](../api/refunds.md)                        |
| [Rentals](rentals.md)                                               | module-ecommerce-rentals-flutter                        | [Core](../core/rentals.md)                        | [API](../api/rentals.md)                        |
| [Reporting](reporting.md)                                           | module-ecommerce-reporting-flutter                      | [Core](../core/reporting.md)                      | [API](../api/reporting.md)                      |
| [Reservations](reservations.md)                                     | module-ecommerce-reservations-flutter                   | [Core](../core/reservations.md)                   | [API](../api/reservations.md)                   |
| [Retail Locations](retail-locations.md)                             | module-ecommerce-retail-locations-flutter               | [Core](../core/retail-locations.md)               | [API](../api/retail-locations.md)               |
| [Returns](returns.md)                                               | module-ecommerce-returns-flutter                        | [Core](../core/returns.md)                        | [API](../api/returns.md)                        |
| [Reviews And Ratings](reviews-and-ratings.md)                       | module-ecommerce-reviews-and-ratings-flutter            | [Core](../core/reviews-and-ratings.md)            | [API](../api/reviews-and-ratings.md)            |
| [Sales Channels](sales-channels.md)                                 | module-ecommerce-sales-channels-flutter                 | [Core](../core/sales-channels.md)                 | [API](../api/sales-channels.md)                 |
| [Sales Representative Workspace](sales-representative-workspace.md) | module-ecommerce-sales-representative-workspace-flutter | [Core](../core/sales-representative-workspace.md) | [API](../api/sales-representative-workspace.md) |
| [Sandbox And Release](sandbox-and-release.md)                       | module-ecommerce-sandbox-and-release-flutter            | [Core](../core/sandbox-and-release.md)            | [API](../api/sandbox-and-release.md)            |
| [Saved Lists](saved-lists.md)                                       | module-ecommerce-saved-lists-flutter                    | [Core](../core/saved-lists.md)                    | [API](../api/saved-lists.md)                    |
| [Search And Discovery](search-and-discovery.md)                     | module-ecommerce-search-and-discovery-flutter           | [Core](../core/search-and-discovery.md)           | [API](../api/search-and-discovery.md)           |
| [Seller Marketplace](seller-marketplace.md)                         | module-ecommerce-seller-marketplace-flutter             | [Core](../core/seller-marketplace.md)             | [API](../api/seller-marketplace.md)             |
| [Shared Catalogs](shared-catalogs.md)                               | module-ecommerce-shared-catalogs-flutter                | [Core](../core/shared-catalogs.md)                | [API](../api/shared-catalogs.md)                |
| [Shipping](shipping.md)                                             | module-ecommerce-shipping-flutter                       | [Core](../core/shipping.md)                       | [API](../api/shipping.md)                       |
| [Social Commerce](social-commerce.md)                               | module-ecommerce-social-commerce-flutter                | [Core](../core/social-commerce.md)                | [API](../api/social-commerce.md)                |
| [Store Templates](store-templates.md)                               | module-ecommerce-store-templates-flutter                | [Core](../core/store-templates.md)                | [API](../api/store-templates.md)                |
| [Subscription Commerce](subscription-commerce.md)                   | module-ecommerce-subscription-commerce-flutter          | [Core](../core/subscription-commerce.md)          | [API](../api/subscription-commerce.md)          |
| [Tax](tax.md)                                                       | module-ecommerce-tax-flutter                            | [Core](../core/tax.md)                            | [API](../api/tax.md)                            |
| [Transfers And Replenishment](transfers-and-replenishment.md)       | module-ecommerce-transfers-and-replenishment-flutter    | [Core](../core/transfers-and-replenishment.md)    | [API](../api/transfers-and-replenishment.md)    |
| [Unified Commerce](unified-commerce.md)                             | module-ecommerce-unified-commerce-flutter               | [Core](../core/unified-commerce.md)               | [API](../api/unified-commerce.md)               |
| [Warehouse Operations](warehouse-operations.md)                     | module-ecommerce-warehouse-operations-flutter           | [Core](../core/warehouse-operations.md)           | [API](../api/warehouse-operations.md)           |
| [Warranty And Claims](warranty-and-claims.md)                       | module-ecommerce-warranty-and-claims-flutter            | [Core](../core/warranty-and-claims.md)            | [API](../api/warranty-and-claims.md)            |
