# Implement Vue and React with Laravel and Inertia

Follow the [foundation steps](README.md) first. Choose either Vue or React for this host. Both use Laravel routes and sessions with Inertia 3; Nuxt and Next.js have separate API-consuming shells. These examples deliberately use manual page resolution and client rendering, which the official [Vue adapter source](https://github.com/inertiajs/inertia/blob/3.x/packages/vue3/src/createInertiaApp.ts) and [React adapter source](https://github.com/inertiajs/inertia/blob/3.x/packages/react/src/createInertiaApp.ts) support. SSR is a separate configuration step below.

## 1. Prepare the Laravel skeleton

In a new foundation clone, follow its `DEVELOPMENT.md`, copy safe local environment configuration and install from its Composer lock. Configure the database and session driver, then run:

```bash
composer install
php artisan key:generate
php artisan migrate
php artisan test
```

The key-generation command applies only to a new local environment. Existing credentials, migration procedures and version constraints take precedence. Keep the foundation identity/session/team modules; do not generate a second authentication system over them.

If Inertia is absent, add its compatible server adapter and middleware:

```bash
composer require inertiajs/inertia-laravel:^3.0
php artisan inertia:middleware
```

Append `App\Http\Middleware\HandleInertiaRequests::class` once to the existing `web` middleware group in `bootstrap/app.php`, retaining the host's existing middleware and ordering. The [Laravel adapter middleware](https://github.com/inertiajs/inertia-laravel/blob/3.x/src/Middleware.php) handles Inertia request/redirect behavior. Share only a minimal actor summary, established workspace summary and authorized navigation flags; never serialize full models or tokens. Keep session/CSRF middleware on mutation routes.

## 2. Install one frontend adapter

For Vue:

```bash
npm install vue@^3 @inertiajs/vue3@^3
npm install --save-dev vite@^7 laravel-vite-plugin@^2 @vitejs/plugin-vue@^6 typescript vue-tsc
```

For React:

```bash
npm install react@^19.2 react-dom@^19.2 @inertiajs/react@^3
npm install --save-dev vite@^7 laravel-vite-plugin@^2 @vitejs/plugin-react@^5 typescript @types/react @types/react-dom
```

Use the supported Node release and compatible Vite/plugin versions, review peers, then commit `package-lock.json`. Preserve useful existing scripts. Set `private: true` on the host `package.json`; add `dev: vite`, `build: vite build`, and `typecheck: vue-tsc --noEmit` or `tsc --noEmit`. Use this `tsconfig.json` for the React shell:

```json
{
  "compilerOptions": {
    "strict": true,
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "target": "ES2022",
    "lib": ["ES2022", "DOM"],
    "noEmit": true,
    "types": ["vite/client"],
    "jsx": "react-jsx",
    "skipLibCheck": true
  },
  "include": ["resources/js/**/*.ts", "resources/js/**/*.tsx", "resources/js/**/*.vue"]
}
```

For Vue remove `jsx` and run `vue-tsc` for the same included files. Retain the host's existing alias definitions when extending an established configuration.

## 3. Configure the application asset entry

For Vue, `vite.config.ts`:

```ts
import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [
    laravel({ input: ['resources/js/app.ts'], refresh: true }),
    vue(),
  ],
});
```

For React, replace the Vue import with `react` from `@vitejs/plugin-react`, call `react()` and set input to `resources/js/app.tsx`. Keep only the selected adapter. Create `resources/css/app.css`, load the host's theme tokens there, and import it from the entry.

Create `resources/views/app.blade.php` (React variant shown):

```blade
<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    @viteReactRefresh
    @vite('resources/js/app.tsx')
    @inertiaHead
</head>
<body>
    @inertia
</body>
</html>
```

For Vue remove `@viteReactRefresh` and use `resources/js/app.ts`. Allow browser zoom. Retain the host's CSP/nonces and safe metadata.

## 4. Boot Vue or React and resolve pages explicitly

Vue `resources/js/app.ts`:

```ts
import '../css/app.css';
import { createApp, h, type DefineComponent } from 'vue';
import { createInertiaApp } from '@inertiajs/vue3';
import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers';

createInertiaApp({
  resolve: name => resolvePageComponent(
    `./Pages/${name}.vue`,
    import.meta.glob<DefineComponent>('./Pages/**/*.vue'),
  ),
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) }).use(plugin).mount(el);
  },
});
```

React `resources/js/app.tsx`:

```tsx
import '../css/app.css';
import { createRoot } from 'react-dom/client';
import { createInertiaApp, type ResolvedComponent } from '@inertiajs/react';
import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers';

createInertiaApp({
  resolve: name => resolvePageComponent(
    `./Pages/${name}.tsx`,
    import.meta.glob<{ default: ResolvedComponent }>('./Pages/**/*.tsx'),
  ).then(module => module.default),
  setup({ el, App, props }) {
    createRoot(el).render(<App {...props} />);
  },
});
```

The application owns its layout and page map. For an installed package, import a documented page export and register a unique key such as `Example/Index` in an explicit map before the local glob fallback. Fail on unknown/duplicate keys during checks. A package should not discover arbitrary application pages or reference `node_modules` filesystem paths at runtime.

## 5. Add a server boundary and a first page

Use `php artisan make:controller ExampleController` and add authenticated GET/POST routes to `routes/web.php` using the host's established workspace middleware. For example, name them `example.index` and `example.store`. Do not accept a client-supplied tenant ID as proof of membership.

The controller's index method calls the actual public query with the authenticated actor and established context, maps the authorized result to a minimal DTO, and returns:

```php
return Inertia\Inertia::render('Example/Index', [
    'records' => $authorizedRecordDtos,
    'storeUrl' => route('example.store'),
]);
```

`$authorizedRecordDtos` is an integration seam: implement it with the source-reviewed query, not a new `App` model/table. The POST method validates shape with a Form Request, authorizes through the owner contract, invokes the owner command and returns `to_route('example.index')`. The owner rechecks business invariants and performs its transaction/audit. Translate owner validation failures to Laravel field errors; represent conflicts and asynchronous operations distinctly. An HTTP accepted result is not a completed action.

For the illustrative DTO `{ id: string; title: string }`, Vue `resources/js/Pages/Example/Index.vue`:

```vue
<script setup lang="ts">
import { Head, useForm } from '@inertiajs/vue3';
defineProps<{ records: { id: string; title: string }[]; storeUrl: string }>();
const form = useForm({ title: '' });
</script>

<template>
  <Head title="Records" />
  <main>
    <h1>Records</h1>
    <p v-if="records.length === 0">No records available.</p>
    <ul><li v-for="record in records" :key="record.id">{{ record.title }}</li></ul>
    <form @submit.prevent="form.post(storeUrl, { onSuccess: () => form.reset() })">
      <label for="example-title">Title</label>
      <input id="example-title" v-model="form.title" aria-describedby="example-error">
      <p id="example-error" role="alert">{{ form.errors.title }}</p>
      <button :disabled="form.processing">Create record</button>
    </form>
  </main>
</template>
```

React `resources/js/Pages/Example/Index.tsx`:

```tsx
import { Head, useForm } from '@inertiajs/react';
type Props = { records: { id: string; title: string }[]; storeUrl: string };
export default function Index({ records, storeUrl }: Props) {
  const form = useForm({ title: '' });
  return <main>
    <Head title="Records" /><h1>Records</h1>
    {records.length === 0 && <p>No records available.</p>}
    <ul>{records.map(record => <li key={record.id}>{record.title}</li>)}</ul>
    <form onSubmit={event => {
      event.preventDefault();
      form.post(storeUrl, { onSuccess: () => form.reset() });
    }}>
      <label htmlFor="example-title">Title</label>
      <input id="example-title" value={form.data.title}
        onChange={event => form.setData('title', event.target.value)}
        aria-describedby="example-error" />
      <p id="example-error" role="alert">{form.errors.title}</p>
      <button disabled={form.processing}>Create record</button>
    </form>
  </main>;
}
```

Supply named URLs from Laravel or the host's typed route generator. Use Inertia `Link` for internal visits and `useForm` for this redirect/error lifecycle. Do not substitute a REST fetch for the Inertia form protocol. Add focus to the first invalid field/error summary, safe draft retention and conflict recovery before calling the journey complete. Render server-supplied text normally; avoid raw HTML.

## 6. Extract the capability adapter

Keep reusable components/composables/hooks free of Inertia imports when sharing with Nuxt or Next.js. Export separate page/navigation wrappers that depend on the official Inertia adapter. Use the module basenames in the [layer index](README.md); the PHP bridge can register routes/providers through Composer while the JS library exposes explicit page exports through npm. Keep framework runtimes as peers and externalize them. Build Vue SFCs/declarations or React JS/declarations using the [package recipes](PACKAGES.md).

## 7. Develop, verify and build the host

Run `php artisan serve` and `npm run dev` in separate terminals (plus the host's queue worker when needed). Run `npm run typecheck`, the declared frontend tests and `php artisan test`, then `npm run build`. Verify a full page load, Inertia navigation, form validation/redirect, CSRF/session expiry, denied and wrong-workspace actions, accessible keyboard interaction and fresh assets after deployment. Inertia response assertions should confirm exact component names and allowed props, including absent protected fields.

Deploy the Laravel artifact with `public/build` and its manifest; the Vite development server does not run in production. Follow the host's migration, worker restart, config/cache and rollback procedures. Keep previously referenced hashed assets available during rollout.

## 8. Add SSR deliberately if required

The manual examples above are client-rendered. Choose either the Inertia 3 Vite integration's documented automatic SSR setup or separate client/server entries supported by the selected adapter; do not mix both boot paths. With manual setup, add a server entry using the adapter's `createServer` and framework server renderer, configure a Vite SSR build, and hydrate the rendered markup with React `hydrateRoot` or Vue `createSSRApp` on the browser side. Match page maps, plugins, locale and theme on both sides. Run the resulting SSR service under the deployment's process manager and verify fallback behavior when unavailable.

Test SSR/hydration and request isolation before enabling it: avoid browser APIs during server rendering and shared mutable per-user state. Record the actual SSR scripts, ports, health check and restart command in the application's README. See [Inertia source](https://github.com/inertiajs/inertia) and the [Inertia standard](../../standards/INERTIA.md) for the supported major-line integration; existing starter-kit SSR configuration takes precedence over this manual CSR recipe.
