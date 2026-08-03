# Liberu CRM

## Product Scope

**Purpose:** Composable customer platform for data, demand generation, sales, marketing, service, customer success, partner operations, and agency delivery.
**Architecture:** Packages and provider adapters follow [MODULES.md](../../architecture/MODULES.md); APIs, marketplace connectors, and webhooks follow [API.md](../../architecture/API.md); staff, partner, and customer experiences follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines CRM-domain behavior only. Reuse CMS, Automation, Billing, Ecommerce, Accounting, and other Liberu contracts instead of duplicating their authoritative capabilities.

## 1. Outcomes

- Maintain a governed, permission-aware customer graph and timeline across the complete lifecycle.
- Capture and qualify demand, guide repeatable sales execution, and produce trustworthy forecasts.
- Orchestrate consent-aware engagement across marketing, sales, support, and success channels.
- Turn accepted business into contracts, orders, subscriptions, projects, onboarding, retention, and expansion.
- Support direct businesses, multi-brand enterprises, partners, and white-label agencies without provider lock-in.
- Match the commonly expected capability breadth of HubSpot, Salesforce, Pipedrive, and HighLevel while retaining independently installable package boundaries.

## 2. Domain ownership rules

- CRM owns customer relationships, engagement context, demand, sales/service processes, and customer-facing lifecycle coordination.
- Boilerplate owns identity, organizations/teams, authorization, localization, currency context, settings, audit, and generic integrations.
- CMS owns durable website/content publishing; CRM owns conversion journeys, campaign landing experiences, forms, and attribution mappings that consume CMS/theme extension points.
- Automation owns the generic workflow/AI runtime; CRM packages own CRM triggers, actions, recipes, policies, and approval requirements.
- Billing/Ecommerce own authoritative catalog, pricing, checkout, invoices, subscriptions, payments, and refunds; CRM stores references and commercial snapshots required for selling.
- Accounting owns postings and financial statements; Projects owns delivery coordination where installed.
- External systems are implemented as contract, core, and provider-adapter packages under `MODULES.md`.

## 3. Customer data and platform modules

| Module                    | Responsibilities                                                                                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRM Core                  | Contacts, organizations, households, relationships, owners, teams, tags, notes, attachments, favorites, record lifecycle, and unified timeline                 |
| Customer Data Model       | Standard/custom objects, fields, relationships, layouts, validation, calculated fields, required-by-stage fields, and schema versioning                        |
| Customer Data Platform    | Source profiles, identity resolution, unified profiles, audience activation, event ingestion, consent-aware calculated attributes, and profile lineage         |
| Data Operations           | Imports/exports, field mapping, normalization, enrichment orchestration, duplicate detection/merge, formatting, quality rules, schedules, and exception queues |
| Consent and Preferences   | Lawful basis, subscriptions, channel/topic preferences, suppression, quiet hours, recording consent, proof, expiry, withdrawal, and policy evaluation          |
| Territories and Ownership | Territories, books of business, teams, queues, assignment rules, round-robin/capacity routing, temporary coverage, and ownership history                       |
| CRM Search                | Permission-aware global search, saved views, filters, related-record search, recents, suggestions, and index reconciliation                                    |
| CRM Documents             | Sales/service files, templates, folders, links, access, engagement tracking, versioning, retention, and external-storage adapters                              |
| Collaboration             | Record comments, mentions, followers, shared work queues, approvals, handoffs, internal channels, and collaboration-provider adapters                          |

## 4. Demand generation and acquisition modules

| Module                    | Responsibilities                                                                                                                                                |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lead Capture              | Leads inbox, manual/import/API capture, forms, surveys, QR codes, chat, calls, advertisements, events, referrals, and source metadata                           |
| Prospecting               | Ideal-customer profiles, prospect searches, list building, research queues, contact reveal/credits, provider provenance, and compliant export/outreach handoff  |
| Enrichment                | Company/contact firmographic, demographic, technographic, social, verification, change monitoring, confidence, field-level provenance, and provider adapters    |
| Web Intent                | First-party visits, account identification adapters, page/content engagement, scoring signals, alerts, buyer intent, consent, and lead/account conversion       |
| Lead Qualification        | Lifecycle stages, fit/engagement scoring, MQL/PQL/SQL/service-qualified rules, qualification frameworks, disqualification, nurture, and conversion              |
| Routing                   | Rule, territory, skill, language, availability, workload, value, SLA, and round-robin assignment with fallback and acceptance timers                            |
| Forms and Surveys         | Drag-and-drop schemas, conditional fields, progressive profiling, validation, spam controls, consent, hidden attribution, embedding, submissions, and follow-up |
| Chat and Bots             | Web chat, bot/playbook builder, qualification, knowledge answers, meeting booking, live-agent handoff, office hours, transcripts, and channel identity          |
| Landing Pages and Funnels | Multi-step funnels, landing/thank-you pages, templates, domains, SEO metadata, personalization, forms, order links, preview, publish, and conversion tracking   |
| Conversion Optimization   | A/B and multivariate tests, traffic allocation, goals, statistical policy, popups, banners, CTAs, personalization rules, and experiment reporting               |
| Events and Webinars       | Physical/virtual events, registration, capacity, tickets/attendance, sessions, speakers, reminders, check-in, recording links, follow-up, and provider adapters |

## 5. Sales execution modules

| Module                    | Responsibilities                                                                                                                                                      |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sales Pipelines           | Multiple pipelines, stages, opportunities, products, values, probabilities, close dates, competitors, dependencies, stage history, rotting, and loss reasons          |
| Sales Workspace           | Prioritized seller feed, leads/deals inbox, overdue/risk indicators, next best action, daily agenda, quick updates, and contextual customer history                   |
| Activities                | Tasks, calls, meetings, emails, deadlines, recurrence, queues, bulk completion, reminders, outcomes, goals, and activity reporting                                    |
| Scheduling                | Personal/team/round-robin links, availability, buffers, minimum notice, questions, reminders, reschedule/cancel, no-show, routing, and calendar adapters              |
| Sales Engagement          | Sequences/cadences, multi-channel steps, templates/snippets, task queues, enrollment/re-entry, throttles, timezone windows, reply/meeting stop rules, and experiments |
| Email Productivity        | Mailbox sync, send/log, templates, snippets, scheduling, open/click/reply tracking policy, shared/team inbox, signatures, sidebars, and Gmail/Outlook adapters        |
| Conversation Intelligence | Call/meeting recording, transcription, summaries, topics, questions, objections, competitors, sentiment policy, action items, highlights, and searchable evidence     |
| Playbooks and Enablement  | Guided scripts, qualification cards, battlecards, onboarding content, required evidence, coaching checklists, document/content recommendations, and usage analytics   |
| Forecasting               | Forecast categories, rollups, manager adjustments, commit/best-case/pipeline views, coverage, trend, scenario, history, accuracy, and submission workflow             |
| Revenue Intelligence      | Pipeline inspection, health/risk, engagement gaps, opportunity scoring, relationship maps, white-space/next-product suggestions, anomaly detection, and alerts        |
| Goals and Performance     | Individual/team/company goals, activity/outcome targets, scorecards, leaderboards, reviews, coaching plans, and performance history                                   |
| Quotas and Incentives     | Quotas, ramps, crediting, splits, territories, attainment, commission plans, accelerators, adjustments, disputes, approvals, and payroll/export adapters              |
| Account Planning          | Account hierarchies, stakeholders, influence maps, whitespace, account plans, objectives, risks, mutual action plans, and account-based coordination                  |

## 6. Revenue and commercial modules

