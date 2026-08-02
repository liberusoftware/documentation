# Queues standard

Queues are for work that can be delayed, retried, distributed, or isolated from the request. Queue configuration, workers, Horizon, and deployment remain application/operations concerns.

- Select queues by workload, priority, tenant isolation, and operational ownership.
- Set explicit connection, queue, timeout, retry, backoff, `tries`, and `maxExceptions` behavior.
- Make delivery and external calls idempotent and observable with correlation IDs.
- Do not enqueue uncommitted assumptions, secrets, request objects, or authorization decisions.
- Monitor age, throughput, failure rate, retries, dead letters, and saturation; document safe replay and discard procedures.

See [JOBS.md](JOBS.md), [deployment queues](../deployment/QUEUES.md), and [Laravel queues](https://laravel.com/docs/13.x/queues).
