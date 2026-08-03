# Models standard

Models represent persistence-owned data and its local mapping rules. They do not replace aggregates, application actions, policies, or API contracts.

- A module owns its tables, migrations, models, casts, indexes, retention, export, deletion, and upgrade behavior.
- Use guarded/validated assignment, explicit casts, relationships, scopes, and database constraints.
- Keep business invariants in domain/application boundaries when they span records, workflows, permissions, or providers.
- Avoid hidden queries in accessors, serialization, views, jobs, and authorization checks; prevent N+1 behavior intentionally.
- Do not expose private models or tables as cross-module extension points.

See [Laravel Eloquent](https://laravel.com/docs/13.x/eloquent), [migrations](https://laravel.com/docs/13.x/migrations), and [DOMAIN-DRIVEN-DESIGN-PATTERNS.md](DOMAIN-DRIVEN-DESIGN-PATTERNS.md).

## Delivery checklist

For each model, document its owning module, table, classification, relationships, indexes, retention, export, deletion, and migration history. Use constraints for enforceable local rules and actions/policies for workflow and authorization. Test fresh install, upgrade/backfill, uniqueness, foreign keys, tenant scoping, query performance, and restore behavior.