| Module                        | Responsibilities                                                                                                                                                 |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRM Product Workspace         | Sales-facing catalog projections, bundles, entitlements, price-book references, product eligibility, and governed Billing/Ecommerce synchronization              |
| CPQ                           | Guided configuration, compatibility rules, price books, tiers, discounts, approvals, margin guardrails, amendments, renewals, and authoritative pricing adapters |
| Proposals and Quotes          | Branded templates, sections, scope, line items, optional choices, versions, comments, approvals, delivery, engagement, acceptance, and expiry                    |
| Contracts                     | Parties, terms, clauses, obligations, versions, negotiation, approvals, signatures, amendments, renewals, notices, repository links, and compliance dates        |
| Orders and Payments Workspace | Payment links, deposits, order/subscription references, invoice/payment status, refunds/disputes visibility, and Billing/Ecommerce handoff                       |
| Revenue Lifecycle             | Opportunity-to-order orchestration, assets/installed products, entitlements, renewals, upgrades, downgrades, cancellation, usage signals, and fallout queues     |

These modules never duplicate authoritative pricing, payment, subscription, invoice, order, or accounting ledgers.

## 7. Marketing modules

| Module                  | Responsibilities                                                                                                                                               |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Segmentation            | Static/dynamic audiences, nested conditions, behavioral events, calculated attributes, exclusions, estimated counts, refresh, and lineage                      |
| Campaigns               | Campaign hierarchy, briefs, objectives, budget, assets, channels, audience, owners, calendar, tasks, costs, responses, influence, and ROI                      |
| Journey Orchestration   | Triggered/scheduled journeys, branching, waits, goals, re-entry, suppression, frequency caps, experiments, stop-on-response, and versioned publication         |
| Email Marketing         | Drag-and-drop and code templates, personalization, dynamic content, test sends, inbox previews, deliverability controls, scheduling, throttling, and analytics |
| Mobile Messaging        | Consent-aware SMS/MMS/WhatsApp/push campaigns, templates, short links, keywords, opt-in/out, quiet hours, sender governance, and delivery/reply handling       |
| Advertising             | Ad-account connections, campaign visibility, lead-ad ingestion, CRM audiences, offline/server conversions, spend/performance sync, and attribution             |
| Account-Based Marketing | Target accounts, tiers, buying committees, intent, engagement rollups, account audiences, plays, coverage, pipeline influence, and measurement                 |
| Personalization         | Rules and decisioning for content, offer, channel, send time, locale, lifecycle, and customer attributes with holdouts and fallback                            |
| Marketing Resources     | Brand kits, reusable content blocks, campaign files, templates, approvals, usage rights, and CMS/media references                                              |
| Attribution             | First/last/multi-touch models, campaign members, source normalization, UTM/click IDs, offline conversions, influence, cost allocation, and model comparison    |

## 8. Communications and contact-center modules

| Module                        | Responsibilities                                                                                                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unified Conversations         | Omnichannel threads, participants, identity matching, assignments, collision detection, drafts, internal notes, attachments, delivery/read state, and timeline          |
| Channel Gateway               | Provider-neutral email, SMS/MMS, WhatsApp, web chat, social messaging, and push contracts, routing, templates, health, and provider selection                           |
| Telephony                     | Numbers, caller ID, IVR, queues, business hours, skills, recording, voicemail, transfers, dispositions, click-to-call, call logging, and provider adapters              |
| Dialer and Outreach           | Power/preview/progressive dialing, prioritized lists, scripts, local-time policy, retries, voicemail drop, answer detection adapters, outcomes, and compliance controls |
| Contact Center                | Agent presence, capacity, skills, routing, supervisor views, whisper/barge policy, quality review, workforce demand, queue SLA, and overflow                            |
| AI Reception and Conversation | Governed chat/voice agents, approved knowledge/tools, qualification, booking, summaries, confidence, live handoff, testing, and human-approval policy                   |

## 9. Service, success, and experience modules

| Module                         | Responsibilities                                                                                                                                             |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Case Management                | Tickets/cases, types, pipelines, statuses, priorities, ownership, parent/child cases, related assets/orders, entitlements, escalation, and audit             |
| Omnichannel Service            | Email/chat/social/phone intake, routing, agent workspace, macros, suggested replies, swarming, collision control, and complete interaction history           |
| SLA and Entitlements           | Service contracts, coverage, business calendars, response/resolution targets, milestones, pauses, warnings, breaches, escalations, and exceptions            |
| Knowledge                      | Internal/public articles, categories, versions, review/approval, localization, search, feedback, case linking, suggested answers, and stale-content controls |
| Customer Self-Service          | Customer portal, case submission/status, knowledge search, community links, appointments, documents, invoices/orders references, profile, and preferences    |
| Customer Success               | Customer segments, lifecycle, onboarding plans, success plans, objectives, health scores, product/usage signals, risks, playbooks, touchpoints, and renewals |
| Feedback and Voice of Customer | CSAT, NPS, CES, custom surveys, sampling, delivery, responses, text analysis, alerts, close-the-loop cases, and trend reporting                              |
| Reputation Management          | Review requests, review-site connections, monitoring, response workflow, templates, escalation, sentiment, location rollups, and reputation reporting        |
| Field Service Coordination     | Work types, service appointments, dispatch references, technician/contractor visibility, asset/service history, and Maintenance module handoff               |
| Service Analytics              | Volume, backlog, deflection, first response, resolution, reopen, transfer, SLA, satisfaction, quality, staffing, and cost-to-serve                           |

## 10. Community, learning, loyalty, and growth modules

| Module               | Responsibilities                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Communities          | Customer/partner groups, spaces, memberships, posts, comments, events, moderation, gamification, knowledge links, and CRM profile activity             |
| Learning and Courses | Courses, lessons, media, cohorts, enrollment, access, progress, assessments, certificates, drip schedules, and product/contract entitlements           |
| Memberships          | Membership plans, gated resources, lifecycle, access grants, renewal references, community/course bundles, and member portal                           |
| Loyalty              | Programs, tiers, points ledger, earning/redemption rules, rewards, expiry, partner activity, liabilities export, fraud controls, and member statements |
| Referrals            | Referral programs, links/codes, advocates, prospects, qualification, rewards, fraud/duplicate controls, status, and attribution                        |
| Affiliate Management | Affiliates, applications, links, campaigns, clicks, conversions, commission rules, payout approvals/exports, disputes, assets, and portal              |
| Advocacy             | References, testimonials, reviews, case-study consent, speakers, advisory boards, nominations, requests, and recognition history                       |

## 11. Partner and agency modules

| Module                          | Responsibilities                                                                                                                                                                 |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Partner Relationship Management | Partner accounts, contacts, tiers, recruitment, onboarding, competencies, agreements, enablement, certification, plans, and performance                                          |
| Deal Registration               | Partner-submitted leads/deals, duplicate/conflict checks, territory rules, approval, protection windows, collaboration, and attribution                                          |
| Channel Sales                   | Partner opportunities, shared pipelines, referrals, reseller pricing references, quotes/orders handoff, commissions, forecasts, and partner portal                               |
| Marketing Development Funds     | Requests, budgets, plans, approvals, evidence, claims, reimbursements, and ROI                                                                                                   |
| Agency Workspace                | Agency/client hierarchy, sub-accounts, delegated administration, usage visibility, support access, branding, and cross-account operations                                        |
| White Label                     | Brand/domain/email/application settings, theme selection, custom client experience, provider abstraction, and safe platform attribution policy                                   |
| SaaS Packaging                  | Plans, feature/module entitlements, limits, trials, signup provisioning, upgrade/downgrade, suspension, cancellation, and Billing integration                                    |
| Usage Wallet and Rebilling      | Provider usage imports, wallets/credits, threshold reloads, cost/markup rules, client charges, exceptions, reconciliation, and Billing/Accounting handoff                        |
| Templates and Snapshots         | Versioned bundles of fields, pipelines, workflows, forms, funnels, calendars, templates, dashboards, and settings with preview, protected sharing, install, update, and rollback |
| Client Onboarding               | Intake, domain/provider connections, data import, snapshot application, verification, launch checklist, training, handoff, and health                                            |

## 12. Delivery, productivity, and operations modules

