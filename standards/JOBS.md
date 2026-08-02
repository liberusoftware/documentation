# Jobs standard

Jobs represent asynchronous application work with explicit ownership, input, authorization context, retry policy, idempotency, observability, and recovery.

- Pass stable identifiers and immutable values, not live models or request/session state.
- Establish tenant/team context explicitly and fail closed when it is absent.
- Make handlers safe to retry; use idempotency keys, unique jobs, deduplication, or compensating actions as appropriate.
- Define backoff, timeout, max attempts, dead-letter behavior, alerting, and operator recovery.
- Dispatch after commit when a job depends on committed state; redact secrets and personal data from payloads and logs.

See [QUEUES.md](QUEUES.md), [Laravel queues](https://laravel.com/docs/13.x/queues), and [Horizon](https://laravel.com/docs/13.x/horizon).
