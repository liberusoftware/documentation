# Required project modules and dependency matrix

Install the Boilerplate foundation first, then enable only the rows required by the current milestone. “Required” means the vertical slice cannot be released safely without it; “phase 2” means install/configure after the first slice; “optional” must not block the public site.

| Project | Required for official websites/staff apps | Phase 2 or conditional | Ownership boundary |
| --- | --- | --- | --- |
| Boilerplate | Application Core, Identity, Organizations and Teams, Roles and Permissions, Profiles, 2FA, Sessions and Devices, Localization, Settings, Audit, Notifications, Files and Media, Scheduler and Queues, Observability, API Access, Webhooks, Integrations, Feature Flags, Search | Analytics, import/export, activity/comments | Shared identity, tenancy, permissions, settings, audit, transport, and operational foundation |
| CMS | CMS Core, Content Entities, Field System, Metadata, Pages, Editorial Content, Media Library, Navigation, SEO, Redirects, Sitemaps, Publishing, Editorial Workflow, Form Builder, Form Operations, Web Delivery, Multisite, Site Factory, Localization, Content Access, Cache and Performance, Security Operations | Static Publishing, Knowledge Base, Content Intelligence, Personalization, Experimentation | Published content/media and public delivery; Liberu composes sites and workflows |
| CRM | CRM Core, Customer Data Model, Data Operations, Consent and Preferences, CRM Search, CRM Documents, Collaboration, Lead Capture, Routing, Sales Pipelines, Sales Workspace, Activities, Scheduling, Unified Conversations, Case Management, Omnichannel Service, SLA and Entitlements, Knowledge, Customer Self-Service, Customer Success | Telephony, Dialer and Outreach, Contact Center, AI Reception, Campaigns, Projects, Resource Planning, Revenue Intelligence | Customer relationship, consent, sales, support, success, and service records |
| Billing | Billing Core, Catalog, Pricing, Orders, Subscriptions, Usage, Invoicing, Payments, Provisioning, Hosting, Domains, Customer Portal, Reporting | ISP, Collections, Communications | Commercial service state and customer billing |
| Control Panel | Control Core, Accounts, Web Hosting, Mail, Databases, DNS, Files, Certificates, Backups, Security, Monitoring, API and Automation | Containers, Kubernetes | Infrastructure changes and observed service state |
| Ecommerce | Commerce Core, Product Information Management, Catalog, Product Types, Pricing, Availability, Cart, Checkout, Orders, Payments, Tax, Shipping, Fulfillment, Digital Fulfillment, Returns, Refunds, Commerce Customers, Customer Accounts | Search and Discovery, Recommendations, Reviews, Subscriptions, Bookings, Sales Channels | Storefront/order flow; Billing remains authoritative for hosting subscriptions |
| Automation | Automation Core, Rules, Approvals, AI Gateway, Prompt Registry, Data Processing, Connectors, Evaluation | Voice, Image, Video | Generic workflow/AI runtime; Liberu supplies governed composition policy |
| Accounting | Accounting Core, Financial Master Data, Chart of Accounts, General Ledger, Dimensions and Tracking, Accounting Periods, Policies, Sales Invoicing, Customer Payments, AR, AP, Bank Feeds, Bank Reconciliation, Tax Core, Reporting, Audit Support | Multi-entity, Intercompany, Consolidation, Payroll, Fixed Assets | Ledger, postings, reconciliation, tax, and financial reporting |
| Maintenance | Maintenance Core, Customers and Sites, Assets, Work Orders, Scheduling, Inspections, Inventory, Portals | Procurement, Commercial, Compliance, Field Service | Physical asset and maintenance records where enabled |

## AI, communications, and measurement dependencies

| Dependency | Required modules/adapters | Liberu configuration |
| --- | --- | --- |
| AI runtime | Automation Core, Rules, Approvals, AI Gateway, Prompt Registry, Data Processing, Connectors, Evaluation | Provider allowlist, model/prompt versions, spend limits, confidence thresholds, human approval, redaction, and audit |
| CRM channels | Channel Gateway, Unified Conversations, Telephony, AI Reception and Conversation, Omnichannel Service, SLA and Entitlements, Routing, Contact Center where enabled, Email Productivity/Marketing, Mobile Messaging, Campaigns, Journey Orchestration, Advertising, Attribution | Human escalation route, consent/suppression, contact cooling-off, business hours, recording policy, provider numbers/accounts, stop rules, approval matrix |
| Sales knowledge | Approved importer for `liberusoftware/sales` | Pin commit SHA, allowlisted directories, provenance/citations, template review/expiry, webhook/pull reconciliation, prompt-injection quarantine |
| Measurement | Boilerplate Analytics Core, Google Analytics/GA4 adapter, Google Tag Manager browser/theme adapter, Meta client/pixel adapter, Meta Server-Side Tracking/CAPI adapter | Shared event catalog, consent routing, event IDs, browser/server deduplication, UTM/click IDs, test destinations, replay, drift dashboard |

GTM, GA4, Meta, telephony, messaging, social, and AI providers remain replaceable adapters. No CRM domain model or Liberu custom module may depend directly on a provider SDK or provider-specific event as its source of truth.

## Dependency rules

1. Pin compatible versions in the application manifest; do not install a presentation package without its matching core/API contract.
2. Integrate through stable IDs, DTOs, commands, queries, events, webhooks, and operation resources. Never join another package’s private tables.
3. Resolve tenant, team, brand, actor, locale, timezone, and currency from trusted context; caller-supplied context is a filter, never authority.
4. Use outbox/inbox delivery, idempotency, replay, correlation IDs, provider timeouts, and reconciliation for every cross-project workflow.
5. Treat installed, enabled, entitled, and authorized as separate states in manifests, UI, API, jobs, and feature flags.
