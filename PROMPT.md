# Liberu API, Filament, and Livewire implementation prompt

```text
/goal

Refactor the repository into a complete Liberu Laravel application based on a cloned copy of `liberusoftware/boilerplate-laravel`. Generate implementation code only for core, API, Filament, and Livewire modules. Do not create React, Vue, Nuxt, Inertia, React Native, Flutter, or any other separate presentation module in this run; those are later implementation phases.

Use this exact repository bootstrap and promotion order:

1. Inspect the target repository, remotes, current default branch, uncommitted changes, tags, and branch protection. Stop if the target or remote is ambiguous.
2. Clone `https://github.com/liberusoftware/boilerplate-laravel.git` into a temporary source directory at the pinned source commit/tag. Do not use a shallow clone when history, tags, or package provenance are required.
3. Create the target branch `development` from the target repository's current `main`, then import the complete Boilerplate Laravel working tree into `development` while preserving the target repository's `.git` directory, remotes, and branch metadata. Commit this as the new application foundation before implementing project modules.
4. Preserve the original target `main` remotely as `old` before any final branch promotion: verify that `old` does not point to unrelated work, then run `git push origin main:old`. Never delete or overwrite `old` without explicit authorization.
5. Implement and verify only the project-relevant core, API, Filament, and Livewire modules on `development`. Keep the original target state recoverable through `old`.
6. After implementation, tests, package publication, and release verification pass, rename the local `main` branch to `old`, rename `development` to `main`, push the new `main` with a reviewed `--force-with-lease` only when the remote `main` still contains the preserved old state, and set `main` as the GitHub default branch.
7. Remove the obsolete remote `development` only after the new `main` is visible, protected, tested, and confirmed as the default. Keep remote `old` as the historical fallback.

The clone/import must happen before branch promotion and before module implementation. Do not implement modules directly on the old branch or on the final promoted `main` branch.

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

Read the frontend standards (`standards/REACT.md`, `standards/INERTIA.md`, `standards/VUE.md`, and `standards/NUXT.md`) only when they define an integration boundary or compatibility constraint. Do not generate code, packages, routes, screens, components, clients, or presentation indexes for those technologies in this run. The same exclusion applies to React Native and Flutter.

The portfolio composition scope is [projects/LIBERU.md](projects/LIBERU.md). New Liberu-only cross-product modules are indexed under `projects/liberu/`; do not duplicate capabilities already owned by another `projects/*` scope.

If the documentation conflicts with the existing implementation, follow the documentation. If this causes breakage, diagnose and fix the breakage while preserving the documented design principles. Do not silently omit or simplify required functionality.

## Branch bootstrap and safety requirements

Use commands equivalent to the following after reviewing the actual repository state; substitute the real repository and owner and never paste credentials into shell history:

```bash
# From the target repository, before changing branches
git fetch --all --tags --prune
git status --short --branch
git branch --show-current
git ls-remote --heads origin main old development

# Clone the source foundation separately, then create/import development
git clone --branch main https://github.com/liberusoftware/boilerplate-laravel.git "${TMPDIR:-/tmp}/liberu-boilerplate"
git switch -c development
rsync -a --delete --exclude='.git' "${TMPDIR:-/tmp}/liberu-boilerplate/" ./
git add -A
git commit -m "Bootstrap application from Liberu Laravel Boilerplate"

# Preserve the old target main before final promotion
git push origin refs/heads/main:refs/heads/old
git push origin development
```

Before the final promotion, verify the remote `old` object ID matches the original `main` object ID. Then use the least destructive supported sequence:

```bash
git switch development
git branch -m main old
git branch -m development main
git fetch origin main old
git push --force-with-lease=main:$(git rev-parse origin/main) origin refs/heads/main:refs/heads/main
gh repo edit OWNER/REPOSITORY --default-branch main
# Equivalent API fallback:
gh api --method PATCH repos/OWNER/REPOSITORY -f default_branch=main
git push origin --delete development
git push origin main old
```

