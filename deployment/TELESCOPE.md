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

## CI and release deployment

Every push to `main` runs [CI](../architecture/CI.md) and may deploy Telescope configuration to staging. Production Telescope changes must not be applied automatically from `main`. A protected `vX.Y.Z` tag or GitHub Release may deploy only after the 100% release-scope coverage gate, access-control and configuration checks, smoke tests, and production approval pass. Verify authorization and retention after deployment; never expose Telescope as a substitute for application monitoring.

## References

- [CI and release policy](../architecture/CI.md)
- [Laravel Telescope](https://laravel.com/docs/13.x/telescope)
- [Laravel logging](https://laravel.com/docs/13.x/logging)
- [Security policy](../architecture/SECURITY.md)
- [Deployment index](README.md)
