# JavaScript standard

Liberu uses modern JavaScript through Vite, with Node.js 22+ as the current supported runtime baseline. Verify the exact supported even-numbered Node release in the application lockfile and CI matrix. The [MDN JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [ECMAScript specification](https://tc39.es/ecma262/) are authoritative.

- Use modules, `const` by default, strict equality, explicit error handling, and small pure functions.
- Prefer `async`/`await`, abortable requests, and explicit timeout/cancellation behavior for I/O.
- Never trust browser input, store long-lived tokens in local storage, or expose secrets to client bundles.
- Avoid global mutable state, prototype mutation, `eval`, unsafe HTML insertion, and unbounded event listeners.
- Use semantic DOM APIs, keyboard support, reduced motion, localization, and accessible status/error announcements.
- Keep dependencies pinned through lockfiles, audit production bundles, and code-split optional features.

## Liberu usage

JavaScript is used for progressive enhancement, Inertia clients, Vue/Nuxt applications, and Vite configuration. Keep domain decisions on the Laravel boundary and treat API/page payloads as untrusted:

```js
const controller = new AbortController();
const timeout = setTimeout(() => controller.abort(), 8000);

try {
  const response = await fetch("/api/v1/health", {
    headers: { Accept: "application/json" },
    signal: controller.signal,
  });
  if (!response.ok) throw new Error(`Request failed: ${response.status}`);
} finally {
  clearTimeout(timeout);
}
```

See [Vite](https://vite.dev/guide/), [Web APIs](https://developer.mozilla.org/en-US/docs/Web/API), [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), [GUIDELINES.md](../standards/GUIDELINES.md), and the [React](../modules/react/README.md), [Vue](../modules/vue/README.md), and [Nuxt](../modules/nuxt/README.md) implementation indexes.
