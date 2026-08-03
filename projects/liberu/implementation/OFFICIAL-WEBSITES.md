# Liberu official websites implementation

## Shared site architecture

Use one CMS installation and one Liberu brand registry with four site recipes. Each recipe selects domain, brand tokens, navigation, content collections, forms, consent topics, analytics destinations, SEO defaults, support entry points, and enabled product cards. Content editors publish through CMS; the Laravel application composes the recipe; Nuxt or the approved web adapter consumes the released API/content contract.

```text
Request domain → site/brand resolver → public theme recipe → CMS content/API
                                      ├→ consent + analytics policy
                                      ├→ CRM form/lead handoff
                                      ├→ Billing/Ecommerce product handoff
                                      └→ authenticated portal/support deep link
```

## Site responsibilities

| Site | Required first-release journeys | Primary handoffs |
| --- | --- | --- |
| Liberu Software | product discovery, documentation, releases, roadmap, community, support, contribution | CMS, CRM lead/support, Social Network/Communities |
| Liberu Hosting | plan comparison, domain search, checkout, provisioning status, service portal, incident/support, renewal | Billing, Ecommerce, Control Panel, CRM, Accounting |
| Liberu Services | capability pages, enquiry, qualification, booking, proposal, contract, project/client portal, case studies | CRM, Scheduling, Contracts, Projects, Billing, CMS |
| Liberu Group | corporate profile, brands, leadership, governance, careers, partners, press, policies | CMS, CRM, People/SAP, Governance/Risk/Compliance |

## Required implementation details

- Resolve the site from the request host and trusted deployment configuration; reject unknown hosts safely.
- Keep public and authenticated layouts distinct. Never put CRM, invoice, infrastructure, or staff data in public/SSR payloads.
- Use progressive forms: ask only for the next decision, retain attribution/consent evidence, prevent spam, and hand off to CRM with an idempotency key.
- Keep pricing/order authority in Billing/Ecommerce; website cards are projections with freshness and eligibility messaging.
- Show queued states for provisioning, proposals, support, publishing, and AI; provide status URLs or portal deep links.
- Set budgets for Core Web Vitals, image weight, JavaScript, accessibility, cache freshness, and error rates; measure by site recipe.
- Define canonical URLs, redirects, sitemap ownership, robots policy, structured data, localization, cookie/consent behavior, and incident/status messaging per site.
- Connect approved AI website chat/voice, CRM forms, email follow-up, social messaging/comment response, post scheduling, and advertising plans through the [AI/channel contract](AI-CHANNELS.md); every public AI surface must offer human escalation.
- Publish browser events through the GTM data layer only after consent and send authoritative server events through Analytics Core to GA4 and Meta CAPI; share event IDs with optional client/pixel delivery for deduplication.

## Public acceptance journey

```text
Discover → understand value → consent-aware form or checkout → confirm request
→ receive reference/status → authenticate when needed → continue in portal/support
```

Test anonymous, mobile, keyboard, screen-reader, blocked-cookie, slow-network, duplicate-submit, invalid-form, unavailable-provider, and handoff-recovery paths for every first-release journey.

Test AI low-confidence responses, explicit human requests, callback queueing, reply/opt-out suppression, public comment moderation, scheduled-post cancellation, advertising approval, GTM consent mode, GA4/Meta client-server deduplication, and attribution reconciliation.
