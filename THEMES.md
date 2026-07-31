# Liberu Theme Architecture

## Canonical Implementation Specification

**Status:** Source of truth
**Applies to:** Public sites, customer portals, application shells, and Filament panels
**Related architecture:** [MODULES.md](MODULES.md)

## 1. Purpose

A theme is a versioned presentation package that controls visual identity and rendering without owning business rules. It may provide Blade layouts, views, components, Livewire presentation components, JavaScript, CSS, fonts, images, logos, icons, and video. Themes consume documented module view models and extension points.

Modules own behavior and functional defaults. Themes own composition, styling, branded assets, and presentation overrides. A theme must never query module tables, bypass policies, or duplicate domain workflows.

## 2. Theme types

| Type | Intended surface |
|---|---|
| Public | Marketing sites, publishing, ecommerce storefronts, and public product pages |
| Portal | Authenticated customer, partner, member, or staff experiences |
| Admin | Filament panels and operational dashboards |
| Shared | Design tokens, primitives, icons, fonts, and cross-surface assets inherited by other themes |

A deployment may select different themes by site, tenant, brand, locale, or surface. Theme selection must use trusted configuration and fall back safely.

## 3. Standard theme layout

```text
themes/
└── Corporate/
    ├── composer.json
    ├── theme.json
    ├── README.md
    ├── CHANGELOG.md
    ├── resources/
    │   ├── css/
    │   │   ├── app.css
    │   │   ├── components/
    │   │   └── tokens.css
    │   ├── js/
    │   │   ├── app.js
    │   │   └── components/
    │   ├── images/
    │   ├── logos/
    │   ├── icons/
    │   ├── fonts/
    │   ├── videos/
    │   ├── lang/
    │   └── views/
    │       ├── components/
    │       ├── layouts/
    │       ├── livewire/
    │       ├── modules/
    │       └── pages/
    ├── src/
    │   ├── Livewire/
    │   ├── Providers/
    │   ├── View/
    │   │   ├── Components/
    │   │   └── Composers/
    │   └── CorporateThemeServiceProvider.php
    ├── tests/
    │   ├── Accessibility/
    │   ├── Feature/
    │   └── Visual/
    └── vite.config.js
```

Create only directories the theme uses. Generated build output is not committed unless a distribution package explicitly requires it.

## 4. Manifest contract

Every theme provides `theme.json`:

```json
{
  "$schema": "https://schemas.liberu.dev/theme/v1.json",
  "name": "corporate",
  "display_name": "Liberu Corporate",
  "version": "1.0.0",
  "provider": "Liberu\\Themes\\Corporate\\CorporateThemeServiceProvider",
  "type": "public",
  "parent": "liberu-base",
  "supports": ["cms.pages", "cms.posts", "search"],
  "assets": {
    "css": ["resources/css/app.css"],
    "js": ["resources/js/app.js"]
  }
}
```

The manifest declares compatibility, parent theme, supported module extension points, asset entry points, and safe fallback. CI validates its schema, paths, unique name, dependency versions, and inheritance cycles.

## 5. Resolution and inheritance

Theme resolution follows: configured surface/tenant/site theme → parent theme chain → module default view → application fallback. The first existing compatible view wins.

- Overrides use stable names such as `modules.cms.pages.show`.
- A child theme overrides only what differs and inherits all other assets and views.
- Parent chains are finite, deterministic, and cached in production.
- Missing or incompatible themes fall back to a configured safe theme and emit an operational alert.
- Themes cannot replace authorization, validation, routes, actions, or domain services.

## 6. Design tokens

All themes define or inherit semantic tokens for color, typography, spacing, radius, elevation, borders, motion, breakpoints, focus, and layering. Components consume semantic tokens such as `--color-surface` and `--color-action-primary`, not brand-specific raw values.

Tokens must cover light, dark, high-contrast, error, warning, success, disabled, and focus states. A brand override changes tokens before it forks component markup.

## 7. Blade views and layouts

- Layouts define document structure, metadata slots, navigation regions, content, notices, and footer regions.
- Blade components are small, escaped by default, documented, and independent of ambient database state.
- Views receive explicit, typed view models where practical.
- Module overrides preserve documented variables, slots, events, test identifiers, and accessibility behavior.
- Templates use translation strings and locale-aware formatting; user-facing copy is not embedded in PHP classes.
- SEO metadata, canonical URLs, structured data, and social cards use shared components.

## 8. Livewire components

Theme Livewire components may manage presentation state such as menus, dialogs, filters, carousels, and progressive interactions. Business mutations call authorized module actions rather than implementing domain logic.

- Public properties and actions are validated and authorized.
- Component state remains minimal and serializable.
- Loading, empty, error, offline, and success states are designed explicitly.
- Events and component aliases are namespaced and documented.
- JavaScript integrations use Livewire lifecycle hooks and clean up listeners on navigation.
- Critical content and actions remain usable with progressive enhancement where feasible.

## 9. CSS

- Use one documented cascade-layer order for reset, tokens, base, components, utilities, and overrides.
- Scope component styles and avoid selectors coupled to undocumented module markup.
- Respect reduced motion, forced colors, zoom, text resizing, logical properties, and bidirectional layouts.
- Establish performance budgets for compressed CSS and eliminate unused production styles.
- Filament customization uses supported theme hooks and variables rather than vendor-file edits.

