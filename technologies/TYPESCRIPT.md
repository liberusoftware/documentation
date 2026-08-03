# TypeScript standard

Liberu uses strict TypeScript for React, Vue, Nuxt, Inertia, and shared frontend contracts. The [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html) and [TypeScript GitHub repository](https://github.com/microsoft/TypeScript) are authoritative.

- Enable strict mode and no-implicit-any behavior; do not weaken compiler options to silence a local error.
- Model API/page props with explicit types, discriminated unions, branded identifiers, and safe nullable states.
- Treat external responses, query strings, form input, files, and SSR payloads as untrusted; validate at trust boundaries.
- Prefer `unknown` over `any`, narrow values explicitly, and avoid type assertions unless the boundary and invariant are documented.
- Export only intentional package contracts and keep generated types tied to a versioned API schema.
- Test loading, empty, error, unauthorized, stale, offline, and success states in addition to the happy path.

## Liberu usage

Validate data at the network boundary and then narrow it before rendering. Prefer discriminated unions for state machines:

```ts
type LoadState<T> =
  | { status: "loading" }
  | { status: "ready"; data: T }
  | { status: "error"; message: string };
```

Generated API types must be tied to the versioned contract and must not replace server-side authorization. See [React](../standards/REACT.md), [Vue](../standards/VUE.md), [Nuxt](../standards/NUXT.md), [Inertia](../standards/INERTIA.md), and the [API architecture](../architecture/API.md).
