# Browser Game: Live Ops API\n\n## Canonical one-to-one API module specification\n\n**API package:** `module-browser-game-live-ops-api` \n**Matching domain module:** `browser-game-live-ops` \n**Application:** Browser Game \n**Source feature:** [Live Ops](../features/live-ops.md) \n**Architecture:** [API.md](../BROWSER-GAME.md) · [MODULES.md](../BROWSER-GAME.md) · [TESTING.md](../BROWSER-GAME.md)\n\n## 1. Purpose and ownership\n\nThis optional API presentation package exposes approved HTTP operations for the Live Ops domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.\n\nThe domain capability includes:\n\n- Daily activities\n- events\n- seasons\n- content schedules\n- announcements\n- grants\n- rollback\n\nInstallation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.\n\n## 2. Contract design\n\n- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.\n- Use `/api/v1/browser-game/live-ops` as the default module route prefix unless the application owns and documents a compatible façade path.\n- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.\n- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.\n- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.\n\n## 3. Endpoint examples\n\n**Base path:** `/api/v1/browser-game/live-ops`\n\nThese examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.\n\n| Method | Endpoint | Purpose | Possible request data |\n|---|---|---|---|\n| `GET` | `/api/v1/browser-game/live-ops?page[size]=25&sort=-created_at` | List authorized resources | Query parameters for pagination, filtering, sorting, field selection, and documented includes |\n| `GET` | `/api/v1/browser-game/live-ops/{id}` | Retrieve one resource | Opaque resource `id` in the path; no request body |\n| `POST` | `/api/v1/browser-game/live-ops` | Create a resource | JSON body using the module schema and required team/context fields |\n| `PATCH` | `/api/v1/browser-game/live-ops/{id}` | Update permitted fields | JSON body containing changed fields and `If-Match` when concurrency is supported |\n| `DELETE` | `/api/v1/browser-game/live-ops/{id}` | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted |\n| `POST` | `/api/v1/browser-game/live-ops/{id}/<explicit-action>` | Execute a documented domain action | Action-specific JSON body and `Idempotency-Key` for retryable writes |\n\nExample create request (illustrative fields only):\n\n`json\n{\n  "daily_activities": "example-value",\n  "events": "example-value",\n  "seasons": "example-value"\n}\n`\n\nExample request headers:\n\n`http\nAccept: application/json\nAuthorization: Bearer YOUR_SANCTUM_TOKEN\nContent-Type: application/json\nIdempotency-Key: 01JEXAMPLEIDEMPOTENCYKEY\nX-Request-ID: 01JEXAMPLEREQUESTID\n`\n\nSuccessful reads and writes return the standard `data` envelope from [API.md](../BROWSER-GAME.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.\n\n## 4. OpenAPI schema\n\nThis module owns a versioned OpenAPI 3.1 fragment for `browser-game-live-ops`. Keep the fragment at the repository's declared OpenAPI path, normally `openapi/v1/browser-game-live-ops.yaml`, and aggregate it only through the host application's API manifest. The fragment must document the base path, operation IDs, security requirements, parameters, request bodies, response envelopes, reusable schemas, errors, pagination, idempotency, concurrency, and deprecation metadata.\n\n### Required schema elements\n\n- Use stable operation IDs such as `browser.game.live.ops.list`, `browser.game.live.ops.get`, `browser.game.live.ops.create`, `browser.game.live.ops.update`, and `browser.game.live.ops.delete`; use an explicit domain action ID when applicable.\n- Define the module's resource schema as `BrowserGameLiveOpsResource` with opaque `id`, stable `type`, field classification, relationships, state, timestamps, and only authorized attributes.\n- Document possible module fields including `daily_activities`, `events`, `seasons`, `content_schedules`, `announcements`, `grants`; each field must state its type, required/nullable behavior, validation, example, sensitivity, and read/write authorization.\n- Define request schemas separately from response schemas, use `snake_case`, and document team/context, pagination, filter, sort, include, `If-Match`, and `Idempotency-Key` behavior.\n- Reuse the standard `data`, `links`, `meta`, and RFC 9457 Problem Details shapes from [API.md](../BROWSER-GAME.md); do not serialize Eloquent models automatically.\n\n### Minimal fragment example\n\n`yaml\nopenapi: 3.1.0\ninfo:\n  title: browser game live ops API\n  version: 1.0.0\npaths:\n  /api/v1/browser-game/live-ops:\n    get:\n      operationId: browser.game.live.ops.list\n      security:\n        - sanctum: []\n      parameters:\n        - $ref: '#/components/parameters/PageSize'\n      responses:\n        '200':\n          $ref: '#/components/responses/ResourceCollection'\ncomponents:\n  parameters:\n    PageSize:\n      name: page[size]\n      in: query\n      schema:\n        type: integer\n        minimum: 1\n        maximum: 100\n  securitySchemes:\n    sanctum:\n      type: http\n      scheme: bearer\n      bearerFormat: Sanctum\n  schemas:\n    BrowserGameLiveOpsResource:\n      type: object\n      required: [id, type, attributes]\n      properties:\n        id:\n          type: string\n          description: Opaque Liberu resource identifier.\n        type:\n          type: string\n          const: browser-game-live-ops\n        attributes:\n          type: object\n          additionalProperties: true\n    ResourceCollection:\n      type: object\n      required: [data]\n      properties:\n        data:\n          type: array\n          items:\n            $ref: '#/components/schemas/BrowserGameLiveOpsResource'\n  responses:\n    ResourceCollection:\n      description: Authorized paginated resources.\n      content:\n        application/json:\n          schema:\n            $ref: '#/components/schemas/ResourceCollection'\n`\n\nThe example is a contract outline, not a substitute for the complete module schema: replace `additionalProperties` with explicit fields and add create/update/action schemas before release. Validate the fragment, bundle it into the application specification, run breaking-change detection against the supported release, and generate typed clients only from the released specification.\n\n**References:** [OpenAPI 3.1 specification](https://spec.openapis.org/oas/v3.1.0) · [OpenAPI and contract registry](../../../architecture/API.md#8-openapi-and-contract-registry) · [Module API design](../../../architecture/API.md#19-module-api-design) · [Response conventions](../../../architecture/API.md#10-response-conventions)\n\n## 5. Audience and operation matrix\n\n| Audience | Default exposure | Required controls |\n|---|---|---|\n| Public/anonymous | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls |\n| Authenticated customer/partner | Explicit allowlist | Tenant/resource ownership, purpose-specific scopes, field policy |\n| Staff/administrator | Explicit allowlist | Role/permission policy, tenant context, recent authentication for risky actions, audit |\n| Service/integration client | Explicit allowlist | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas |\n\nEvery exposed operation must map to one audience, domain query/action, permission/scope, request/response schema, rate limit, idempotency/concurrency policy, audit event, and test set. Unmapped operations fail CI.\n\n## 6. Implementation strategy\n\n- Keep routes, controllers/handlers, requests, API resources, OpenAPI fragments, and transport tests in this API package.\n- Validate shape at the request boundary and enforce authoritative invariants again in the domain action.\n- Resolve tenant and actor context from trusted authentication/application routing; never grant context from a caller-supplied tenant identifier alone.\n- Authorize field visibility as well as record/action access, and return concealment-safe errors where enumeration is a risk.\n- Use idempotency keys for retryable writes, ETags/`If-Match` for relevant concurrent updates, and asynchronous operation resources for slow/bulk/provider-dependent work.\n- Compose cross-module workflows in the application layer; do not query or mutate another module's private storage from this API package.\n\n## 7. Security, resilience, and observability\n\n- Threat-model authentication, authorization, tenant isolation, mass assignment, object references, abusive queries, uploads/downloads, webhooks, and sensitive data.\n- Bound pagination, filters, includes, payloads, batch sizes, timeouts, and retry budgets.\n- Redact credentials and protected data from logs and errors while recording request, correlation, API/module/version, tenant, principal, operation, status, latency, rate-limit, and idempotency outcomes.\n- Define availability, latency, error-rate and queued-operation objectives plus alerts and recovery/reconciliation runbooks.\n\n## 8. Verification strategy\n\n- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.\n- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.\n- Test pagination, filtering, sorting, includes, dates, money, identifiers, enums, idempotency, ETags, async operations, bulk partial failure, and stable Problem Details.\n- Add one-to-one architecture tests proving this package depends on and presents only `browser-game-live-ops`.\n- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.\n- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.\n\n## 9. Definition of done\n\n- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `browser-game-live-ops`.\n- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.\n- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.\n- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.\n- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.

