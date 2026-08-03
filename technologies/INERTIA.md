# Inertia 3 technology reference

Inertia connects Laravel routes/controllers to React or Vue pages without requiring a separate client-side router. The server remains the authority for authorization, validation, redirects, and page data.

## Page example

```php
return Inertia::render('Records/Index', [
    'records' => RecordResource::collection($records),
    'filters' => $filters,
]);
```

Keep shared props small and classified, use forms that map server validation errors, preserve focus and history intentionally, and never treat hidden client navigation as authorization. Use the API contract for Nuxt or separately deployed clients.

Official references: [Inertia 3 getting started](https://inertiajs.com/docs/v3/getting-started), [forms](https://inertiajs.com/docs/v3/the-basics/forms), [partial reloads](https://inertiajs.com/docs/v3/data-props/partial-reloads), and [Inertia GitHub](https://github.com/inertiajs/inertia). Related local guides: [Inertia standard](../standards/INERTIA.md), [React](REACT.md), [Vue](VUE.md), and [API architecture](../architecture/API.md).
