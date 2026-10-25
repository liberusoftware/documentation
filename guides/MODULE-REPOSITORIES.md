# Maintain module repositories and project-local copies

Use this guide when one module has its own Git repository and also appears inside an application checkout. Read the [Composer](COMPOSER.md) or [npm](NPM.md) guide for package-manager commands, the [publishing runbook](PACKAGE-PUBLISHING.md) for releases, and the [security audit guide](SECURITY-AUDITS.md) for verification. All package names, versions and filesystem paths below are examples to replace with verified values.

## Decide which copy owns changes

A directory named `modules/example` does not establish ownership. Record the package manifest name, canonical Git URL, install path, current release/source commit, supported consumers, and synchronization method before changing it. Use [source inventories](../architecture/SOURCE-INVENTORY.md) and [shared-module adoption profiles](../architecture/shared-adoption/README.md) to distinguish aliases and divergent implementations.

| Layout | Durable source of changes | What the application records |
| --- | --- | --- |
| Application-owned module, not independently released | Application repository | Module source and application tests |
| Independently released package installed in `vendor/`, `node_modules/` or `modules/` | Package repository | Dependency constraint, application lockfile, integration changes; tracked installed files if required by the host policy |
| Sibling checkout linked through Composer path or npm file/workspace settings | Package checkout | Development override only when intentionally shared; restore registry resolution for release |
| Git submodule | Child repository | `.gitmodules` and the exact child commit |
| Subtree or automated split | The single owner defined by the split policy | Imported/split commits and an auditable synchronization record |

Choose one authoritative write direction. A copied directory must not quietly become a second upstream. Never run Composer, subtree synchronization and a Git submodule against the same destination. Nested `.git` directories do not make ordinary tracked files independent automatically.

Ecommerce has application-owned capabilities in controllers, routes, models, services and views outside `modules/`. Retain those capabilities and their documentation when extracting or updating packages; consult its [application capability map](../projects/ecommerce/SOURCE-APPLICATION.md). Package manifests alone cannot establish the full product boundary.

## Record ownership in the module README

Keep this information beside each package, using the real values:

```yaml
package: vendor/example
canonical_repository: https://github.com/example/module-example
application_path: modules/example
source_model: independent-package
update_method: composer-release
installed_version: 1.4.2
source_commit: <full-reviewed-commit-sha>
owner: <maintaining-team>
consumers:
  - <application-repository>
local_patch: none
```

This is a documentation specimen, not a configuration file consumed by Liberu tooling. For npm, record its scoped name and registry too. Record any temporary patch's upstream issue, patch file, base version, expiration and verification. A release number without a source identity is insufficient to explain a locally modified copy.

## Set up sibling checkouts

Keep independent repositories alongside the application so their histories remain easy to inspect:

```text
workspace/
  application/        # application Git root
  module-example/     # independent package Git root
```

From the workspace parent, clone the verified package URL into `module-example`. Before pulling or changing branches, inspect both worktrees:

```bash
git -C application status --short
git -C module-example status --short
git -C module-example remote -v
git -C module-example fetch origin
```

Preserve local work before integrating upstream. Review commits and use the repository's normal merge/rebase policy; do not run a reset or forced cleanup to make synchronization appear successful. Create the module feature branch in its own checkout and keep application integration changes on an application branch.

### Composer local integration

Add a narrowly scoped path repository to the application's root `composer.json`, preserving its other repositories and approved installer configuration:

```json
{
  "repositories": [
    {
      "type": "path",
      "url": "../module-example",
      "options": { "symlink": true }
    }
  ]
}
```