| Module                         | Responsibilities                                                                                                                               |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Projects                       | Post-sale projects, templates, milestones, tasks, dependencies, owners, time, files, status, risks, client visibility, and opportunity handoff |
| Resource Planning              | Skills, capacity, allocation, utilization, tentative/confirmed bookings, conflicts, rates, and staffing forecasts                              |
| Work Management                | Cross-record task boards, queues, recurring work, checklists, approvals, workload, dependencies, and personal/team views                       |
| Business Process Management    | Guided stages, required steps/data, approvals, validations, service processes, exception routing, and process versioning                       |
| CRM Automation Pack            | CRM triggers/actions/conditions, recipes, enrollment history, versioning, simulation, approval gates, and generic Automation module adapters   |
| Sandbox and Release Management | Configuration snapshots, test data policy, change sets, validation, dependency analysis, promotion, rollback, and environment comparison       |

## 13. Intelligence and AI modules

| Module                 | Responsibilities                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRM Analytics          | Governed datasets, dashboards, reports, pivots, funnels, cohorts, goals, schedules, exports, row-level access, and metric lineage                   |
| Predictive Models      | Lead/opportunity scoring, churn/renewal risk, next action/product, forecast, routing, model registry, evaluation, drift, and explanations           |
| CRM Copilot            | Permission-bounded search, summaries, preparation, drafting, record updates, task creation, and action confirmation using the Automation AI Gateway |
| Prospecting Agent      | Approved research, target selection, personalization, sequence preparation, engagement monitoring, and policy-based review/dispatch                 |
| Service Agent          | Case classification, knowledge retrieval, response drafts, resolution plans, tool use, confidence, escalation, and quality review                   |
| Marketing Agent        | Audience/campaign/content assistance, variations, journey recommendations, brand/consent checks, experiments, and approval workflow                 |
| Conversation Analytics | Topics, objections, competitors, talk ratios, questions, outcomes, coaching moments, quality scorecards, and trend comparison                       |

AI modules must expose sources, confidence, model/prompt versions, cost, approvals, and audit. They cannot widen access, silently make contractual commitments, or autonomously contact people outside configured consent and risk policy.

## 14. Extension marketplace and integration packs

### 14.1 Marketplace module

The Marketplace manages first-party and third-party apps, provider adapters, automation actions/triggers, themes, templates, and snapshots.

- App manifests declare publisher, package/category, compatibility, permissions/scopes, webhooks, data accessed, regions, pricing/entitlements, support, and uninstall behavior.
- Installation provides dependency and permission review, consent, configuration validation, connection tests, audit, and rollback.
- Publishers use signing/verification, versioned releases, review status, security contacts, changelogs, deprecation, and vulnerability response.
- Tenant administrators can allowlist/deny categories, approve elevated scopes, inspect activity, rotate/revoke credentials, and export installed-app inventory.
- Runtime isolation, rate limits, webhook signing, secret storage, egress controls, data minimization, delivery logs, and uninstall cleanup are mandatory.
- Reviews, ratings, trials, billing references, revenue share, refunds, support links, and protected template/snapshot distribution are optional marketplace capabilities.

### 14.2 Common integration packs

Build these as provider-neutral contracts plus separate adapters; product modules consume the contract, never a named vendor SDK.

| Pack                      | Common capabilities represented                                                                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Productivity              | Google Workspace and Microsoft 365 email, calendar, contacts, files, meetings, and identity connections                                                                     |
| Team Collaboration        | Slack and Microsoft Teams notifications, record unfurls, commands, approvals, and conversation linking                                                                      |
| Scheduling and Meetings   | Calendly-style schedulers plus Zoom, Teams, and Meet conference creation, attendance, and recording metadata                                                                |
| Sales Intelligence        | LinkedIn Sales Navigator-style context and Apollo/ZoomInfo/Clearbit-style prospecting, enrichment, intent, and verification                                                 |
| Documents and E-signature | DocuSign/PandaDoc-style document generation, negotiation, signatures, status, evidence, and storage                                                                         |
| Telephony and Messaging   | Twilio, Aircall, RingCentral and similar calling, numbers, recording, SMS, WhatsApp, and event adapters                                                                     |
| Marketing and Advertising | Google/Meta/LinkedIn ad leads, audiences, campaign performance, offline conversions, and consent signals                                                                    |
| Customer Service          | Intercom/Zendesk-style case, conversation, knowledge, customer, and status synchronization                                                                                  |
| Finance                   | Stripe/PayPal payment links/status plus QuickBooks/Xero accounting customer, invoice, payment, and reconciliation adapters                                                  |
| Commerce                  | Shopify/WooCommerce-style customer, catalog, cart, order, fulfillment, and lifecycle synchronization                                                                        |
| Delivery                  | Jira/GitHub/Linear-style issue, project, milestone, deployment, status, and customer-visible progress adapters                                                              |
| Integration Automation    | Zapier/Make-style triggers/actions, inbound/outbound webhooks, recipes, polling, replay, and connection diagnostics                                                         |
| Data Warehouse and BI     | Governed batch/stream export, reverse ETL, semantic metrics, warehouse/lake connections, and dashboard embedding                                                            |
| Migration                 | HubSpot, Salesforce, Pipedrive, and HighLevel import adapters with dry run, object/field mapping, identity matching, attachments, activities, ownership, and reconciliation |

Vendor names illustrate expected interoperability, not embedded dependencies or guaranteed provider availability.

## 15. Required end-to-end workflows

1. **Anonymous demand to lead:** consent-aware visit/ad/event/chat/form → identity/account matching → source/attribution → qualification → routing → response SLA.
2. **Prospect to opportunity:** ICP search/enrichment → review lawful outreach context → sequence/call/tasks → reply/meeting stop → qualify → convert with history.
3. **Opportunity to revenue:** execute playbook → inspect/coaching → configure/price → approve discount → quote/sign → order/subscription/payment handoff → forecast actualization.
4. **Customer onboarding:** won deal → provision client/project/success plan → tasks/appointments/training → activation/adoption → handoff and health baseline.
5. **Campaign to pipeline:** segment → campaign/journey/assets → consent and frequency evaluation → deliver → capture engagement → score/route → attribute pipeline/revenue.
6. **Omnichannel support:** message/call/portal → identity and entitlement → route → SLA → knowledge/agent response → escalation → resolution → feedback/knowledge improvement.
7. **Customer success and renewal:** ingest usage/service/commercial signals → calculate health → trigger playbook → manage risks/objectives → renewal/expansion opportunity → outcome.
8. **Partner sale:** recruit/onboard partner → register deal → conflict/territory review → collaborate/quote → order → credit/commission → partner performance.
9. **Agency SaaS onboarding:** select plan → create sub-account → apply protected snapshot → connect providers/domain → import/validate → launch → meter/rebill/support.
10. **Marketplace app lifecycle:** discover → review scopes/data/pricing → approve/install → configure/test → monitor/update → revoke/uninstall/export/delete according to policy.
11. **Data stewardship:** ingest/sync → normalize → match → review merge → preserve lineage/consent/ownership → activate audiences → monitor quality and sync drift.

Every workflow identifies its record owner, source of truth, states, actor/tenant/site context, permissions, consent, approvals, events, idempotency, compensation, SLA, audit, metrics, and operator recovery.

## 16. Shared product requirements

- Support tenant, legal entity, division, brand, branch, territory, team, queue, partner, agency, and client-account contexts without competing tenancy models.
- Provide configurable objects/fields/layouts/pipelines while preserving schema validation, upgrade compatibility, authorization, search, audit, and reporting.
- Maintain one chronological timeline of material customer interactions, state changes, documents, automation, consent, provider sync, and linked product records.
- Support list, Kanban, calendar, inbox, map where relevant, dashboard, workspace, and mobile-responsive views with saved filters and bulk actions.
- Make imports, synchronizations, automations, message delivery, stage actions, attribution, and provider webhooks idempotent and replayable.
- Distinguish authored facts, imported facts, calculated values, enrichment, predictions, and generated suggestions with field-level provenance.
- Offer versioned REST APIs, webhooks, domain events, provider registries, Filament plugins, and theme-ready Livewire/Blade extension points.
- Provide configurable limits/entitlements by application, tenant/client, plan, module, user, channel, provider, and usage unit.
- Require approvals for material discounts, contracts, refunds, payouts, bulk destructive changes, high-risk outbound automation, impersonation, and provider-scope escalation.

