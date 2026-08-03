# Liberu Theme Architecture

## Canonical Implementation Specification

**Status:** Source of truth
**Applies to:** Public sites, customer portals, application shells, Filament panels, Livewire, React/Inertia, Vue/Inertia, and Nuxt surfaces
**Related architecture:** [MODULES.md](../architecture/MODULES.md) · [API.md](../architecture/API.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [TESTING.md](TESTING.md) · [TECHNOLOGIES.md](../TECHNOLOGIES.md)

## 1. Purpose

A theme is a versioned presentation package that controls visual identity and rendering without owning business rules. Its canonical identity is technology-neutral; optional adapters may provide Blade views, Livewire components, React/Inertia pages, Vue/Inertia SFCs, Nuxt layers/components, JavaScript, CSS, fonts, images, logos, icons, and video. Themes consume documented module view models and extension points.

Modules own behavior and functional defaults. Themes own composition, styling, branded assets, and presentation overrides. A theme must never query module tables, bypass policies, or duplicate domain workflows.

Themes consume APIs only through documented application or module contracts governed by [API.md](../architecture/API.md). They must not embed provider credentials, invent private endpoints, or make a remote API the source of presentation-specific business rules.

Themes use a unified design, manifest, installation, inheritance, testing, and documentation approach. They may be mixed into different repository-based projects as needed. A theme may be designed and optimized for a specific Liberu repository to produce the best result, but it should remain installable and reasonably compatible with other Liberu repositories or compatible Laravel projects. Outside its optimized hosts, some views or integrations may be unavailable or imperfect; those limitations must be declared and must fail or fall back safely.

Each theme is developed and released from an independent GitHub repository under the [`liberusoftware`](https://github.com/liberusoftware) organization. Composer resolves Laravel/theme packages, while the custom Liberu Composer installer places them in `/themes`; Node-based adapters use the same identity and manifest through the consuming Vite/Nuxt build.

## 2. Theme types

| Type   | Intended surface                                                                            |
| ------ | ------------------------------------------------------------------------------------------- |
| Public | Marketing sites, publishing, ecommerce storefronts, and public product pages                |
| Portal | Authenticated customer, partner, member, or staff experiences                               |
| Admin  | Filament panels and operational dashboards                                                  |
| Shared | Design tokens, primitives, icons, fonts, and cross-surface assets inherited by other themes |

A deployment may select different themes by site, tenant, brand, locale, or surface. Theme selection must use trusted configuration and fall back safely.

## 3. Standard theme layout

The source repository is rooted at the theme package itself:

```text
github.com/liberusoftware/theme-corporate/
    ├── .github/
    │   └── workflows/
    │       ├── compatibility.yml
    │       ├── install.yml
    │       ├── tests.yml
    │       └── visual.yml
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
    ├── adapters/
    │   ├── react-inertia/
    │   │   ├── Pages/
    │   │   ├── Components/
    │   │   └── index.ts
    │   ├── vue-inertia/
    │   │   ├── Pages/
    │   │   ├── Components/
    │   │   └── index.ts
    │   └── nuxt/
    │       ├── components/
    │       ├── layouts/
    │       └── layer/
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

Composer installs that repository as `<project-root>/themes/corporate`. Create only directories the theme uses. Generated build output is not committed unless a distribution/release package explicitly requires it.

## 3.1 Composer installation policy

Themes declare `"type": "liberu-theme"` in `composer.json` and a stable installer name in Composer `extra` metadata. The canonical `liberu/composer-installer` plugin installs them to `<project-root>/themes/{theme-name}` and also handles `liberu-module` packages as defined in `MODULES.md`.

The installer must validate names, reject absolute paths/path traversal, detect collisions, install deterministically, support install/update/remove, and remain compatible with Composer 2 plugin security. Normal PHP/npm dependencies remain in their standard dependency locations; only the Liberu theme package is relocated to `/themes`.

Applications explicitly require selected themes and the installer plugin, authorize the plugin through Composer `allow-plugins`, and commit `composer.json` and `composer.lock`. Production builds use a non-interactive locked install and fail if the expected theme path cannot be reproduced.

The application root is the single owner of `liberu/composer-installer` and its `allow-plugins` entry. Individual themes declare their package type and installer name but do not repeat the installer plugin as a runtime requirement.

### 3.1.1 Canonical Composer test setup

Theme repositories target stable Pest 5 and declare test tooling only under `require-dev`:

```json
{
  "require-dev": {
    "liberu/package-testbench": "^1.0",
    "pestphp/pest": "^5.0",
    "pestphp/pest-plugin-laravel": "^5.0"
  },
  "autoload-dev": {
    "psr-4": {
      "Liberu\\Themes\\Corporate\\Tests\\": "tests/"
    }
  },
  "scripts": {
    "test": "pest --ci",
    "test:feature": "pest tests/Feature",
    "test:coverage": "pest --ci --coverage --min=100 --coverage-clover=build/coverage/clover.xml --coverage-html=build/coverage/html",
    "test:parallel": "pest --parallel"
  }
}
```

Use the theme's real namespace and only define commands for suites it contains. Pest-maintained plugins use compatible `^5.0` constraints. Browser, Livewire or other plugins are required only when the theme uses their evidence. Do not require `phpunit/phpunit` separately when Pest supplies the compatible PHPUnit runtime.

`liberu/package-testbench` is the single shared bootstrap for independently running module and theme package suites. Each theme still owns its tests, `Pest.php`, `phpunit.xml` or `phpunit.xml.dist`, Composer command aliases, and GitHub workflows. Themes must not require a second scripts/tooling package that duplicates or proxies those responsibilities.

## 3.2 Independent repositories and tracked `/themes`

One independent theme repository normally contains one primary theme package. It owns its releases, issues, assets, licenses, tests, coverage, documentation, compatibility matrix, build tooling, and changelog.

The current decision, matching `/modules`, is **not to add `/themes` to `.gitignore`**. Installed theme contents are committed in each consuming application repository.

- Make changes in the theme's source repository, release a version, then update consuming applications through Composer.
- Do not edit an installed `/themes/{theme-name}` copy directly in an application.
- Commit `composer.json`, `composer.lock`, and resulting `/themes` changes together.
- Review theme source, compiled/distributable assets where included, licenses, and release notes during updates.
- CI performs a clean locked install/build and fails when it produces an unexpected `/themes` diff.
- Resolve conflicts by selecting the intended lockfile version and reinstalling, not by hand-merging installed theme code.

This tracked-directory policy may change only through an ADR and migration plan. The independent theme repository remains authoritative.

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
  "optimized_for": ["liberu-cms/cms-laravel"],
  "tested_with": ["liberu-cms/cms-laravel", "liberu/boilerplate-laravel"],
  "supports": ["cms.pages", "cms.posts", "search"],
  "adapters": {
    "blade": {
      "entrypoints": ["resources/css/app.css", "resources/js/app.js"]
    },
    "livewire": {
      "entrypoints": ["resources/css/app.css", "resources/js/app.js"]
    },
    "react-inertia": {
      "package": "theme-corporate-react-inertia",
      "entrypoints": ["adapters/react-inertia/index.ts"]
    },
    "vue-inertia": {
      "package": "theme-corporate-vue-inertia",
      "entrypoints": ["adapters/vue-inertia/index.ts"]
    },
    "nuxt": {
      "package": "theme-corporate-nuxt",
      "layer": "adapters/nuxt/layer"
    }
  },
  "assets": {
    "css": ["resources/css/app.css"],
    "js": ["resources/js/app.js"]
  }
}
```

The manifest declares compatibility, optimized/tested host repositories, parent theme, required and optional capabilities, supported module extension points, asset entry points, and safe fallback. CI validates its schema, paths, unique name, dependency versions, capabilities, and inheritance cycles.

Installed theme discovery and application asset composition are manifest-driven. Applications read validated `theme.json` files instead of maintaining parallel literal theme or entry-point arrays. Manifest paths are package-relative, normalized, collision-checked, and verified to exist before activation or build. Technology adapters are optional and may be selected only when the host uses that technology.

`optimized_for` is informative and identifies where the theme delivers its intended complete experience. `tested_with` records verified hosts and version ranges in the full schema. Neither field creates a hidden dependency. Required capabilities fail installation/activation clearly; missing optional capabilities omit the relevant UI and use documented fallbacks.

## 5. Resolution and inheritance

Theme resolution follows: configured surface/tenant/site theme → parent theme chain → module default view → application fallback. The first existing compatible view wins.

- Overrides use stable names such as `modules.cms.pages.show`.
- A child theme overrides only what differs and inherits all other assets and views.
- Parent chains are finite, deterministic, and cached in production.
- Every declared parent resolves to an installed compatible theme; missing parents and inheritance cycles fail validation before activation.
- Missing or incompatible themes fall back to a configured safe theme and emit an operational alert.
- Themes cannot replace authorization, validation, routes, actions, or domain services.
- Cross-repository use resolves only declared extension points; repository-specific overrides must be isolated, capability-checked, and documented.

## 6. Design tokens

All themes define or inherit semantic tokens for color, typography, spacing, radius, elevation, borders, motion, breakpoints, focus, and layering. Components consume semantic tokens such as `--color-surface` and `--color-action-primary`, not brand-specific raw values.

Tokens must cover light, dark, high-contrast, error, warning, success, disabled, and focus states. A brand override changes tokens before it forks component markup.

### 6.1 Technology-neutral theme contract

The theme identity, semantic token names, component states, content regions, asset roles, accessibility behavior, and module extension-point names are shared across technologies. The adapter translates that contract into its framework's rendering and build system.

| Shared contract    | Laravel/Blade               | Livewire                        | React/Inertia                          | Vue/Inertia                            | Nuxt                                   |
| ------------------ | --------------------------- | ------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| Layout regions     | Blade layouts/components    | Blade layouts + Livewire views  | Inertia layouts/components             | Inertia layouts/SFCs                   | Nuxt layouts/components                |
| Presentation state | progressive JS              | Livewire state                  | hooks/local state                      | composables/local state                | composables/local state                |
| Tokens             | CSS custom properties       | CSS custom properties           | CSS custom properties or typed exports | CSS custom properties or typed exports | CSS custom properties or typed exports |
| Module extension   | documented view names/slots | documented view/component hooks | typed component/page slots             | typed component/page slots             | typed component/slot props             |
| Server boundary    | Laravel view model          | Livewire public state           | Inertia props/API contract             | Inertia props/API contract             | API contract/runtime config            |

Adapters must not change token meaning, responsive states, focus behavior, copy, permission semantics, or required loading/error/empty states. If a framework cannot support a capability, the manifest declares the limitation and uses the documented fallback.

### 6.2 Theme adapter packages

Use one technology adapter package per supported framework when framework code is non-trivial:

```text
theme-{name}                         # shared identity, tokens, assets, Blade defaults
theme-{name}-livewire                # optional Livewire presentation adapter
theme-{name}-react-inertia            # optional React/Inertia adapter
theme-{name}-vue-inertia              # optional Vue/Inertia adapter
theme-{name}-nuxt                     # optional Nuxt adapter
```

The shared theme owns the contract and brand assets. An adapter may add framework-specific composition and tests, but it must not fork domain behavior or redefine the theme identity.

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

The application Vite configuration discovers installed `themes/*/theme.json` manifests and derives entry points exclusively from each manifest's `assets.css` and `assets.js` declarations. It must not repeat installed themes or their asset paths in a maintained literal list. Theme packages use the same manifest contract in independent builds so package and host results cannot drift.

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

Every theme follows [TESTING.md](TESTING.md#13-coverage-policy), uses stable Pest 5 as its primary PHP/Livewire runner, and includes:

- render tests for layouts, components, module extension points, and fallback behavior;
- Livewire tests for state, validation, authorization, and events;
- accessibility tests plus manual checks for primary journeys;
- visual regression at representative viewports, themes, locales, and color modes;
- asset build, broken-link, missing-translation, and manifest validation;
- performance checks against agreed budgets;
- compatibility tests against supported module and framework versions.
- cross-adapter contract tests proving token names, required states, extension-point names, and fallback behavior are equivalent across declared adapters.
- clean Composer-install tests proving the theme resolves to `/themes/{theme-name}` in each declared tested host;
- graceful-degradation tests for missing optional modules and at least one compatible non-optimized host where practical.

Every theme suite runs independently from its source repository with `composer install` and `composer test`; it must not extend the consuming application's `Tests\\TestCase`. Tests use correctly cased, Composer-autoloadable PSR-4 namespaces and the canonical `liberu/package-testbench` bootstrap.

A shared `ThemeBoundariesTest` contract, supplied by the package testbench and executed by every theme, verifies manifest completeness, confirms the declared provider is a real Laravel service provider, resolves every parent, rejects cycles, and verifies every declared asset path exists. A render contract also proves that a child without `layouts/app.blade.php` falls back to its parent implementation.

Meaningful owned PHP and Livewire code targets 100% line coverage. `composer test:coverage` enforces `--min=100` and produces Clover and HTML reports. CSS, images and static templates use render, accessibility, visual-regression, asset-build and performance evidence instead of misleading executable coverage. Files are not excluded merely to reach the target.

### 18.1 Required repository workflows

Each independent theme repository owns these GitHub Actions workflows:

| Workflow            | Required evidence                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `install.yml`       | Clean Composer dependency resolution/install, manifest/provider validation, independent bootstrap, asset dependency install, build, and documented quick start |
| `tests.yml`         | Pest 5 feature/Livewire/boundary/security suites, static analysis, asset validation, and 100% meaningful owned PHP coverage reports                                  |
| `visual.yml`        | Accessibility and visual regression across representative viewports, locales, directions, color modes, parent fallback, and supported hosts                    |
| `compatibility.yml` | Declared minimum/current PHP, Laravel, Livewire/Filament where used, parent-theme, and representative optimized/non-optimized hosts                            |

Performance or broad browser matrices may be scheduled or release-gated, but required release evidence must complete before publication. Workflows invoke repository-owned Composer/npm scripts directly and must not require a duplicated scripts package. Generated coverage, screenshots and reports are retained as protected CI artifacts.

## 19. Versioning and documentation

Themes use semantic versioning. Stable surfaces include manifest fields, token names, component names/props/slots, Livewire aliases/events, view override names, and asset entry points. Breaking changes require a major release and migration guide.

Every independent theme repository contains a professionally written `README.md` documenting purpose, visual examples/screenshots, optimized and tested repositories, known limitations outside those hosts, Composer installation and `/themes` path behavior, selection, parent theme, required/optional modules, supported surfaces, build commands, design tokens, component/view/Livewire inventory, extension points, assets and licenses, responsive/browser support, accessibility, localization/RTL, performance budgets, security/privacy notes, testing, coverage, contribution, release, upgrade, and uninstall instructions.

Theme CI generates test coverage for PHP/Livewire behavior where meaningful, plus accessibility, visual-regression, asset-build, and performance results. The README displays current CI/coverage status and explains local test/build commands. Generated reports and screenshots are retained as CI artifacts or approved release assets rather than normally committed as raw test output. CSS or static templates that do not produce meaningful line coverage document the applicable alternative quality evidence.

The README states that Pest 5 is the canonical PHP/Livewire runner, lists local Composer and asset commands, identifies the shared package-testbench version, and links the install, tests, visual, compatibility, coverage and build evidence.

## 20. Definition of done

A theme is ready when:

- its manifest, parent chain, surface, and compatibility are valid;
- layouts, navigation, states, module views, Livewire components, and assets are complete;
- light/dark, responsive, localization, RTL, and brand behavior are verified as applicable;
- accessibility, visual, functional, security, and performance tests pass;
- fallback behavior works without optional assets or providers;
- its independent Pest 5 suite passes, meaningful owned PHP reaches the [100% coverage target](TESTING.md#13-coverage-policy), and non-executable assets have equivalent quality evidence;
- asset rights, documentation, changelog, and migration guidance are complete;
- its independent `liberusoftware` repository, README, tagged release, CI results, generated meaningful coverage/quality reports, and host compatibility evidence are available;
- a clean locked Composer install places it in `/themes`, and the consuming repository has no unexpected generated diff;
- optimized hosts render the complete intended experience and compatible non-optimized hosts degrade according to documented limitations and fallbacks.

## 21. GitHub issue mapping

Create one theme epic, then child issues for: manifest and inheritance; shared tokens and typography; technology adapter matrix; layouts and navigation; Blade components; Livewire interactions; React/Inertia components; Vue/Inertia components; Nuxt layer/components; module view integrations; CSS/JavaScript pipeline; imagery/logos/icons/video; localization/RTL; accessibility; visual regression; performance/security; documentation and release.

Each issue identifies target surfaces, supported modules, affected extension points, assets, responsive states, accessibility criteria, tests, performance budget, and explicit exclusions.
