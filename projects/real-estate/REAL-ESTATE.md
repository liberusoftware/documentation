# Liberu Real Estate\n\n## Product Scope\n\n**Purpose:** Residential and commercial agency operations covering listings, sales, lettings, progression, property management, maintenance, and portals.\n**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); portal, property, and marketplace connector APIs follow [API.md](../../architecture/API.md); agent, vendor, landlord, tenant, and applicant interfaces follow [THEMES.md](../../standards/THEMES.md).\n\n**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines real-estate behavior only.\n\n## Outcomes\n\n- Maintain a single permission-aware record for properties, parties, instructions, transactions, and communications.\n- Match demand to property, coordinate viewings/offers, and progress sales or tenancies with auditable milestones.\n- Publish accurate listings and synchronize portal state without provider lock-in.\n\n## Module plan\n\n| Module | Responsibilities |\n|---|---|\n| Real Estate Core | Agencies, branches, teams, territories, terminology, statuses, numbering, and audit |\n| Parties | Applicants, vendors, landlords, tenants, buyers, solicitors, contractors, relationships, and consent |\n| Properties | Address/location, units, characteristics, tenure, utilities, features, status, history, and keys |\n| Media and Documents | Photos, floorplans, video, certificates, rights, ordering, brochures, and retention |\n| Valuations | Appraisals, comparables, pricing, fees, recommendations, follow-up, and conversion |\n| Instructions | Agency agreements, ownership checks, terms, disclosures, approvals, and withdrawal |\n| Listings | Channel content, pricing, availability, publication rules, portal feeds, and reconciliation |\n| Matching | Applicant requirements, affordability, preferences, scoring, alerts, feedback, and exclusions |\n| Viewings | Availability, booking, confirmation, access, accompaniment, reminders, feedback, and no-shows |\n| Offers | Terms, qualification, negotiation, proof, decision history, and accepted-offer controls |\n| Sales Progression | Chain, milestones, memoranda, legal/finance contacts, dependencies, risks, and completion |\n| Lettings | Applications, referencing, deposits, agreements, move-in/out, renewals, rent changes, and notices |\n| Property Management | Rent schedule, statements, inspections, compliance, maintenance, contractors, and owner approvals |\n| Marketing | Campaigns, boards, brochures, portals, website, social/email, attribution, and consent |\n| Portals and Reporting | Party self-service plus pipeline, conversion, source, fee, time-to-complete, occupancy, and compliance metrics |\n\n## Required workflows\n\n1. **List property:** valuation → due diligence/instruction → collect content/evidence → approve → publish → reconcile portals.\n2. **Buyer journey:** register/consent → qualify → match → view → feedback → offer → negotiate → accept → sales progression → complete.\n3. **Tenant journey:** enquire → qualify/reference → offer → agreement/deposit → inventory/check-in → tenancy → renewal/notice → check-out.\n4. **Managed repair:** report → assess responsibility/urgency → obtain owner approval/quote → dispatch → verify → charge/pay → retain evidence.\n5. **Portal drift:** receive/poll provider status → compare listing → repair safe differences or queue conflict → record result.\n\n## Product requirements\n\n- Support residential/commercial, sales/lettings, multi-branch, multi-country localization, configurable workflows, and custom fields.\n- Prevent publication until mandatory ownership, energy, safety, material-information, media-rights, and instruction checks pass per jurisdiction.\n- Preserve price/status/instruction/offer history and separate confidential negotiation data from public listing data.\n- Detect duplicate parties/properties safely and preserve portal identifiers during approved merges.\n- Support calendar conflicts, keys/access controls, chain dependencies, milestone alerts, and role-specific portals.\n- Expose authorized APIs/events for properties, listings, viewings, offers, tenancies, progression, and maintenance.\n\n## Integrations\n\nProperty portals, maps/geocoding, calendars, email/SMS/telephony, identity/reference/AML providers, e-signature, deposit schemes, accounting/payments, CMS/website, CRM, and Maintenance use replaceable drivers.\n\n## Quality and control gates\n\n- Test branch/record confidentiality, consent, portal mapping, offer races, calendar timezones, progression dependencies, deposit/rent calculations, and jurisdictional fields.\n- Encrypt identity/financial/access data and audit key access, sensitive downloads, offer decisions, and compliance overrides.\n- Verify image rights, accessible listings, accurate feeds, failed-provider recovery, and deletion/retention policies.\n- Alert on expiring certificates/instructions, unmatched portal state, unqualified offers, stalled progression, arrears, and overdue repairs.\n\n## Delivery phases\n\n1. Core, Parties, Properties, Media, Valuations, Instructions, Listings, matching, viewings, offers, and website feed.\n2. Sales Progression, portals, marketing, reporting, communications, and document/e-signature flows.\n3. Lettings, deposits, inspections, property management, maintenance, accounting, and owner/tenant portals.\n4. Multi-country packs, advanced automation, data enrichment, and portfolio analytics.\n\n## Definition of done\n\nProperty-to-completion and property-to-tenancy journeys are permission-safe, compliant, historically traceable, portal-reconciled, and operationally recoverable. Each module maps to a GitHub epic.

