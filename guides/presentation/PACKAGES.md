# Build presentation packages and publish to npm

This runbook builds reusable libraries for the [presentation layers](README.md). Application production builds are deployed; library artifacts are published. Examples use the unregistered placeholder scope `@example` and capability `example`; substitute your owned scope, real module identity and tested peer ranges. For independent repositories put the package manifest at the release root; in a workspace run the same commands from the selected package directory.

## 1. Create the package contract

Start an empty package directory with `npm init`, then set a meaningful `name`, version, description, repository URL, license and supported runtime/framework versions. Add a README, LICENSE, CHANGELOG and an `src/index.ts` public entry. Use TypeScript strict mode. Decide explicitly whether consumers receive built ESM, source for Metro, a Nuxt layer, CSS, or native code. Never point `exports` at application output such as `.next`, `.output` or `public/build`.

A minimal built-library manifest, after choosing a Vue or React recipe below:

```json
{
  "name": "@example/module-example-react-inertia",
  "version": "0.1.0",
  "type": "module",
  "files": ["dist", "README.md", "LICENSE", "CHANGELOG.md"],
  "types": "./dist/index.d.ts",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" }
  },
  "publishConfig": { "access": "public", "registry": "https://registry.npmjs.org/" }
}
```

Remove `private: true` only from the library selected for publication. Keep apps/workspace roots private. Do not claim CommonJS support without producing and testing a CJS artifact. Add a separate export for required CSS, include it in `files`, document the consumer import and mark CSS as a side effect if using `sideEffects`. Do not set `sideEffects: false` when initialization or styles must survive tree shaking. See [npm package metadata](https://docs.npmjs.com/cli/v11/configuring-npm/package-json).

## 2. React library

For React/Inertia or shared React UI, install tested dependencies:

```bash
npm install --save-dev typescript react@^19.2 react-dom@^19.2 @types/react @types/react-dom @inertiajs/react@^3
```

Add React/React DOM to `peerDependencies` at tested ranges; add `@inertiajs/react` as a peer only for an Inertia wrapper. Do not add Inertia to a Next.js-neutral primitive library. They remain dev dependencies for compiling/testing the library. Keep runtime dependencies only for non-peer imports actually required by consumers.

Use `tsconfig.build.json`:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "jsx": "react-jsx",
    "strict": true,
    "declaration": true,
    "rootDir": "src",
    "outDir": "dist",
    "lib": ["ES2022", "DOM"],
    "skipLibCheck": true
  },
  "include": ["src/**/*.ts", "src/**/*.tsx"]
}
```

Set scripts `clean: node -e "require('node:fs').rmSync('dist',{recursive:true,force:true})"`, `build: npm run clean && tsc -p tsconfig.build.json` and `typecheck: tsc -p tsconfig.build.json --noEmit`. Export each public component/type from `src/index.ts`. This recipe emits separate ESM files and declarations without bundling React. Use `.js` extensions in relative source imports/exports so emitted ESM works in Node as well as bundlers; TypeScript resolves them to the matching `.ts`/`.tsx` source. Copy declared CSS/assets as an explicit build step if they are part of the contract.

For Next.js, preserve `'use client'` at the start of interactive component entry files. Keep the root entry safe for server imports and export client components separately, for example `./client` -> `dist/client.js` with matching declarations. Add a separate `./server` entry for secret-bearing integration, import `server-only` in that entry and declare its dependency. Never re-export server-only code through the client/root barrel. The unbundled TypeScript build preserves directives; check the packed JS to ensure they remain. Test both server and client imports in a clean Next.js app, not only a Vite playground.

## 3. Vue library

For a Vue/Inertia or Nuxt-consumed UI library:

```bash
npm install --save-dev vue@^3 @inertiajs/vue3@^3 typescript vue-tsc vite@^7 @vitejs/plugin-vue@^6
```

Declare Vue as a peer, and Inertia as a peer only for an Inertia wrapper. Create `src/components/ExampleList.vue` and export it from `src/index.ts`. Use this `tsconfig.build.json`:

```json
{
  "compilerOptions": {
    "strict": true,
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "lib": ["ES2022", "DOM"],
    "declaration": true,
    "emitDeclarationOnly": true,
    "rootDir": "src",
    "outDir": "dist"
  },
  "include": ["src/**/*.ts", "src/**/*.vue"]
}
```

Use this Vite library config for the Vite 7 toolchain; if selecting a later Vite major, review its build-option migration and compatible plugin peers:

```ts
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
export default defineConfig({
  plugins: [vue()],
  build: {
    lib: { entry: 'src/index.ts', formats: ['es'], fileName: () => 'index.js' },
    rollupOptions: {
      external: id => /^(vue|@inertiajs\/vue3)(\/|$)/.test(id),
    },
  },
});
```

Set `build: vite build && vue-tsc -p tsconfig.build.json`, and `typecheck: vue-tsc -p tsconfig.build.json --noEmit --emitDeclarationOnly false`. Vite builds JS first (and clears `dist`); declarations are emitted afterwards. Confirm every `.d.ts` reference resolves and all SFC declarations ship. Add an export for emitted CSS using its actual output filename. See [Vite library mode](https://vite.dev/guide/build.html#library-mode). Nuxt can consume this package through explicit imports; a Nuxt module/layer is a different packaging contract described in the [Nuxt guide](NUXT.md).

## 4. Build and inspect a release candidate

Once the package has a reviewed lockfile, scripts and meaningful tests:

```bash
npm ci
npm run typecheck
npm run build
npm pack --dry-run
npm pack
```

Run the declared lint/test/contract checks too; create scripts for the chosen runner rather than documenting commands that do not exist. List the actual tarball with `tar -tf <generated-file>.tgz`. Inspect exports, type declarations, license, styles, native files where applicable and absence of secrets/private fixtures. Exercise public entry points only, so tests cannot silently import unpublished source.

Install that **tarball** in a new disposable app of every supported framework, using `npm install /absolute/path/to/generated-file.tgz`. Run its typecheck and production build and render a real page or screen. Check validation, navigation, CSS, hydration, peer resolution (`npm ls react vue` as relevant), and tree shaking. React Native also needs Metro/device checks; see its [package recipe](REACT-NATIVE.md#7-build-a-reusable-mobile-package). Workspace linking alone cannot validate an artifact.

## 5. Version the release

Check a clean Git tree and the intended package directory. Review breaking API/peer/export/asset changes, changelog, upgrade path and API compatibility window. Use your existing release tool or, in an independently versioned package repository:

```bash
npm version patch --no-git-tag-version
```

Choose `minor`, `major`, or an explicit prerelease instead when appropriate. Commit the manifest and lockfile version changes with release notes. Build/check/pack again from that reviewed commit. Record the commit and tarball SHA-512 (`sha512sum <generated-file>.tgz`). Publish the tarball you tested; avoid rebuilding different content between validation and publication. A `prepack` hook may build library output, but review all lifecycle hooks and avoid depending on a consumer's install hook to generate missing files. See [npm version](https://docs.npmjs.com/cli/v11/commands/npm-version) and [npm pack](https://docs.npmjs.com/cli/v11/commands/npm-pack).

## 6. Publish the reviewed tarball

For an authorized maintainer release, confirm the package name is available or owned by the intended organization, its visibility and registry. Sign in with the approved account/2FA mechanism, then check:

```bash
npm config get registry
npm whoami --registry https://registry.npmjs.org/
npm view @example/module-example-react-inertia versions --json
```

An initial package's lookup can return 404; resolve ownership before continuing. Replace the example scope and tarball below. First prereleases should use a version such as `0.1.0-rc.0` and an explicit non-stable tag:

```bash
npm publish ./example-module-example-react-inertia-0.1.0-rc.0.tgz --access public --tag next
npm view @example/module-example-react-inertia@0.1.0-rc.0 version dist.integrity dist.tarball
```

Install that exact registry version in a clean consumer and repeat the relevant build/journey. For stable release, produce and verify a stable-version artifact, publish it with `--tag latest`, then verify `npm view <name> dist-tags --json`. Do not move `latest` to a prerelease accidentally. Tag the reviewed Git commit with the package/version naming scheme after confirmed publication and push that tag. See [scoped publishing](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages/) and [distribution tags](https://docs.npmjs.com/adding-dist-tags-to-packages).

## 7. Configure CI publication

Use the registry's [trusted publishing setup](https://docs.npmjs.com/trusted-publishers/) for a supported CI provider. Configure the exact organization, repository, workflow filename and optional protected environment on npm. Follow its current Node/npm requirements and first-publication/bootstrap procedure before expecting OIDC to work. Grant the publishing job `contents: read` and `id-token: write`; keep checks on untrusted pull requests separate from release credentials.

The release workflow checks out the immutable release ref, sets the reviewed Node/npm versions, runs `npm ci`, checks/tests/build, packs, validates a clean consumer, stores the tarball/check results, then publishes that tarball using the selected tag. Pin third-party actions to reviewed commits. Configure npm's registry URL, use only the release job's OIDC identity, and do not leave a token-based `.npmrc` overriding trusted authentication. Apply the documented provenance/public-repository constraints; record the resulting registry metadata with the release. If a token is required by a different private registry, use its least-privilege supported authentication and keep it in the CI secret store.

## 8. Adopt and recover

Upgrade consumers using an exact reviewed version or approved semver range, commit their lockfiles, and run integration checks against the supported API. Deploy backwards-compatible owner/API changes first; preserve support for older mobile binaries. A published version is immutable: fix a bad artifact with a new version, deprecate affected releases with a useful message if needed, and restore the stable tag to a verified version through the authorized release workflow. Roll applications back to known-good locks/artifacts while retaining compatible database and API contracts. Never rewrite a released Git tag to disguise a changed artifact.
