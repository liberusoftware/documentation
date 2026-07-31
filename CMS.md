# Liberu CMS

## Product Scope

**Purpose:** Composable content and digital-experience platform for websites, portals, applications, and headless delivery.
**Architecture:** Packages and extensions follow [MODULES.md](MODULES.md); rendering, themes, layouts, and assets follow [THEMES.md](THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md). Identity, teams, authorization, localization primitives, files, audit, queues, integrations, and observability are not reimplemented here.

## 1. Outcomes

- Let editors model, create, review, localize, publish, discover, reuse, and retire structured content safely.
- Support simple publishing, enterprise editorial operations, multisite estates, and API-first delivery from independently installable packages.
- Match commonly expected WordPress, Drupal, and Joomla capability families without copying their internal architecture.
- Provide governed extension and theme ecosystems while preserving upgrade, security, and performance controls.

## 2. Domain ownership

- CMS owns content entities, editorial lifecycle, information architecture, content delivery, and site configuration.
- Themes own final presentation; CMS supplies typed view models, functional defaults, regions, and stable extension points.
- CRM owns marketing journeys and customer profiles; Ecommerce owns commercial records; CMS embeds or references their capabilities.
- Generic authentication, roles, files, search infrastructure, automation runtime, analytics destinations, and integrations come from Boilerplate contracts.

## 3. Content modeling modules

| Module | Responsibilities |
|---|---|
| CMS Core | Sites, channels, content identity, aliases, ownership, shared terminology, settings, and domain events |
| Content Entities | Typed entities, bundles/content types, lifecycle, authorship, status, cloning, relationships, and canonical identifiers |
| Field System | Reusable typed fields, cardinality, defaults, validation, computed fields, conditional fields, field groups, and schema migrations |
| Metadata | Arbitrary governed metadata, definitions, inheritance, validation, provenance, indexing, and API exposure |
| Taxonomy | Vocabularies, hierarchical terms, synonyms, relationships, ordering, permissions, localization, and term merging |
| Pages | Hierarchy, slugs, routing, home/error pages, aliases, redirects, breadcrumbs, templates, and previews |
| Editorial Content | Posts/articles, authors, excerpts, series, categories, tags, featured content, related content, and archives |
| Structured Collections | Reusable records, directories, FAQs, testimonials, profiles, locations, datasets, and custom collection types |

## 4. Authoring and editorial modules

| Module | Responsibilities |
|---|---|
| Rich Text Editor | Semantic rich text, links, tables, embeds, code, paste cleanup, accessibility hints, formats, and sanitization |
| Block Editor | Typed content blocks, nesting rules, patterns, reusable/global blocks, locking, transforms, previews, and revision-safe data |
| Layout Builder | Regions, grids, sections, drag/drop composition, type defaults, per-record overrides, responsive settings, and permissions |
| Content Templates | Starter content, presets, default fields/blocks/layouts, template locking, versioning, and controlled rollout |
| Revisions | Immutable revisions, autosave, compare, restore, branching, attribution, retention, and published-versus-working copies |
| Editorial Workflow | Configurable states/transitions, assignments, review, approvals, rejection, delegation, separation of duties, and evidence |
| Publishing | Immediate/scheduled publishing, embargo, expiry, unpublish/archive, recurring review, atomic release, and cache/index events |
| Content Calendar | Editorial calendar, campaigns, deadlines, assignments, conflicts, drag/drop rescheduling, and channel/site filters |
| Content Locking | Optimistic concurrency, edit presence, takeover policy, conflict comparison, merge, and recovery |
| Accessibility Assistant | Authoring checks for headings, links, tables, alternatives, contrast metadata, language, captions, and exceptions |

## 5. Media and asset modules

| Module | Responsibilities |
|---|---|
| Media Library | Files/media entities, folders, tags, collections, metadata, usage references, search, bulk operations, and replacement |
| Image Processing | Validation, orientation, crops/focal points, responsive variants, format conversion, quality, optimization, and CDN URLs |
| Video and Audio | Upload/remote media, transcoding adapters, posters, chapters, captions, transcripts, streaming, and playback metadata |
| Digital Asset Management | Rights, licenses, attribution, consent/model releases, expiry, brand assets, renditions, approvals, and distribution |
| Document Management | Documents, previews, OCR/text extraction adapters, versions, access, downloads, watermarks, and retention |
| Embeds | Provider allowlists, normalized embed records, privacy modes, consent, responsive rendering, fallback, and provider adapters |

