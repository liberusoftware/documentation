# Liberu CRM

## Product Scope

**Purpose:** Customer relationship, sales, marketing, communications, support, and delivery coordination.
**Architecture:** Modules follow [MODULES.md](MODULES.md); staff and customer experiences follow [THEMES.md](THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md); this scope defines relationship and engagement behavior only.

## Outcomes

- Maintain one permission-aware customer timeline across sales, communications, support, and projects.
- Convert demand into governed opportunities, proposals, contracts, delivery, and revenue.
- Coordinate omnichannel engagement with consent, attribution, SLA, and automation controls.

## Module plan

| Module | Responsibilities |
|---|---|
| CRM Core | Contacts, organizations, relationships, ownership, tags, custom fields, duplicates, and timeline |
| Leads | Capture, enrichment, consent, qualification, scoring, routing, conversion, and source attribution |
| Sales | Pipelines, stages, opportunities, products, forecasts, competitors, activities, and close reasons |
| Activities | Tasks, calls, meetings, calendars, reminders, recurrence, and shared availability |
| Communications | Email, SMS, chat, social, WhatsApp, templates, threads, delivery, and preferences |
| Telephony | Numbers, IVR, routing, queues, dialer, recordings, transcripts, outcomes, and provider drivers |
| Marketing | Segments, campaigns, journeys, forms, consent, frequency caps, experiments, and attribution |
| Social | Accounts, publishing calendar, comments/messages, approval, monitoring, and provider drivers |
| Support | Tickets, queues, priorities, SLA, assignment, escalation, knowledge links, and satisfaction |
| Proposals | Quotes, scopes, pricing, versions, approvals, e-signature adapters, and acceptance |
| Contracts | Terms, parties, obligations, renewals, amendments, documents, and alerts |
| Projects | Delivery projects, milestones, tasks, dependencies, time, status, risks, and client visibility |
| Customer Portal | Profile, consent, communications, tickets, proposals, contracts, projects, and requests |
| Intelligence | Dashboards, forecasts, attribution, quality, SLA, productivity, and governed AI assistance |

## Required workflows

1. **Lead to customer:** capture → deduplicate/consent → enrich/score → route → qualify → opportunity/contact/account conversion.
2. **Opportunity to delivery:** progress stages → build/approve proposal → accept/sign → create contract/order/project → hand off context.
3. **Omnichannel support:** receive message/call → identify contact → thread → triage → SLA/assign → respond/escalate → resolve and survey.
4. **Campaign:** define audience and lawful basis → approve content → send within preferences/caps → stop on reply/opt-out → attribute outcome.
5. **Data stewardship:** detect duplicates → compare → approve merge → preserve identifiers, relationships, consent, ownership, and audit.

## Product requirements

- Support tenant/division/team ownership, configurable pipelines, custom fields, saved views, import/export, and bulk actions.
- Resolve identities across email, phone, social, forms, billing, support, and marketplace sources without unsafe automatic merges.
- Apply channel-specific consent, suppression, quiet hours, retention, recording, and do-not-contact rules.
- Keep a chronological timeline of material interactions, state changes, documents, automation, and linked product records.
- Make stage changes and automation idempotent and require approvals for contractual or high-risk outbound actions.
- Expose authorized APIs, webhooks, events, Filament resources, and portal Livewire components.

## Integrations

Email/calendar, telephony/SMS/WhatsApp, social networks, advertising, forms, e-signature, enrichment, marketplaces, CMS, Billing, Accounting, Ecommerce, GitHub, and Automation use replaceable drivers and reconciliation.

## Quality and control gates

- Test tenant/division/record visibility, consent, suppression, message threading, duplicate merges, SLA clocks, attribution, and webhook replay.
- Encrypt sensitive contact/recording credentials; control transcript/recording access and jurisdictional retention.
- Measure delivery failures, reply/opt-out handling, lead leakage, stale opportunities, forecast accuracy, SLA breach, and connector drift.
- AI suggestions identify source/context and require policy-based approval; they cannot exceed actor permissions.

## Delivery phases

1. Core, Leads, Sales, Activities, permissions, imports, timeline, and reporting basics.
2. Communications, Support, portal, proposals, and Billing handoff.
3. Marketing, telephony, contracts, projects, social, and deeper integrations.
4. Advanced attribution, automation, forecasting, and governed AI assistance.

## Definition of done

Customer journeys retain identity, consent, ownership, history, and cross-product traceability; messages and automations are authorized and recoverable; sales/support metrics are reproducible. Each module becomes a GitHub epic.
