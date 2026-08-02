# Contracts standard

Contracts are stable boundaries for replaceable behavior and public package interoperability. Add one when substitution, testing, integration, or versioned extension is real—not for every class.

- Keep interfaces small, capability-focused, typed, and framework-neutral where practical.
- Document authorization, tenancy, error, consistency, idempotency, and lifecycle semantics.
- Version public changes deliberately and provide adapters/migrations for breaking changes.
- Prefer immutable DTOs and explicit result/error types over leaking ORM models or framework internals.
- Test the contract against the concrete adapter and meaningful alternate/fake implementations.

See [Laravel contracts](https://laravel.com/docs/13.x/contracts), [PSR.md](PSR.md), and [API.md](../architecture/API.md).