## 6. Information architecture and display modules

| Module | Responsibilities |
|---|---|
| Navigation | Unlimited menus, nested items, content/custom/system links, menu variants, visibility rules, active trails, and validation |
| Regions and Widgets | Theme regions, reusable widgets, placement, ordering, visibility by route/context/audience, schedules, and caching |
| Views and Query Builder | Permission-safe listings from content/fields/relationships with filters, sorting, grouping, exposed filters, pagination, feeds, and displays |
| Display Modes | Named view/form modes, field formatters, per-type display configuration, responsive variants, and API projections |
| Related Content | Manual/rule/search-driven relationships, similarity, recency, taxonomy, exclusions, explainability, and fallback |
| Content Search | Authorized indexing, facets, spelling, synonyms, relevance, autocomplete, federated sources, reindex, and search analytics |
| Comments and Discussion | Threaded comments, guest/member policy, moderation, subscriptions, mentions, spam control, editing, reports, and retention |
| Contact Directory | People/departments/contact records, categories, locations, contact forms, protected fields, and directory views |

## 7. Sites, localization, and governance modules

| Module | Responsibilities |
|---|---|
| Multisite | Site network, shared/isolated content, domains, site admins, quotas, site lifecycle, network operations, and safe cross-site references |
| Site Factory | Site templates/recipes, provisioning, domain verification, initial content/configuration, cloning, suspension, archival, and teardown |
| Localization | Content/configuration/menu/taxonomy translation, locale variants, fallback, localized slugs, direction, and completeness |
| Translation Management | Jobs, source changes, assignments, vendor adapters, machine translation, review, memory/glossaries, status, cost, and reconciliation |
| Content Access | Per-site/type/record/field visibility, audience rules, scheduled access, private links, content partitioning, and preview authorization |
| Configuration Management | Exportable versioned CMS configuration, environment comparison, dependency validation, promotion, secrets exclusion, and rollback |
| Content Governance | Owners/stewards, policy labels, review cycles, retention, legal hold, sensitive-content classification, and compliance evidence |
| Audit and History | Content/configuration change history, publication evidence, privileged reads/actions, exports, and tamper-aware retention |

## 8. Delivery and experience modules

| Module | Responsibilities |
|---|---|
| Theme Integration | Theme selection by site/channel, regions, view contracts, component registry, inheritance, preview, and safe fallback |
| Web Delivery | Canonical route rendering, response metadata, cache tags, preview mode, redirects, errors, maintenance, and edge invalidation |
| Headless API | Versioned REST/GraphQL-style delivery, sparse fields, includes, filters, pagination, locales, previews, persisted queries, and rate limits |
| Content Federation | Content APIs, remote-source adapters, normalized references, cache/revalidation, source health, and failure fallbacks |
| Syndication and Feeds | RSS/Atom and structured feeds, outbound syndication, inbound feed imports, mappings, deduplication, attribution, and schedules |
| Static Publishing | Full/incremental builds, route manifests, cache invalidation, deployment adapters, preview builds, rollback, and build diagnostics |
| Offline and PWA | Manifest/service-worker integration points, content caching policy, offline pages, update behavior, and install metadata |
| Personalization | Audience/context rules, variants, eligibility, priority, fallback, consent, holdouts, and decision evidence |
| Experimentation | A/B/multivariate content tests, allocation, goals, guardrails, analysis policy, winner promotion, and history |

## 9. Discovery, SEO, and audience modules

| Module | Responsibilities |
|---|---|
| SEO | Titles/descriptions, canonical URLs, robots, structured data, social cards, hreflang, index controls, and content checks |
| Redirects | Redirect records, imports, automatic slug-change redirects, chains/loops, hit counts, expiry, and 404 suggestions |
| Sitemaps | Site/type/locale-aware indexes, exclusions, images/video/news extensions, chunking, cache, and search-engine notification adapters |
| Analytics Integration | Canonical content/view/conversion events, consent-aware analytics mappings, dashboards, and Boilerplate analytics adapters |
| Recommendations | Popular/latest/related/trending/editorial lists, pluggable ranking, audience context, exclusions, and explanation |
| Notifications and Subscriptions | Follow content/terms/authors, publication/update digests, frequency, channel preferences, unsubscribe, and delivery state |

