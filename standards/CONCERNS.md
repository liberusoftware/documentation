# Concerns standard

Traits and concerns are for small, cohesive cross-cutting behavior with a clear contract. They must not hide dependencies or become inheritance by another name.

- Prefer composition, services, contracts, or value objects when behavior has meaningful collaborators or lifecycle.
- Keep traits narrow, namespaced, documented, and safe when applied to more than one class.
- Do not use traits to hide authorization, queries, transactions, external calls, mutable global state, or unexpected boot hooks.
- Test the concern through representative owners and document required methods, properties, events, and conflicts.

See [PHP traits](https://www.php.net/manual/en/language.oop5.traits.php) and [CLASSES.md](CLASSES.md).
