# Publish and adopt module releases

This runbook connects a canonical module repository to Packagist/Composer or npm and then to each consuming application. Use it with [repository ownership and local copies](MODULE-REPOSITORIES.md), [Composer](COMPOSER.md), [npm](NPM.md), and [security audits](SECURITY-AUDITS.md). Examples are templates; replace identities and versions before use. This documentation update does not register accounts, submit packages or publish artifacts.

## Establish the release owner

Record the canonical repository, package identity, registry, visibility, maintainers, supported runtime matrix and consumers. Confirm the organization owns the intended vendor/scope. Avoid creating a second name for an existing shared capability; consult the [shared-module guide](../architecture/SHARED-MODULES.md). Independent modules can have independent versions; a single application release need not increment them all.

Keep the package manifest at its release repository root. A split repository must have a documented mapping from application/monorepo commit to package commit and tag. Identify which repository accepts fixes; generated mirrors should direct contributors to that owner.

## Prepare the release candidate

1. Review source and dependency changes, public contracts, exported types, provider registration, permissions and migration effects. Pick a version matching the compatibility impact, with prerelease status where appropriate.
2. Update changelog, supported versions, upgrade/recovery notes, license, README installation instructions and security contact. Where the actual package requires matching explicit manifest versions, update them together with the tag.
3. Run the package's declared checks on supported runtime/dependency combinations and integration tests in affected consumers. A package passing alone does not verify the host's custom installer or framework adapter.
4. Inspect the exact release artifact for missing classes/assets/types and unintended credentials, fixtures, environment files or private data. Use an allowlist where practical; check contents, not only ignore rules.
5. Complete the [audit record](SECURITY-AUDITS.md), resolve blockers, and record any time-limited accepted risk with an owner. Keep sensitive findings private until disclosure is coordinated.
6. Release the exact reviewed commit through the authorized workflow. Keep existing tags immutable. Record artifact identity, version, commit, checks and publication result for later consumer verification.

Do not put application environment credentials, account tokens or release secrets in either repository. A publishing job needs registry permissions only for the package it owns; build/test jobs should not receive those credentials.

## Register a Composer package with Packagist

Composer resolves and installs dependencies. Packagist registers repository metadata and versions; there is no `composer publish` command for uploading a PHP library.

For first registration, confirm a public canonical repository has a valid root `composer.json` with its intended package identity. Sign in to the appropriate Packagist maintainer account, use the [package submission form](https://packagist.org/packages/submit) to submit the repository URL, inspect the resulting entry, and configure the documented repository integration. Confirm subsequent tags appear on the package page. Follow [Packagist's submission and update instructions](https://packagist.org/about).

Use a private Composer repository or authenticated VCS for private packages; do not submit private source to public Packagist. Declare required repositories in the consuming application's root configuration because dependency packages cannot supply the root's repository policy. See [Composer repository behavior](https://getcomposer.org/doc/05-repositories.md).

### Release and verify PHP versions

From the canonical package checkout, run:

```bash
composer validate --strict
```

Run its declared tests/static analysis and the relevant [dependency audits](SECURITY-AUDITS.md). If the established release pipeline creates version tags, let it do so. Otherwise the maintainer creates and pushes the reviewed version tag through repository policy. Do not move an indexed tag to repair a defect.

After indexing, from a disposable compatible consumer configured with the required installer:

```bash
composer show vendor/example 1.4.3 --all
composer require vendor/example:1.4.3 --with-all-dependencies --dry-run
composer require vendor/example:1.4.3 --with-all-dependencies
composer show vendor/example
composer check-platform-reqs
```

Use the actual name and version. Review the resolved source/dist reference and install destination and verify autoloading, providers, assets and migrations. Preserve the host's approved plugin allowlist; do not enable every Composer plugin to get an install to pass. Then update each application's intended version range and lockfile through review, with tracked module files where its policy requires them.

### Diagnose Packagist problems

| Symptom | Checks before retrying |
| --- | --- |
| Submission rejected | Repository access, root manifest, vendor ownership, valid package name and license |
| Tag not visible | Tag pushed to canonical repository, supported version syntax, webhook/update status, manifest at the tagged commit |
| Visible version not installable | PHP/extensions/framework constraints, stability, root repository priority, private registry credentials |
| Wrong code installs | Canonical URL, tag/source commit, competing root path/VCS repositories and package identity collision |

Treat registry availability and indexing as separate from a successful Git push. Inspect errors without printing authentication configuration. Do not disable TLS, platform checks or advisory blocking to present a release as valid.

## Register and publish an npm package

npm publishes package tarballs; pushing a Git tag alone does not publish one. Confirm the target registry with `npm config get registry` and verify scope/access ownership in the registry. Use the authorized account or configured CI publisher. Keep application/workspace roots `private: true`; only intended libraries should be publishable.

The package needs its actual name/version, license, repository URL, public exports, runtime/peer dependencies, declarations when relevant and an explicit set of distributed files. Build before packing if exports point into `dist/`; confirm both package and consumer use compatible React/framework peers. See [npm public scoped publishing](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages/).

From the package checkout, run its declared checks and build, then:

```bash
npm pack --dry-run
npm pack
```

Inspect the tarball and install its exact path into a disposable consumer. Verify exports, declarations, styles and runtime behavior. Account for lifecycle scripts that can change the packed output; the approved publisher must use the tested release process. Review [npm pack](https://docs.npmjs.com/cli/v11/commands/npm-pack).

### Authentication and release channels

Prefer [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) when the registry supports the repository's CI environment. It uses OIDC instead of a long-lived publishing token. Match the configured repository/workflow identity and give only the publishing job `id-token: write`. Verify current supported runners and CLI/runtime requirements before adopting the workflow. For other workflows, use the registry's supported maintainer authentication, with least privilege, two-factor protection and CI secret storage.

For an authorized public scoped package, the release command is:

```bash
npm publish --access public
```

For a prerelease, set an actual prerelease version first and use:

```bash
npm publish --access public --tag next
```

Tags such as `next` and `latest` are consumer channels, distinct from Git tags. Verify the intended channel after publishing; do not promote a prerelease to the stable channel accidentally. Automatic provenance depends on registry and CI conditions; inspect the published evidence rather than assuming every workflow creates it.

### Verify npm and update consumers

Replace the example identity and version:

```bash
npm view @example/module-example@1.4.3 version dist.integrity dist.tarball
npm view @example/module-example dist-tags
npm install @example/module-example@1.4.3 --save-exact
npm ls @example/module-example
```

Run those install checks in a disposable consumer before changing production applications. Verify registry signatures/provenance where supported, as described in the [audit guide](SECURITY-AUDITS.md). A source link or provenance statement establishes origin information, not freedom from defects. Review the consumer's manifest/lockfile and run its application checks before rollout.

A published name/version cannot be overwritten. Correct defects with a new version. Decide deliberately whether deprecation or a channel adjustment is needed; follow [npm deprecation guidance](https://docs.npmjs.com/deprecating-and-undeprecating-packages-or-package-versions/) and its registry rules rather than relying on unpublish as rollback.

## Close the release across projects

Maintain a consumer record with package version, source commit, application upgrade PR, deployed environment/version, migration status, audit result and owner. A package release is not proof all applications adopted it. Track pending upgrades and unsupported consumers explicitly.

For a security fix, coordinate the [private response process](SECURITY-ISSUES.md), publish accurate affected/fixed ranges, and test the actual package artifact. Retest affected consumers and remove temporary local patches after adopting the fixed release. Update [source and documentation references](DOCUMENTATION-MAINTENANCE.md) without removing product capabilities that live outside package folders.
