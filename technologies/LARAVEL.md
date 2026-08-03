# Laravel 13 technology reference

Laravel is Liberu's server-side application framework for composition, HTTP, authorization, persistence, queues, schedules, notifications, and testing. Domain modules remain presentation-neutral and expose contracts consumed by Laravel applications.

## Typical module boundary

```text
Route/controller/request
        ↓
Policy + typed application action/query
        ↓
module-{name} core package
        ↓
Eloquent mapping, migrations, jobs, events, integrations
```

Keep controllers thin and authorize before reading or mutating tenant-scoped data. Use service providers for package registration, Form Requests or validators for input, policies for access, events after commit, and idempotent jobs for asynchronous work.

```php
Route::get('/api/v1/records/{record}', ShowRecordController::class)
    ->middleware(['auth:sanctum'])
    ->can('view', 'record');
```

Official references: [Laravel 13 documentation](https://laravel.com/docs/13.x), [installation](https://laravel.com/docs/13.x/installation), [request lifecycle](https://laravel.com/docs/13.x/lifecycle), [testing](https://laravel.com/docs/13.x/testing), and [Laravel GitHub](https://github.com/laravel/laravel). Related local guides: [Laravel standard](../standards/LARAVEL.md), [modules](../architecture/MODULES.md), and [security](../architecture/SECURITY.md).
