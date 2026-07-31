# Liberu Ecommerce

## Product Scope

**Purpose:** Composable commerce platform for direct-to-consumer, B2B, retail/POS, marketplace, subscription, digital, and service business models.
**Architecture:** Packages and provider adapters follow [MODULES.md](MODULES.md); storefront, account, checkout, and POS experiences follow [THEMES.md](THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md). Reuse CMS content, CRM relationships, Billing subscriptions/invoices, Accounting postings, and shared payment/tax/shipping contracts rather than duplicating authoritative capabilities.

## 1. Outcomes

- Provide reliable product-to-payment-to-fulfillment-to-return journeys across channels and markets.
- Maintain authoritative, auditable commercial snapshots, stock movements, payment references, and order state.
- Match commonly expected WooCommerce, Adobe Commerce/Magento, and Shopify capability families through cohesive optional modules.
- Support provider, storefront, channel, and extension replacement without rewriting commerce domains.

## 2. Domain ownership

- Ecommerce owns sellable assortments, carts, checkout, commerce orders, fulfillment coordination, returns, and customer buying experiences.
- Shared Payments owns gateway-neutral authorization/capture/refund orchestration; adapters own provider SDKs and identifiers.
- Billing owns recurring invoice/subscription ledgers when installed; Ecommerce owns storefront enrollment and references Billing records.
- Accounting owns financial postings; CRM owns customer engagement; CMS owns editorial content; Ecommerce publishes events/projections to them.
- Boilerplate owns identity, organizations, authorization, localization/currency context, analytics adapters, generic integrations, and extension lifecycle foundations.

## 3. Product information and catalog modules

| Module | Responsibilities |
|---|---|
| Commerce Core | Stores, channels, commercial context, order numbering, shared states, settings, capabilities, and domain events |
| Product Information Management | Product masters, attributes, attribute sets, completeness, lifecycle, translations, relationships, provenance, and bulk enrichment |
| Catalog | Products, variants, categories, collections, tags, brands, vendors, channel publication, visibility, and effective dates |
| Product Types | Simple, configurable/variant, grouped, bundle, kit, virtual, downloadable, service, subscription, gift card, and custom type contracts |
| Options and Customization | Buyer-selectable options, personalization, uploads, add-ons, validation, pricing modifiers, production data, and order snapshots |
| Bundles and Kits | Fixed/configurable bundles, component rules, availability, pricing, inventory behavior, substitutions, and fulfillment decomposition |
| Categories and Navigation | Hierarchies, menus, landing references, layered navigation, permissions, merchandising positions, and redirects |
| Catalog Staging | Draft/effective catalog changes, grouped campaigns, preview, schedules, conflicts, approvals, atomic activation, and rollback |
| Catalog Import and Export | Schemas, mappings, validation, dry run, media/relationship resolution, batches, schedules, errors, resume, and reconciliation |
| Digital Assets | Commerce media, swatches, documents, manuals, rights, ordering, transformations, videos, and CMS/DAM references |

## 4. Pricing and merchandising modules

| Module | Responsibilities |
|---|---|
| Pricing | Base/sale prices, price lists/books, currencies, markets, channels, customer groups, schedules, tiers, cost, MAP, and snapshots |
| Pricing Rules | Catalog/cart rules, conditions/actions, priorities, stacking, exclusivity, usage budgets, effective dates, simulation, and explanation |
| Promotions | Codes, automatic discounts, buy-X-get-Y, bundles, free shipping/gifts, customer/product eligibility, limits, attribution, and fraud controls |
| Gift Cards and Store Credit | Issue, activate, send, redeem, partial use, balances, expiry, refund, transfer policy, liabilities, and immutable ledger |
| Merchandising | Category/product placement, pins, boosts/buries, badges, rules, campaigns, preview, schedules, and performance |
| Search and Discovery | Full-text search, facets, autocomplete, synonyms, redirects, ranking rules, typo tolerance, query analytics, and provider adapters |
| Recommendations | Manual/rule/model recommendations, related/up-sell/cross-sell, recently viewed, popularity, context, exclusions, and explanation |
| Personalization | Audience/market/customer context, catalog/content/offer variants, eligibility, consent, fallback, holdouts, and decision history |
| Product Comparison | Comparable attributes, saved comparisons, difference highlighting, share links, channel rules, and accessibility |

## 5. Inventory and availability modules

