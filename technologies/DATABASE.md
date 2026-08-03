# Database technology reference

This file describes database technology concerns; ownership and implementation rules are in [standards/DATABASE.md](../standards/DATABASE.md), and cross-module ownership is in [architecture/MODULES.md](../architecture/MODULES.md).

Laravel applications use a supported relational database through Laravel’s database layer and Eloquent. The exact engine, version, extensions, collation, charset, queue/cache stores, and production topology belong in the application lock/compatibility matrix and deployment documentation.

- Prefer portable Laravel schema/query features unless an engine-specific capability is a deliberate, tested decision.
- Define indexes and constraints from measured access patterns and domain invariants.
- Use transactions for local consistency and an outbox/inbox or reconciliation workflow for cross-system delivery.
- Treat migrations as versioned deployment code; use seeders for reference/configuration data and factories for tests.
- Test backups, restores, replica lag, failover, encryption, retention, deletion, and tenant isolation.

## Example migration

Keep the invariant in the database as well as in application code:

```php
Schema::create('module_records', function (Blueprint $table): void {
    $table->ulid('id')->primary();
    $table->foreignUlid('organization_id')->constrained()->cascadeOnDelete();
    $table->string('status', 32);
    $table->timestampsTz();
    $table->index(['organization_id', 'status']);
});
```

Official references: [Laravel database](https://laravel.com/docs/13.x/database), [migrations](https://laravel.com/docs/13.x/migrations), [MySQL 8.4 manual](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/manual-info.html), [PostgreSQL](https://www.postgresql.org/docs/), and [SQLite](https://www.sqlite.org/docs.html). See the local [database standard](../standards/DATABASE.md) and [module implementation guide](../modules/features/IMPLEMENTATION.md).
