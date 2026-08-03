# Liberu AI, voice, messaging, social, and measurement implementation

This document defines how Liberu uses AI across official websites, CRM, staff apps, email, voice, social channels, and advertising. Automation owns the generic AI/workflow runtime. CRM owns customer/channel actions. CMS owns published content. Liberu owns composition, approved sales context, cross-brand policy, and the operational handoff.

## Approved sales knowledge source

Use the public [liberusoftware/sales](https://github.com/liberusoftware/sales) repository as an approved sales-enablement source. Its documented library includes `docs`, `sales`, `scripts`, `bids`, `services`, `portals`, `profiles`, `templates`, and `links`, with qualification guidance, messaging and telephone scripts, service catalogue, bids, and technical references.

The repository is reference material, not a live prompt or executable integration. The Liberu adapter must:

1. Fetch only an approved branch/tag and record the exact commit SHA, fetch time, license/provenance, and content hash.
2. Allowlist paths and file types; exclude credentials, issue data, hidden files, arbitrary code, and unreviewed personal data.
3. Parse approved front matter/metadata such as audience, channel, brand, service, locale, approval state, expiry, and sensitivity.
4. Scan imported text for prompt injection, unsafe instructions, unsupported claims, secrets, and stale links; quarantine failures for human review.
5. Index chunks with source path, commit SHA, title, owner, expiry, and access policy. Retrieval must return citations/evidence to the reviewer.
6. Promote a template only through a reviewed registry. A repository change creates a candidate version; it never silently changes a production prompt or outbound message.
7. Reconcile the registry against GitHub on schedule and on approved webhook events. A deleted, revoked, or expired template is disabled for new generations while existing approved sends remain auditable.

## AI interaction flow

```text
Inbound event or staff request
  → identity, tenant/brand, consent, quiet hours, channel and risk policy
  → retrieve approved Liberu sales/CMS/CRM context with citations
  → generate draft/classification/summary/next action with model + prompt versions
  → evaluate quality, confidence, claims, tone, policy and cost
  → human approval or explicitly pre-approved low-risk action
  → provider adapter sends/calls/posts/schedules
  → log outcome, event ID, evidence, cost, delivery state and next action
  → reconcile provider state and escalate to a human when required
```

AI must never widen permissions, invent pricing/availability/legal commitments, expose private records, bypass consent/contact cooling-off, or make a high-risk outbound action solely because a model is confident.

## Channel coverage and ownership

| Channel/action | AI may prepare or assist with | Send/post authority | Human escalation |
| --- | --- | --- | --- |
| Voice calls | greeting, qualification, knowledge answer, call summary, disposition, next action | Telephony/CRM action after consent and policy; recording is separately controlled | warm transfer or callback queue on request, low confidence, complaint, risk, repeated failure, or SLA/VIP rule |
| SMS/WhatsApp/web messaging | reply draft, classification, translation, appointment/support answer, follow-up suggestion | CRM Channel Gateway after consent, quiet hours, frequency and cooling-off checks | explicit “talk to a person”, negative sentiment, sensitive request, unresolved loop, or no-answer threshold |
| Email | triage, draft reply, personalize from approved context, summarize thread, schedule suggestion | CRM Email Productivity/Marketing after approval or approved low-risk recipe | reply-to-human route, legal/financial/security topic, low confidence, complaint, or repeated failed delivery |
| Social direct messages/comments | classify, draft reply, moderation suggestion, sentiment/intent, route to case | CRM social adapter; publishing/replying requires approval by default | public complaint, safety/legal issue, identity uncertainty, escalation request, or brand-risk score |
| Social posts | content variation, accessibility text, hashtags, schedule proposal, campaign variants | approved social content workflow; no autonomous brand post by default | factual uncertainty, reputational risk, crisis/status content, or missing approval |
| Advertising plans | audience/creative/landing-page recommendations, budget/scenario draft, UTM plan, experiment design | human-approved Campaigns/Advertising action; server-side conversion events remain authoritative | policy/claims issue, budget threshold, audience sensitivity, or destination mismatch |

## Voice and human handoff

CRM must expose a consistent human escalation method on every AI voice and messaging surface: a visible “Talk to a person”/“Request a callback” action, a spoken equivalent on calls, and a fallback route when the AI or provider is unavailable.

The handoff creates or updates the owning CRM conversation/case with a correlation ID, channel, consent/recording state, transcript or summary according to policy, detected intent, unresolved questions, customer identity confidence, urgency/SLA, and requested callback window. It routes to a staffed queue using CRM Routing, Contact Center, SLA, and team availability. The AI stops sending automated responses after handoff unless a human explicitly resumes it.

Human escalation is mandatory for explicit requests, complaints, legal/financial/security matters, vulnerable-customer signals, low confidence, repeated misunderstanding, payment or entitlement disputes, account access changes, crisis/status communications, and any configured VIP/SLA rule. Preserve a redacted transcript and evidence for the agent; do not expose model chain-of-thought.

## Email, social, scheduling, and advertising workflow

Campaigns and journeys may plan a coordinated release across website, email, social messaging, comments, posts, and advertising, but each channel has its own consent, audience, approval, rate, and provider state. A campaign stores the parent plan, approved copy/asset versions, audience snapshot, schedule/timezone, budget, UTM/click identifiers, destination, owner, approver, and rollback/stop action.

Scheduling uses CRM Journey Orchestration/Scheduling and provider adapters. A reply, opt-out, complaint, conversion, human handoff, or campaign stop immediately suppresses later automated steps across linked channels. Social comments and direct messages remain conversation records; public posts and ads remain approved campaign artifacts.

## Synchronized Google and Meta measurement

Use Boilerplate Analytics Core as the canonical event layer. Google Tag Manager (browser/theme adapter), Google Analytics/GA4 (browser and server adapter), Meta client/pixel (theme adapter), and Meta Conversions API (server adapter) consume the same consent-filtered event envelope.

```text
Authoritative product event
  → Analytics Core: event_name/version, event_id, time, site/brand, source, consent, safe properties
  ├→ GTM data layer → GA4 browser
  ├→ GA4 server/event adapter
  ├→ Meta client/pixel
  └→ Meta server/CAPI
```

The same stable `event_id` deduplicates browser/server delivery. Server-side delivery is derived from authoritative CRM/Billing/Ecommerce events, not from a client claim. Track approved events such as `page_view`, `view_item`, `generate_lead`, `schedule`, `human_handoff`, `begin_checkout`, `purchase`, `subscribe`, `support_request`, and `campaign_engagement`; do not send message bodies, transcripts, secrets, payment credentials, protected consent evidence, or unrestricted free text.

Every event records destination, consent decision, mapping version, delivery state, provider response, retry/replay status, and source record reference. Reconcile GA/Meta delivery, deduplication, campaign IDs, UTM parameters, click IDs, offline conversions, revenue values, and attribution windows against CRM/Billing/Ecommerce truth. GTM is a routing/presentation layer, never a source of conversion truth.

## Required tests and operations

- Contract-test the sales-repository importer, template registry, retrieval citations, commit pinning, revocation, prompt-injection quarantine, and rollback.
- Test voice/message/email/social consent, quiet hours, contact cooling-off, stop-on-reply, human handoff, provider outage, callback queue, recording policy, and transcript redaction.
- Test draft/post/schedule/ad approval, budget thresholds, audience suppression, campaign stop, duplicate webhook, idempotency, and provider reconciliation.
- Test GTM/GA4/Meta client/server event deduplication, consent suppression, event mapping versions, retries, rejection, replay, attribution, and authoritative revenue reconciliation.
- Monitor generation quality, citation coverage, unsupported-claim rate, confidence, human-handoff rate, response latency, delivery/reply rate, opt-out/complaint rate, provider errors, cost, and analytics drift.
