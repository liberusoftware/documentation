# React 19.2 technology reference

React is used for rich application interfaces, usually through Inertia 3 and a Laravel-owned API/action boundary. Components render typed public data; they do not own authorization or domain state.

## Component example

```tsx
type EmptyStateProps = { heading: string; action?: React.ReactNode };

export function EmptyState({ heading, action }: EmptyStateProps) {
  return (
    <section aria-labelledby="empty-heading">
      <h2 id="empty-heading">{heading}</h2>
      {action}
    </section>
  );
}
```

Use strict TypeScript, stable keys, semantic HTML, keyboard support, explicit loading/error/empty/denied states, and server-authorized forms. Avoid client-side secrets and duplicated business rules.

Official references: [React Learn](https://react.dev/learn), [React API reference](https://react.dev/reference/react), [React installation](https://react.dev/learn/installation), and [React GitHub](https://github.com/facebook/react). Related local guides: [React standard](../standards/REACT.md), [Inertia](INERTIA.md), and [React module index](../modules/react/README.md).