If `gh repo edit --default-branch` is unavailable, use the API fallback. Never force-push until `old` is present on the remote, the expected remote `main` object ID is recorded, branch protection/default-branch changes are approved, and the force-with-lease target is exact. If any command reports an unexpected branch, object ID, protection rule, or default branch, stop and report the state.

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
- Implement the shared Blade/theme integration required by the host application and `THEMES.md`, but do not create a separate theme package or any unrequested presentation package.
- Implement only the API, Filament, and Livewire foundations according to their standards, plus the framework-neutral core domain packages they consume.
- Do not generate React, Vue, Nuxt, Inertia, frontend JavaScript, frontend TypeScript, React Native, Flutter, mobile, or other presentation-module implementation code. Mention those technologies only when documenting a later boundary or preventing accidental duplication.
- Preserve Laravel, PHP, PSR, and framework best practices.
- Add or update configuration, migrations, seeders, factories, routes, resources, components, services, and tests as required.
- Ensure all generated code follows the existing repository conventions.

## Goal 2: Implement every relevant core, API, Filament, and Livewire module

Treat this as a repeatable loop. Use the root implementation indexes below to discover the supported scopes:

- [`modules/features/README.md`](modules/features/README.md) — generic domain-level feature scopes and their canonical specifications.
- [`modules/api/README.md`](modules/api/README.md)
- [`modules/filament/README.md`](modules/filament/README.md)
- [`modules/livewire/README.md`](modules/livewire/README.md)

The core implementation index is [`modules/core/README.md`](modules/core/README.md). For each selected project, the core, API, Filament, and Livewire indexes must remain one-to-one. Use the project scope and implementation guide to determine which modules are relevant; do not implement every project in the portfolio into every application.

The implementation documentation for each product remains under `projects/<project>/api/`, `projects/<project>/filament/`, and `projects/<project>/livewire/`. Do not rename files or directories under `projects/`. Do not use the React, Vue, or Nuxt indexes as implementation targets in this prompt.

Implement the corresponding module completely.

For each module:

1. Read the relevant feature, API, Filament, Livewire, tenancy, policy, teams, settings, database, testing, CI, deployment, and all applicable standards documentation.
2. Implement the framework-neutral core package and its domain actions, queries, policies, persistence, events, jobs, and tests.
3. Implement the API contract and matching API package where the documented scope requires it.
4. Implement the matching Filament presentation package where the documented scope requires it.
5. Implement the matching Livewire presentation package where the documented scope requires it.
6. Implement or update only the corresponding host Blade/theme integration where required by `standards/THEMES.md`; do not create another presentation package.
7. Add migrations, factories, seeders, fixtures, tests, documentation links, and OpenAPI coverage.
8. Verify tenant isolation, team authorization, policy enforcement, encrypted settings, validation, queues, events, and failure handling.
9. Do not duplicate existing functionality. If multiple modules provide overlapping behavior, unify them into one coherent, reusable implementation.
10. Keep public contracts stable unless the documentation explicitly requires a breaking change.
11. If exact implementation instructions cause breakage, make the smallest well-designed correction, document the reason, and continue.

Repeat this loop until every relevant documented core, API, Filament, and Livewire module has been implemented and verified. For the new cross-product Liberu features, process `projects/liberu/features/`, `projects/liberu/core/`, `projects/liberu/api/`, `projects/liberu/filament/`, and `projects/liberu/livewire/`. Implement only the new Liberu capabilities documented there; do not copy or reimplement existing product modules. Do not process Liberu React, Vue, Nuxt, React Native, or Flutter implementation indexes in this run.

## Goal 3: Repository and Composer/Packagist package publishing

After implementation is complete:

