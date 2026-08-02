# Database implementation standard

Liberu databases are owned by domain modules and composed by Laravel applications. Use the supported database engine and version declared by the application compatibility matrix; Laravel migrations, seeders, factories, and Eloquent are implementation tools, not substitutes for domain ownership.

## Migrations

- A module owns its tables, indexes, foreign keys, constraints, migrations, upgrade path, retention, export, and deletion behavior.
- Make migrations deterministic, reversible where practical, safe for production data, and compatible with rolling deploys.
- Separate destructive changes from additive changes; backfill in resumable jobs, validate results, then remove old structures in a later release.
- Never edit a released migration. Add a new migration and document deployment order, locks, expected duration, and rollback limits.

## Seeders

- Seeders create required reference/configuration data and safe local/demo fixtures; they must be explicit, repeatable, and environment-aware.
- Never seed production credentials, personal data, secrets, or nondeterministic records.
- Separate baseline/reference seeders from demo/sample seeders. Production deployments run only the required baseline set.
- Use stable keys and upserts for reference data so rerunning a seeder does not duplicate records.

## Factories

- Factories generate isolated, valid test data with realistic relationships and explicit states such as `draft`, `active`, `disabled`, or `unauthorized`.
- Do not use factories to bypass domain actions, policies, tenant context, invariants, or audit behavior in feature tests.
- Keep sensitive fields safe and deterministic enough for tests; use sequences for uniqueness and avoid production-like personal data.

## Queries and operations

Use constraints for invariants, indexes for observed access paths, transactions for local consistency, read models/query objects for complex reads, and backups/restore tests for operational safety. Prevent N+1 queries and hidden database access in views, serializers, policies, jobs, and accessors.

See [Laravel migrations](https://laravel.com/docs/13.x/migrations), [seeders](https://laravel.com/docs/13.x/seeding), [factories](https://laravel.com/docs/13.x/eloquent-factories), [Eloquent](https://laravel.com/docs/13.x/eloquent), [architecture/MODULES.md](../architecture/MODULES.md), and [standards/MODELS.md](MODELS.md).
