# CRM: Sales Engagement API

## Canonical one-to-one API module specification

**API package:** `module-crm-sales-engagement-api`  
**Matching domain module:** `crm-sales-engagement`  
**Application:** CRM  
**Source feature:** [Sales Engagement](../../features/crm/sales-engagement.md)  
**Architecture:** [API.md](../../API.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Sales Engagement domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Sequences/cadences
- multi-channel steps
- templates/snippets
- task queues
- enrollment/re-entry
- throttles
- timezone windows
- reply/meeting stop rules
- experiments

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Use `/api/v1/crm/sales-engagement` as the default module route prefix unless the application owns and documents a compatible façade path.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Base path:** `/api/v1/crm/sales-engagement`

These examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.

| Method | Endpoint | Purpose | Possible request data |
|---|---|---|---|
| `GET` | `/api/v1/crm/sales-engagement?page[size]=25&sort=-created_at` | List authorized resources | Query parameters for pagination, filtering, sorting, field selection, and documented includes |
| `GET` | `/api/v1/crm/sales-engagement/{id}` | Retrieve one resource | Opaque resource `id` in the path; no request body |
| `POST` | `/api/v1/crm/sales-engagement` | Create a resource | JSON body using the module schema and required team/context fields |
| `PATCH` | `/api/v1/crm/sales-engagement/{id}` | Update permitted fields | JSON body containing changed fields and `If-Match` when concurrency is supported |
| `DELETE` | `/api/v1/crm/sales-engagement/{id}` | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted |
| `POST` | `/api/v1/crm/sales-engagement/{id}/<explicit-action>` | Execute a documented domain action | Action-specific JSON body and `Idempotency-Key` for retryable writes |

Example create request (illustrative fields only):

```json
{
  "sequences_cadences": "example-value",
  "multi_channel_steps": "example-value",
  "templates_snippets": "example-value"
}
```

Example request headers:

```http
Accept: application/json
Authorization: Bearer YOUR_SANCTUM_TOKEN
Content-Type: application/json
Idempotency-Key: 01JEXAMPLEIDEMPOTENCYKEY
X-Request-ID: 01JEXAMPLEREQUESTID
```

Successful reads and writes return the standard `data` envelope from [API.md](../../API.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.

## 4. Audience and operation matrix

| Audience | Default exposure | Required controls |
|---|---|---|
| Public/anonymous | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls |
| Authenticated customer/partner | Explicit allowlist | Tenant/resource ownership, purpose-specific scopes, field policy |
| Staff/administrator | Explicit allowlist | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client | Explicit allowlist | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas |

Every exposed operation must map to one audience, domain query/action, permission/scope, request/response schema, rate limit, idempotency/concurrency policy, audit event, and test set. Unmapped operations fail CI.

## 5. Implementation strategy

- Keep routes, controllers/handlers, requests, API resources, OpenAPI fragments, and transport tests in this API package.
- Validate shape at the request boundary and enforce authoritative invariants again in the domain action.
- Resolve tenant and actor context from trusted authentication/application routing; never grant context from a caller-supplied tenant identifier alone.
- Authorize field visibility as well as record/action access, and return concealment-safe errors where enumeration is a risk.
- Use idempotency keys for retryable writes, ETags/`If-Match` for relevant concurrent updates, and asynchronous operation resources for slow/bulk/provider-dependent work.
- Compose cross-module workflows in the application layer; do not query or mutate another module's private storage from this API package.

## 6. Security, resilience, and observability

- Threat-model authentication, authorization, tenant isolation, mass assignment, object references, abusive queries, uploads/downloads, webhooks, and sensitive data.
- Bound pagination, filters, includes, payloads, batch sizes, timeouts, and retry budgets.
- Redact credentials and protected data from logs and errors while recording request, correlation, API/module/version, tenant, principal, operation, status, latency, rate-limit, and idempotency outcomes.
- Define availability, latency, error-rate and queued-operation objectives plus alerts and recovery/reconciliation runbooks.

## 7. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Test pagination, filtering, sorting, includes, dates, money, identifiers, enums, idempotency, ETags, async operations, bulk partial failure, and stable Problem Details.
- Add one-to-one architecture tests proving this package depends on and presents only `crm-sales-engagement`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 8. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `crm-sales-engagement`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
