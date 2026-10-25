# Ecommerce: design and source reconciliation

This map connects existing design filenames to observed package identities. Matching is based on exact/local naming patterns plus the documented foundation aliases below; it is navigation evidence, not proof of equivalent behavior or complete implementation. Read the source reference before using a proposed field, endpoint, permission or installation example.

**Preservation rule:** all existing product scopes and module documents remain in place. A blank package match means only that this scan did not find a dedicated manifest under the expected naming pattern; implementation can exist elsewhere or use another identity.

Ecommerce has application-owned implementations outside the immediate package folder. Use the [application capability map](SOURCE-APPLICATION.md) and retain the [full catalogue](ECOMMERCE.md). Every blank row below preserves the existing module design; it is not a recommendation to remove that module.

## Read the mapping

Core/API/Filament/Livewire columns show dedicated observed identities where names match. JavaScript/mobile source matches are recorded in the JSON index and individual annotations when present. An adapter can also be application-owned or ship assets through a PHP package; absence of a dedicated npm manifest does not establish absence of UI.

Multiple matches are left visible for review. Repeated design spellings may point to the same package; they must not become independent competing owners. Installation uses the observed manifest name, not a generated design slug.

| Design scope | Core source reference | API source reference | Filament source reference | Livewire source reference |
| --- | --- | --- | --- | --- |
| <a id="abandoned-checkout"></a>[abandoned-checkout](features/abandoned-checkout.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="app-marketplace"></a>[app-marketplace](features/app-marketplace.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="attribution-and-analytics"></a>[attribution-and-analytics](features/attribution-and-analytics.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="availability"></a>[availability](features/availability.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="b2b-purchasing-rules"></a>[b2b-purchasing-rules](features/b2b-purchasing-rules.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="b2b-self-service"></a>[b2b-self-service](features/b2b-self-service.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="back-in-stock-and-price-alerts"></a>[back-in-stock-and-price-alerts](features/back-in-stock-and-price-alerts.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="bookings-and-appointments"></a>[bookings-and-appointments](features/bookings-and-appointments.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="bundles-and-kits"></a>[bundles-and-kits](features/bundles-and-kits.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="carrier-operations"></a>[carrier-operations](features/carrier-operations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="cart"></a>[cart](features/cart.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="cash-management"></a>[cash-management](features/cash-management.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="catalog"></a>[catalog](features/catalog.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="catalog-import-and-export"></a>[catalog-import-and-export](features/catalog-import-and-export.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="catalog-staging"></a>[catalog-staging](features/catalog-staging.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="categories-and-navigation"></a>[categories-and-navigation](features/categories-and-navigation.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="checkout"></a>[checkout](features/checkout.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="checkout-extensibility"></a>[checkout-extensibility](features/checkout-extensibility.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="commerce-automation-pack"></a>[commerce-automation-pack](features/commerce-automation-pack.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="commerce-copilot"></a>[commerce-copilot](features/commerce-copilot.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="commerce-core"></a>[commerce-core](features/commerce-core.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="commerce-customers"></a>[commerce-customers](features/commerce-customers.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="commerce-extensions"></a>[commerce-extensions](features/commerce-extensions.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="commerce-functions"></a>[commerce-functions](features/commerce-functions.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="commissions-and-settlements"></a>[commissions-and-settlements](features/commissions-and-settlements.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="companies"></a>[companies](features/companies.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="cross-border"></a>[cross-border](features/cross-border.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="customer-accounts"></a>[customer-accounts](features/customer-accounts.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="customer-service-workspace"></a>[customer-service-workspace](features/customer-service-workspace.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="delivery-promises"></a>[delivery-promises](features/delivery-promises.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="digital-assets"></a>[digital-assets](features/digital-assets.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="digital-fulfillment"></a>[digital-fulfillment](features/digital-fulfillment.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="donations"></a>[donations](features/donations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="draft-and-assisted-orders"></a>[draft-and-assisted-orders](features/draft-and-assisted-orders.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="dropshipping"></a>[dropshipping](features/dropshipping.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="exchanges"></a>[exchanges](features/exchanges.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="express-checkout"></a>[express-checkout](features/express-checkout.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="feed-management"></a>[feed-management](features/feed-management.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="fraud-and-risk"></a>[fraud-and-risk](features/fraud-and-risk.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="fraud-intelligence"></a>[fraud-intelligence](features/fraud-intelligence.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="fulfillment"></a>[fulfillment](features/fulfillment.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="gift-cards-and-store-credit"></a>[gift-cards-and-store-credit](features/gift-cards-and-store-credit.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="inventory-counting"></a>[inventory-counting](features/inventory-counting.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="inventory-ledger"></a>[inventory-ledger](features/inventory-ledger.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="invoices-and-documents"></a>[invoices-and-documents](features/invoices-and-documents.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="localization"></a>[localization](features/localization.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="lots-and-serials"></a>[lots-and-serials](features/lots-and-serials.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="loyalty"></a>[loyalty](features/loyalty.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="marketplace-channels"></a>[marketplace-channels](features/marketplace-channels.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="marketplace-orders"></a>[marketplace-orders](features/marketplace-orders.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="markets"></a>[markets](features/markets.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="membership-commerce"></a>[membership-commerce](features/membership-commerce.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="merchandising"></a>[merchandising](features/merchandising.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="merchandising-intelligence"></a>[merchandising-intelligence](features/merchandising-intelligence.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="migration-framework"></a>[migration-framework](features/migration-framework.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="module-ecommerce-warehouse-operations"></a>[module-ecommerce-warehouse-operations](features/module-ecommerce-warehouse-operations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="module-ecommerce-warranty-and-claims"></a>[module-ecommerce-warranty-and-claims](features/module-ecommerce-warranty-and-claims.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="multi-source-inventory"></a>[multi-source-inventory](features/multi-source-inventory.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="multi-tender-payments"></a>[multi-tender-payments](features/multi-tender-payments.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="negotiated-quotes"></a>[negotiated-quotes](features/negotiated-quotes.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="offline-pos"></a>[offline-pos](features/offline-pos.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="options-and-customization"></a>[options-and-customization](features/options-and-customization.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="order-editing"></a>[order-editing](features/order-editing.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="order-orchestration"></a>[order-orchestration](features/order-orchestration.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="order-tracking"></a>[order-tracking](features/order-tracking.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="orders"></a>[orders](features/orders.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="payment-operations"></a>[payment-operations](features/payment-operations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="payments"></a>[payments](features/payments.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="personalization"></a>[personalization](features/personalization.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="pickup-and-local-delivery"></a>[pickup-and-local-delivery](features/pickup-and-local-delivery.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="point-of-sale"></a>[point-of-sale](features/point-of-sale.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="pos-devices"></a>[pos-devices](features/pos-devices.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="post-purchase-experience"></a>[post-purchase-experience](features/post-purchase-experience.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="pricing"></a>[pricing](features/pricing.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="pricing-rules"></a>[pricing-rules](features/pricing-rules.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="product-comparison"></a>[product-comparison](features/product-comparison.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="product-information-management"></a>[product-information-management](features/product-information-management.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="product-types"></a>[product-types](features/product-types.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="promotions"></a>[promotions](features/promotions.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="purchase-orders"></a>[purchase-orders](features/purchase-orders.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="quick-order"></a>[quick-order](features/quick-order.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="recommendations"></a>[recommendations](features/recommendations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="recurring-orders"></a>[recurring-orders](features/recurring-orders.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="referrals"></a>[referrals](features/referrals.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="refunds"></a>[refunds](features/refunds.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="rentals"></a>[rentals](features/rentals.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="reporting"></a>[reporting](features/reporting.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="reservations"></a>[reservations](features/reservations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="retail-locations"></a>[retail-locations](features/retail-locations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="returns"></a>[returns](features/returns.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="reviews-and-ratings"></a>[reviews-and-ratings](features/reviews-and-ratings.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="sales-channels"></a>[sales-channels](features/sales-channels.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="sales-representative-workspace"></a>[sales-representative-workspace](features/sales-representative-workspace.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="sandbox-and-release"></a>[sandbox-and-release](features/sandbox-and-release.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="saved-lists"></a>[saved-lists](features/saved-lists.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="search-and-discovery"></a>[search-and-discovery](features/search-and-discovery.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="seller-marketplace"></a>[seller-marketplace](features/seller-marketplace.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="shared-catalogs"></a>[shared-catalogs](features/shared-catalogs.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="shipping"></a>[shipping](features/shipping.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="social-commerce"></a>[social-commerce](features/social-commerce.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="store-templates"></a>[store-templates](features/store-templates.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="subscription-commerce"></a>[subscription-commerce](features/subscription-commerce.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="tax"></a>[tax](features/tax.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="transfers-and-replenishment"></a>[transfers-and-replenishment](features/transfers-and-replenishment.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="unified-commerce"></a>[unified-commerce](features/unified-commerce.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="warehouse-operations"></a>[warehouse-operations](features/warehouse-operations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="warranty-and-claims"></a>[warranty-and-claims](features/warranty-and-claims.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |

## Observed packages without a design-name match

These package references document observed modules even when an existing feature filename did not match. Review their capabilities, call sites and ownership before deciding whether to extend an existing feature or add a distinct product capability. They are not silently omitted or merged by this tool.

| Actual directory | Manifest identity and implementation reference |
| --- | --- |
| — | No unmatched dedicated package identities in this scan |

Reproduce with `python3 tools/reconcile_source_modules.py` after rebuilding the inventory and package references. The [machine-readable mapping](../../architecture/source-design-mapping.json) includes every layer match. Follow the [reuse guide](../../architecture/SHARED-MODULES.md), [Composer lifecycle](../../guides/COMPOSER.md) and [npm lifecycle](../../guides/NPM.md) when implementing or adopting a module.