## Canonical one-to-one API module specification

**API package:** `module-browser-game-live-ops-api`  
**Matching domain module:** `browser-game-live-ops`  
**Application:** Browser Game  
**Source feature:** [Live Ops](../features/live-ops.md)  
**Architecture:** [API.md](../BROWSER-GAME.md) · [MODULES.md](../BROWSER-GAME.md) · [TESTING.md](../BROWSER-GAME.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Live Ops domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Daily activities
- events
- seasons
- content schedules
- announcements
- grants
- rollback

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Use `/api/v1/browser-game/live-ops` as the default module route prefix unless the application owns and documents a compatible façade path.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Base path:** `/api/v1/browser-game/live-ops`

These examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.

| Method   | Endpoint                                                       | Purpose                                       | Possible request data                                                                         |
| -------- | -------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `GET`    | `/api/v1/browser-game/live-ops?page[size]=25&sort=-created_at` | List authorized resources                     | Query parameters for pagination, filtering, sorting, field selection, and documented includes |
| `GET`    | `/api/v1/browser-game/live-ops/{id}`                           | Retrieve one resource                         | Opaque resource `id` in the path; no request body                                             |
| `POST`   | `/api/v1/browser-game/live-ops`                                | Create a resource                             | JSON body using the module schema and required team/context fields                            |
| `PATCH`  | `/api/v1/browser-game/live-ops/{id}`                           | Update permitted fields                       | JSON body containing changed fields and `If-Match` when concurrency is supported              |
| `DELETE` | `/api/v1/browser-game/live-ops/{id}`                           | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted           |
| `POST`   | `/api/v1/browser-game/live-ops/{id}/<explicit-action>`         | Execute a documented domain action            | Action-specific JSON body and `Idempotency-Key` for retryable writes                          |

Example create request (illustrative fields only):

```json
{
  "daily_activities": "example-value",
  "events": "example-value",
  "seasons": "example-value"
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

Successful reads and writes return the standard `data` envelope from [API.md](../BROWSER-GAME.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.

## 4. OpenAPI schema

This module owns a versioned OpenAPI 3.1 fragment for `browser-game-live-ops`. Keep the fragment at the repository's declared OpenAPI path, normally `openapi/v1/browser-game-live-ops.yaml`, and aggregate it only through the host application's API manifest. The fragment must document the base path, operation IDs, security requirements, parameters, request bodies, response envelopes, reusable schemas, errors, pagination, idempotency, concurrency, and deprecation metadata.

### Required schema elements

- Use stable operation IDs such as `browser.game.live.ops.list`, `browser.game.live.ops.get`, `browser.game.live.ops.create`, `browser.game.live.ops.update`, and `browser.game.live.ops.delete`; use an explicit domain action ID when applicable.
- Define the module's resource schema as `BrowserGameLiveOpsResource` with opaque `id`, stable `type`, field classification, relationships, state, timestamps, and only authorized attributes.
- Document possible module fields including `daily_activities`, `events`, `seasons`, `content_schedules`, `announcements`, `grants`; each field must state its type, required/nullable behavior, validation, example, sensitivity, and read/write authorization.
- Define request schemas separately from response schemas, use `snake_case`, and document team/context, pagination, filter, sort, include, `If-Match`, and `Idempotency-Key` behavior.
- Reuse the standard `data`, `links`, `meta`, and RFC 9457 Problem Details shapes from [API.md](../BROWSER-GAME.md); do not serialize Eloquent models automatically.

### Minimal fragment example

```yaml
openapi: 3.1.0
info:
  title: browser game live ops API
  version: 1.0.0
paths:
  /api/v1/browser-game/live-ops:
    get:
      operationId: browser.game.live.ops.list
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
    BrowserGameLiveOpsResource:
      type: object
      required: [id, type, attributes]
      properties:
        id:
          type: string
          description: Opaque Liberu resource identifier.
        type:
          type: string
          const: browser-game-live-ops
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
            $ref: "#/components/schemas/BrowserGameLiveOpsResource"
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
- Add one-to-one architecture tests proving this package depends on and presents only `browser-game-live-ops`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `browser-game-live-ops`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
