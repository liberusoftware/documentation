# Node.js technology reference

Node.js 22+ is the portfolio baseline for Vite, React, Vue, Nuxt, TypeScript, and frontend tooling. Confirm the exact active LTS patch in the consuming application's lockfile and CI matrix.

## Safe workflow

```bash
node --version
npm --version
npm ci
npm audit
npm run build
```

Use the repository's selected package manager and lockfile consistently. Do not install dependencies with a different manager, commit `node_modules/`, expose environment secrets to client bundles, or rely on unbounded child processes. Keep server-only Nuxt code behind server routes and runtime configuration.

Official references: [Node.js Learn](https://nodejs.org/learn), [Node.js documentation](https://nodejs.org/docs/latest/api/), [Node.js releases](https://nodejs.org/en/about/previous-releases), and [npm documentation](https://docs.npmjs.com/). Related local guides: [JavaScript](JAVASCRIPT.md), [TypeScript](TYPESCRIPT.md), [Vite](VITE.md), and [Nuxt](NUXT.md).
