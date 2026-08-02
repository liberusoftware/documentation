# Inertia 3 standard

Inertia is the bridge between Laravel server-side routing/controllers and React, Vue, or Svelte page components. It is not a domain layer or client-side authorization system. Liberu targets Inertia 3 with the official Laravel adapter and the matching client adapter.

## Rules

- Laravel owns routes, middleware, authorization, validation, redirects, shared props, and error semantics.
- Pages receive explicit, minimal props; never serialize secrets, private models, unnecessary personal data, or protected data into public caches.
- Use named routes, `Link`, `router`, forms, partial reloads, deferred props, remembered state, and progress indicators according to the freshness and failure semantics of the feature.
- Preserve CSRF, Sanctum cookie authentication, team/tenant context, correlation IDs, idempotency keys, pagination, and concurrency headers.
- Keep page resolution and SSR configuration application-owned; packages expose explicit pages and public exports without global discovery collisions.
- Test full redirects, validation errors, authorization denial, stale data, partial reloads, SSR hydration, navigation, accessibility, and asset builds.

## Official references

[Inertia documentation](https://inertiajs.com/docs/v3/getting-started) · [Laravel adapter](https://inertiajs.com/docs/v3/installation/server-side) · [React adapter](https://inertiajs.com/docs/v3/installation/react) · [Vue adapter](https://inertiajs.com/docs/v3/installation/vue) · [Inertia GitHub](https://github.com/inertiajs/inertia)
