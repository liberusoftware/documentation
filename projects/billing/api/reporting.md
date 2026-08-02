# Billing: Reporting API

## Canonical one-to-one API module specification

**API package:** `module-billing-reporting-api`
**Matching domain module:** `billing-reporting`
**Application:** Billing
**Source feature:** [Reporting](../features/reporting.md)
**Architecture:** [API.md](../BILLING.md) · [MODULES.md](../BILLING.md) · [TESTING.md](../BILLING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Reporting domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- MRR/ARR
- churn
- aging
- revenue
- tax
- usage
- provisioning
- collection
- provider metrics

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Use `/api/v1/billing/reporting` as the default module route prefix unless the application owns and documents a compatible façade path.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Base path:** `/api/v1/billing/reporting`

These examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.

| Method   | Endpoint                                                   | Purpose                                       | Possible request data                                                                         |
| -------- | ---------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `GET`    | `/api/v1/billing/reporting?page[size]=25&sort=-created_at` | List authorized resources                     | Query parameters for pagination, filtering, sorting, field selection, and documented includes |
| `GET`    | `/api/v1/billing/reporting/{id}`                           | Retrieve one resource                         | Opaque resource `id` in the path; no request body                                             |
| `POST`   | `/api/v1/billing/reporting`                                | Create a resource                             | JSON body using the module schema and required team/context fields                            |
| `PATCH`  | `/api/v1/billing/reporting/{id}`                           | Update permitted fields                       | JSON body containing changed fields and `If-Match` when concurrency is supported              |
| `DELETE` | `/api/v1/billing/reporting/{id}`                           | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted           |
| `POST`   | `/api/v1/billing/reporting/{id}/<explicit-action>`         | Execute a documented domain action            | Action-specific JSON body and `Idempotency-Key` for retryable writes                          |

Example create request (illustrative fields only):

`json
{
  "mrr_arr": "example-value",
  "churn": "example-value",
  "aging": "example-value"
}
`

Example request headers:

`http
Accept: application/json
Authorization: Bearer YOUR_SANCTUM_TOKEN
Content-Type: application/json
Idempotency-Key: 01JEXAMPLEIDEMPOTENCYKEY
X-Request-ID: 01JEXAMPLEREQUESTID
`

Successful reads and writes return the standard `data` envelope from [API.md](../BILLING.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.

## 4. OpenAPI schema

This module owns a versioned OpenAPI 3.1 fragment for `billing-reporting`. Keep the fragment at the repository's declared OpenAPI path, normally `openapi/v1/billing-reporting.yaml`, and aggregate it only through the host application's API manifest. The fragment must document the base path, operation IDs, security requirements, parameters, request bodies, response envelopes, reusable schemas, errors, pagination, idempotency, concurrency, and deprecation metadata.

### Required schema elements

- Use stable operation IDs such as `billing.reporting.list`, `billing.reporting.get`, `billing.reporting.create`, `billing.reporting.update`, and `billing.reporting.delete`; use an explicit domain action ID when applicable.
- Define the module's resource schema as `BillingReportingResource` with opaque `id`, stable `type`, field classification, relationships, state, timestamps, and only authorized attributes.
- Document possible module fields including `mrr_arr`, `churn`, `aging`, `revenue`, `tax`, `usage`; each field must state its type, required/nullable behavior, validation, example, sensitivity, and read/write authorization.
- Define request schemas separately from response schemas, use `snake_case`, and document team/context, pagination, filter, sort, include, `If-Match`, and `Idempotency-Key` behavior.
- Reuse the standard `data`, `links`, `meta`, and RFC 9457 Problem Details shapes from [API.md](../BILLING.md); do not serialize Eloquent models automatically.

### Minimal fragment example

`yaml
openapi: 3.1.0
info:
  title: billing reporting API
  version: 1.0.0
paths:
  /api/v1/billing/reporting:
    get:
      operationId: billing.reporting.list
      security:
        - sanctum: []
      parameters:
        - $ref: '#/components/parameters/PageSize'
      responses:
        '200':
          $ref: '#/components/responses/ResourceCollection'
components:
  parameters:
    PageSize:
      name: page[size]
      in: query
      schema:
        type: integer
        minimum: 1
        maximum: 100
  securitySchemes:
    sanctum:
      type: http
      scheme: bearer
      bearerFormat: Sanctum
  schemas:
    BillingReportingResource:
      type: object
      required: [id, type, attributes]
      properties:
        id:
          type: string
          description: Opaque Liberu resource identifier.
        type:
          type: string
          const: billing-reporting
        attributes:
          type: object
          additionalProperties: true
    ResourceCollection:
      type: object
      required: [data]
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/BillingReportingResource'
  responses:
    ResourceCollection:
      description: Authorized paginated resources.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ResourceCollection'
`

The example is a contract outline, not a substitute for the complete module schema: replace `additionalProperties` with explicit fields and add create/update/action schemas before release. Validate the fragment, bundle it into the application specification, run breaking-change detection against the supported release, and generate typed clients only from the released specification.

**References:** [OpenAPI 3.1 specification](https://spec.openapis.org/oas/v3.1.0) · [OpenAPI and contract registry](../../../architecture/API.md#8-openapi-and-contract-registry) · [Module API design](../../../architecture/API.md#19-module-api-design) · [Response conventions](../../../architecture/API.md#10-response-conventions)

## 5. Audience and operation matrix

| Audience                       | Default exposure                    | Required controls                                                                      |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| Public/anonymous               | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls         |
| Authenticated customer/partner | Explicit allowlist                  | Tenant/resource ownership, purpose-specific scopes, field policy                       |
| Staff/administrator            | Explicit allowlist                  | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client     | Explicit allowlist                  | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas         |

Every exposed operation must map to one audience, domain query/action, permission/scope, request/response schema, rate limit, idempotency/concurrency policy, audit event, and test set. Unmapped operations fail CI.

## 6. Implementation strategy

- Keep routes, controllers/handlers, requests, API resources, OpenAPI fragments, and transport tests in this API package.
- Validate shape at the request boundary and enforce authoritative invariants again in the domain action.
- Resolve tenant and actor context from trusted authentication/application routing; never grant context from a caller-supplied tenant identifier alone.
- Authorize field visibility as well as record/action access, and return concealment-safe errors where enumeration is a risk.
- Use idempotency keys for retryable writes, ETags/`If-Match` for relevant concurrent updates, and asynchronous operation resources for slow/bulk/provider-dependent work.
- Compose cross-module workflows in the application layer; do not query or mutate another module's private storage from this API package.

## 7. Security, resilience, and observability

- Threat-model authentication, authorization, tenant isolation, mass assignment, object references, abusive queries, uploads/downloads, webhooks, and sensitive data.
- Bound pagination, filters, includes, payloads, batch sizes, timeouts, and retry budgets.
- Redact credentials and protected data from logs and errors while recording request, correlation, API/module/version, tenant, principal, operation, status, latency, rate-limit, and idempotency outcomes.
- Define availability, latency, error-rate and queued-operation objectives plus alerts and recovery/reconciliation runbooks.

## 8. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Test pagination, filtering, sorting, includes, dates, money, identifiers, enums, idempotency, ETags, async operations, bulk partial failure, and stable Problem Details.
- Add one-to-one architecture tests proving this package depends on and presents only `billing-reporting`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `billing-reporting`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.

## Canonical one-to-one API module specification

**API package:** `module-billing-reporting-api`  
**Matching domain module:** `billing-reporting`  
**Application:** Billing  
**Source feature:** [Reporting](../features/reporting.md)  
**Architecture:** [API.md](../BILLING.md) · [MODULES.md](../BILLING.md) · [TESTING.md](../BILLING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Reporting domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- MRR/ARR
- churn
- aging
- revenue
- tax
- usage
- provisioning
- collection
- provider metrics

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Use `/api/v1/billing/reporting` as the default module route prefix unless the application owns and documents a compatible façade path.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Base path:** `/api/v1/billing/reporting`

These examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.

| Method   | Endpoint                                                   | Purpose                                       | Possible request data                                                                         |
| -------- | ---------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `GET`    | `/api/v1/billing/reporting?page[size]=25&sort=-created_at` | List authorized resources                     | Query parameters for pagination, filtering, sorting, field selection, and documented includes |
| `GET`    | `/api/v1/billing/reporting/{id}`                           | Retrieve one resource                         | Opaque resource `id` in the path; no request body                                             |
| `POST`   | `/api/v1/billing/reporting`                                | Create a resource                             | JSON body using the module schema and required team/context fields                            |
| `PATCH`  | `/api/v1/billing/reporting/{id}`                           | Update permitted fields                       | JSON body containing changed fields and `If-Match` when concurrency is supported              |
| `DELETE` | `/api/v1/billing/reporting/{id}`                           | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted           |
| `POST`   | `/api/v1/billing/reporting/{id}/<explicit-action>`         | Execute a documented domain action            | Action-specific JSON body and `Idempotency-Key` for retryable writes                          |

Example create request (illustrative fields only):

```json
{
  "mrr_arr": "example-value",
  "churn": "example-value",
  "aging": "example-value"
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

Successful reads and writes return the standard `data` envelope from [API.md](../BILLING.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.

## 4. OpenAPI schema

This module owns a versioned OpenAPI 3.1 fragment for `billing-reporting`. Keep the fragment at the repository's declared OpenAPI path, normally `openapi/v1/billing-reporting.yaml`, and aggregate it only through the host application's API manifest. The fragment must document the base path, operation IDs, security requirements, parameters, request bodies, response envelopes, reusable schemas, errors, pagination, idempotency, concurrency, and deprecation metadata.

### Required schema elements

- Use stable operation IDs such as `billing.reporting.list`, `billing.reporting.get`, `billing.reporting.create`, `billing.reporting.update`, and `billing.reporting.delete`; use an explicit domain action ID when applicable.
- Define the module's resource schema as `BillingReportingResource` with opaque `id`, stable `type`, field classification, relationships, state, timestamps, and only authorized attributes.
- Document possible module fields including `mrr_arr`, `churn`, `aging`, `revenue`, `tax`, `usage`; each field must state its type, required/nullable behavior, validation, example, sensitivity, and read/write authorization.
- Define request schemas separately from response schemas, use `snake_case`, and document team/context, pagination, filter, sort, include, `If-Match`, and `Idempotency-Key` behavior.
- Reuse the standard `data`, `links`, `meta`, and RFC 9457 Problem Details shapes from [API.md](../BILLING.md); do not serialize Eloquent models automatically.

### Minimal fragment example

```yaml
openapi: 3.1.0
info:
  title: billing reporting API
  version: 1.0.0
paths:
  /api/v1/billing/reporting:
    get:
      operationId: billing.reporting.list
      security:
        - sanctum: []
      parameters:
        - $ref: "#/components/parameters/PageSize"
      responses:
        "200":
          $ref: "#/components/responses/ResourceCollection"
components:
  parameters:
    PageSize:
      name: page[size]
      in: query
      schema:
        type: integer
        minimum: 1
        maximum: 100
  securitySchemes:
    sanctum:
      type: http
      scheme: bearer
      bearerFormat: Sanctum
  schemas:
    BillingReportingResource:
      type: object
      required: [id, type, attributes]
      properties:
        id:
          type: string
          description: Opaque Liberu resource identifier.
        type:
          type: string
          const: billing-reporting
        attributes:
          type: object
          additionalProperties: true
    ResourceCollection:
      type: object
      required: [data]
      properties:
        data:
          type: array
          items:
            $ref: "#/components/schemas/BillingReportingResource"
  responses:
    ResourceCollection:
      description: Authorized paginated resources.
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ResourceCollection"
```

The example is a contract outline, not a substitute for the complete module schema: replace `additionalProperties` with explicit fields and add create/update/action schemas before release. Validate the fragment, bundle it into the application specification, run breaking-change detection against the supported release, and generate typed clients only from the released specification.

**References:** [OpenAPI 3.1 specification](https://spec.openapis.org/oas/v3.1.0) · [OpenAPI and contract registry](../../../architecture/API.md#8-openapi-and-contract-registry) · [Module API design](../../../architecture/API.md#19-module-api-design) · [Response conventions](../../../architecture/API.md#10-response-conventions)

## 5. Audience and operation matrix

| Audience                       | Default exposure                    | Required controls                                                                      |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| Public/anonymous               | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls         |
| Authenticated customer/partner | Explicit allowlist                  | Tenant/resource ownership, purpose-specific scopes, field policy                       |
| Staff/administrator            | Explicit allowlist                  | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client     | Explicit allowlist                  | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas         |

Every exposed operation must map to one audience, domain query/action, permission/scope, request/response schema, rate limit, idempotency/concurrency policy, audit event, and test set. Unmapped operations fail CI.

## 6. Implementation strategy

- Keep routes, controllers/handlers, requests, API resources, OpenAPI fragments, and transport tests in this API package.
- Validate shape at the request boundary and enforce authoritative invariants again in the domain action.
- Resolve tenant and actor context from trusted authentication/application routing; never grant context from a caller-supplied tenant identifier alone.
- Authorize field visibility as well as record/action access, and return concealment-safe errors where enumeration is a risk.
- Use idempotency keys for retryable writes, ETags/`If-Match` for relevant concurrent updates, and asynchronous operation resources for slow/bulk/provider-dependent work.
- Compose cross-module workflows in the application layer; do not query or mutate another module's private storage from this API package.

## 7. Security, resilience, and observability

- Threat-model authentication, authorization, tenant isolation, mass assignment, object references, abusive queries, uploads/downloads, webhooks, and sensitive data.
- Bound pagination, filters, includes, payloads, batch sizes, timeouts, and retry budgets.
- Redact credentials and protected data from logs and errors while recording request, correlation, API/module/version, tenant, principal, operation, status, latency, rate-limit, and idempotency outcomes.
- Define availability, latency, error-rate and queued-operation objectives plus alerts and recovery/reconciliation runbooks.

## 8. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Test pagination, filtering, sorting, includes, dates, money, identifiers, enums, idempotency, ETags, async operations, bulk partial failure, and stable Problem Details.
- Add one-to-one architecture tests proving this package depends on and presents only `billing-reporting`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `billing-reporting`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