| Module | Responsibilities |
|---|---|
| Inventory Ledger | Receipts, issues, adjustments, transfers, reservations, releases, returns, counts, reason codes, cost references, and audit |
| Multi-Source Inventory | Sources/warehouses/stores/drop shippers, stocks, channel assignment, aggregated salable quantity, priority/distance rules, and source health |
| Availability | In-stock/backorder/preorder policy, safety stock, lead times, incoming supply, sellable-to-promise, channel buffers, and availability messages |
| Reservations | Cart/checkout/order reservations, expiry, extension, conversion, release, concurrency, oversell prevention, and reconciliation |
| Transfers and Replenishment | Transfer orders, in-transit stock, min/max/reorder, demand signals, purchase references, receiving, discrepancies, and alerts |
| Lots and Serials | Lot/batch/serial identity, expiry, traceability, allocation policy, recall, warranty links, and fulfillment/return capture |
| Inventory Counting | Cycle/full counts, blind counts, approvals, variances, adjustments, freeze policy, mobile scanning, and reconciliation |

## 6. Cart and checkout modules

| Module | Responsibilities |
|---|---|
| Cart | Guest/customer/company carts, lines, configuration, quantity, validation, persistence, merge, sharing, estimates, and recalculation |
| Saved Lists | Wishlists, favorites, gift registries, requisition lists, repeat-order lists, sharing, privacy, alerts, and cart conversion |
| Checkout | Contact, addresses, delivery/pickup, tax, discounts, gift/store credit, payment, consent, review, idempotency, and order placement |
| Checkout Extensibility | Validated extension points, UI blocks, delivery/payment customization, business rules, scopes, compatibility, and failure fallback |
| Express Checkout | Wallet/provider accelerated checkout, known-customer context, shipping/payment callbacks, totals validation, and fallback |
| Abandoned Checkout | Cart/checkout state, consent-aware reminders, recovery links, incentives, suppression, attribution, expiry, and conversion reporting |
| Fraud and Risk | Rules, velocity, identity/device/provider signals, review queues, holds, decisions, evidence, chargeback feedback, and provider adapters |

## 7. Order and payment modules

| Module | Responsibilities |
|---|---|
| Orders | Immutable product/price/tax/discount/address/terms snapshots, state machine, history, notes, documents, holds, and audit |
| Draft and Assisted Orders | Staff-created carts/orders, customer selection, quotes, negotiated adjustments, payment links, impersonation safeguards, and conversion |
| Order Editing | Governed pre/post-fulfillment changes, recalculation, payment difference, stock impact, approvals, customer notice, and complete history |
| Payments | Shared payment-core integration, tender selection, authorize/capture/void/refund references, payment status projection, and reconciliation |
| Multi-Tender Payments | Split payments, gift/store credit, deposits, installments references, partial payments, outstanding balances, and allocation |
| Payment Operations | Capture/refund queues, disputes/chargebacks, manual review, provider webhooks, settlement reconciliation, and exception handling |
| Invoices and Documents | Receipt/order/invoice/credit document projections, numbering references, PDFs, localization, delivery, and Billing adapters |
| Order Orchestration | Dependencies, split/routing decisions, holds, releases, backorders, partial operations, fallout queues, compensation, and status aggregation |

## 8. Tax, shipping, and fulfillment modules

| Module | Responsibilities |
|---|---|
| Tax | Inclusive/exclusive pricing, classes, nexus/registration, destination/origin rules, exemptions, evidence, rounding, calculation adapters, and reports |
| Shipping | Zones, methods, rates, packages, restrictions, free shipping, table rates, carrier adapters, and delivery estimates |
| Delivery Promises | Cutoffs, processing/transit calendars, capacity, inventory/source selection, postcode coverage, promise dates, and recalculation |
| Fulfillment | Allocation, pick/pack/ship, partial shipments, digital/service fulfillment, substitutions, proof, status, and customer notification |
| Warehouse Operations | Waves/batches, pick paths, packing stations, scans, labels, manifests, exceptions, and warehouse-system adapters |
| Carrier Operations | Labels, rates, pickup, manifests, tracking, address validation, claims, delivery events, and reconciliation |
| Pickup and Local Delivery | Locations, availability, slots, preparation, ready-for-pickup, verification, curbside, routes, proof, and no-collection policy |
| Dropshipping | Supplier/source routing, purchase references, order transmission, acknowledgements, shipment sync, cost, SLA, and exceptions |
| Digital Fulfillment | Entitlements, secure downloads/streams, limits, expiry, license-key adapters, version access, revocation, and evidence |

## 9. Returns and post-purchase modules

