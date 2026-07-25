# Liberu Platform — Feature Scopes Document

**Stack:** Laravel 13 · PHP 8.5 · Filament 5 · Livewire 4
**Status:** Draft v0.2
**Owner:** Liberu Group Engineering

---

## 1. Purpose & Vision

Build a single, modular monorepo/multi-app platform that powers every public-facing Liberu domain from one codebase family, by **extending** (not forking) the existing open-source repositories:

- [`liberu-cms/cms-laravel`](https://github.com/liberu-cms/cms-laravel) — content management
- [`liberu-crm/crm-laravel`](https://github.com/liberu-crm/crm-laravel) — sales & support CRM
- [`liberu-billing/billing-laravel`](https://github.com/liberu-billing/billing-laravel) — subscriptions & payments
- [`liberu-accounting/accounting-laravel`](https://github.com/liberu-accounting/accounting-laravel) — ledgers, payroll, reconciliation
- [`liberu-control-panel/control-panel-laravel`](https://github.com/liberu-control-panel/control-panel-laravel) — service/account administration

Each remains an independently usable open-source product. The platform layer composes them as **modules/packages** consumed via Composer, so upstream improvements flow both ways: features built for the platform are contributed back where generic, and platform-specific glue stays in a thin "orchestration" layer.

This revision expands the AI/automation scope to cover omnichannel support & sales (chat, voice, social), freelance-marketplace bidding, outbound lead generation (LinkedIn, cold calling, email), scheduled social content, and deeper project/GitHub/RBAC integration across sub-divisions.

---

## 2. Domains & Routing

Single application (or a shared kernel across services) resolves behaviour by **CNAME/host-based routing**, not by separate deploys:

| Domain | Primary Module(s) | Purpose |
|---|---|---|
| `liberusoftware.com` | CMS | Docs, changelogs/releases, catalogue of OSS projects, prominent CTAs to Hosting & Services |
| `liberuhosting.com` | Billing + Control Panel | Managed hosting storefront, plan selection, provisioning, invoicing |
| `liberuservices.com` | CRM + CMS | Custom contracting/consulting services, quote requests, case studies |
| `liberugroup.com` | CMS | Corporate/parent company site, brand, leadership, press |

**Routing approach:**
- Middleware resolves the current `Host`/CNAME on each request, sets a `Tenant`/`Site` context (domain → brand config: theme, nav, footer, feature flags).
- One Filament admin (control-panel) manages all sites; content, plans, and CRM pipelines are scoped by `site_id`/brand and by **sub-division** (see §12).
- Shared identity across domains (single customer & staff identity via platform SSO — see §14), with per-brand storefront presentation.

---

## 3. Module Boundaries (Modular Composition)

| Package | Extends | Adds for Platform |
|---|---|---|
| `liberu/cms` | cms-laravel | Multi-site page/blog rendering, GitHub release/doc sync, project directory, AI-generated social content source |
| `liberu/crm` | crm-laravel | AI lead enrichment, AI outreach/chase sequences, omnichannel inbox, marketplace bidding, escalation workflow |
| `liberu/billing` | billing-laravel | Stripe + PayPal dual-gateway, hosting plan catalogue, usage-based provisioning triggers |
| `liberu/accounting` | accounting-laravel | Payroll runs, bulk wage payout, bank/gateway reconciliation |
| `liberu/control-panel` | control-panel-laravel | Self-service customer portal, staff role dashboards, provisioning orchestration |
| `liberu/platform-core` (new) | boilerplate | Multi-brand routing, SSO, RBAC, GitHub sync service, notifications, audit log |
| `liberu/ai-gateway` (new) | — | Provider-agnostic AI abstraction (OpenAI, Claude, Gemini), prompt/workflow registry, cost/usage tracking |
| `liberu/omnichannel` (new) | — | Unified inbox, AI receptionist, telephony/switchboard, social messaging & comment automation |
| `liberu/growth` (new) | — | Marketplace bidding, LinkedIn/social lead-gen, cold calling, outbound campaigns, social scheduling |

Each package ships its own Filament panel/plugin, migrations, and config, installable à la carte — a deployment can run CMS + Billing only, or the full suite.

---

## 4. AI Provider Abstraction (`liberu/ai-gateway`)

- Common interface (`AiProvider` contract) with drivers for **OpenAI**, **Anthropic Claude**, and **Google Gemini** at minimum; pluggable for future providers.
- Per-workflow provider selection (e.g., "lead enrichment → Gemini", "voice receptionist → Claude") configurable in admin, with automatic fallback if a provider errors or rate-limits.
- Central prompt/template registry, versioned, with per-brand and per-sub-division overrides.
- Usage metering and cost tracking per provider/workflow, surfaced to Finance.
- Guardrails: human-approval gates on outbound comms and any financial/contractual action (configurable per workflow); PII redaction before sending data to external AI APIs where required.

---

## 5. Self-Service Automation Portal

### 5.1 Customers
- Account dashboard: active services, invoices, usage, support tickets
- One-click service provisioning & plan changes (upgrade/downgrade/cancel)
- Payment method management (Stripe & PayPal), auto-pay toggle
- Ticket submission with AI-suggested resolutions before human escalation
- Document/contract access, download of invoices & statements
- Job/consultation **booking** (calendar-based), pre-filled from AI receptionist conversations (see §7)

### 5.2 Team Members (role-based dashboards)
- **Sales:** pipeline, AI-enriched/scored leads, marketplace bid queue, LinkedIn lead feed, quote/proposal builder, auto-dialer
- **Support:** unified omnichannel queue, SLA timers, AI-drafted responses, escalation intake
- **Finance:** invoice/payment status, reconciliation queue, payroll runs, aging reports, AI cost tracking
- **Developers:** linked GitHub repos/issues (incl. private repos), deployment/provisioning status, release notes feed
- **Management:** cross-division reporting, permission administration, AI workflow approvals

Roles and permissions are covered in detail in §12–13.

---

## 6. Omnichannel Support & Sales Inbox (`liberu/omnichannel`)

A single unified inbox aggregates and threads conversations regardless of source, with one contact/timeline per customer:

- **Channels:** IMAP/SMTP email, Facebook Messenger, WhatsApp Business (messages **and** calls), telephone (see §8 telephony), web chat widget, SMS.
- Each inbound message/call is matched or created against a CRM contact; full history visible to whichever agent picks it up.
- AI triage: categorises intent (support vs. sales vs. billing), assigns priority, drafts a first response, and either auto-sends (low-risk, high-confidence) or queues for agent approval.
- Clear, auditable **escalation path**: AI → queued for human → specific agent/team, with SLA countdowns visible at every stage.

### 6.1 AI Receptionist (voice + chat)
- Handles inbound WhatsApp Business calls and telephone calls (via telephony provider, §8) using speech-to-text → AI-gateway → text-to-speech.
- Can: answer FAQs, explain company processes/pricing, qualify a sales enquiry, **book jobs/consultations directly into the calendar**, and hand off live to a human agent on request or low confidence.
- Full call/chat transcript and recording stored against the CRM contact for QA and training.
- Same logic reused across chat and voice so behaviour/policy stays consistent per channel.

---

## 7. Social Media Automation & Lead Generation

### 7.1 Scheduled AI Content
- AI-generated scheduled posts across supported platforms, including **generated imagery and video** where relevant to the post.
- Editorial calendar with per-brand/per-division scheduling, draft → review → approve → publish workflow.
- Content sourced/informed by CMS articles, releases, and case studies for consistency.

### 7.2 Comment & DM Automation (ManyChat-style)
- Rule + AI-driven automated replies and follow-ups triggered by:
  - Specific comment keywords/phrases on a post ("comment PRICE for details")
  - General question-like comments (AI-classified) → auto-reply or DM follow-up
  - **@highlight** mentions on personal profiles (Facebook) and **@followers**/mentions on owned Facebook Pages
- Configurable per-post trigger → action mapping (public reply, DM, add to CRM as lead, tag for sales follow-up).

### 7.3 Supported Platforms
- Facebook (Pages & profiles), Instagram, LinkedIn (company + personal), X/Twitter, WhatsApp Business, plus room to add TikTok/YouTube later — each behind a platform-driver interface so new networks can be added without core changes.

### 7.4 Outbound Lead Generation (`liberu/growth`)
- **LinkedIn:** automatic lead generation from Sales Navigator searches and from engagement on company/personal posts; automated connection requests and first-touch messages within platform ToS-aware rate limits.
- **Cold calling:** AI-assisted or AI-run outbound calling campaigns to generate and qualify leads, using telephony (§8); optional integration with data providers (e.g., an Apollo/Lusha-style contact-data API) or compliant LinkedIn/Sales Navigator data export, respecting each platform's terms of service and applicable data-protection law.
- **Automated multi-channel outreach:** LinkedIn, Facebook, and email sequences triggered from CRM segments, with reply-detection pausing/adjusting sequences automatically.
- All scraping/automation integrations are implemented as swappable drivers so they can be enabled, disabled, or replaced per compliance requirements or platform policy changes.

### 7.5 Freelance Marketplace Bidding (PeoplePerHour, Freelancer, Upwork)
- Sync open jobs/briefs from **PeoplePerHour**, **Freelancer**, and **Upwork** via their APIs (or authenticated scraping where no API exists).
- AI evaluates each job against Liberu's services/skills profile, drafts a tailored proposal/bid, and either auto-submits (within configured limits) or queues for sales review.
- Won jobs auto-create a CRM opportunity → contract → project (and, where relevant, a provisioning/billing record), keeping marketplace, CRM, and project management in sync.
- Dashboard shows bid win-rate, response times, and marketplace-by-marketplace performance for Sales/Management.

---

## 8. Telephony & Switchboard (Twilio or equivalent)

- Multiple phone numbers across countries, routed through a switchboard/IVR to the right division (sales, support, billing) or straight to the AI receptionist.
- Twilio (or comparable provider) integration for voice, SMS, and call recording; abstracted behind a telephony driver so the provider can be swapped.
- Call routing rules: business hours, language/country detection, queue overflow to voicemail-to-AI-summary, or human agent.
- **Auto-dialer** for the human sales team: prioritised call lists from the pipeline, click-to-call, automatic call logging and outcome capture back into the CRM.
- Full call analytics (volume, duration, conversion) per number/division/country.

---

## 9. Billing & Payments

- Dual gateway: **Stripe** and **PayPal**, unified subscription/invoice model
- Plans, add-ons, metered/usage billing, proration, coupons/discounts
- Automated dunning for failed payments, retry schedules, service suspension rules
- Invoice generation (PDF), tax handling, multi-currency support
- Webhook-driven status sync (payment succeeded/failed/refunded/disputed)

---

## 10. Accounting, Payroll & Reconciliation

- Chart of accounts, ledger entries generated from billing transactions
- **Bank/gateway reconciliation:** automated matching of incoming Stripe/PayPal payouts against invoices; exception queue for unmatched items
- **Payroll:** staff pay records, pay runs, payslip generation
- **Bulk wage payment:** admin selects a pay run and triggers batch payout (e.g., via Stripe Connect payouts / bank file export), with approval step before execution
- Financial reporting: P&L, cashflow, outstanding receivables/payables

---

## 11. Lead/Contact/Job Lifecycle & Pipeline

A single, explicit lifecycle spans marketing, sales, delivery, and billing so any role can see where a record stands:

```
Lead → Qualified → Opportunity → Proposal/Bid → Won/Lost
                                   Won → Contract → Project → Delivery → Invoiced → Paid → Closed
```

- **Pipeline display:** Kanban + list views, per-division pipelines (e.g., Hosting vs. Services vs. Marketplace bids), configurable stages, SLA/aging indicators per stage, and a merged "all sources" view (organic, marketplace, LinkedIn, cold call, referral) with source attribution on every record.
- Every lead carries its originating channel (email, WhatsApp, marketplace, LinkedIn, cold call, web form) for reporting and AI-model feedback.
- Stage-change automation (e.g., "Won" auto-creates project + billing record + GitHub repo where applicable — see §13).
- Lost-reason capture feeds back into AI lead-scoring to improve future targeting.

---

## 12. Roles, Permissions & Sub-Divisions

- RBAC (e.g., Filament Shield or equivalent) scoped across three dimensions: **module** (CRM/Billing/Accounting/CMS/Control Panel), **division/brand** (Hosting, Services, Software/CMS, Group), and **team function** (Sales, Support, Finance, Developers, Management).
- Roles are composable: a user can hold "Sales – Hosting division" and "Support – Services division" simultaneously with different permissions in each.
- Divisional data scoping ensures, e.g., a Hosting-only sales rep doesn't see Services-division pipeline unless explicitly granted.
- Management roles get cross-division visibility and approval authority over AI-automated actions (bids, outbound sends, bulk payouts).
- Full audit log of permission changes and privileged actions.

---

## 13. GitHub Integration & Project Management

- OAuth/GitHub App connection to Liberu org(s), including **private repositories** (not just public OSS repos).
- **Automatic private repo creation:** when a deal is Won (or a project is created manually), the platform can provision a new private GitHub repository from a template, wire up default branches/CI, and link it to the CRM opportunity/project record.
- Two-way sync of issues, PRs, milestones, and releases between GitHub and the platform's project records; webhooks for near-real-time updates, scheduled reconciliation as fallback.
- Public release/changelog data continues to feed `liberusoftware.com`; private project data stays scoped to authorised Developer/Management roles.
- **Role-tuned project views:**
  - *Developers:* Kanban/backlog close to GitHub Issues/PRs, code-centric (branches, CI status, review queue)
  - *Management:* portfolio view — status, budget/hours vs. estimate, risk flags, timeline
  - *Support/Sales:* simplified status ("On track / Delayed / Blocked / Delivered") with no code-level noise, linked back to the originating CRM deal
- Time tracking / effort logging optional per project, feeding Finance for project profitability reporting.

---

## 14. Single Source of Truth & SSO

- **One identity model** shared by CRM, Billing, Accounting, CMS, and Control Panel — a customer or staff member has exactly one core account record, referenced (not duplicated) by every module.
- Platform-wide **SSO**: one login for customers across all storefront domains, and one login for staff across every admin/Filament panel, respecting the divisional/role scoping in §12.
- Each module owns its domain-specific extension of the identity (e.g., CRM owns contact/lead detail, Billing owns payment methods, Accounting owns payee/bank detail) via a shared user/contact key — avoiding duplicate or drifting records.
- Change events (e.g., address or contact-detail update) propagate to all modules through the platform-core event bus rather than being re-entered per module.
- Full audit trail of identity and permission changes, supporting compliance and support investigations.

---

## 15. Cross-Cutting Concerns

- **Notifications:** email/SMS/in-app, templated per brand and channel
- **Audit & compliance:** full activity log for financial, provisioning, AI-automated, and outbound-communication actions
- **API-first:** REST (and/or GraphQL) endpoints for all modules to support the portal, integrations, telephony/social webhooks, and future mobile/CLI clients
- **Testing/CI:** module-level test suites plus platform integration tests; CI mirrors each upstream repo's pipeline
- **Compliance:** data handling for AI processing, call recording, and marketplace/social scraping should be reviewed per jurisdiction and per platform's terms of service before enabling automation in production

---

## 16. Phasing (Suggested)

1. **Foundation:** `platform-core` (multi-brand routing, SSO, RBAC), deploy CMS across all 4 domains with brand theming
2. **Commerce:** Billing (Stripe + PayPal) + hosting plan catalogue on `liberuhosting.com`
3. **Operations:** Control Panel provisioning automation wired to billing events
4. **Finance:** Accounting module — reconciliation, then payroll/bulk payouts
5. **Growth (CRM core):** CRM pipeline, GitHub sync (public + private repos), project management surfaces
6. **AI Gateway:** provider abstraction (OpenAI/Claude/Gemini), lead enrichment/scoring
7. **Omnichannel:** unified inbox (email/Messenger/WhatsApp), AI receptionist (chat first, then voice), telephony/switchboard + auto-dialer
8. **Social & Marketplace Growth:** scheduled AI content + comment/DM automation, LinkedIn lead-gen, marketplace bidding (PeoplePerHour/Freelancer/Upwork), cold-calling campaigns

---

## 17. Open Questions

- Single Laravel app with brand-aware routing vs. several apps behind a shared package layer?
- Which entity owns customer identity master record — CRM or Control Panel — as the canonical writer, with others as read-scoped extensions?
- Payroll: build in-house vs. integrate a third-party payroll/compliance provider for tax jurisdictions?
- Default AI provider per workflow, and data-handling/privacy requirements for lead, support, and call-recording data?
- Which marketplace/social integrations use official APIs vs. scraping, and what's the fallback if a platform blocks/limits automation?
- Telephony provider decision (Twilio vs. alternatives) and per-country number sourcing/compliance requirements?
- Approval-threshold policy: which AI actions (bids, outbound sends, bulk payouts) are allowed to auto-execute vs. always require human sign-off?