- Use the GitHub CLI (`gh`) to create the required public repositories under the `liberusoftware` organization.
- Configure repository descriptions, visibility, default branches, topics, branch protection, issue settings, and required CI checks.
- Create or configure one public GitHub repository under the `liberusoftware` organization for every independently released package, unless an existing package repository is explicitly designated as its owner.
- Ensure every created core, API, Filament, and Livewire package has valid Composer metadata, repository links, license, README, changelog, service provider, PHP/Laravel constraints, and dependency boundaries.
- Use the Composer vendor namespace `liberusoftware/` for every created package. Recommended names are `liberusoftware/module-{module}`, `liberusoftware/module-{module}-api`, `liberusoftware/module-{module}-filament`, and `liberusoftware/module-{module}-livewire`; use the exact package naming decision recorded in the module ADR.
- Ensure namespaces, PSR-4 autoloading, service providers, package discovery, migrations, config publishing, translations, routes, views, assets, and dependencies are correct and do not require application `App\\` classes.
- Tag and push a tested release for each package. Submit every created package to Packagist using the Packagist submission/API flow or configured GitHub synchronization webhook; `gh` alone does not publish a Composer package to Packagist.
- Authenticate Packagist using an environment secret or approved secret manager, never a committed token. Verify the Packagist package page, version, source URL, dist archive, dependencies, PHP constraints, and a clean `composer require liberusoftware/<package>` install.
- Add Packagist update/webhook configuration and document the package owner, release tag, support policy, deprecation policy, and upgrade notes.
- Do not submit documentation-only files, host applications, private packages, secrets, local paths, generated credentials, or environment files as Composer packages.

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

1. Ensure the completed implementation, package tags, Packagist submissions, tests, and release evidence are committed on `development` and pushed to the remote.
2. Confirm the original target `main` commit is preserved remotely as `old`; `old` is the historical fallback and must remain available.
3. Rename the local old branch to `old`, rename `development` to `main`, and push the new `main` with the exact reviewed `--force-with-lease` target described in the bootstrap section.
4. Use `gh repo edit OWNER/REPOSITORY --default-branch main`, or the documented `gh api` fallback, to set `main` as the repository default branch.
5. Confirm branch protection, required status checks, workflows, links, package/release configuration, and Packagist source URLs target `main`.
6. Remove the obsolete remote `development` reference only after the new `main` branch is confirmed and protected.
7. Determine the latest major version from existing Git tags and GitHub Releases. If no major version exists, use `v1.0.0`; otherwise increment the major component and reset minor and patch components to zero. For example, `v2.4.1` becomes `v3.0.0`.
8. Use the GitHub CLI to publish that new major GitHub Release from the final `main` branch, with release notes describing the completed refactor, core/API/Filament/Livewire package implementation, Packagist packages, compatibility changes, verification results, and documented limitations.

The final repository state must have `main` as the default branch, `old` as the preserved former branch, the new major release published, and all changes committed and pushed.

## Completion criteria

The `/goal` is complete only when:

- The `development` branch exists and contains the refactored application.
- Boilerplate functionality and all documented foundations are implemented.
- Core, API, Filament, and Livewire modules are implemented or deliberately unified with a documented reason.
- No React, Vue, Nuxt, Inertia, React Native, Flutter, or other deferred presentation module was generated.
- The Liberu Composer plugin is installed and loaded successfully.
- Tests, builds, static analysis, security checks, API validation, and deployment validation pass.
- The 100% release-scope coverage gate passes.
- CI workflows are operational.
- Public GitHub repositories are created under `liberusoftware`.
- Every created Composer package uses the `liberusoftware/` vendor namespace, is tagged, submitted to Packagist, and verified installable.
- Documentation indexes and links are valid.
- Changes are committed and pushed to the final `main` branch after branch promotion.
- The former `main` branch is preserved as `old`.
- The repository default branch is `main`.
- A new major GitHub Release has been published with `gh` above the previous major version.
- Provide a final report listing implemented foundations, modules, unified duplicates, generated themes, repositories, Packagist packages, verification commands, coverage results, and any remaining documented limitations.
```