## Product Scope

**Purpose:** Residential and commercial agency operations covering listings, sales, lettings, progression, property management, maintenance, and portals.
**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); portal, property, and marketplace connector APIs follow [API.md](../../architecture/API.md); agent, vendor, landlord, tenant, and applicant interfaces follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines real-estate behavior only.

## Outcomes

- Maintain a single permission-aware record for properties, parties, instructions, transactions, and communications.
- Match demand to property, coordinate viewings/offers, and progress sales or tenancies with auditable milestones.
- Publish accurate listings and synchronize portal state without provider lock-in.

## Module plan

| Module                | Responsibilities                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| Real Estate Core      | Agencies, branches, teams, territories, terminology, statuses, numbering, and audit                            |
| Parties               | Applicants, vendors, landlords, tenants, buyers, solicitors, contractors, relationships, and consent           |
| Properties            | Address/location, units, characteristics, tenure, utilities, features, status, history, and keys               |
| Media and Documents   | Photos, floorplans, video, certificates, rights, ordering, brochures, and retention                            |
| Valuations            | Appraisals, comparables, pricing, fees, recommendations, follow-up, and conversion                             |
| Instructions          | Agency agreements, ownership checks, terms, disclosures, approvals, and withdrawal                             |
| Listings              | Channel content, pricing, availability, publication rules, portal feeds, and reconciliation                    |
| Matching              | Applicant requirements, affordability, preferences, scoring, alerts, feedback, and exclusions                  |
| Viewings              | Availability, booking, confirmation, access, accompaniment, reminders, feedback, and no-shows                  |
| Offers                | Terms, qualification, negotiation, proof, decision history, and accepted-offer controls                        |
| Sales Progression     | Chain, milestones, memoranda, legal/finance contacts, dependencies, risks, and completion                      |
| Lettings              | Applications, referencing, deposits, agreements, move-in/out, renewals, rent changes, and notices              |
| Property Management   | Rent schedule, statements, inspections, compliance, maintenance, contractors, and owner approvals              |
| Marketing             | Campaigns, boards, brochures, portals, website, social/email, attribution, and consent                         |
| Portals and Reporting | Party self-service plus pipeline, conversion, source, fee, time-to-complete, occupancy, and compliance metrics |

## Required workflows

1. **List property:** valuation → due diligence/instruction → collect content/evidence → approve → publish → reconcile portals.
2. **Buyer journey:** register/consent → qualify → match → view → feedback → offer → negotiate → accept → sales progression → complete.
3. **Tenant journey:** enquire → qualify/reference → offer → agreement/deposit → inventory/check-in → tenancy → renewal/notice → check-out.
4. **Managed repair:** report → assess responsibility/urgency → obtain owner approval/quote → dispatch → verify → charge/pay → retain evidence.
5. **Portal drift:** receive/poll provider status → compare listing → repair safe differences or queue conflict → record result.

## Product requirements

- Support residential/commercial, sales/lettings, multi-branch, multi-country localization, configurable workflows, and custom fields.
- Prevent publication until mandatory ownership, energy, safety, material-information, media-rights, and instruction checks pass per jurisdiction.
- Preserve price/status/instruction/offer history and separate confidential negotiation data from public listing data.
- Detect duplicate parties/properties safely and preserve portal identifiers during approved merges.
- Support calendar conflicts, keys/access controls, chain dependencies, milestone alerts, and role-specific portals.
- Expose authorized APIs/events for properties, listings, viewings, offers, tenancies, progression, and maintenance.

## Integrations

Property portals, maps/geocoding, calendars, email/SMS/telephony, identity/reference/AML providers, e-signature, deposit schemes, accounting/payments, CMS/website, CRM, and Maintenance use replaceable drivers.

## Quality and control gates

- Test branch/record confidentiality, consent, portal mapping, offer races, calendar timezones, progression dependencies, deposit/rent calculations, and jurisdictional fields.
- Encrypt identity/financial/access data and audit key access, sensitive downloads, offer decisions, and compliance overrides.
- Verify image rights, accessible listings, accurate feeds, failed-provider recovery, and deletion/retention policies.
- Alert on expiring certificates/instructions, unmatched portal state, unqualified offers, stalled progression, arrears, and overdue repairs.

## Delivery phases

1. Core, Parties, Properties, Media, Valuations, Instructions, Listings, matching, viewings, offers, and website feed.
2. Sales Progression, portals, marketing, reporting, communications, and document/e-signature flows.
3. Lettings, deposits, inspections, property management, maintenance, accounting, and owner/tenant portals.
4. Multi-country packs, advanced automation, data enrichment, and portfolio analytics.

## Definition of done

Property-to-completion and property-to-tenancy journeys are permission-safe, compliant, historically traceable, portal-reconciled, and operationally recoverable. Each module maps to a GitHub epic.