| Module | Responsibilities |
|---|---|
| Returns | Eligibility, self-service requests, reasons, authorization, labels, receipts, inspection, disposition, exchange, and status |
| Refunds | Refund calculation, original/alternative tender policy, approval, provider execution, store credit, failure recovery, and accounting events |
| Exchanges | Replacement selection, price/tax difference, stock reservation, cross-shipment policy, payment/refund, and fulfillment |
| Warranty and Claims | Warranty terms, registration, claims, evidence, troubleshooting, repair/replace/refund decisions, providers, and history |
| Order Tracking | Unified fulfillment/tracking timeline, delivery estimates, exceptions, subscriptions, guest access, and carrier fallback |
| Post-Purchase Experience | Branded status, instructions, documents, product registration, review/referral prompts, support links, and relevant recommendations |

## 10. Customer and retention modules

| Module | Responsibilities |
|---|---|
| Commerce Customers | Commerce profiles, addresses, preferences, tax status, customer groups, tags, lifecycle, and CRM identity references |
| Customer Accounts | Registration/guest conversion, order history, returns, saved carts/lists, payment-method references, preferences, and privacy requests |
| Reviews and Ratings | Verified purchase, ratings, text/media reviews, questions/answers, moderation, merchant replies, syndication, incentives disclosure, and reports |
| Loyalty | Programs, tiers, points ledger, earn/redeem, rewards, expiry, referrals, fraud controls, liabilities export, and customer statements |
| Referrals | Advocate links/codes, referred customers, qualification, rewards, duplicate/fraud rules, attribution, and status |
| Back-in-Stock and Price Alerts | Subscriptions, consent, thresholds, notification deduplication, expiry, channel selection, and conversion reporting |
| Customer Service Workspace | Orders, payments, shipments, returns, customer timeline, safe actions, notes, macros, and CRM/Support handoff |

## 11. Recurring, service, and access modules

| Module | Responsibilities |
|---|---|
| Subscription Commerce | Storefront plans/options, signup, trial, prepaid terms, add-ons, customer changes, cancellation/retention, and Billing handoff |
| Recurring Orders | Repeat schedules, editable upcoming orders, cutoff, skips, substitutions, payment references, fulfillment generation, and failures |
| Membership Commerce | Membership products, access grants, tiers, bundles, renewal references, member pricing/content, and portal integration |
| Bookings and Appointments | Resources, services, staff, availability, durations, capacity, buffers, questions, price, confirmation, reschedule, and no-show |
| Rentals | Inventory units, availability, reservation periods, deposits, pickup/return, late/damage charges, inspection, and maintenance blocks |
| Donations | Funds/campaigns, one-time/recurring gifts, suggested/custom amount, donor preferences, receipts, anonymity, and CRM/accounting references |

## 12. B2B and wholesale modules

| Module | Responsibilities |
|---|---|
| Companies | Company accounts/locations, contacts, roles, buyers, approvers, sales reps, tax/exemption, payment terms, addresses, and lifecycle |
| Shared Catalogs | Company/market-specific assortment, price lists, category access, product visibility, effective dates, and inheritance |
| B2B Purchasing Rules | Minimum/maximum/increment quantities, case packs, order thresholds, payment/shipping methods, deposits, PO numbers, and approvals |
| Negotiated Quotes | Buyer/seller negotiation, messages, line/price changes, versions, expiry, approval, conversion, and history |
| Purchase Orders | Company requisition, approval chains, budgets, cost centers, PO documents/numbers, release, matching references, and status |
| Quick Order | SKU/name entry, matrix ordering, CSV upload, validation, availability, saved/requisition lists, and bulk cart add |
| B2B Self-Service | Company/location switching, users/roles, shared addresses, catalogs, quotes, orders, invoices references, returns, and reordering |
| Sales Representative Workspace | Assigned companies, assisted orders/quotes, account pricing, activity, approvals, order status, and territory permissions |

## 13. International and channel modules

| Module | Responsibilities |
|---|---|
| Markets | Customer/region/channel market definitions, domains, locale, currency, pricing, availability, tax/duty, content/theme references, and fallback |
| Localization | Product/category/attribute/checkout/email/document translations, units, addresses, names, dates, and right-to-left support |
| Cross-Border | Duties/import taxes, landed cost estimates, restrictions, harmonized codes, origin, importer policy, customs documents, and adapters |
| Sales Channels | Channel registry, assortment/pricing/inventory/order mappings, publication, sync cursors, conflicts, health, and reconciliation |
| Marketplace Channels | Amazon/eBay/social-marketplace-style listings, offers, fees, orders, cancellations, fulfillment, returns, and provider adapters |
| Social Commerce | Product feeds, shops, tagged products, checkout handoff, lead/order events, policy status, and channel adapters |
| Feed Management | Search/ad/affiliate product feeds, field mappings, rules, schedules, validation, destination errors, and diagnostics |

