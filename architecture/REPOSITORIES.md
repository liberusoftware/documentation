# Liberu Repository README Standard

## Canonical Design and Content Specification

**Applies to:** Main application repositories, module repositories, theme repositories, and reusable packages under Liberu organizations
**Reference implementation:** [`liberusoftware/boilerplate-laravel`](https://github.com/liberusoftware/boilerplate-laravel)
**Related standards:** [MODULES.md](MODULES.md) · [THEMES.md](THEMES.md) · [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) · [API.md](API.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [TESTING.md](TESTING.md)

## 1. Purpose

Every Liberu repository must have a concise, professional, and current root `README.md`. It should let a visitor understand the project, confirm its health, see it in action, install it safely, find detailed documentation, and contribute without reading source code first.

The README is a landing page, not the complete manual. Keep detailed architecture, deployment, module/theme development, API, provider, and troubleshooting material in `/docs` and link to it.

## 2. Required content order

Use this order unless the repository type makes a section irrelevant:

1. Project title and one-line purpose
2. Liberu website links
3. Branded cover image or logo
4. Technology, release, quality, and workflow badges
5. Short project description and aims
6. Video thumbnail linked to the project video
7. Key features
8. Requirements and quick start
9. Architecture or package usage summary
10. Documentation and support links
11. Related Liberu projects
12. Security
13. License
14. Feedback and contributing
15. Contributors graph

Do not add an oversized table of contents to a short README. Add one only when the rendered document is long enough that navigation materially helps.

## 3. Header and title

The first heading is the clear public product/package/theme name, not its Composer name or repository slug.

```markdown
# Liberu Boilerplate

> Production-ready Laravel foundation for modular, single-tenant and multi-tenant applications.
```

Rules:

- Use one H1 only.
- Keep the purpose line to one sentence and avoid marketing superlatives that cannot be verified.
- State maturity prominently when the project is experimental, alpha, beta, deprecated, or archived.
- Do not place installation instructions or a long feature list before the identity/status header.

## 4. Official Liberu links

Place a compact link line directly below the title/purpose:

```markdown
[Software](https://liberusoftware.com) ·
[Hosting](https://liberuhosting.com) ·
[Services](https://liberuservices.com) ·
[Liberu Group](https://liberugroup.com)
```

Add product documentation, demo, status, or support links only when their URLs exist and are maintained. Use HTTPS and descriptive labels rather than bare URLs.

## 5. Cover image or logo

Use an approved Liberu-owned asset derived from the official [`facebook.com/liberusoftware`](https://www.facebook.com/liberusoftware) page or the current brand asset library.

### Asset preparation

- Confirm Liberu owns or is licensed to reuse the image outside Facebook.
- Crop a repository cover to a wide `4:1` ratio, preferably `1280 × 320` pixels.
- Keep the important subject/logo inside the central safe area so it renders well on narrow screens.
- Export as optimized WebP, PNG, or JPEG; target less than 400 KB without visible degradation.
- Store the final file in `.github/assets/readme-cover.webp` rather than hotlinking Facebook.
- Use lowercase, stable filenames; update the file in place when branding changes.
- A logo-only repository may use a transparent image around `240 × 240` pixels instead of a cover.
- Never place essential title text only inside the image.

```markdown
<p align="center">
  <a href="https://liberusoftware.com">
    <img src=".github/assets/readme-cover.webp"
         alt="Liberu Software — open-source Laravel products and services"
         width="1280">
  </a>
</p>
```

Use meaningful alternative text. Do not use animated banners, auto-playing media, or a different visual style in every repository.

## 6. Badge standard

Badges must be useful, accurate, linked to their source, and kept to two compact rows. Remove badges that are stale, redundant, unavailable, or unrelated to the repository.

### 6.1 Technology badges

Show only direct, material technologies actually used by the repository. For the Laravel application family, the normal order is:

1. PHP
2. Laravel
3. Filament
4. Livewire
5. Jetstream, when installed

Versions must come from the repository's locked or declared dependencies. Do not hard-code a version that CI does not verify. Static examples:

```markdown
![PHP](https://img.shields.io/badge/PHP-8.5-777BB4?logo=php&logoColor=white)
![Laravel](https://img.shields.io/badge/Laravel-13-FF2D20?logo=laravel&logoColor=white)
![Filament](https://img.shields.io/badge/Filament-5-FDAE4B)
![Livewire](https://img.shields.io/badge/Livewire-4-FB70A9)
![Jetstream](https://img.shields.io/badge/Jetstream-enabled-6875F5)
```

Prefer an automated README/badge update workflow when dependency versions change. A module or theme must list only the frameworks it directly requires; compatibility belongs in its README table, not a misleading badge.

### 6.2 Release and coverage badges

```markdown
[![Latest release](https://img.shields.io/github/v/release/OWNER/REPOSITORY?sort=semver)](https://github.com/OWNER/REPOSITORY/releases/latest)
[![Test coverage](https://codecov.io/gh/OWNER/REPOSITORY/branch/main/graph/badge.svg)](https://codecov.io/gh/OWNER/REPOSITORY)
```

Replace `OWNER/REPOSITORY` with the exact repository path. Use the configured coverage service's official badge when Codecov is not used. Do not claim `100%` or any percentage in text unless generated from the current default-branch report.

For CSS/static themes where line coverage is not meaningful, use a linked quality badge for visual regression, accessibility, or theme tests and explain the quality evidence in the Testing section.

### 6.3 Workflow badges

Show passing state for the default branch using the exact workflow filenames:

```markdown
[![Install](https://github.com/OWNER/REPOSITORY/actions/workflows/install.yml/badge.svg?branch=main)](https://github.com/OWNER/REPOSITORY/actions/workflows/install.yml)
[![Tests](https://github.com/OWNER/REPOSITORY/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/OWNER/REPOSITORY/actions/workflows/tests.yml)
[![Docker](https://github.com/OWNER/REPOSITORY/actions/workflows/docker.yml/badge.svg?branch=main)](https://github.com/OWNER/REPOSITORY/actions/workflows/docker.yml)
```

Required workflow meaning:

| Workflow | Expected validation |
|---|---|
| `install.yml` | Clean supported installation, dependency lock, migrations, module/theme paths, and basic application boot |
| `tests.yml` | Automated tests, static analysis, formatting checks, architecture/security checks, and coverage upload |
| `docker.yml` | Reproducible image build, container boot/health, migration smoke test, and relevant vulnerability scan |

Only display a workflow badge when that workflow exists. Package-only or theme repositories may replace `docker.yml` with the relevant compatibility/build workflow.

### 6.4 Optional badges

License, Packagist version/downloads, supported PHP range, accessibility, documentation, security policy, container image, or OpenSSF-style health badges may be added when maintained. Stars, forks, chat-member counts, and decorative badges should not displace release or quality status.

## 7. Project description and aims

Use two or three short paragraphs:

1. What the project is and who it helps.
2. The problem it solves and its main outcome.
3. How it fits the Liberu ecosystem and differs from related repositories.

For an application, state whether it is usable independently and which modules it composes. For a module, state its one owned capability, required/optional dependencies, and installed `/modules` location. For a theme, state its surface, optimized hosts, compatibility/fallback expectations, and installed `/themes` location.

Avoid unqualified claims such as “best,” “complete,” “enterprise-ready,” or “secure” unless the README immediately links to evidence.

## 8. Project video

Include one current, short overview or demonstration video when available on the official [Liberu YouTube channel](https://www.youtube.com/@liberusoftware). Store the video ID as the only repository-specific value:

```markdown
## See it in action

[![Watch the Liberu PROJECT_NAME overview](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID)
```

If `maxresdefault.jpg` is unavailable, use `hqdefault.jpg`. The thumbnail must link to the corresponding video, use descriptive alternative text, and not imply a video exists before it is published. Prefer a 16:9 thumbnail and place this section before the detailed feature list.

## 9. Features

List the most important user/developer outcomes, not every class or database table.

- Use 6–12 concise bullets grouped under two or three subheadings when necessary.
- Start with the project’s differentiating capability.
- Link advanced features to their documentation.
- Mark optional, experimental, provider-dependent, or planned behavior clearly.
- Do not duplicate entire feature scopes from this repository or issue trackers.
- Keep versions and feature claims synchronized with released code.

Example:

```markdown
## Features

- Modular Composer packages installed into `/modules` with explicit lifecycle and dependencies.
- Filament administration and Livewire application surfaces with policy-based access.
- Single-tenant or multi-tenant composition using shared Liberu foundation contracts.
- Theme packages installed into `/themes` with inheritance and safe fallback.
- Reproducible local, Docker, and CI installation paths.
```

## 10. Requirements and quick start

Keep the default path copy-and-pasteable and tested by `install.yml`.

````markdown
## Requirements

- PHP 8.5
- Composer 2
- Node.js LTS and npm
- A supported database

## Quick start

```bash
git clone https://github.com/OWNER/REPOSITORY.git
cd REPOSITORY
composer install
cp .env.example .env
php artisan key:generate
php artisan migrate
npm ci
npm run build
php artisan serve
```
````

Adapt commands to the repository; do not publish steps CI has not exercised. Explain whether seeding creates example data. Link separate guides for Docker, Kubernetes, production deployment, graphical installers, upgrades, modules, and themes instead of embedding every path in the root README.

Module/package READMEs replace cloning with the exact Composer command and show discovery/enablement. Theme READMEs show Composer installation, selection, asset build, optimized hosts, and fallback behavior.

## 11. Architecture and documentation

Summarize architecture in no more than one short paragraph or small diagram, then link the authoritative documents:

```markdown
## Documentation

- [Installation](docs/INSTALLATION.md)
- [Configuration](docs/CONFIGURATION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Module development](docs/MODULE_DEVELOPMENT.md)
- [Theme development](docs/THEME_DEVELOPMENT.md)
- [Testing](docs/TESTING.md)
- [Deployment](docs/DEPLOYMENT.md)
- [Upgrade guide](UPGRADE.md)
- [Changelog](CHANGELOG.md)
```

Include only files that exist. Architecture text must agree with `MODULES.md` and `THEMES.md`; remove legacy module paths or installation approaches when superseded.

## 12. Related Liberu projects

Applications should include a curated table of the primary ecosystem. Modules and themes may show only directly related projects.

```markdown
## Liberu ecosystem

| Project | Repository | Purpose |
|---|---|---|
| Boilerplate | [liberusoftware/boilerplate-laravel](https://github.com/liberusoftware/boilerplate-laravel) | Shared Laravel application foundation and reference composition |
| CMS | [liberu-cms/cms-laravel](https://github.com/liberu-cms/cms-laravel) | Structured content, publishing, media, multisite, and headless delivery |
| CRM | [liberu-crm/crm-laravel](https://github.com/liberu-crm/crm-laravel) | Customer data, sales, marketing, service, and customer success |
| Billing | [liberu-billing/billing-laravel](https://github.com/liberu-billing/billing-laravel) | Products, subscriptions, invoicing, payments, and provisioning |
| Accounting | [liberu-accounting/accounting-laravel](https://github.com/liberu-accounting/accounting-laravel) | Ledgers, banking, tax, expenses, close, and financial reporting |
| Ecommerce | [liberu-ecommerce/ecommerce-laravel](https://github.com/liberu-ecommerce/ecommerce-laravel) | Catalog, checkout, orders, fulfillment, returns, B2B, and omnichannel commerce |
| Control Panel | [liberu-control-panel/control-panel-laravel](https://github.com/liberu-control-panel/control-panel-laravel) | Hosting, infrastructure, DNS, mail, databases, backups, and security operations |
| Automation | [liberu-automation/automation-laravel](https://github.com/liberu-automation/automation-laravel) | Governed workflows, provider-neutral AI, approvals, and connectors |
```

Descriptions should be one sentence, factual, and updated centrally when names or ownership change. Avoid listing every experimental repository.

## 13. Security and support

Every README must tell users not to disclose vulnerabilities in public issues:

```markdown
## Security

Please do not report security vulnerabilities through public GitHub issues.
Follow our [security policy](SECURITY.md) for private reporting and supported versions.
```

Link product support, discussions, documentation, or issue templates separately. Do not promise response times that are not governed by a published support policy.

## 14. License

Include a plain-language summary followed by the authoritative link:

```markdown
## License

This project is open-source software. You may use, modify, and distribute it
under the terms described in [LICENSE.md](LICENSE.md).

The linked license text is authoritative; this summary is not legal advice.
```

Use the exact filename and SPDX license name used by the repository. Never copy an incompatible license summary across repositories. Themes must also document third-party font, image, icon, video, and template licenses.

## 15. Feedback and contributions

Make the invitation specific and useful:

```markdown
## Feedback and contributing

Feedback and contributions are welcome. You can help by reporting reproducible
bugs, proposing focused enhancements, improving documentation or translations,
and submitting tested code changes.

Before contributing, please read [CONTRIBUTING.md](CONTRIBUTING.md) and our
[Code of Conduct](CODE_OF_CONDUCT.md). Search existing issues first, then use
the appropriate issue template. Pull requests should explain the problem and
approach, remain focused, include or update tests, pass the required workflows,
and document user-visible or breaking changes.

For support questions, use [GitHub Discussions](../../discussions) when enabled.
Security concerns must follow [SECURITY.md](SECURITY.md), not a public issue.
```

Repositories must provide the linked governance files before using this block. Adapt the support route when Discussions is disabled.

## 16. Contributors graph

End the README by recognizing contributors. Use a linked image with an accessible fallback:

```markdown
## Contributors

Thank you to everyone who helps improve Liberu.

<a href="https://github.com/OWNER/REPOSITORY/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OWNER/REPOSITORY"
       alt="Contributors to OWNER/REPOSITORY">
</a>

[View the full contributors graph](https://github.com/OWNER/REPOSITORY/graphs/contributors).
```

`contrib.rocks` is optional third-party rendering. Repositories with privacy, reliability, or supply-chain concerns may use a generated local contributors image or only GitHub’s contributors graph link. Do not manually curate contributor names in a way that omits eligible contributors.

## 17. Repository-type adjustments

| Repository type | Required emphasis |
|---|---|
| Main application | User outcomes, screenshots/video, install paths, composed modules, operations, and deployment docs |
| Module | One capability, Composer command, `/modules` path, contracts, dependencies, permissions, migrations, events, compatibility, tests, and coverage |
| Theme | Visual preview, Composer command, `/themes` path, optimized/tested hosts, supported modules, build, assets/licenses, accessibility, visual tests, and fallbacks |
| Contract package | Public interfaces/value types, supported implementations, versioning, examples, and contract tests |
| Provider adapter | Provider prerequisites, credentials, capabilities, sandbox, webhooks, rate limits, reconciliation, security, and core contract dependency |
| Distribution | Included packages, version policy, installation, exclusions, and links to package documentation; no duplicated feature manuals |

## 18. Maintenance and validation

Treat README accuracy as a release requirement.

- Assign a maintainer/owner for each README.
- Review links, versions, badges, screenshots, video, commands, features, compatibility, and project table on every release.
- CI should lint Markdown, verify internal links and referenced files, check badge workflow paths, and test every published quick-start command where practical.
- Dependency-update automation should flag technology badges and compatibility tables for review.
- Remove claims for removed or disabled features immediately.
- Keep the opening section concise; move detail into `/docs` before the README becomes a full manual.
- Use sentence case, consistent Liberu terminology, UK English unless product policy states otherwise, and accessible descriptive link text.

## 19. Definition of done

A repository README is complete when:

- the project name, purpose, maturity, Liberu links, and approved visual identity are clear;
- technology, release, coverage, and workflow badges are accurate and linked;
- a current official video is linked through an accessible thumbnail when available;
- aims, released features, requirements, and the tested quick-start path are concise;
- architecture and documentation links are accurate and do not preserve superseded approaches;
- the related-project table reflects the project’s actual ecosystem position;
- security, license, feedback, contribution, conduct, and support routes exist and are linked;
- contributors are recognized through the GitHub graph or an approved equivalent;
- Markdown/link validation and the repository's required workflows pass.
