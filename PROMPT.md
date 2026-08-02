# Liberu API, Filament, and Livewire implementation prompt

```text
/goal

Refactor the repository into a complete Liberu Laravel application based on `liberusoftware/boilerplate-laravel`. Generate implementation code only for API, Filament, and Livewire scopes.

Work on a new branch named `development`. Create the branch first, then replace its contents with a complete copy of `liberusoftware/boilerplate-laravel`. Preserve the repository history where practical, but do not modify `main` unless explicitly required.

Follow these architecture decisions and implementation standards from github.com/liberusoftware/documentation :

- `architecture/README.md` and `architecture/MODULES.md`
- `architecture/API.md`
- `architecture/TENANCY.md`, `architecture/TEAMS.md`, `architecture/POLICY.md`, and `architecture/SETTINGS.md`
- `architecture/JETSTREAM.md` and `architecture/SOCIALSTREAM.md`
- `architecture/REPOSITORIES.md` and `architecture/SECURITY.md`
- `standards/README.md` and `standards/GUIDELINES.md`
- `standards/PHP.md`, `standards/PSR.md`, `standards/PINT.md`, `standards/LARAVEL.md`, and `standards/DATABASE.md`
- `standards/THEMES.md`, `standards/TESTING.md`, `standards/CI.md`, `standards/DOCUMENTATION.md`, and `standards/CONTRIBUTING.md`
- `standards/FILAMENT.md` and `standards/LIVEWIRE.md`
- `standards/JOBS.md`, `standards/QUEUES.md`, `standards/SERVICES.md`, `standards/CONTROLLERS.md`, `standards/MODELS.md`, `standards/VIEWS.md`, `standards/BLADE.md`, `standards/CONCERNS.md`, `standards/CONTRACTS.md`, `standards/CLASSES.md`, `standards/OBJECT-ORIENTED-PROGRAMMING.md`, `standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md`, and `standards/TRANSLATIONS.md`
- `technologies/README.md`, `technologies/PHP.md`, `technologies/DATABASE.md`, `technologies/JAVASCRIPT.md`, and `technologies/TYPESCRIPT.md`
- `deployment/README.md`

The complete standards index is [standards/README.md](standards/README.md). It is authoritative for coding, design, testing, documentation, delivery, persistence, jobs, queues, services, controllers, models, views, Blade, concerns, contracts, classes, object-oriented programming, domain-driven design, and translations. Read every relevant standard before implementation and do not bypass a standard because it is not repeated in this prompt.

Read the frontend standards (`standards/REACT.md`, `standards/INERTIA.md`, `standards/VUE.md`, and `standards/NUXT.md`) when they define an integration boundary or compatibility constraint, but do not generate code for those technologies.

The portfolio composition scope is [projects/LIBERU.md](projects/LIBERU.md). New Liberu-only cross-product modules are indexed under `projects/liberu/`; do not duplicate capabilities already owned by another `projects/*` scope.

If the documentation conflicts with the existing implementation, follow the documentation. If this causes breakage, diagnose and fix the breakage while preserving the documented design principles. Do not silently omit or simplify required functionality.

## Goal 1: Recreate the application foundation

Implement all existing boilerplate logic, code, configuration, dependencies, service providers, commands, policies, authentication, teams, tenancy, settings, themes, tests, CI, deployment configuration, and supporting infrastructure required by the documentation.

At this stage:

- Install and correctly load the Liberu custom Composer plugin.
- Implement Jetstream authentication and team functionality.
- Implement Socialstream integrations.
- Implement tenancy according to `TENANCY.md`.
- Implement policies and permissions according to `POLICY.md`.
- Use Jetstream teams for team membership and context; do not introduce Spatie teams or roles where the documentation prohibits them.
- Implement the settings architecture, including encrypted secrets and tenant-aware settings.
- Generate and implement the required themes according to `THEMES.md`.
- Implement the API, Filament, and Livewire foundations according to their standards.
- Do not generate React, Vue, Nuxt, Inertia, frontend JavaScript, or frontend TypeScript implementation code. Mention those technologies only when documenting boundaries or preventing accidental duplication.
- Preserve Laravel, PHP, PSR, and framework best practices.
- Add or update configuration, migrations, seeders, factories, routes, resources, components, services, and tests as required.
- Ensure all generated code follows the existing repository conventions.

## Goal 2: Implement every documented API, Filament, and Livewire module

Treat this as a repeatable loop. Use the root implementation indexes below to discover the supported scopes:

- [`modules/api/README.md`](modules/api/README.md)
- [`modules/filament/README.md`](modules/filament/README.md)
- [`modules/livewire/README.md`](modules/livewire/README.md)

The implementation documentation for each product remains under `projects/<project>/api/`, `projects/<project>/filament/`, and `projects/<project>/livewire/`. Do not rename files or directories under `projects/`. Do not use the React, Vue, or Nuxt indexes as implementation targets in this prompt.

Implement the corresponding module completely.

For each module:

1. Read the relevant feature, API, Filament, Livewire, tenancy, policy, teams, settings, database, testing, CI, deployment, and all applicable standards documentation.
2. Implement the required domain logic, models, migrations, services, actions, validation, authorization, policies, routes, API resources, events, jobs, notifications, and configuration.
3. Implement the API contract and presentation module where the documented scope requires it.
4. Implement the matching Filament presentation module where the documented scope requires it.
5. Implement the matching Livewire presentation module where the documented scope requires it.
6. Implement or update the corresponding Blade/theme integration where required by `standards/THEMES.md`.
7. Add migrations, factories, seeders, fixtures, tests, documentation links, and OpenAPI coverage.
8. Verify tenant isolation, team authorization, policy enforcement, encrypted settings, validation, queues, events, and failure handling.
9. Do not duplicate existing functionality. If multiple modules provide overlapping behavior, unify them into one coherent, reusable implementation.
10. Keep public contracts stable unless the documentation explicitly requires a breaking change.
11. If exact implementation instructions cause breakage, make the smallest well-designed correction, document the reason, and continue.

Repeat this loop until every documented API, Filament, and Livewire module has been implemented and verified. For the new cross-product Liberu features, process `projects/liberu/features/`, `projects/liberu/api/`, `projects/liberu/filament/`, and `projects/liberu/livewire/`. Implement only the new Liberu capabilities documented there; do not copy or reimplement existing product modules.

## Goal 3: Repository and package publishing

After implementation is complete:

- Use the GitHub CLI (`gh`) to create the required public repositories under the `liberusoftware` organization.
- Configure repository descriptions, visibility, default branches, topics, branch protection, issue settings, and required CI checks.
- Ensure each package has valid Composer metadata and repository links.
- Ensure package names, namespaces, autoloading, service providers, and dependencies are correct.
- Publish the packages to Packagist under the appropriate Liberu vendor namespace.
- Confirm the packages are discoverable and installable from Packagist.
- Do not publish secrets, private configuration, local paths, generated credentials, or environment files.

## Goal 4: Final verification and maintenance scripts

As the final implementation step, create or update scripts that:

- Update all modules and themes consistently.
- Run formatting and linting.
- Run static analysis and architecture checks.
- Validate Composer and npm dependencies.
- Build frontend assets.
- Validate API and OpenAPI contracts.
- Run unit, feature, integration, browser, and presentation tests.
- Verify migrations, seeders, factories, queues, tenancy, teams, policies, settings, and authorization.
- Build and scan deployment artifacts.
- Validate Docker, Docker Compose, Kubernetes, NGINX, Apache, Supervisor, Reverb, Horizon, and Telescope configuration where applicable.
- Verify documentation links and generated indexes.
- Produce useful CI artifacts and failure output.

The final verification must require 100% coverage for the configured owned executable release scope, with documented exclusions limited to vendor code, generated files, static assets, and configuration-only paths. A failed coverage gate blocks completion. Do not lower thresholds to make tests pass.

## CI and deployment requirements

- Every pull request must run the required validation workflows.
- Every push to `main` must run CI and may deploy staging.
- Production must not deploy directly from `main`.
- Production deployment must require a protected version tag or GitHub Release.
- The release must use the exact tested commit and artifact.
- Production requires all checks to pass, including the 100% release-scope coverage gate, security scans, deployment verification, smoke tests, and environment approval.
- Use least-privilege GitHub Actions permissions.
- Pin third-party GitHub Actions to full commit SHAs.
- Protect production secrets with GitHub Environments or the appropriate deployment secret manager.
- Configure concurrency, rollback, health checks, migration safety, and deployment observability.

## Final branch and release promotion

This is the final goal and must be completed after all implementation, testing, publishing, and verification work:

1. Ensure the completed work is committed on `development` and pushed to the remote.
2. Preserve the current `main` branch by renaming it to `old`. Keep `old` available as a historical fallback unless repository policy explicitly requires its later removal.
3. Rename `development` to `main` locally and remotely.
4. Use the GitHub CLI to set `main` as the repository default branch.
5. Confirm branch protection, required status checks, workflows, links, and release configuration now target `main`.
6. Remove the obsolete remote `development` reference only after the new `main` branch is confirmed and protected.
7. Determine the latest major version from existing Git tags and GitHub Releases. If no major version exists, use `v1.0.0`; otherwise increment the major component and reset minor and patch components to zero. For example, `v2.4.1` becomes `v3.0.0`.
8. Use the GitHub CLI to publish that new major GitHub Release from the final `main` branch, with release notes describing the completed refactor, module and theme implementation, compatibility changes, verification results, and any documented limitations.

The final repository state must have `main` as the default branch, `old` as the preserved former branch, the new major release published, and all changes committed and pushed.

## Completion criteria

The `/goal` is complete only when:

- The `development` branch exists and contains the refactored application.
- Boilerplate functionality and all documented foundations are implemented.
- API, Filament, and Livewire themes are generated and integrated where required by `standards/THEMES.md`.
- Every documented API, Livewire, and Filament module is implemented or deliberately unified with a documented reason.
- The Liberu Composer plugin is installed and loaded successfully.
- Tests, builds, static analysis, security checks, API validation, and deployment validation pass.
- The 100% release-scope coverage gate passes.
- CI workflows are operational.
- Public GitHub repositories are created under `liberusoftware`.
- Packages are correctly published or submitted to Packagist.
- Documentation indexes and links are valid.
- Changes are committed and pushed to the final `main` branch after branch promotion.
- The former `main` branch is preserved as `old`.
- The repository default branch is `main`.
- A new major GitHub Release has been published with `gh` above the previous major version.
- Provide a final report listing implemented foundations, modules, unified duplicates, generated themes, repositories, Packagist packages, verification commands, coverage results, and any remaining documented limitations.
```
