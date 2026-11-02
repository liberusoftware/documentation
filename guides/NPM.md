# JavaScript modules with npm

Use this guide for independently packaged React, Next.js, Vue, Nuxt, or other JavaScript modules. A PHP presentation adapter may contain JavaScript assets without being an npm package. Check for `package.json` and its exact `name` in the [source inventory](../architecture/SOURCE-INVENTORY.md) before choosing a workflow.

## Install and verify a clone

Read the root manifest's `engines`, `packageManager`, scripts, workspace settings, and lockfile. Use the repository's declared package manager; do not introduce an npm lockfile into a pnpm or Yarn project casually. Inspect install scripts before trusting a new checkout.

For a repository using npm with a committed, synchronized `package-lock.json`:

```bash
npm ci
npm run
npm ls --depth=0
```

`npm run` lists available scripts. Execute the declared build, typecheck, lint, and test commands appropriate to the change; their names vary. A project without a lockfile needs a deliberate `npm install` to generate one before `npm ci` can reproduce the installation. Application lockfiles should be reviewed and committed. See [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci).

## Develop local packages

For a monorepo, declare actual package directories in the root:

```json
{
  "private": true,
  "workspaces": ["packages/*", "apps/*"]
}
```

Each workspace needs its own manifest and unique package identity. The private root prevents accidental publication of the workspace container. Declare a dependency from the consuming workspace using a version range compatible with the local package. Running root `npm install` links configured workspaces. Use `npm run build --workspace <actual-package-name>` when the package exports compiled output. See [npm workspaces](https://docs.npmjs.com/cli/v11/using-npm/workspaces/).

For a package outside that workspace, an explicit `file:../module-example` dependency supports local integration. Review whether the framework transpiles linked source and how its watcher resolves changes. A development link is not a release verification: run `npm pack --dry-run`, create a tarball with `npm pack`, and install that tarball in a disposable consumer to exercise the files and exports users receive. See [npm pack](https://docs.npmjs.com/cli/v11/commands/npm-pack).

React libraries should declare supported React versions as peer dependencies and avoid bundling a second React runtime. Keep React UI that is shared with Inertia free of framework navigation imports. The [Next.js standard](../standards/NEXTJS.md) explains server-only exports, client boundaries, routing ownership, and authentication.

## Keep packages current while working in a project clone

Commit or otherwise preserve local work before integrating upstream changes. Update the application checkout and independent module checkouts separately. Application-owned workspace/module source changes belong to that repository. A tracked installed copy of an independently released package still has a separate canonical source: fix/release it there, then update the consumer rather than committing a local installed-copy edit alone. If Git submodules are used, update the parent's pointer after the child change is available remotely.

After pulling a changed npm lockfile, run `npm ci`. To investigate available versions, use `npm outdated` and review release notes. `npm update <package>` resolves within allowed ranges; moving beyond a range requires a deliberate manifest change such as `npm install <package>@<reviewed-version>`. Review both manifest and lockfile changes. See [npm update](https://docs.npmjs.com/cli/v11/commands/npm-update).

Verify affected workspace builds and consumer workflows. For adapters, include login expiry, permission denials, validation errors, and compatibility with the API version deployed alongside the application. Upgrade Next.js/React and related peer dependencies as a compatible set. If npm reports dependency conflicts, inspect `npm ls` and the declared peer ranges rather than suppressing the conflict globally. A successful install alone does not prove runtime compatibility.

## Prepare a reusable package

Define a public API using explicit `exports`; publish type declarations where relevant and document supported runtime and framework versions. Include the required built files with a `files` allowlist, README, license, changelog, and migration notes. Document styles or other assets consumers must load. Declare runtime dependencies separately from build dependencies and framework peers.

Confirm that package output contains no `.env`, service keys, internal URLs, development fixtures with personal information, or application-only configuration. Check package contents with `npm pack --dry-run` and test the tarball in a clean consumer. Document any required build steps and avoid exports pointing at missing `dist/` files.

## Publish to npm

Publication is a maintainer action, separate from documenting or testing a package. Replace all placeholders and use the repository's authorized release workflow:

1. Verify registry, scope ownership, account or CI identity, and intended public/private access. Keep the application/workspace root private. See [scoped public package publishing](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages/).
2. Select a semantic version, update release notes, run declared checks, build, and inspect the tarball. Coordinate version changes and tags with the existing release tooling; do not duplicate automated versioning steps manually.
3. For a public scoped package, the publishing command is `npm publish --access public` from the package directory or with the correct workspace selected. Use the approved authentication mechanism. For CI, prefer a supported [trusted publisher configuration](https://docs.npmjs.com/trusted-publishers/) when available to the repository.
4. Use a prerelease version and an explicit tag, for example `npm publish --access public --tag next`, when testing a prerelease. Confirm that the default consumer channel still points to the intended stable release.
5. Verify registry metadata with `npm view <actual-package-name>@<version>` and install that exact version in a fresh consumer. Commit consumer upgrades and lockfiles separately through their normal review process.

Published name/version pairs cannot simply be overwritten. Correct release defects with a new version and communicate compatibility or security impact. Restore consumers to a known working version when necessary; review registry deprecation and unpublish rules before taking registry actions. Never commit registry tokens in `.npmrc`; provide credentials using the supported local or CI secret mechanism.

When a presentation package changes, follow the [documentation synchronization guide](DOCUMENTATION-MAINTENANCE.md) and update its consumer/version/route integration notes with the release.

## Related module lifecycle guides

- [Repository ownership and project-local copies](MODULE-REPOSITORIES.md) — canonical sources, local integration, tracked copies and drift recovery.
- [Package publishing runbook](PACKAGE-PUBLISHING.md) — registry registration, release artifacts and consumer upgrades.
- [Security issue handling](SECURITY-ISSUES.md) — private reports, affected copies, fixes and disclosure.
- [Security audits](SECURITY-AUDITS.md) — dependency/source checks, CI gates and evidence.

## Complete library build and release recipes

Use [presentation package building and npm publishing](presentation/PACKAGES.md) for manifests, React/Vue compilation, declaration output, framework boundaries, tarball consumers, versioning, maintainer releases and CI publishing. [React Native packaging](presentation/REACT-NATIVE.md#7-build-a-reusable-mobile-package) adds Metro/native requirements; [Flutter](presentation/FLUTTER.md) uses Dart/pub instead.
