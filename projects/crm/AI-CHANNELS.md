# CRM AI-assisted channel guide

This is the Liberu CRM profile for AI voice, messaging, email, social, and advertising workflows. CRM owns the customer conversation and channel action; [Automation](../automation/AUTOMATION.md) owns the generic AI runtime; [Analytics Core and provider tracking](../boilerplate/BOILERPLATE.md#12-analytics-and-server-side-tracking) own canonical measurement.

## Required CRM behavior

- Voice calls use Telephony and AI Reception/Conversation for qualification, summaries, dispositions, and approved actions. Recording, transcription, caller identity, and outbound contact obey consent and local policy.
- SMS, WhatsApp, web chat, and social messages use Channel Gateway and Unified Conversations. Email uses Email Productivity/Marketing. Public comments/posts and advertising plans use Campaigns, Journey Orchestration, Advertising, Marketing Resources, Attribution, and provider adapters.
- Every AI channel shows or speaks a human route: **Talk to a person**, **Request a callback**, or an equivalent support action. The request creates/updates a CRM conversation or case, stops AI automation, preserves a policy-safe summary, and routes through Routing/Contact Center/SLA.
- Escalation is automatic for explicit request, low confidence, complaint, sensitive/legal/financial/security matter, repeated misunderstanding, payment/entitlement dispute, safety concern, or configured VIP/SLA risk.
- The dialer contact-protection invariant still applies to AI calls and follow-up sequences: `next_contact_at`, opt-out, suppression, quiet hours, and frequency caps are checked before every automated attempt.

## Email and social coverage

AI may classify inbound mail/DMs/comments, draft replies, translate, summarize, recommend a case/owner, propose posts, prepare accessible variants, schedule approved content, and draft advertising/audience/UTM plans. It does not autonomously publish public posts, place ads, change budgets, make claims, or send sensitive replies unless a reviewed low-risk policy explicitly permits it.

Replies, comments, posts, schedules, and advertising plans have separate consent, audience, approval, provider, and stop states. A reply, opt-out, conversion, complaint, or human handoff suppresses linked later outreach across channels.

## Human handoff contract

The CRM handoff record includes conversation/case ID, channel, source, actor/tenant/team, consent and recording state, identity confidence, redacted transcript/summary, intent, urgency/SLA, callback window, correlation ID, and AI/prompt versions. The assigned human sees the evidence and next action without seeing model chain-of-thought. If no agent is available, the customer receives a callback/request reference and a truthful queued status.

See Liberu's [AI and channel implementation](../liberu/implementation/AI-CHANNELS.md) for the GitHub sales-template importer, cross-brand orchestration, and synchronized GTM/GA4/Meta client/server tracking.
