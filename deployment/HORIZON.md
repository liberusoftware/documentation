# Laravel Horizon

Use Horizon to operate Redis-backed Laravel queues with named supervisors, balancing, metrics, and failed-job visibility. Horizon is an operational layer over [QUEUES.md](QUEUES.md), not a replacement for job design or authorization.

## Production setup

- Install and pin Horizon through Composer and commit the compatible lock file.
- Define environment-specific supervisors in `config/horizon.php`; keep production worker counts and memory limits explicit.
- Separate critical, provider, bulk, and low-priority queues. Set balancing, tries, timeout, backoff, max jobs, and max time deliberately.
- Protect the Horizon dashboard with trusted authentication and authorization; never expose it publicly without access controls.
- Store Redis credentials in runtime secrets and use TLS/private networking where supported.

```bash
php artisan horizon
php artisan horizon:status
php artisan horizon:terminate
```

Run Horizon under [Supervisor](SUPERVISORD.md), a container restart policy, or a Kubernetes workload. Terminate it gracefully during releases so new workers load reviewed code. Monitor throughput, wait time, failures, memory, restarts, Redis health, and backlog.

## CI and release deployment

Every push to `main` runs [CI](../architecture/CI.md) and may deploy Horizon configuration to staging. Production supervisors and Horizon workers must not be restarted automatically from `main`. A protected `vX.Y.Z` tag or GitHub Release may deploy only after the 100% release-scope coverage gate, queue/configuration checks, smoke tests, and production approval pass. Terminate or restart supervisors gracefully and verify queue throughput and failures.

## References

- [CI and release policy](../architecture/CI.md)
- [Laravel Horizon](https://laravel.com/docs/13.x/horizon)
- [Laravel queues](https://laravel.com/docs/13.x/queues)
- [Deployment index](README.md)