The package identity and development version must satisfy the application's constraint. Use an explicit development constraint or branch alias when necessary; do not claim a development checkout is a published stable release. Check repository priority and any existing `modules/*` path repository that can shadow the intended package. Path repositories support symlink or mirror installs; inspect Composer's installation output to confirm which was used. See [Composer repositories](https://getcomposer.org/doc/05-repositories.md#path).

From the application root:

```bash
composer update vendor/example --with-all-dependencies --dry-run
composer update vendor/example --with-all-dependencies
composer show vendor/example
```

The dependency flag can change related packages; review the complete lockfile diff. In a symlink install, edits affect the sibling package checkout. In a mirror install, edits to the sibling are not automatically copied into the application. After preserving any installed-copy changes, use the package manager's reinstall workflow and verify the resulting files. Inspect the custom installer destination rather than assuming `vendor/`.

Keep local development configuration and lockfile changes out of a release PR unless the team deliberately supports that layout. Do not blanket-ignore the application manifest or lockfile: that hides real integration upgrades too. Track a reviewed diff of local overrides and restore only those changes when returning to registry packages.

### npm local integration

Use the repository's existing package manager and workspace design. For an independent sibling repository, a consuming manifest can temporarily declare:

```json
{
  "dependencies": {
    "@example/module-example": "file:../module-example"
  }
}
```

Install the sibling module's own development dependencies using its declared package manager, then run the consumer's installation step and the module's declared build/watch scripts. Check whether exports point at built files and whether the framework follows/transpiles linked code. Workspace links require declared workspaces; a sibling checkout is not automatically a workspace. Test React peer dependencies to avoid loading two runtimes. Local-path handling is documented in [npm package metadata](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/#local-paths).

Use `npm pack` in the module directory, then install the resulting exact tarball path in a disposable consumer. This tests distributed files and exports without relying on the development link. Record and remove only the temporary file/link resolution when preparing the application release; retain real feature changes.

## Fix a module discovered inside an application

1. Inspect the application diff, dependency metadata and install provenance. Determine whether the directory is authoritative application code or a copy of an independent package.
2. Preserve the changed files and a diff outside the installer destination before running an update. A reinstall can replace local edits.
3. Reproduce the defect in the canonical package's test environment. Port only the intended change and its meaningful regression test to that repository; do not copy application credentials, caches or unrelated customizations.
4. Integrate the package branch locally with the application and test the failing user journey. Include affected tenants, permissions, asynchronous jobs and data transitions where applicable.
5. Review, merge and release the package using the [publishing runbook](PACKAGE-PUBLISHING.md). Application Git commits do not publish that package.
6. Restore registry resolution in the application, update to the fixed release, review its lockfile and any tracked installed files, and repeat integration checks in a clean checkout.
7. Commit the application upgrade separately with the package release, source commit, migration notes and checks linked in the change description. Notify other consumers through the established release process.

For an urgent unreleased fix, use an explicitly reviewed immutable VCS commit or a documented patch mechanism supported by that repository. Record its scope, source and replacement deadline. A mutable branch or an unexplained installed-tree edit is unsuitable evidence of a reproducible production release.

## Return from local development to a registry release

After the independent package release is available, remove only its temporary path/file override and restore the application's intended registry constraint. Preserve unrelated repository entries and integration changes. In a Composer host that intentionally resolves its tracked modules through `modules/*`, follow that host's synchronization process and verify against an independent clean registry installation; removing all local repositories could break other modules.

For a consumer that should resolve the released Composer package, after restoring its root configuration:

```bash
composer update vendor/example --with-all-dependencies --dry-run
composer update vendor/example --with-all-dependencies
composer show vendor/example
```

Confirm the lockfile no longer resolves this package to the developer's sibling path. Verify the reviewed release version/source reference, run the application checks, and commit the intended manifest/lockfile plus tracked installed-tree changes required by the host. A symlink or local mirrored path reference left in a lockfile may fail on CI or another developer's machine.

For an npm consumer, replace the temporary `file:` dependency with the intended registry version, for example:

```bash
npm install @example/module-example@1.4.3 --save-exact
npm ls @example/module-example
```

Review the manifest and lockfile to confirm that this dependency uses the expected registry artifact rather than a sibling link. An existing workspace with the same identity can still affect local resolution; verify the registry artifact in a separate clean consumer as well. After committing the intended upgrade, check installation from the committed lockfile in a disposable application clone. Do not delete all lockfiles or local working changes to force the switch.

## Maintain tracked installed copies

Some Liberu applications commit Composer-installed module trees. Follow the [tracked-module policy](../architecture/MODULES.md#62-tracked-modules-policy); do not delete those directories or add a blanket ignore rule as part of a package upgrade.

Before accepting an upgrade, compare the tracked tree against its locked upstream version. Classify differences as upstream fixes, application extension points, generated artifacts or unexplained drift. Move reusable fixes upstream and keep product customization behind documented interfaces. If identical package names have divergent implementations, consult the [shared comparison](../architecture/SHARED-MODULE-COMPARISON.md) before selecting a common version.

Verify in a disposable application clone with the intended runtime and installer that the committed manifest/lockfile recreate the expected tree. Check that a root path repository is not simply copying the tracked local files back into place: that would prove local consistency, not agreement with the published package. Compare against a clean independent install of the exact registry version when the host intentionally resolves local paths. Record the comparison scope and excluded generated files. Do not use `composer status` alone as proof that every custom installed tree matches its release.

## Git submodules and subtree imports

Only use these approaches when the repository has chosen them. A submodule stores a child commit; initialize recorded children after a clone with:

```bash
git submodule update --init --recursive
git submodule status
```

Make child changes on a named branch, publish the child commit first, and then commit the reviewed parent pointer. A default submodule checkout may be detached. Do not use `git submodule update --remote` as a reproducible deployment step. See the [Git submodule reference](https://git-scm.com/docs/git-submodule).

For a subtree or split pipeline, document prefix, source remote, target branch, release/tag mapping, synchronization direction and who resolves conflicts. Split package repositories must expose their manifest at the package root. Keep tags associated with the intended split commit. Before import/export, test in an isolated clone and compare the intended subtree content. Never overwrite either side blindly or publish every nested module from an application tag without its explicit release mapping.

## Routine updates and completion criteria

Fetch/review application and package changes independently. After an application pull, use `composer install` or `npm ci` to reproduce a changed lockfile; do not perform a broad dependency update just to start development. Select upgrades using release notes, compatibility constraints and [audit findings](SECURITY-AUDITS.md).

A module change is complete when the canonical fix is reviewed, the package artifact is verified, the application resolves that artifact without a developer-only path, tests cover the affected journey, and the version/lockfile/tracked-tree changes agree. Update source mappings and user guidance through [documentation maintenance](DOCUMENTATION-MAINTENANCE.md). Keep database recovery and package rollback separate: restoring an old dependency lockfile does not undo a destructive migration.