## 10. JavaScript

- JavaScript enhances server-rendered experiences and must not duplicate authoritative business state.
- Modules are loaded only on surfaces that require them; large dependencies use dynamic imports.
- Third-party scripts require documented purpose, consent category, integrity/version policy, and failure behavior.
- Avoid inline scripts unless protected by the application's content security policy nonce mechanism.
- Client errors include release and correlation context without sensitive data.
- Components support keyboard, pointer, touch, and assistive technology interaction.

## 11. Images, logos, icons, and video

- Store editable source assets separately from optimized delivery variants where applicable.
- Images define meaningful alternative text at content level; decorative assets use empty alternatives.
- Provide responsive dimensions, modern formats, explicit width/height, lazy loading below the fold, and a fallback.
- Logos include approved variants for light/dark backgrounds, compact marks, safe space, and accessible naming.
- Icons use a reviewed set, inherit semantic color, and include labels when meaning is not accompanied by text.
- Video provides captions, transcript, poster, controls, and reduced-motion/autoplay-safe behavior.
- Asset filenames are stable, lowercase, and content-hashed at build time.
- Licensing, attribution, provenance, usage restrictions, and model releases are recorded for non-original assets.

## 12. Asset pipeline

Vite resolves theme entry points and produces versioned, cacheable assets. Builds must be deterministic and fail on missing manifest paths, unresolved imports, oversized assets beyond budget, or incompatible dependencies.

Production uses long-lived caching for hashed files and appropriate CDN headers. Runtime-generated brand tokens or tenant assets must use controlled storage URLs and cannot trigger arbitrary source compilation.

## 13. Filament integration

Admin themes may register supported Filament CSS/JS assets, render hooks, icons, and panel colors through a provider or panel plugin. They must preserve Filament authorization, action behavior, validation, responsive behavior, and upgrade compatibility.

Resources, pages, widgets, forms, tables, and infolists remain owned by modules. The theme changes their presentation only through supported extension points.

## 14. Localization and content direction

- All visible strings are translatable and support pluralization and interpolation.
- Layouts support left-to-right and right-to-left direction using logical CSS properties.
- Dates, numbers, addresses, names, currencies, and timezones use locale-aware services.
- Images containing text require localized variants or must be replaced by semantic HTML.
- Font selections declare language coverage and sensible fallbacks.

## 15. Accessibility

Themes target WCAG 2.2 AA. Required checks include semantic landmarks and headings, keyboard operation, visible focus, skip links, accessible names, form errors, status announcements, contrast, reflow at zoom, target size, reduced motion, captions, and screen-reader behavior.

Automated scanning is necessary but not sufficient. Each release includes keyboard and representative screen-reader checks for primary journeys.

## 16. Security and privacy

- Escape output by default and sanitize explicitly allowed rich content through a shared service.
- Do not embed secrets, privileged data, internal identifiers, or unapproved personal information in HTML or assets.
- Honor consent before analytics, advertising, chat, or external media scripts run.
- Support CSP, subresource integrity where applicable, CSRF protections, and secure upload/download flows.
- External embeds use allowlists, privacy-enhanced modes, and clear failure placeholders.

## 17. Performance and resilience

Each surface defines budgets for CSS, JavaScript, fonts, images, video, requests, and Core Web Vitals. Themes use responsive assets, font subsetting/preload sparingly, code splitting, server rendering, and caching.

Navigation, authentication, checkout, forms, and core portal tasks must remain understandable when optional scripts, analytics, media providers, or CDN resources fail.

## 18. Testing

Every theme includes:

- render tests for layouts, components, module extension points, and fallback behavior;
- Livewire tests for state, validation, authorization, and events;
- accessibility tests plus manual checks for primary journeys;
- visual regression at representative viewports, themes, locales, and color modes;
- asset build, broken-link, missing-translation, and manifest validation;
- performance checks against agreed budgets;
- compatibility tests against supported module and framework versions.

## 19. Versioning and documentation

Themes use semantic versioning. Stable surfaces include manifest fields, token names, component names/props/slots, Livewire aliases/events, view override names, and asset entry points. Breaking changes require a major release and migration guide.

The README documents installation, selection, parent theme, supported surfaces/modules, build commands, tokens, component inventory, extension points, asset licenses, browser support, accessibility notes, and upgrade instructions.

## 20. Definition of done

A theme is ready when:

- its manifest, parent chain, surface, and compatibility are valid;
- layouts, navigation, states, module views, Livewire components, and assets are complete;
- light/dark, responsive, localization, RTL, and brand behavior are verified as applicable;
- accessibility, visual, functional, security, and performance tests pass;
- fallback behavior works without optional assets or providers;
- asset rights, documentation, changelog, and migration guidance are complete.

## 21. GitHub issue mapping

Create one theme epic, then child issues for: manifest and inheritance; tokens and typography; layouts and navigation; Blade components; Livewire interactions; module view integrations; CSS/JavaScript pipeline; imagery/logos/icons/video; localization/RTL; accessibility; visual regression; performance/security; documentation and release.

Each issue identifies target surfaces, supported modules, affected extension points, assets, responsive states, accessibility criteria, tests, performance budget, and explicit exclusions.
