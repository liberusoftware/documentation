# Liberu Billing\n\n## Product Scope\n\n**Purpose:** Billing, subscription, ordering, payment, provisioning, domain, hosting, ISP, and service automation.\n**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); APIs, payment/provisioning connectors, and webhooks follow [API.md](../../architecture/API.md); storefront and portal presentation follows [THEMES.md](../../standards/THEMES.md).\n\n**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines billing and service behavior only.\n\n## Outcomes\n\n- Manage the quote/order-to-cash lifecycle for recurring, usage, one-time, domain, hosting, ISP, and communications services.\n- Keep commercial terms, invoices, payments, service state, and provider state reconciled.\n- Support self-service and operational automation without coupling to one gateway or provisioning platform.\n\n## Module plan\n\n| Module | Responsibilities |\n|---|---|\n| Billing Core | Accounts, contacts, currencies, tax profiles, sequences, terms, and billing settings |\n| Catalog | Products, plans, add-ons, bundles, configurable options, eligibility, channels, and lifecycle |\n| Pricing | Recurring/one-time/usage/tiered pricing, contracts, discounts, proration, and snapshots |\n| Orders | Quotes, carts, checkout, fraud review, agreements, order state, and change orders |\n| Subscriptions | Activation, renewal, trial, upgrade/downgrade, pause, cancellation, and entitlement state |\n| Usage | Meter definitions, ingestion, deduplication, aggregation, rating, corrections, and thresholds |\n| Invoicing | Schedules, line generation, tax, credits, adjustments, PDFs, delivery, and finalization |\n| Payments | Methods, mandates, gateway drivers, capture, allocation, refunds, disputes, and reconciliation |\n| Collections | Retries, dunning, reminders, promises, credit control, suspension, write-off, and recovery |\n| Provisioning | Service state machine, provider drivers, queued operations, rollback, polling, and reconciliation |\n| Hosting | Hosting accounts, plans, control-panel adapters, SSL, resources, and lifecycle operations |\n| Domains | Search, contacts, registration, transfer, renewal, redemption, EPP, DNS, and registrar adapters |\n| ISP | Access services, coverage, installation, RADIUS/AAA, usage, equipment, and network adapters |\n| Communications | VoIP/SMS service inventory, number lifecycle, usage/rating imports, and provider adapters |\n| Customer Portal | Profile, orders, services, usage, invoices, payments, tickets, changes, and cancellation |\n| Reporting | MRR/ARR, churn, aging, revenue, tax, usage, provisioning, collection, and provider metrics |\n\n## Required workflows\n\n1. **Order and activate:** configure → validate eligibility/price/tax → consent/payment → create order → provision → activate subscription → invoice/notify.\n2. **Renew:** calculate term/usage → draft invoice → collect → renew entitlement/domain/service → reconcile provider state.\n3. **Change service:** quote proration → approve/pay → perform provider change → update entitlement → invoice credit/charge.\n4. **Payment failure:** webhook/collection failure → retry/dunning → grace policy → suspend safely → recover and unsuspend or terminate.\n5. **Provider reconciliation:** compare local services/domains/transactions to provider inventory → classify drift → repair automatically or queue review.\n\n## Product requirements\n\n- Snapshot accepted product, price, tax, term, consent, and contract data.\n- Make order, payment, usage, webhook, invoice, and provisioning operations idempotent.\n- Support partial payments, credits, refunds, deposits, multiple currencies, tax evidence, and configurable invoice timing.\n- Separate subscription/entitlement state from external service state and expose drift.\n- Model dependencies so suspension or cancellation cannot orphan related services or data.\n- Provide bulk operations with previews, limits, approvals, progress, and recoverable failures.\n- Expose versioned APIs/events for accounts, catalog, orders, subscriptions, invoices, payments, usage, domains, and services.\n\n## Integrations\n\nStripe, PayPal, bank/open-banking, tax, registrars, DNS, cPanel/Plesk/DirectAdmin/Virtualmin/Liberu Control Panel, RADIUS/network, VoIP, email/SMS, CRM, Accounting, and support systems use replaceable drivers.\n\n## Quality and control gates\n\n- Test money/rounding, proration boundaries, renewal races, usage duplicates, webhooks, provider timeouts, rollback, and reconciliation.\n- Protect payment data using hosted/tokenized provider flows and enforce scoped provider credentials.\n- Require approval for refunds above policy, write-offs, bulk price changes, destructive termination, and manual financial adjustments.\n- Alert on missed billing runs, invoice imbalance, payment drift, provisioning backlog/failure, expiring domains, and usage anomalies.\n\n## Delivery phases\n\n1. Core, Catalog, Pricing, Orders, Subscriptions, Invoicing, Payments, and portal basics.\n2. Provisioning, Hosting, Collections, credits/refunds, Accounting integration, and reporting.\n3. Domains/DNS, Usage, service changes, provider reconciliation, and advanced tax.\n4. ISP/communications, reseller/marketplace capabilities, and regional extensions.\n\n## Definition of done\n\nOrder-to-cash and service lifecycles are financially correct, idempotent, authorized, auditable, recoverable, and reconciled against providers. Each module maps to an independently deliverable GitHub epic.

