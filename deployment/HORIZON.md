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

## References

- [Laravel Horizon](https://laravel.com/docs/13.x/horizon)
- [Laravel queues](https://laravel.com/docs/13.x/queues)
- [Deployment index](README.md)
