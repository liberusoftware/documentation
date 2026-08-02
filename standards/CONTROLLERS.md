# Controllers standard

Controllers are thin HTTP adapters. They translate a request into an authorized application action and a response; they do not contain domain workflows.

- Use one controller method per route/use case with explicit route names and middleware.
- Validate through form requests or dedicated validators, authorize through policies/gates, and resolve team/tenant context before access.
- Delegate writes to actions/services and reads to purpose-built queries/read models.
- Return redirects, views, Inertia responses, or API resources with stable documented semantics.
- Avoid database queries, provider SDK calls, hidden side effects, and cross-module orchestration in controllers.

See [Laravel controllers](https://laravel.com/docs/13.x/controllers), [INERTIA.md](INERTIA.md), and [API.md](../architecture/API.md).
