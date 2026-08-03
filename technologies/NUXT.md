# Nuxt 4 technology reference

Nuxt 4 is used for Vue SSR, public sites, and API-consuming applications. It provides file-based routing, server routes, runtime configuration, and hybrid rendering; Laravel remains the domain and authorization authority.

## Data example

```ts
const { data, error, pending } = await useFetch("/api/v1/records", {
  query: { page: 1 },
});
```

Keep secrets in private runtime configuration or server routes, validate external responses, configure caching deliberately, handle hydration differences, and apply authorization at the API boundary even when a route is hidden. Choose SSR, static, or client rendering per data sensitivity and freshness requirements.

Official references: [Nuxt 4 guide](https://nuxt.com/docs/4.x/guide), [installation](https://nuxt.com/docs/4.x/getting-started/installation), [data fetching](https://nuxt.com/docs/4.x/getting-started/data-fetching), [runtime config](https://nuxt.com/docs/4.x/guide/going-further/runtime-config), and [Nuxt GitHub](https://github.com/nuxt/nuxt). Related local guides: [Nuxt standard](../standards/NUXT.md), [API architecture](../architecture/API.md), and [Nuxt module index](../modules/nuxt/README.md).
