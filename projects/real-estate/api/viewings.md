# Real Estate: Viewings API

## Canonical one-to-one API module specification

**API package:** `module-real-estate-viewings-api`
**Matching domain module:** `real-estate-viewings`
**Application:** Real Estate
**Source feature:** [Viewings](../features/viewings.md)
**Architecture:** [API.md](../REAL-ESTATE.md) · [MODULES.md](../REAL-ESTATE.md) · [TESTING.md](../REAL-ESTATE.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Viewings domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Availability
- booking
- confirmation
- access
- accompaniment
- reminders
- feedback
- no-shows

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Use `/api/v1/real-estate/viewings` as the default module route prefix unless the application owns and documents a compatible façade path.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Base path:** `/api/v1/real-estate/viewings`

These examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.

| Method   | Endpoint                                                      | Purpose                                       | Possible request data                                                                         |
| -------- | ------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `GET`    | `/api/v1/real-estate/viewings?page[size]=25&sort=-created_at` | List authorized resources                     | Query parameters for pagination, filtering, sorting, field selection, and documented includes |
| `GET`    | `/api/v1/real-estate/viewings/{id}`                           | Retrieve one resource                         | Opaque resource `id` in the path; no request body                                             |
| `POST`   | `/api/v1/real-estate/viewings`                                | Create a resource                             | JSON body using the module schema and required team/context fields                            |
| `PATCH`  | `/api/v1/real-estate/viewings/{id}`                           | Update permitted fields                       | JSON body containing changed fields and `If-Match` when concurrency is supported              |
| `DELETE` | `/api/v1/real-estate/viewings/{id}`                           | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted           |
| `POST`   | `/api/v1/real-estate/viewings/{id}/<explicit-action>`         | Execute a documented domain action            | Action-specific JSON body and `Idempotency-Key` for retryable writes                          |

Example create request (illustrative fields only):

```json
{
  "availability": "example-value",
  "booking": "example-value",
  "confirmation": "example-value"
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

Successful reads and writes return the standard `data` envelope from [API.md](../REAL-ESTATE.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.

## 4. OpenAPI schema

This module owns a versioned OpenAPI 3.1 fragment for `real-estate-viewings`. Keep the fragment at the repository's declared OpenAPI path, normally `openapi/v1/real-estate-viewings.yaml`, and aggregate it only through the host application's API manifest. The fragment must document the base path, operation IDs, security requirements, parameters, request bodies, response envelopes, reusable schemas, errors, pagination, idempotency, concurrency, and deprecation metadata.

### Required schema elements

- Use stable operation IDs such as `real.estate.viewings.list`, `real.estate.viewings.get`, `real.estate.viewings.create`, `real.estate.viewings.update`, and `real.estate.viewings.delete`; use an explicit domain action ID when applicable.
- Define the module's resource schema as `RealEstateViewingsResource` with opaque `id`, stable `type`, field classification, relationships, state, timestamps, and only authorized attributes.
- Document possible module fields including `availability`, `booking`, `confirmation`, `access`, `accompaniment`, `reminders`; each field must state its type, required/nullable behavior, validation, example, sensitivity, and read/write authorization.
- Define request schemas separately from response schemas, use `snake_case`, and document team/context, pagination, filter, sort, include, `If-Match`, and `Idempotency-Key` behavior.
- Reuse the standard `data`, `links`, `meta`, and RFC 9457 Problem Details shapes from [API.md](../REAL-ESTATE.md); do not serialize Eloquent models automatically.

### Minimal fragment example

```yaml
openapi: 3.1.0
info:
  title: real estate viewings API
  version: 1.0.0
paths:
  /api/v1/real-estate/viewings:
    get:
      operationId: real.estate.viewings.list
      security:
        - sanctu…84605 tokens truncated…m context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch`or`useAsyncData`for SSR-safe reads and`$fetch`for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match`real-estate-valuations` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

```