## 14. Retail and POS modules

| Module | Responsibilities |
|---|---|
| Point of Sale | Registers, carts, customers, products, taxes, discounts, tenders, receipts, returns/exchanges, holds, and staff actions |
| Retail Locations | Store hierarchy, hours, market, stock source, pickup, registers, staff assignments, fulfillment, and location reporting |
| POS Devices | Device enrollment, capabilities, health, updates, offline keys, assignment, revocation, and provider adapters |
| Offline POS | Local catalog/price/stock subset, offline orders/payments policy, sequence IDs, synchronization, conflict resolution, and risk limits |
| Cash Management | Tills, opening float, movements, paid-in/out, counts, discrepancies, close, deposits, approvals, and audit |
| Unified Commerce | Shared customer, loyalty, gift/store credit, orders, returns, inventory, promotions, and fulfillment across online/POS channels |

## 15. Marketplace and platform modules

| Module | Responsibilities |
|---|---|
| Seller Marketplace | Sellers, onboarding, verification, stores, offers, catalog contributions, approval, policies, performance, suspension, and portal |
| Commissions and Settlements | Commission rules, fees, split references, reserves, adjustments, seller statements, payout approval/export, and reconciliation |
| Marketplace Orders | Seller allocation, acceptance, fulfillment SLA, communication, cancellation, returns, disputes, and aggregate customer status |
| Commerce Extensions | Extension manifests, install/update/uninstall, scopes, webhooks, functions, UI extensions, compatibility, health, and rollback |
| App Marketplace | Publishers, listings, reviews, pricing/trials, licenses/entitlements, signing, security review, support, billing references, and distribution |
| Commerce Functions | Sandboxed typed hooks for discounts, validation, delivery/payment customization, routing, and transformations with limits and diagnostics |
| Store Templates | Versioned bundles of configuration, catalog samples, pages, navigation, workflows, themes, and provider requirements |

Production extensions cannot patch core/vendor files, query private package tables, bypass checkout/order invariants, or run unsigned arbitrary code through an admin upload.

## 16. Operations, analytics, and intelligence modules

| Module | Responsibilities |
|---|---|
| Commerce Automation Pack | Commerce triggers/actions/recipes, versioning, simulation, approvals, idempotency, and generic Automation integration |
| Reporting | Sales, margin, tax, discount, inventory, fulfillment, returns, customer, channel, market, B2B, POS, and seller metrics |
| Attribution and Analytics | Canonical commerce events, sessions, funnels, campaign/source mapping, server-side conversion adapters, consent, and reconciliation |
| Fraud Intelligence | Risk features, model/provider scores, decision explanations, drift, review quality, and chargeback feedback |
| Merchandising Intelligence | Search gaps, zero results, conversion, affinity, trends, recommendations, inventory-aware ranking, and experiment analysis |
| Commerce Copilot | Permission-bounded product/order/customer search, summaries, catalog assistance, safe operational actions, and confirmation |
| Migration Framework | WooCommerce, Magento/Adobe Commerce, Shopify, and generic source adapters with mappings, dry run, batches, resume, media, redirects, and reconciliation |
| Sandbox and Release | Test stores/data policy, configuration/catalog snapshots, dependency comparison, staging, promotion, rollback, and smoke tests |

## 17. Required workflows

1. **Catalog launch:** model/enrich product → validate completeness/rights/price/stock/channels → preview staged campaign → approve → publish/index/feed.
2. **D2C purchase:** discover → configure → cart → price/tax/availability → checkout/risk/payment → commit order/reservation → confirm.
3. **B2B purchase:** authenticate company/location → assigned catalog/terms → quick/requisition order → approval/quote → PO/payment → order.
4. **Omnichannel fulfillment:** source/route → allocate → pick/pack/ship or pickup/digital deliver → partial status → tracking → completion.
5. **Return/exchange:** eligibility → authorization → receive/inspect → disposition/restock → replacement/refund/store credit → accounting event.
6. **Subscription/service:** choose plan/time/resource → validate availability/terms → enroll/pay → Billing/booking record → entitlement/fulfillment → changes/renewal.
7. **International order:** resolve market → localize assortment/price/currency/tax/duty/content → validate restrictions → checkout → customs/fulfillment.
8. **Channel sync:** publish offer/stock → ingest order/event → deduplicate/map → fulfill/update → reconcile provider and local state.
9. **Extension lifecycle:** review publisher/scopes/data/compatibility → test/install → configure → monitor/update → revoke/uninstall safely.

