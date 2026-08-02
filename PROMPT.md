# Repository refactoring prompt

```text
/goal

Refactor the repository into a complete Liberu Laravel application based on `liberusoftware/boilerplate-laravel`.

Work on a new branch named `development`. Create the branch first, then replace its contents with a complete copy of `liberusoftware/boilerplate-laravel`. Preserve the repository history where practical, but do not modify `main` unless explicitly required.

Follow these documentation standards from github.com/liberusoftware/documentation :

- `MODULES.md`
- `THEMES.md`
- `TENANCY.md`
- `JETSTREAM.md`
- `SOCIALSTREAM.md`
- `TESTING.md`
- `CI.md`
- `deployment/README.md`
- `API.md`
- `POLICY.md`
- `TEAMS.md`
- `SETTINGS.md`

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
- Implement the API, Filament, and Livewire foundations.
- Preserve Laravel, PHP, PSR, and framework best practices.
- Add or update configuration, migrations, seeders, factories, routes, resources, components, services, and tests as required.
- Ensure all generated code follows the existing repository conventions.

## Goal 2: Implement every documented module

Treat this as a repeatable loop. For every module directory listed under each relevant application directory in:

- `api/`
- `livewire/`
- `filament/`

Implement the corresponding module completely.

For each module:

1. Read the relevant feature, API, Filament, Livewire, tenancy, policy, teams, settings, testing, CI, and deployment documentation.
2. Implement the required domain logic, models, migrations, services, actions, validation, authorization, policies, routes, API resources, events, jobs, notifications, and configuration.
3. Implement the matching API presentation module.
4. Implement the matching Filament presentation module.
5. Implement the matching Livewire presentation module.
6. Implement or update the corresponding theme integration where required.
7. Add factories, seeders, fixtures, tests, documentation links, and OpenAPI coverage.
8. Verify tenant isolation, team authorization, policy enforcement, encrypted settings, validation, queues, events, and failure handling.
9. Do not duplicate existing functionality. If multiple modules provide overlapping behavior, unify them into one coherent, reusable implementation.
10. Keep public contracts stable unless the documentation explicitly requires a breaking change.
11. If exact implementation instructions cause breakage, make the smallest well-designed correction, document the reason, and continue.

Repeat this loop until every documented module under the relevant application directories has been implemented and verified.

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
- Themes are generated and integrated.
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