## 10. Forms, community, and application modules

| Module | Responsibilities |
|---|---|
| Form Builder | Typed/conditional multi-step forms, reusable fields, uploads, validation, calculations, drafts, confirmations, and embedding |
| Form Operations | Spam/rate controls, consent, submissions, encryption, retention, notifications, exports, workflow actions, and CRM adapters |
| Polls and Surveys | Questions, branching, anonymous/authenticated response policy, schedules, results, exports, and privacy controls |
| Membership Content | Gated content, access rules, memberships/entitlement references, drip schedules, downloads, and portal integration |
| Events Content | Event/session/speaker/venue content, calendars, registration-provider references, archives, and structured data |
| Knowledge Base | Article hierarchies, versions, feedback, review cycles, search tuning, related articles, and support integration |
| Forums Integration | Forum/community provider contracts, content/profile references, recent discussions, moderation links, and SSO context |

## 11. Extension ecosystem modules

| Module | Responsibilities |
|---|---|
| Extension Manager | Install/enable/disable/update/uninstall, dependencies, compatibility, permissions, configuration, migrations, health, and rollback |
| Extension Marketplace | Publishers, listings, categories, versions, signing, reviews, licensing, trials, security status, support, and distribution |
| Hook and Event SDK | Stable content/editor/render/admin/CLI events, typed extension points, priorities, isolation, diagnostics, and deprecation |
| Theme Marketplace | Theme manifests, compatibility, previews, licenses, child themes, installation, updates, security review, and ratings |
| Site Recipes | Versioned bundles of modules, configuration, content types, workflows, menus, blocks, themes, and starter content |
| Integration Directory | Provider connections, capability discovery, credentials, configuration tests, sync health, and extension links |

Extensions cannot patch core files, bypass policies, query private package tables, or execute arbitrary unsigned code through an admin upload. Composer/deployment installation is the production default.

## 12. Operations and migration modules

| Module | Responsibilities |
|---|---|
| Migration Framework | Source adapters, inventories, mapping, dry run, transforms, identity/media/link resolution, batches, resume, and reconciliation |
| WordPress Migration | Posts/pages/custom types, taxonomies, metadata, users/authors, comments, media, menus, redirects, and source identifiers |
| Drupal Migration | Entity/bundle/field data, revisions, moderation, taxonomy, media, menus, views mapping, translations, and configuration evidence |
| Joomla Migration | Articles/categories, custom fields, contacts, menus, modules/positions, media, users/authors, tags, languages, and redirects |
| Backup and Restore | Content/configuration/database/file backup contracts, schedules, encryption, retention, verification, restore preview, and evidence |
| Cache and Performance | Page/render/query/object cache contracts, cache tags, warming, invalidation, asset optimization hooks, and diagnostics |
| Content Integrity | Broken links/embeds/media, orphan detection, schema validation, duplicate content, scheduled scans, repair queues, and reports |
| Security Operations | Update inventory, extension provenance, content integrity, upload scanning, security headers integration, advisories, and incident aids |

## 13. Intelligence modules

| Module | Responsibilities |
|---|---|
| Content Intelligence | Inventory, quality, readability, accessibility, SEO, freshness, duplication, gaps, performance, and improvement queues |
| CMS Copilot | Permission-bounded search, summaries, drafting, transforms, metadata, internal links, and action confirmation via Automation |
| Translation Assistant | Draft translations, glossary/style enforcement, confidence, review, and provider/model provenance |
| Media Assistant | Alt-text/caption/transcript suggestions, tagging, crops, rights warnings, and human review |
| Experience Assistant | Layout/block suggestions, brand/design constraints, responsive/accessibility checks, preview, and approval |

Generated content remains attributable, reviewable, versioned, and subject to the same workflow, rights, policy, and accessibility gates as human-authored content.

## 14. Required workflows

