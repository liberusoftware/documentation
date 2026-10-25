# Next.js technology reference

Next.js supports React applications with application-owned routing and server/client rendering. Liberu uses it as an optional API-consuming presentation layer alongside Laravel-owned React/Inertia applications. Their React components can share presentation primitives, but their routing, form transport, session integration, and page lifecycles need separate adapters. See the [Next.js standard](../standards/NEXTJS.md).

## Create a separate application

Check the supported Node.js version for the selected Next.js release and the consuming repository's `engines`/toolchain configuration. For a new application in a suitable parent directory:

```bash
npx create-next-app@latest liberu-portal
cd liberu-portal
npm run dev
```

Select TypeScript and App Router when prompted. Open the local address printed by the development server. This scaffolds the frontend only; it does not install Liberu domain modules, configure Laravel authentication, or create API endpoints. Record the resulting package versions and commit the generated lockfile before treating the application as reproducible. For an existing clone use its declared package manager and lockfile instead of scaffolding over it. See the [official installation guide](https://nextjs.org/docs/app/getting-started/installation).

## Share React UI deliberately

A framework-independent component can render a DTO without knowing how the application obtained it:

```tsx
export type OrderSummaryProps = {
  reference: string;
  statusLabel: string;
  formattedTotal: string;
};

export function OrderSummary(props: OrderSummaryProps) {
  return (
    <section aria-label="Order summary">
      <h2>{props.reference}</h2>
      <p>{props.statusLabel}</p>
      <p>{props.formattedTotal}</p>
    </section>
  );
}
```

An Inertia page can pass authorized page props to this component. A Next.js page can pass serializable data from its server API integration. Keep framework-specific links, mutations, authentication, and loading logic in wrappers. Do not pass ordinary callback functions from a Server Component to a Client Component as if they were serializable data; compose interactive callbacks inside the client boundary or use the framework's documented server-action mechanism.

Server Components suit server-side data access; Client Components provide interaction and browser APIs. Keep secret-bearing helpers out of client imports and browser bundles. See the [server/client component guide](https://nextjs.org/docs/app/getting-started/server-and-client-components).

## Connect to Liberu

Choose a real, documented API operation from the owning product. Validate its response schema, authorize both the frontend entry point and Laravel operation, and define error mapping before building the form. For authenticated enterprise reads, start with explicit no-store behavior until tenant-aware caching is designed. Treat URL tenant IDs as selections that require membership checks.

Use the [project adapter plans](../modules/nextjs/README.md), [API architecture](../architecture/API.md), [theme contract](../standards/THEMES.md), and [npm lifecycle guide](../guides/NPM.md). Verify the application's build, declared static checks, key browser journeys, expired-session recovery, and cross-tenant cache isolation before deploying.
