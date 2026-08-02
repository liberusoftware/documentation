# Queues

Use Laravel queues for slow, retryable, provider-dependent, or bulk work. Keep HTTP requests bounded and return an operation resource when completion is asynchronous.

## Design

- Define explicit queue names, payload DTOs, timeouts, retry limits, backoff, uniqueness, and failure behavior.
- Authorize and resolve team context before dispatch; re-authorize sensitive work when the job runs.
- Make jobs idempotent, bounded, observable, and safe to retry. Do not serialize models, secrets, request objects, or unnecessary personal data.
- Separate latency-sensitive, provider, bulk, and low-priority queues; apply per-queue concurrency and rate limits.

## Operations

Run workers as supervised, replaceable processes using [Supervisor](SUPERVISORD.md), [Horizon](HORIZON.md), containers, or Kubernetes. Align worker timeout, process-manager kill timeout, termination grace periods, and retry policy.

Monitor queue depth, oldest age, throughput, retries, failures, execution time, provider throttling, and memory. Use `php artisan queue:failed`, a reviewed retry policy, and tested replay/deletion procedures.

## References

- [Laravel queues](https://laravel.com/docs/13.x/queues)
- [Laravel scheduling](https://laravel.com/docs/13.x/scheduling)
- [Deployment index](README.md)
