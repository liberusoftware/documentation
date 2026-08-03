# API implementation standard

APIs expose stable contracts over authorized domain capabilities. The API layer is an adapter, not a second domain model.

- Version public contracts, document authentication, permissions, tenancy, rate limits, validation, pagination, errors, idempotency, and concurrency.
- Return purpose-built resources/read models and RFC 9457-compatible errors where defined by the ecosystem.
- Authorize before protected queries and mutations; redact sensitive fields by policy and context.
- Make external callbacks verifiable, replay-safe, deduplicated, observable, and reconcilable.
- Generate or contract-test references from the versioned schema and keep examples executable.

See [architecture/API.md](../architecture/API.md), [OpenAPI](https://spec.openapis.org/oas/latest.html), and [Laravel API resources](https://laravel.com/docs/13.x/eloquent-resources).

## Delivery checklist

Before release, record the owning core module, audience, data classification, route prefix, operation IDs, authentication, scopes, policy, tenant/team behavior, limits, error contract, idempotency, concurrency, and deprecation plan. Test the happy path, denial, wrong tenant, invalid input, duplicate/replay, timeout, partial failure, and recovery path. Keep the same contract usable by personal, SME, and enterprise deployments; scale infrastructure without changing domain ownership.