1. **Model:** propose schema → validate dependencies/data impact → approve → migrate → reindex → make available to editors/APIs.
2. **Publish:** author blocks/content → validate accessibility/SEO/rights → preview by site/locale/theme → review → schedule/publish → invalidate and index.
3. **Translate:** create job → translate → resolve source changes → review → publish locale independently → verify fallback/hreflang.
4. **Release:** group content/configuration changes → preview → approve → publish atomically → monitor → roll back or restore revisions.
5. **Multisite provision:** select recipe → validate domain/entitlements → create site → apply config/theme/starter content → verify → hand over.
6. **Extension lifecycle:** review provenance/scopes/compatibility → install in non-production → test → approve/deploy → monitor → update or remove safely.
7. **Migrate:** inventory source → map/dry run → import resumably → validate counts/links/media/permissions → redirect → reconcile and sign off.

## 15. Shared requirements and quality gates

- Preserve content/field/revision identifiers, authorship, publication evidence, translations, references, and import provenance.
- Enforce authorization at site, type, record, field, revision, locale, media, preview, search, API, and bulk-operation boundaries.
- Sanitize rich content, validate uploads, protect preview/private links, verify extension provenance, and isolate optional provider failure.
- Support accessible authoring and WCAG 2.2 AA delivery, localization/RTL, responsive output, semantic HTML, captions, and alternative media.
- Test schema evolution, concurrent editing, moderation, schedules/timezones, cache invalidation, search, redirects, locale fallback, multisite isolation, and extension upgrades.
- Benchmark large content/media estates, query-built views, APIs, publication bursts, migrations, cache warming, and multisite operations.
- Provide structured logs, publishing/index/cache metrics, failed-job replay, health checks, alerts, backup/restore drills, and runbooks.

## 16. Delivery phases

1. Core, Content Entities, Field System, Taxonomy, Pages/Editorial Content, Rich Text, Revisions, Publishing, Media, Navigation, SEO, and web delivery.
2. Block Editor, Layout Builder, Workflow, Calendar, Views/Query Builder, Widgets, Comments, Search, Forms, Localization, and headless API.
3. Multisite/Site Factory, Translation Management, DAM/video/documents, Configuration Management, access/governance, syndication, static publishing, and migration framework.
4. Extension/Theme Marketplaces, Site Recipes, personalization/experiments, recommendations, knowledge/membership/event integrations, and operational tooling.
5. Intelligence assistants, advanced federation, performance optimization, and benchmark migration adapters.

## 17. Benchmark coverage and sources

- **WordPress:** approachable posts/pages/media, revisions, custom types/taxonomies/metadata, block editing, menus/widgets, themes/plugins, comments, multisite, feeds, and REST delivery.
- **Drupal:** entity/field modeling, Views-style query displays, blocks/layouts, revisions/moderation workflows, configuration promotion, multilingual depth, structured access, and decoupled delivery.
- **Joomla:** articles/categories/custom fields, components/modules/plugins, menu-driven display, template positions/overrides, contacts, workflows, multilingual sites, and granular ACL integration.
- **Common extensions:** SEO, forms, cache/performance, security, backup/migration, multilingual workflows, page building, memberships, events, learning, forums, analytics, and commerce integration are represented as owned modules or adapters rather than core patches.

Official reference starting points:

- [WordPress features](https://wordpress.org/about/features/)
- [WordPress REST API reference](https://developer.wordpress.org/rest-api/reference/)
- [Drupal feature overview](https://www.drupal.org/features)
- [Drupal content moderation](https://www.drupal.org/docs/8/core/modules/content-moderation/overview)
- [Drupal Layout Builder](https://www.drupal.org/docs/8/core/modules/layout-builder)
- [Joomla core features](https://docs.joomla.org/J4.x%3AJoomla_Core_Features/en)
- [Joomla extension types](https://docs.joomla.org/Extension_types_%28technical_definitions%29/en)

## 18. Definition of done

Editors and developers can model, author, review, localize, compose, publish, deliver, migrate, extend, and recover content across selected sites/channels without losing provenance or compromising authorization, accessibility, upgradeability, performance, or provider independence. Each module table row is suitable for a focused GitHub epic.
