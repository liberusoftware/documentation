# Laravel Telescope

Use Telescope for controlled local, staging, and incident diagnostics. It captures application activity and can contain sensitive data, so it is not an unrestricted production observability system.

## Safe operation

- Install and pin Telescope only where required; disable or strictly gate it in production by default.
- Protect the dashboard with trusted authentication, authorization, network controls, and HTTPS.
- Configure recording filters, pruning, storage, and retention deliberately. Exclude credentials, tokens, secrets, full request bodies, and unnecessary personal data.
- Use separate storage and access policies for diagnostics. Do not grant Telescope access to ordinary users or tenants.
- Prefer structured logs, metrics, traces, queue monitoring, and audit events for durable production observability.

```bash
php artisan telescope:prune --hours=48
```

Review captured queries, jobs, exceptions, mail, notifications, dumps, and model events for data leakage. Monitor Telescope storage and overhead, and remove captured data according to the approved retention policy.

## References

- [Laravel Telescope](https://laravel.com/docs/13.x/telescope)
- [Laravel logging](https://laravel.com/docs/13.x/logging)
- [Security policy](../SECURITY.md)
- [Deployment index](README.md)
