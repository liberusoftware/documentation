# Laravel 13 standard

Laravel is the application composition framework. Use the latest stable Laravel 13 patch release supported by the application lock file and [official Laravel documentation](https://laravel.com/docs/13.x).

## Boundaries

- Keep domain rules in modules and application services; controllers, Livewire components, Filament resources, and Inertia pages orchestrate them.
- Use route model binding, form requests or dedicated validators, policies/gates, middleware, service providers, and Laravel contracts deliberately.
- Resolve team/tenant context before protected queries and mutations; UI route guards are not authorization.
- Use Eloquent models for persistence ownership, query objects/read models for complex reads, and transactions for local invariant changes.
- Dispatch events after commit, make retryable jobs idempotent, and use queues for work that exceeds the request budget.
- Keep configuration in `config/`, environment values in secrets/environment configuration, and application composition in the root application.

## Official references

[Installation](https://laravel.com/docs/13.x/installation) · [Architecture concepts](https://laravel.com/docs/13.x/container) · [Controllers](https://laravel.com/docs/13.x/controllers) · [Validation](https://laravel.com/docs/13.x/validation) · [Authorization](https://laravel.com/docs/13.x/authorization) · [Queues](https://laravel.com/docs/13.x/queues) · [Testing](https://laravel.com/docs/13.x/testing)

## Delivery checklist

Choose the simplest Laravel composition that meets the workload, but keep module boundaries, policies, validation, migrations, events, jobs, and tests identical across deployment profiles. Record configuration defaults, environment secrets, queue/storage/mail requirements, health checks, update procedure, backup/restore evidence, and the point at which a single process must become supervised or distributed.