## 17. Security, privacy, and compliance gates

- Enforce record, field, object, pipeline, territory, team, partner, client-account, channel, and action permissions across UI, API, search, exports, automation, jobs, and analytics.
- Apply consent, suppression, do-not-contact, recording, quiet-hour, age/region, data-purpose, retention, and residency rules before collection and delivery.
- Encrypt provider credentials and sensitive identity/contact/recording data; redact secrets and message bodies from routine telemetry.
- Prevent unsafe automatic identity merges and preserve undo/review evidence for high-impact data operations.
- Protect forms/chat/portals from spam, injection, enumeration, malicious uploads, replay, and abusive automation.
- Provide audit and separation of duties for exports, bulk communications, consent changes, data merges, forecasts, commissions, marketplace apps, agency access, and AI actions.
- Require security review for marketplace apps and high-risk provider scopes, including webhook verification, secret rotation, egress/data access, uninstall, and incident response.

## 18. Quality and operational gates

- Contract-test every provider adapter and migration connector against shared capability behavior.
- Test tenant/client/partner/territory/field visibility, consent and suppression, identity merge, routing races, sequence stop rules, attribution, SLA clocks, forecast rollups, commission splits, and webhook replay.
- Test large imports, high-volume timeline/feed, audience refresh, journey fanout, email/message queues, search indexing, reporting, portal traffic, and agency cross-account operations.
- Reconcile email/calendar, ad, payment, order, invoice, telephony, enrichment, support, and marketplace state; expose drift and operator repair.
- Measure lead response, conversion, sales cycle, activity quality, forecast accuracy, win/loss, campaign influence, deliverability, SLA, satisfaction, health, retention, app failures, sync latency, and cost.
- Alert on lead leakage, routing backlog, sequence misbehavior, deliverability/reputation risk, consent failure, stale deals, forecast anomalies, SLA breach, churn risk, provider outage, and integration drift.
- Provide fixtures, fake providers, sandboxes/test destinations, representative migrations, dashboards, runbooks, replay, and disaster-recovery procedures.

## 19. Delivery phases

1. **Customer foundation:** CRM Core, Customer Data Model, Data Operations, Consent, Territories/Ownership, Search, timeline, Activities, and base APIs.
2. **Sales CRM:** Lead Capture/Qualification/Routing, Sales Pipelines/Workspace, Scheduling, Email Productivity, Sales Engagement, goals, base analytics, and common productivity adapters.
3. **Revenue execution:** Forecasting, Revenue Intelligence, Conversation Intelligence, Playbooks, Account Planning, CPQ, Proposals, Contracts, and Billing/Ecommerce handoff.
4. **Marketing and acquisition:** Segmentation, Campaigns, Journeys, Email/Mobile Marketing, Forms/Surveys, Chat/Bots, Landing Pages/Funnels, Ads, Web Intent, Prospecting/Enrichment, Attribution, and ABM.
5. **Service and success:** Unified Conversations, Channel Gateway, Telephony/Contact Center, Case Management, SLA, Knowledge, Self-Service, Feedback, Reputation, Customer Success, and Service Analytics.
6. **Growth ecosystems:** Communities, Learning, Memberships, Loyalty, Referrals, Affiliates, Advocacy, Events/Webinars, and field-service coordination.
7. **Enterprise and channel:** Quotas/Incentives, Partner Management, Deal Registration, Channel Sales, MDF, resource/project operations, BPM, sandbox/release management, and advanced CDP/data activation.
8. **Agency and extensibility:** Agency Workspace, White Label, SaaS Packaging, Usage/Rebilling, Snapshots, Client Onboarding, Marketplace, integration packs, and migration adapters.
9. **Governed intelligence:** predictive models, CRM Copilot, prospecting/service/marketing agents, advanced conversation analytics, evaluation, and continuous optimization.

Each phase delivers complete vertical workflows, migrations, accessible UI, permissions, consent, provider failure handling, reconciliation, telemetry, runbooks, and issue-ready acceptance criteria.

## 20. Benchmark coverage and source basis

The module map intentionally covers the following official benchmark capability families without copying vendor-specific architecture:

- **HubSpot:** Smart CRM, Marketing, Sales, Service, Content, Data, and commerce/revenue capabilities, including custom objects, sequences, forecasting, playbooks, help desk, customer success, data quality, landing content, and automation.
- **Salesforce:** sales, service/contact center, marketing journeys/personalization, unified customer data, revenue lifecycle, partner/customer experiences, field service, analytics, and platform extensibility.
- **Pipedrive:** pipeline-first selling, Leads Inbox, LeadBooster-style chatbot/live chat/forms/prospecting, web visitors, scheduling, activities/goals, Pulse-style enrichment/scoring/sequences/feed, campaigns, projects, and smart documents.
- **HighLevel:** opportunities, conversations, workflows, funnels/websites, appointments, reputation, social/advertising, documents/contracts, communities/courses, affiliates, agency sub-accounts, white label, SaaS packaging, rebilling/wallets, snapshots, and marketplace distribution.

Official reference starting points:

