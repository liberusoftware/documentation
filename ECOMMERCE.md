# Liberu Ecommerce

## Product Scope

**Purpose:** Composable commerce for physical, digital, subscription, service, and marketplace products.
**Architecture:** Modules follow [MODULES.md](MODULES.md); storefronts and portal presentation follow [THEMES.md](THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md); this scope defines commerce behavior only.

## Outcomes

- Provide reliable catalog-to-fulfillment and return/refund journeys across channels.
- Keep pricing, stock, payment, tax, and order state authoritative and auditable.
- Support independent provider drivers and integration with CMS, CRM, Billing, and Accounting.

## Module plan

| Module | Responsibilities |
|---|---|
| Catalog | Products, variants, bundles, options, categories, attributes, media, channels, and lifecycle |
| Pricing | Price lists, currencies, customer groups, tiers, schedules, tax mode, and price snapshots |
| Inventory | Locations, stock ledger, reservations, transfers, adjustments, availability, and low-stock rules |
| Cart | Guest/customer carts, line configuration, validation, recalculation, persistence, and merge |
| Promotions | Coupons, automatic rules, eligibility, stacking, budgets, limits, and attribution |
| Checkout | Address, delivery, tax, payment, consent, fraud checks, idempotency, and order placement |
| Orders | Immutable commercial snapshots, status machine, edits, notes, documents, and audit |
| Payments | Authorize/capture, alternative methods, refunds, disputes, webhooks, and reconciliation |
| Fulfillment | Shipments, digital delivery, service fulfillment, split orders, tracking, and proof |
| Shipping | Zones, packages, rates, carrier drivers, labels, manifests, and tracking updates |
| Tax | Nexus/registration settings, calculation drivers, exemptions, evidence, rounding, and reports |
| Returns | Requests, authorization, receipts, inspection, restock, exchange, refund, and reasons |
| Customers | Commerce profiles, addresses, preferences, groups, wishlists, and order self-service |
| Marketplace | Sellers, offers, commissions, moderation, split settlements, and seller portal (optional) |
| Reporting | Sales, margin, tax, stock, fulfillment, returns, promotion, and cohort metrics |

## Required workflows

1. **Purchase:** browse → price/availability → cart → checkout → authorize payment → commit order/reservation → confirm.
2. **Fulfill:** allocate → pick/prepare → ship or deliver digitally → track → confirm completion.
3. **Payment failure:** preserve idempotent checkout → classify result → retry or select method → release expired stock safely.
4. **Return:** request → eligibility → authorize → receive/inspect → restock/dispose → refund/exchange → accounting event.
5. **Catalog change:** draft → validate channel/pricing/stock dependencies → approve → publish → reindex/invalidate caches.

## Product requirements

- Support multi-channel, multi-currency, localization, guest checkout, saved carts, quotes, and customer portals.
- Snapshot product, price, discount, tax, address, and terms on the order.
- Use stock ledgers and timed reservations; never infer stock only from mutable counters.
- Enforce payment and webhook idempotency and reconcile provider state.
- Support partial capture, fulfillment, cancellation, refund, return, and backorder.
- Provide accessible Filament operations and theme-ready storefront components.
- Expose versioned APIs/events for catalogs, carts, orders, payments, fulfillment, stock, and returns.

## Integrations

Payment gateways, tax engines, carriers, warehouses, fraud services, search, CMS, CRM, Billing, Accounting, Notifications, and analytics use documented adapters/events. PCI-sensitive data stays with certified providers wherever possible.

## Quality gates

- Test concurrency for stock, promotions, checkout, webhooks, captures, refunds, and returns.
- Verify authorization, tenant/channel scope, monetary precision, rounding, tax evidence, and audit history.
- Meet accessibility and performance budgets for browse, cart, checkout, account, and order tracking.
- Provide reconciliation, dead-letter replay, provider outage behavior, and operational alerts.

## Delivery phases

1. Catalog, Pricing, Inventory, Cart, Checkout, Orders, and one payment driver.
2. Fulfillment, Shipping, Tax, customer portal, notifications, and reporting.
3. Promotions, Returns, multiple providers, multi-channel/localization, and integrations.
4. Marketplace and advanced optimization where required.

## Definition of done

Critical commerce journeys are authorized, idempotent, concurrency-safe, traceable, accessible, reconciled, recoverable, and tested across provider failures. Each module is independently scoped for a GitHub epic.