## Product Scope

**Purpose:** Billing, subscription, ordering, payment, provisioning, domain, hosting, ISP, and service automation.
**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); APIs, payment/provisioning connectors, and webhooks follow [API.md](../../architecture/API.md); storefront and portal presentation follows [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines billing and service behavior only.

## Outcomes

- Manage the quote/order-to-cash lifecycle for recurring, usage, one-time, domain, hosting, ISP, and communications services.
- Keep commercial terms, invoices, payments, service state, and provider state reconciled.
- Support self-service and operational automation without coupling to one gateway or provisioning platform.

## Module plan

| Module          | Responsibilities                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------- |
| Billing Core    | Accounts, contacts, currencies, tax profiles, sequences, terms, and billing settings              |
| Catalog         | Products, plans, add-ons, bundles, configurable options, eligibility, channels, and lifecycle     |
| Pricing         | Recurring/one-time/usage/tiered pricing, contracts, discounts, proration, and snapshots           |
| Orders          | Quotes, carts, checkout, fraud review, agreements, order state, and change orders                 |
| Subscriptions   | Activation, renewal, trial, upgrade/downgrade, pause, cancellation, and entitlement state         |
| Usage           | Meter definitions, ingestion, deduplication, aggregation, rating, corrections, and thresholds     |
| Invoicing       | Schedules, line generation, tax, credits, adjustments, PDFs, delivery, and finalization           |
| Payments        | Methods, mandates, gateway drivers, capture, allocation, refunds, disputes, and reconciliation    |
| Collections     | Retries, dunning, reminders, promises, credit control, suspension, write-off, and recovery        |
| Provisioning    | Service state machine, provider drivers, queued operations, rollback, polling, and reconciliation |
| Hosting         | Hosting accounts, plans, control-panel adapters, SSL, resources, and lifecycle operations         |
| Domains         | Search, contacts, registration, transfer, renewal, redemption, EPP, DNS, and registrar adapters   |
| ISP             | Access services, coverage, installation, RADIUS/AAA, usage, equipment, and network adapters       |
| Communications  | VoIP/SMS service inventory, number lifecycle, usage/rating imports, and provider adapters         |
| Customer Portal | Profile, orders, services, usage, invoices, payments, tickets, changes, and cancellation          |
| Reporting       | MRR/ARR, churn, aging, revenue, tax, usage, provisioning, collection, and provider metrics        |

## Required workflows

1. **Order and activate:** configure → validate eligibility/price/tax → consent/payment → create order → provision → activate subscription → invoice/notify.
2. **Renew:** calculate term/usage → draft invoice → collect → renew entitlement/domain/service → reconcile provider state.
3. **Change service:** quote proration → approve/pay → perform provider change → update entitlement → invoice credit/charge.
4. **Payment failure:** webhook/collection failure → retry/dunning → grace policy → suspend safely → recover and unsuspend or terminate.
5. **Provider reconciliation:** compare local services/domains/transactions to provider inventory → classify drift → repair automatically or queue review.

## Product requirements

- Snapshot accepted product, price, tax, term, consent, and contract data.
- Make order, payment, usage, webhook, invoice, and provisioning operations idempotent.
- Support partial payments, credits, refunds, deposits, multiple currencies, tax evidence, and configurable invoice timing.
- Separate subscription/entitlement state from external service state and expose drift.
- Model dependencies so suspension or cancellation cannot orphan related services or data.
- Provide bulk operations with previews, limits, approvals, progress, and recoverable failures.
- Expose versioned APIs/events for accounts, catalog, orders, subscriptions, invoices, payments, usage, domains, and services.

## Integrations

Stripe, PayPal, bank/open-banking, tax, registrars, DNS, cPanel/Plesk/DirectAdmin/Virtualmin/Liberu Control Panel, RADIUS/network, VoIP, email/SMS, CRM, Accounting, and support systems use replaceable drivers.

## Quality and control gates

- Test money/rounding, proration boundaries, renewal races, usage duplicates, webhooks, provider timeouts, rollback, and reconciliation.
- Protect payment data using hosted/tokenized provider flows and enforce scoped provider credentials.
- Require approval for refunds above policy, write-offs, bulk price changes, destructive termination, and manual financial adjustments.
- Alert on missed billing runs, invoice imbalance, payment drift, provisioning backlog/failure, expiring domains, and usage anomalies.

## Delivery phases

1. Core, Catalog, Pricing, Orders, Subscriptions, Invoicing, Payments, and portal basics.
2. Provisioning, Hosting, Collections, credits/refunds, Accounting integration, and reporting.
3. Domains/DNS, Usage, service changes, provider reconciliation, and advanced tax.
4. ISP/communications, reseller/marketplace capabilities, and regional extensions.

## Definition of done

Order-to-cash and service lifecycles are financially correct, idempotent, authorized, auditable, recoverable, and reconciled against providers. Each module maps to an independently deliverable GitHub epic.