Every workflow defines authoritative records, states, monetary/stock snapshots, actor/tenant/store/channel/market context, permissions, idempotency, events, compensation, audit, metrics, and recovery.

## 18. Shared requirements and quality gates

- Use precise money types and explicit currency, tax, rounding, effective-date, and exchange-rate policy; never binary floating point.
- Snapshot accepted product, option, price, promotion, tax, address, delivery, consent, and terms on the order.
- Use inventory, gift/store-credit, loyalty, commission, and financial ledgers rather than mutable counters alone.
- Enforce concurrency and idempotency for carts, reservations, promotion limits, checkout, orders, webhooks, captures, refunds, returns, imports, and channel sync.
- Apply store/channel/market/company/location/customer/field/action authorization to admin, storefront, API, search, export, jobs, and extensions.
- Protect payment data with tokenized/hosted provider flows where possible and require approvals for material refunds, manual adjustments, bulk price changes, and destructive operations.
- Test provider outages, duplicate/out-of-order events, partial fulfillment/payment/refund, stock races, tax rounding, B2B approvals, offline POS, extension failure, and migration reconciliation.
- Meet WCAG 2.2 AA and performance budgets for browse, search, product, cart, checkout, accounts, order tracking, returns, and POS.
- Provide logs, metrics, traces, health, dead-letter replay, reconciliation, alerts, backups/restores, and runbooks for every critical provider and workflow.

## 19. Delivery phases

1. Core, PIM/Catalog/Product Types, Pricing, Inventory Ledger, Cart, Checkout, Orders, shared Payments, Tax, Shipping, Fulfillment, and customer accounts.
2. Multi-source inventory, merchandising/search/recommendations, promotions/gift credit, returns/exchanges, post-purchase, reviews, loyalty, and analytics.
3. Markets/localization/cross-border, channels/feeds/marketplaces, catalog staging, advanced order orchestration, warehouse/carrier/pickup, and migration framework.
4. B2B companies/catalogs/quotes/purchasing/quick order, sales-rep workspace, POS/retail/offline, and unified commerce.
5. Subscriptions, bookings/rentals, memberships, digital fulfillment, seller marketplace, commissions/settlements, and advanced automation/intelligence.
6. App Marketplace, Commerce Functions, store templates, benchmark migration adapters, sandbox/release tooling, and continued provider expansion.

## 20. Benchmark coverage and sources

- **WooCommerce:** extensible product/cart/checkout/order foundations, physical/virtual/downloadable products, coupons, shipping/tax, themes/extensions, plus common subscriptions, bookings, memberships, bundles, wholesale, payments, and marketplace add-ons.
- **Adobe Commerce/Magento:** rich product types/PIM, staged catalog campaigns, rule-based merchandising, multi-source inventory, customer segments, enterprise B2B companies/shared catalogs/quotes/requisitions/POs, content/page integration, APIs, and operational scale.
- **Shopify:** markets, channels, storefront extensibility, accelerated checkout, POS/unified retail, B2B company/location catalogs and terms, draft orders, discounts/gift cards, Flow-style automation, app/functions ecosystem, and headless delivery.
- **Common marketplace add-ons:** reviews/UGC, loyalty/referrals, subscriptions, search/recommendations, feeds, returns, shipping/tracking, fraud, bundles, digital licensing, preorders/back-in-stock, dropshipping, wholesale, bookings, affiliate, accounting, and support integrations have explicit module homes.

Official reference starting points:

- [WooCommerce documentation](https://woocommerce.com/documentation/woocommerce/)
- [Adobe Commerce documentation](https://experienceleague.adobe.com/en/docs/commerce)
- [Adobe Commerce B2B features](https://experienceleague.adobe.com/en/docs/commerce-admin/b2b/enable-basic-features)
- [Adobe Commerce inventory management](https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/introduction)
- [Shopify Markets](https://help.shopify.com/en/manual/markets)
- [Shopify B2B feature overview](https://help.shopify.com/en/manual/b2b/getting-started/features)
- [Shopify product bundles](https://help.shopify.com/en/manual/products/bundles)

## 21. Definition of done

Selected packages deliver financially correct, inventory-safe, idempotent, authorized, accessible, observable, provider-replaceable, and recoverable commerce across supported channels and markets. Product, order, payment, stock, tax, fulfillment, return, customer, and extension state remains traceable and reconciled. Each module row is suitable for a focused GitHub epic.
