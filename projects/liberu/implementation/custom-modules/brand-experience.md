# Brand Experience Composition

**Package:** `module-liberu-brand-experience`

Owns the four-site registry, domain-to-brand resolution, theme recipe, navigation composition, cross-site links, public status/support slots, and brand configuration metadata. CMS remains authoritative for content/media and Boilerplate remains authoritative for identity, settings, and authorization.

**Public contract:** `site_id`, `brand_id`, host, locale, theme tokens, enabled navigation, consent topics, content/API collections, and safe portal/support links. Reject unknown hosts and never expose staff/customer data in public responses.

**Acceptance:** preview/publish/rollback recipes, host isolation, cache invalidation, localization, accessibility, SEO/redirects, consent, mobile layout, and graceful unknown-site errors.
