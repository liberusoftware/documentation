# Liberu CMS

## Product Scope

**Purpose:** Modular content management for websites, applications, and headless delivery.
**Architecture:** [MODULES.md](MODULES.md) governs functional packages; [THEMES.md](THEMES.md) governs rendering and assets.

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md); this scope defines content behavior only.

## Outcomes

- Let editors model, create, review, localize, publish, and retire content safely.
- Serve multiple sites and channels from governed content without coupling content to one theme.
- Provide extensible SEO, media, forms, search, and API capabilities.

## Module plan

| Module | Responsibilities |
|---|---|
| CMS Core | Sites, channels, content identity, shared taxonomies, module settings, and content events |
| Content Types | Schema builder, typed fields, validation, reusable field groups, and schema migrations |
| Pages | Hierarchy, slugs, routes, redirects, landing pages, previews, and publication |
| Publishing | Drafts, revisions, compare/restore, schedules, approvals, embargoes, expiry, and audit |
| Localization | Locale variants, fallback, translation status, localized slugs, and hreflang metadata |
| Media | Library, folders/tags, metadata, transformations, focal points, rights, access, and retention |
| Navigation | Menus, nested items, link validation, visibility rules, and site/locale variants |
| Blocks | Typed reusable blocks, composition rules, presets, validation, and page-builder ordering |
| SEO | Metadata, canonical URLs, robots, sitemaps, structured data, redirects, and social previews |
| Forms | Form schemas, validation, spam controls, consent, submissions, notifications, and exports |
| Search | Authorized indexing, filters, suggestions, synonyms, and reindex operations |
| Headless API | Versioned content/media/navigation APIs, previews, webhooks, cache tags, and rate limits |
| Extensions | Capability registry and supported hooks for modules, themes, widgets, and integrations |

## Required workflows

1. **Publish:** create content → validate → preview in site/theme context → review → schedule/publish → invalidate caches and index.
2. **Revise:** branch from published revision → compare → approve → publish atomically → retain restoration history.
3. **Localize:** create locale variant → track translation completeness → review → publish with fallback and hreflang rules.
4. **Media:** upload → malware/type validation → metadata/rights capture → transform → approve → deliver through authorized URLs.
5. **Form:** render schema → validate/consent/spam check → persist per retention policy → notify/integrate → export or delete.

## Product requirements

- Support multi-site, optional multi-tenancy, custom domains, channel-specific publication, and per-site theme selection.
- Model pages, posts, collections, taxonomies, authors, relationships, dates, structured fields, and reusable blocks.
- Prevent conflicting slugs, broken references, accidental unpublishing, and publication of invalid schemas.
- Provide editorial dashboard, bulk actions, calendars, revision history, preview links, and permission-aware search.
- Offer accessible functional views that themes can override through stable extension points.
- Provide import/export with validation, dry run, mapping, idempotency, and error reports.
- Emit versioned content, media, redirect, navigation, and publication events.

## Integrations

Storage/CDN, image/video processing, search engines, analytics, email, CRM, ecommerce, social publishing, translation providers, Git repositories, and static-site consumers integrate through replaceable drivers or events.

## Quality gates

- Test authorization and tenant/site/locale isolation across preview, API, search, media, and bulk actions.
- Sanitize rich content, validate uploads, protect previews, rate-limit forms, and honor consent/retention.
- Verify accessibility, responsive rendering, SEO output, cache invalidation, redirects, and restoration.
- Load-test publication, large libraries, navigation, search indexing, and cache-warm workflows.

## Delivery phases

1. CMS Core, Content Types, Pages, Publishing, permissions, and audit.
2. Media, Navigation, Blocks, SEO, and theme extension points.
3. Localization, Search, Forms, and headless APIs.
4. Imports, external integrations, advanced workflow, and analytics.

## Definition of done

Editors can complete the full multilingual content lifecycle with safe previews, approvals, restoration, authorized delivery, accessible themes, reliable cache/search updates, and documented module contracts. Each table row maps to a GitHub epic.