- [HubSpot customer platform and product hubs](https://www.hubspot.com/products/get-started)
- [HubSpot enterprise platform capabilities](https://www.hubspot.com/products/crm/enterprise)
- [Salesforce Customer 360 products](https://www.salesforce.com/products/)
- [Salesforce Revenue Cloud overview](https://www.salesforce.com/sales/revenue-lifecycle-management/revenue-cloud/)
- [Pipedrive product and add-on capabilities](https://www.pipedrive.com/en/products)
- [Pipedrive plan and add-on feature reference](https://support.pipedrive.com/en/article/what-features-do-the-pipedrive-plans-have)
- [HighLevel product knowledge base](https://help.gohighlevel.com/support/solutions)
- [HighLevel snapshot distribution](https://help.gohighlevel.com/support/solutions/articles/48000982513-how-to-share-snapshots)

These references establish expected coverage only. Liberu package boundaries, contracts, terminology, and implementation remain independent and provider-neutral.

## 21. Definition of done

Liberu CRM is complete when selected modules can be installed independently; customer identity, consent, ownership, and provenance remain trustworthy; acquisition-to-renewal workflows are authorized, measurable, recoverable, and reconciled; providers are replaceable; enterprise, partner, and agency isolation holds; marketplace extensions are governed; and every module can be converted into a focused GitHub epic with child issues.

## 22. GitHub issue mapping

Create one epic for each module table row rather than combining a whole section into a monolith. Each epic includes capability boundary and exclusions, package category, dependencies/contracts, data ownership, states/workflows, permissions and consent, APIs/events, provider adapters, Filament/Livewire/theme extension points, migrations/imports, idempotency/failure recovery, tests, telemetry, runbook, and documentation.

Create separate adapter issues for each external provider and separate adoption issues for each product/application. Marketplace-add-on parity belongs in the relevant provider adapter or capability module; it must not introduce vendor-specific behavior into CRM Core.

## 23. Liberu AI-assisted communications profile

Liberu CRM uses AI across voice calls, SMS/WhatsApp/web messaging, email, social direct messages/comments/posts, scheduled social content, and advertising plans. The [Liberu AI/channel implementation](../liberu/implementation/AI-CHANNELS.md) defines the cross-product contract; this CRM scope owns the customer-facing conversation, case, channel, consent, routing, approval, and audit behavior.

- Voice and messaging must provide a clear **Talk to a person** or **Request a callback** method. Explicit requests, low confidence, complaints, sensitive/legal/financial/security topics, repeated misunderstanding, payment/entitlement disputes, and configured SLA/VIP risks stop AI automation and route a CRM conversation/case to a human queue.
- The human receives a policy-safe summary, identity confidence, intent, urgency/SLA, consent/recording state, callback preference, citations, correlation ID, and AI/prompt versions. AI stops replying after handoff until a human resumes it.
- Email and social AI may triage, draft, translate, summarize, suggest cases, propose comments/posts, schedule approved content, and prepare advertising/audience/UTM plans. Public posting, replying, advertising spend, claims, sensitive messages, and schedule publication require approval unless an explicitly reviewed low-risk policy applies.
- Campaign, journey, reply, opt-out, complaint, conversion, and handoff state must suppress linked later outreach. The dialer `next_contact_at` and consent/contact-protection rules apply to AI calls and sequences.
- CRM publishes canonical, consent-filtered events to Analytics Core. GTM/browser GA4, server GA4, Meta client/pixel, and Meta CAPI share event IDs for deduplication; server events reference authoritative CRM/Billing/Ecommerce outcomes and never contain message bodies or transcripts.

## Product Scope

**Purpose:** Composable customer platform for data, demand generation, sales, marketing, service, customer success, partner operations, and agency delivery.
**Architecture:** Packages and provider adapters follow [MODULES.md](../../architecture/MODULES.md); APIs, marketplace connectors, and webhooks follow [API.md](../../architecture/API.md); staff, partner, and customer experiences follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines CRM-domain behavior only. Reuse CMS, Automation, Billing, Ecommerce, Accounting, and other Liberu contracts instead of duplicating their authoritative capabilities.

## 1. Outcomes

- Maintain a governed, permission-aware customer graph and timeline across the complete lifecycle.
- Capture and qualify demand, guide repeatable sales execution, and produce trustworthy forecasts.
- Orchestrate consent-aware engagement across marketing, sales, support, and success channels.
- Turn accepted business into contracts, orders, subscriptions, projects, onboarding, retention, and expansion.
- Support direct businesses, multi-brand enterprises, partners, and white-label agencies without provider lock-in.
- Match the commonly expected capability breadth of HubSpot, Salesforce, Pipedrive, and HighLevel while retaining independently installable package boundaries.

## 2. Domain ownership rules

- CRM owns customer relationships, engagement context, demand, sales/service processes, and customer-facing lifecycle coordination.
- Boilerplate owns identity, organizations/teams, authorization, localization, currency context, settings, audit, and generic integrations.
- CMS owns durable website/content publishing; CRM owns conversion journeys, campaign landing experiences, forms, and attribution mappings that consume CMS/theme extension points.
- Automation owns the generic workflow/AI runtime; CRM packages own CRM triggers, actions, recipes, policies, and approval requirements.
- Billing/Ecommerce own authoritative catalog, pricing, checkout, invoices, subscriptions, payments, and refunds; CRM stores references and commercial snapshots required for selling.
- Accounting owns postings and financial statements; Projects owns delivery coordination where installed.
- External systems are implemented as contract, core, and provider-adapter packages under `MODULES.md`.

## 3. Customer data and platform modules

| Module                    | Responsibilities                                                                                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRM Core                  | Contacts, organizations, households, relationships, owners, teams, tags, notes, attachments, favorites, record lifecycle, and unified timeline                 |
| Customer Data Model       | Standard/custom objects, fields, relationships, layouts, validation, calculated fields, required-by-stage fields, and schema versioning                        |
| Customer Data Platform    | Source profiles, identity resolution, unified profiles, audience activation, event ingestion, consent-aware calculated attributes, and profile lineage         |
| Data Operations           | Imports/exports, field mapping, normalization, enrichment orchestration, duplicate detection/merge, formatting, quality rules, schedules, and exception queues |
| Consent and Preferences   | Lawful basis, subscriptions, channel/topic preferences, suppression, quiet hours, recording consent, proof, expiry, withdrawal, and policy evaluation          |
| Territories and Ownership | Territories, books of business, teams, queues, assignment rules, round-robin/capacity routing, temporary coverage, and ownership history                       |
| CRM Search                | Permission-aware global search, saved views, filters, related-record search, recents, suggestions, and index reconciliation                                    |
| CRM Documents             | Sales/service files, templates, folders, links, access, engagement tracking, versioning, retention, and external-storage adapters                              |
| Collaboration             | Record comments, mentions, followers, shared work queues, approvals, handoffs, internal channels, and collaboration-provider adapters                          |

## 4. Demand generation and acquisition modules

| Module                    | Responsibilities                                                                                                                                                |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lead Capture              | Leads inbox, manual/import/API capture, forms, surveys, QR codes, chat, calls, advertisements, events, referrals, and source metadata                           |
| Prospecting               | Ideal-customer profiles, prospect searches, list building, research queues, contact reveal/credits, provider provenance, and compliant export/outreach handoff  |
| Enrichment                | Company/contact firmographic, demographic, technographic, social, verification, change monitoring, confidence, field-level provenance, and provider adapters    |
| Web Intent                | First-party visits, account identification adapters, page/content engagement, scoring signals, alerts, buyer intent, consent, and lead/account conversion       |
| Lead Qualification        | Lifecycle stages, fit/engagement scoring, MQL/PQL/SQL/service-qualified rules, qualification frameworks, disqualification, nurture, and conversion              |
| Routing                   | Rule, territory, skill, language, availability, workload, value, SLA, and round-robin assignment with fallback and acceptance timers                            |
| Forms and Surveys         | Drag-and-drop schemas, conditional fields, progressive profiling, validation, spam controls, consent, hidden attribution, embedding, submissions, and follow-up |
| Chat and Bots             | Web chat, bot/playbook builder, qualification, knowledge answers, meeting booking, live-agent handoff, office hours, transcripts, and channel identity          |
| Landing Pages and Funnels | Multi-step funnels, landing/thank-you pages, templates, domains, SEO metadata, personalization, forms, order links, preview, publish, and conversion tracking   |
| Conversion Optimization   | A/B and multivariate tests, traffic allocation, goals, statistical policy, popups, banners, CTAs, personalization rules, and experiment reporting               |
| Events and Webinars       | Physical/virtual events, registration, capacity, tickets/attendance, sessions, speakers, reminders, check-in, recording links, follow-up, and provider adapters |

## 5. Sales execution modules

| Module                    | Responsibilities                                                                                                                                                      |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sales Pipelines           | Multiple pipelines, stages, opportunities, products, values, probabilities, close dates, competitors, dependencies, stage history, rotting, and loss reasons          |
| Sales Workspace           | Prioritized seller feed, leads/deals inbox, overdue/risk indicators, next best action, daily agenda, quick updates, and contextual customer history                   |
| Activities                | Tasks, calls, meetings, emails, deadlines, recurrence, queues, bulk completion, reminders, outcomes, goals, and activity reporting                                    |
| Scheduling                | Personal/team/round-robin links, availability, buffers, minimum notice, questions, reminders, reschedule/cancel, no-show, routing, and calendar adapters              |
| Sales Engagement          | Sequences/cadences, multi-channel steps, templates/snippets, task queues, enrollment/re-entry, throttles, timezone windows, reply/meeting stop rules, and experiments |
| Email Productivity        | Mailbox sync, send/log, templates, snippets, scheduling, open/click/reply tracking policy, shared/team inbox, signatures, sidebars, and Gmail/Outlook adapters        |
| Conversation Intelligence | Call/meeting recording, transcription, summaries, topics, questions, objections, competitors, sentiment policy, action items, highlights, and searchable evidence     |
| Playbooks and Enablement  | Guided scripts, qualification cards, battlecards, onboarding content, required evidence, coaching checklists, document/content recommendations, and usage analytics   |
| Forecasting               | Forecast categories, rollups, manager adjustments, commit/best-case/pipeline views, coverage, trend, scenario, history, accuracy, and submission workflow             |
| Revenue Intelligence      | Pipeline inspection, health/risk, engagement gaps, opportunity scoring, relationship maps, white-space/next-product suggestions, anomaly detection, and alerts        |
| Goals and Performance     | Individual/team/company goals, activity/outcome targets, scorecards, leaderboards, reviews, coaching plans, and performance history                                   |
| Quotas and Incentives     | Quotas, ramps, crediting, splits, territories, attainment, commission plans, accelerators, adjustments, disputes, approvals, and payroll/export adapters              |
| Account Planning          | Account hierarchies, stakeholders, influence maps, whitespace, account plans, objectives, risks, mutual action plans, and account-based coordination                  |

## 6. Revenue and commercial modules

| Module                        | Responsibilities                                                                                                                                                 |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRM Product Workspace         | Sales-facing catalog projections, bundles, entitlements, price-book references, product eligibility, and governed Billing/Ecommerce synchronization              |
| CPQ                           | Guided configuration, compatibility rules, price books, tiers, discounts, approvals, margin guardrails, amendments, renewals, and authoritative pricing adapters |
| Proposals and Quotes          | Branded templates, sections, scope, line items, optional choices, versions, comments, approvals, delivery, engagement, acceptance, and expiry                    |
| Contracts                     | Parties, terms, clauses, obligations, versions, negotiation, approvals, signatures, amendments, renewals, notices, repository links, and compliance dates        |
| Orders and Payments Workspace | Payment links, deposits, order/subscription references, invoice/payment status, refunds/disputes visibility, and Billing/Ecommerce handoff                       |
| Revenue Lifecycle             | Opportunity-to-order orchestration, assets/installed products, entitlements, renewals, upgrades, downgrades, cancellation, usage signals, and fallout queues     |

These modules never duplicate authoritative pricing, payment, subscription, invoice, order, or accounting ledgers.

## 7. Marketing modules

| Module                  | Responsibilities                                                                                                                                               |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Segmentation            | Static/dynamic audiences, nested conditions, behavioral events, calculated attributes, exclusions, estimated counts, refresh, and lineage                      |
| Campaigns               | Campaign hierarchy, briefs, objectives, budget, assets, channels, audience, owners, calendar, tasks, costs, responses, influence, and ROI                      |
| Journey Orchestration   | Triggered/scheduled journeys, branching, waits, goals, re-entry, suppression, frequency caps, experiments, stop-on-response, and versioned publication         |
| Email Marketing         | Drag-and-drop and code templates, personalization, dynamic content, test sends, inbox previews, deliverability controls, scheduling, throttling, and analytics |
| Mobile Messaging        | Consent-aware SMS/MMS/WhatsApp/push campaigns, templates, short links, keywords, opt-in/out, quiet hours, sender governance, and delivery/reply handling       |
| Advertising             | Ad-account connections, campaign visibility, lead-ad ingestion, CRM audiences, offline/server conversions, spend/performance sync, and attribution             |
| Account-Based Marketing | Target accounts, tiers, buying committees, intent, engagement rollups, account audiences, plays, coverage, pipeline influence, and measurement                 |
| Personalization         | Rules and decisioning for content, offer, channel, send time, locale, lifecycle, and customer attributes with holdouts and fallback                            |
| Marketing Resources     | Brand kits, reusable content blocks, campaign files, templates, approvals, usage rights, and CMS/media references                                              |
| Attribution             | First/last/multi-touch models, campaign members, source normalization, UTM/click IDs, offline conversions, influence, cost allocation, and model comparison    |

## 8. Communications and contact-center modules

| Module                        | Responsibilities                                                                                                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unified Conversations         | Omnichannel threads, participants, identity matching, assignments, collision detection, drafts, internal notes, attachments, delivery/read state, and timeline          |
| Channel Gateway               | Provider-neutral email, SMS/MMS, WhatsApp, web chat, social messaging, and push contracts, routing, templates, health, and provider selection                           |
| Telephony                     | Numbers, caller ID, IVR, queues, business hours, skills, recording, voicemail, transfers, dispositions, click-to-call, call logging, and provider adapters              |
| Dialer and Outreach           | Power/preview/progressive dialing, prioritized lists, scripts, local-time policy, retries, voicemail drop, answer detection adapters, outcomes, and compliance controls |
| Contact Center                | Agent presence, capacity, skills, routing, supervisor views, whisper/barge policy, quality review, workforce demand, queue SLA, and overflow                            |
| AI Reception and Conversation | Governed chat/voice agents, approved knowledge/tools, qualification, booking, summaries, confidence, live handoff, testing, and human-approval policy                   |

## 9. Service, success, and experience modules

| Module                         | Responsibilities                                                                                                                                             |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Case Management                | Tickets/cases, types, pipelines, statuses, priorities, ownership, parent/child cases, related assets/orders, entitlements, escalation, and audit             |
| Omnichannel Service            | Email/chat/social/phone intake, routing, agent workspace, macros, suggested replies, swarming, collision control, and complete interaction history           |
| SLA and Entitlements           | Service contracts, coverage, business calendars, response/resolution targets, milestones, pauses, warnings, breaches, escalations, and exceptions            |
| Knowledge                      | Internal/public articles, categories, versions, review/approval, localization, search, feedback, case linking, suggested answers, and stale-content controls |
| Customer Self-Service          | Customer portal, case submission/status, knowledge search, community links, appointments, documents, invoices/orders references, profile, and preferences    |
| Customer Success               | Customer segments, lifecycle, onboarding plans, success plans, objectives, health scores, product/usage signals, risks, playbooks, touchpoints, and renewals |
| Feedback and Voice of Customer | CSAT, NPS, CES, custom surveys, sampling, delivery, responses, text analysis, alerts, close-the-loop cases, and trend reporting                              |
| Reputation Management          | Review requests, review-site connections, monitoring, response workflow, templates, escalation, sentiment, location rollups, and reputation reporting        |
| Field Service Coordination     | Work types, service appointments, dispatch references, technician/contractor visibility, asset/service history, and Maintenance module handoff               |
| Service Analytics              | Volume, backlog, deflection, first response, resolution, reopen, transfer, SLA, satisfaction, quality, staffing, and cost-to-serve                           |

## 10. Community, learning, loyalty, and growth modules

| Module               | Responsibilities                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Communities          | Customer/partner groups, spaces, memberships, posts, comments, events, moderation, gamification, knowledge links, and CRM profile activity             |
| Learning and Courses | Courses, lessons, media, cohorts, enrollment, access, progress, assessments, certificates, drip schedules, and product/contract entitlements           |
| Memberships          | Membership plans, gated resources, lifecycle, access grants, renewal references, community/course bundles, and member portal                           |
| Loyalty              | Programs, tiers, points ledger, earning/redemption rules, rewards, expiry, partner activity, liabilities export, fraud controls, and member statements |
| Referrals            | Referral programs, links/codes, advocates, prospects, qualification, rewards, fraud/duplicate controls, status, and attribution                        |
| Affiliate Management | Affiliates, applications, links, campaigns, clicks, conversions, commission rules, payout approvals/exports, disputes, assets, and portal              |
| Advocacy             | References, testimonials, reviews, case-study consent, speakers, advisory boards, nominations, requests, and recognition history                       |

## 11. Partner and agency modules

| Module                          | Responsibilities                                                                                                                                                                 |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Partner Relationship Management | Partner accounts, contacts, tiers, recruitment, onboarding, competencies, agreements, enablement, certification, plans, and performance                                          |
| Deal Registration               | Partner-submitted leads/deals, duplicate/conflict checks, territory rules, approval, protection windows, collaboration, and attribution                                          |
| Channel Sales                   | Partner opportunities, shared pipelines, referrals, reseller pricing references, quotes/orders handoff, commissions, forecasts, and partner portal                               |
| Marketing Development Funds     | Requests, budgets, plans, approvals, evidence, claims, reimbursements, and ROI                                                                                                   |
| Agency Workspace                | Agency/client hierarchy, sub-accounts, delegated administration, usage visibility, support access, branding, and cross-account operations                                        |
| White Label                     | Brand/domain/email/application settings, theme selection, custom client experience, provider abstraction, and safe platform attribution policy                                   |
| SaaS Packaging                  | Plans, feature/module entitlements, limits, trials, signup provisioning, upgrade/downgrade, suspension, cancellation, and Billing integration                                    |
| Usage Wallet and Rebilling      | Provider usage imports, wallets/credits, threshold reloads, cost/markup rules, client charges, exceptions, reconciliation, and Billing/Accounting handoff                        |
| Templates and Snapshots         | Versioned bundles of fields, pipelines, workflows, forms, funnels, calendars, templates, dashboards, and settings with preview, protected sharing, install, update, and rollback |
| Client Onboarding               | Intake, domain/provider connections, data import, snapshot application, verification, launch checklist, training, handoff, and health                                            |

## 12. Delivery, productivity, and operations modules

| Module                         | Responsibilities                                                                                                                               |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Projects                       | Post-sale projects, templates, milestones, tasks, dependencies, owners, time, files, status, risks, client visibility, and opportunity handoff |
| Resource Planning              | Skills, capacity, allocation, utilization, tentative/confirmed bookings, conflicts, rates, and staffing forecasts                              |
| Work Management                | Cross-record task boards, queues, recurring work, checklists, approvals, workload, dependencies, and personal/team views                       |
| Business Process Management    | Guided stages, required steps/data, approvals, validations, service processes, exception routing, and process versioning                       |
| CRM Automation Pack            | CRM triggers/actions/conditions, recipes, enrollment history, versioning, simulation, approval gates, and generic Automation module adapters   |
| Sandbox and Release Management | Configuration snapshots, test data policy, change sets, validation, dependency analysis, promotion, rollback, and environment comparison       |

## 13. Intelligence and AI modules

| Module                 | Responsibilities                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRM Analytics          | Governed datasets, dashboards, reports, pivots, funnels, cohorts, goals, schedules, exports, row-level access, and metric lineage                   |
| Predictive Models      | Lead/opportunity scoring, churn/renewal risk, next action/product, forecast, routing, model registry, evaluation, drift, and explanations           |
| CRM Copilot            | Permission-bounded search, summaries, preparation, drafting, record updates, task creation, and action confirmation using the Automation AI Gateway |
| Prospecting Agent      | Approved research, target selection, personalization, sequence preparation, engagement monitoring, and policy-based review/dispatch                 |
| Service Agent          | Case classification, knowledge retrieval, response drafts, resolution plans, tool use, confidence, escalation, and quality review                   |
| Marketing Agent        | Audience/campaign/content assistance, variations, journey recommendations, brand/consent checks, experiments, and approval workflow                 |
| Conversation Analytics | Topics, objections, competitors, talk ratios, questions, outcomes, coaching moments, quality scorecards, and trend comparison                       |

AI modules must expose sources, confidence, model/prompt versions, cost, approvals, and audit. They cannot widen access, silently make contractual commitments, or autonomously contact people outside configured consent and risk policy.

## 14. Extension marketplace and integration packs

### 14.1 Marketplace module

The Marketplace manages first-party and third-party apps, provider adapters, automation actions/triggers, themes, templates, and snapshots.

- App manifests declare publisher, package/category, compatibility, permissions/scopes, webhooks, data accessed, regions, pricing/entitlements, support, and uninstall behavior.
- Installation provides dependency and permission review, consent, configuration validation, connection tests, audit, and rollback.
- Publishers use signing/verification, versioned releases, review status, security contacts, changelogs, deprecation, and vulnerability response.
- Tenant administrators can allowlist/deny categories, approve elevated scopes, inspect activity, rotate/revoke credentials, and export installed-app inventory.
- Runtime isolation, rate limits, webhook signing, secret storage, egress controls, data minimization, delivery logs, and uninstall cleanup are mandatory.
- Reviews, ratings, trials, billing references, revenue share, refunds, support links, and protected template/snapshot distribution are optional marketplace capabilities.

### 14.2 Common integration packs

Build these as provider-neutral contracts plus separate adapters; product modules consume the contract, never a named vendor SDK.

| Pack                      | Common capabilities represented                                                                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Productivity              | Google Workspace and Microsoft 365 email, calendar, contacts, files, meetings, and identity connections                                                                     |
| Team Collaboration        | Slack and Microsoft Teams notifications, record unfurls, commands, approvals, and conversation linking                                                                      |
| Scheduling and Meetings   | Calendly-style schedulers plus Zoom, Teams, and Meet conference creation, attendance, and recording metadata                                                                |
| Sales Intelligence        | LinkedIn Sales Navigator-style context and Apollo/ZoomInfo/Clearbit-style prospecting, enrichment, intent, and verification                                                 |
| Documents and E-signature | DocuSign/PandaDoc-style document generation, negotiation, signatures, status, evidence, and storage                                                                         |
| Telephony and Messaging   | Twilio, Aircall, RingCentral and similar calling, numbers, recording, SMS, WhatsApp, and event adapters                                                                     |
| Marketing and Advertising | Google/Meta/LinkedIn ad leads, audiences, campaign performance, offline conversions, and consent signals                                                                    |
| Customer Service          | Intercom/Zendesk-style case, conversation, knowledge, customer, and status synchronization                                                                                  |
| Finance                   | Stripe/PayPal payment links/status plus QuickBooks/Xero accounting customer, invoice, payment, and reconciliation adapters                                                  |
| Commerce                  | Shopify/WooCommerce-style customer, catalog, cart, order, fulfillment, and lifecycle synchronization                                                                        |
| Delivery                  | Jira/GitHub/Linear-style issue, project, milestone, deployment, status, and customer-visible progress adapters                                                              |
| Integration Automation    | Zapier/Make-style triggers/actions, inbound/outbound webhooks, recipes, polling, replay, and connection diagnostics                                                         |
| Data Warehouse and BI     | Governed batch/stream export, reverse ETL, semantic metrics, warehouse/lake connections, and dashboard embedding                                                            |
| Migration                 | HubSpot, Salesforce, Pipedrive, and HighLevel import adapters with dry run, object/field mapping, identity matching, attachments, activities, ownership, and reconciliation |

Vendor names illustrate expected interoperability, not embedded dependencies or guaranteed provider availability.

## 15. Required end-to-end workflows

1. **Anonymous demand to lead:** consent-aware visit/ad/event/chat/form → identity/account matching → source/attribution → qualification → routing → response SLA.
2. **Prospect to opportunity:** ICP search/enrichment → review lawful outreach context → sequence/call/tasks → reply/meeting stop → qualify → convert with history.
3. **Opportunity to revenue:** execute playbook → inspect/coaching → configure/price → approve discount → quote/sign → order/subscription/payment handoff → forecast actualization.
4. **Customer onboarding:** won deal → provision client/project/success plan → tasks/appointments/training → activation/adoption → handoff and health baseline.
5. **Campaign to pipeline:** segment → campaign/journey/assets → consent and frequency evaluation → deliver → capture engagement → score/route → attribute pipeline/revenue.
6. **Omnichannel support:** message/call/portal → identity and entitlement → route → SLA → knowledge/agent response → escalation → resolution → feedback/knowledge improvement.
7. **Customer success and renewal:** ingest usage/service/commercial signals → calculate health → trigger playbook → manage risks/objectives → renewal/expansion opportunity → outcome.
8. **Partner sale:** recruit/onboard partner → register deal → conflict/territory review → collaborate/quote → order → credit/commission → partner performance.
9. **Agency SaaS onboarding:** select plan → create sub-account → apply protected snapshot → connect providers/domain → import/validate → launch → meter/rebill/support.
10. **Marketplace app lifecycle:** discover → review scopes/data/pricing → approve/install → configure/test → monitor/update → revoke/uninstall/export/delete according to policy.
11. **Data stewardship:** ingest/sync → normalize → match → review merge → preserve lineage/consent/ownership → activate audiences → monitor quality and sync drift.

Every workflow identifies its record owner, source of truth, states, actor/tenant/site context, permissions, consent, approvals, events, idempotency, compensation, SLA, audit, metrics, and operator recovery.

## 16. Shared product requirements

- Support tenant, legal entity, division, brand, branch, territory, team, queue, partner, agency, and client-account contexts without competing tenancy models.
- Provide configurable objects/fields/layouts/pipelines while preserving schema validation, upgrade compatibility, authorization, search, audit, and reporting.
- Maintain one chronological timeline of material customer interactions, state changes, documents, automation, consent, provider sync, and linked product records.
- Support list, Kanban, calendar, inbox, map where relevant, dashboard, workspace, and mobile-responsive views with saved filters and bulk actions.
- Make imports, synchronizations, automations, message delivery, stage actions, attribution, and provider webhooks idempotent and replayable.
- Distinguish authored facts, imported facts, calculated values, enrichment, predictions, and generated suggestions with field-level provenance.
- Offer versioned REST APIs, webhooks, domain events, provider registries, Filament plugins, and theme-ready Livewire/Blade extension points.
- Provide configurable limits/entitlements by application, tenant/client, plan, module, user, channel, provider, and usage unit.
- Require approvals for material discounts, contracts, refunds, payouts, bulk destructive changes, high-risk outbound automation, impersonation, and provider-scope escalation.

## 17. Security, privacy, and compliance gates

- Enforce record, field, object, pipeline, territory, team, partner, client-account, channel, and action permissions across UI, API, search, exports, automation, jobs, and analytics.
- Apply consent, suppression, do-not-contact, recording, quiet-hour, age/region, data-purpose, retention, and residency rules before collection and delivery.
- Encrypt provider credentials and sensitive identity/contact/recording data; redact secrets and message bodies from routine telemetry.
- Prevent unsafe automatic identity merges and preserve undo/review evidence for high-impact data operations.
- Protect forms/chat/portals from spam, injection, enumeration, malicious uploads, replay, and abusive automation.
- Provide audit and separation of duties for exports, bulk communications, consent changes, data merges, forecasts, commissions, marketplace apps, agency access, and AI actions.
- Require security review for marketplace apps and high-risk provider scopes, including webhook verification, secret rotation, egress/data access, uninstall, and incident response.

## 18. Quality and operational gates

- Contract-test every provider adapter and migration connector against shared capability behavior.
- Test tenant/client/partner/territory/field visibility, consent and suppression, identity merge, routing races, sequence stop rules, attribution, SLA clocks, forecast rollups, commission splits, and webhook replay.
- Test large imports, high-volume timeline/feed, audience refresh, journey fanout, email/message queues, search indexing, reporting, portal traffic, and agency cross-account operations.
- Reconcile email/calendar, ad, payment, order, invoice, telephony, enrichment, support, and marketplace state; expose drift and operator repair.
- Measure lead response, conversion, sales cycle, activity quality, forecast accuracy, win/loss, campaign influence, deliverability, SLA, satisfaction, health, retention, app failures, sync latency, and cost.
- Alert on lead leakage, routing backlog, sequence misbehavior, deliverability/reputation risk, consent failure, stale deals, forecast anomalies, SLA breach, churn risk, provider outage, and integration drift.
- Provide fixtures, fake providers, sandboxes/test destinations, representative migrations, dashboards, runbooks, replay, and disaster-recovery procedures.

## 19. Delivery phases

1. **Customer foundation:** CRM Core, Customer Data Model, Data Operations, Consent, Territories/Ownership, Search, timeline, Activities, and base APIs.
2. **Sales CRM:** Lead Capture/Qualification/Routing, Sales Pipelines/Workspace, Scheduling, Email Productivity, Sales Engagement, goals, base analytics, and common productivity adapters.
3. **Revenue execution:** Forecasting, Revenue Intelligence, Conversation Intelligence, Playbooks, Account Planning, CPQ, Proposals, Contracts, and Billing/Ecommerce handoff.
4. **Marketing and acquisition:** Segmentation, Campaigns, Journeys, Email/Mobile Marketing, Forms/Surveys, Chat/Bots, Landing Pages/Funnels, Ads, Web Intent, Prospecting/Enrichment, Attribution, and ABM.
5. **Service and success:** Unified Conversations, Channel Gateway, Telephony/Contact Center, Case Management, SLA, Knowledge, Self-Service, Feedback, Reputation, Customer Success, and Service Analytics.
6. **Growth ecosystems:** Communities, Learning, Memberships, Loyalty, Referrals, Affiliates, Advocacy, Events/Webinars, and field-service coordination.
7. **Enterprise and channel:** Quotas/Incentives, Partner Management, Deal Registration, Channel Sales, MDF, resource/project operations, BPM, sandbox/release management, and advanced CDP/data activation.
8. **Agency and extensibility:** Agency Workspace, White Label, SaaS Packaging, Usage/Rebilling, Snapshots, Client Onboarding, Marketplace, integration packs, and migration adapters.
9. **Governed intelligence:** predictive models, CRM Copilot, prospecting/service/marketing agents, advanced conversation analytics, evaluation, and continuous optimization.

Each phase delivers complete vertical workflows, migrations, accessible UI, permissions, consent, provider failure handling, reconciliation, telemetry, runbooks, and issue-ready acceptance criteria.

## 20. Benchmark coverage and source basis

The module map intentionally covers the following official benchmark capability families without copying vendor-specific architecture:

- **HubSpot:** Smart CRM, Marketing, Sales, Service, Content, Data, and commerce/revenue capabilities, including custom objects, sequences, forecasting, playbooks, help desk, customer success, data quality, landing content, and automation.
- **Salesforce:** sales, service/contact center, marketing journeys/personalization, unified customer data, revenue lifecycle, partner/customer experiences, field service, analytics, and platform extensibility.
- **Pipedrive:** pipeline-first selling, Leads Inbox, LeadBooster-style chatbot/live chat/forms/prospecting, web visitors, scheduling, activities/goals, Pulse-style enrichment/scoring/sequences/feed, campaigns, projects, and smart documents.
- **HighLevel:** opportunities, conversations, workflows, funnels/websites, appointments, reputation, social/advertising, documents/contracts, communities/courses, affiliates, agency sub-accounts, white label, SaaS packaging, rebilling/wallets, snapshots, and marketplace distribution.

Official reference starting points:

- [HubSpot customer platform and product hubs](https://www.hubspot.com/products/get-started)
- [HubSpot enterprise platform capabilities](https://www.hubspot.com/products/crm/enterprise)
- [Salesforce Customer 360 products](https://www.salesforce.com/products/)
- [Salesforce Revenue Cloud overview](https://www.salesforce.com/sales/revenue-lifecycle-management/revenue-cloud/)
- [Pipedrive product and add-on capabilities](https://www.pipedrive.com/en/products)
- [Pipedrive plan and add-on feature reference](https://support.pipedrive.com/en/article/what-features-do-the-pipedrive-plans-have)
- [HighLevel product knowledge base](https://help.gohighlevel.com/support/solutions)
- [HighLevel snapshot distribution](https://help.gohighlevel.com/support/solutions/articles/48000982513-how-to-share-snapshots)

These references establish expected coverage only. Liberu package boundaries, contracts, terminology, and implementation remain independent and provider-neutral.

## 21. Definition of done

Liberu CRM is complete when selected modules can be installed independently; customer identity, consent, ownership, and provenance remain trustworthy; acquisition-to-renewal workflows are authorized, measurable, recoverable, and reconciled; providers are replaceable; enterprise, partner, and agency isolation holds; marketplace extensions are governed; and every module can be converted into a focused GitHub epic with child issues.

## 22. GitHub issue mapping

Create one epic for each module table row rather than combining a whole section into a monolith. Each epic includes capability boundary and exclusions, package category, dependencies/contracts, data ownership, states/workflows, permissions and consent, APIs/events, provider adapters, Filament/Livewire/theme extension points, migrations/imports, idempotency/failure recovery, tests, telemetry, runbook, and documentation.

Create separate adapter issues for each external provider and separate adoption issues for each product/application. Marketplace-add-on parity belongs in the relevant provider adapter or capability module; it must not introduce vendor-specific behavior into CRM Core.
