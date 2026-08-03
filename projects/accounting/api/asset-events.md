# Accounting: Asset Events API

## Canonical one-to-one API module specification

**API package:** `module-accounting-asset-events-api`
**Matching domain module:** `accounting-asset-events`
**Application:** Accounting
**Source feature:** [Asset Events](../features/asset-events.md)
**Architecture:** [API.md](../ACCOUNTING.md) · [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Asset Events domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Transfer
- improvement
- revaluation
- impairment
- disposal
- sale
- write-off
- gain/loss
- complete history

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Use `/api/v1/accounting/asset-events` as the default module route prefix unless the application owns and documents a compatible façade path.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Base path:** `/api/v1/accounting/asset-events`

These examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.

| Method   | Endpoint                                                         | Purpose                                       | Possible request data                                                                         |
| -------- | ---------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `GET`    | `/api/v1/accounting/asset-events?page[size]=25&sort=-created_at` | List authorized resources                     | Query parameters for pagination, filtering, sorting, field selection, and documented includes |
| `GET`    | `/api/v1/accounting/asset-events/{id}`                           | Retrieve one resource                         | Opaque resource `id` in the path; no request body                                             |
| `POST`   | `/api/v1/accounting/asset-events`                                | Create a resource                             | JSON body using the module schema and required team/context fields                            |
| `PATCH`  | `/api/v1/accounting/asset-events/{id}`                           | Update permitted fields                       | JSON body containing changed fields and `If-Match` when concurrency is supported              |
| `DELETE` | `/api/v1/accounting/asset-events/{id}`                           | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted           |
| `POST`   | `/api/v1/accounting/asset-events/{id}/<explicit-action>`         | Execute a documented domain action            | Action-specific JSON body and `Idempotency-Key` for retryable writes                          |

Example create request (illustrative fields only):

```json
{
  "transfer": "example-value",
  "improvement": "example-value",
  "revaluation": "example-value"
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

Successful reads and writes return the standard `data` envelope from [API.md](../ACCOUNTING.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.

## 4. OpenAPI schema

This module owns a versioned OpenAPI 3.1 fragment for `accounting-asset-events`. Keep the fragment at the repository's declared OpenAPI path, normally `openapi/v1/accounting-asset-events.yaml`, and aggregate it only through the host application's API manifest. The fragment must document the base path, operation IDs, security requirements, parameters, request bodies, response envelopes, reusable schemas, errors, pagination, idempotency, concurrency, and deprecation metadata.

### Required schema elements

- Use stable operation IDs such as `accounting.asset.events.list`, `accounting.asset.events.get`, `accounting.asset.events.create`, `accounting.asset.events.update`, and `accounting.asset.events.delete`; use an explicit domain action ID when applicable.
- Define the module's resource schema as `AccountingAssetEventsResource` with opaque `id`, stable `type`, field classification, relationships, state, timestamps, and only authorized attributes.
- Document possible module fields including `transfer`, `improvement`, `revaluation`, `impairment`, `disposal`, `sale`; each field must state its type, required/nullable behavior, validation, example, sensitivity, and read/write authorization.
- Define request schemas separately from response schemas, use `snake_case`, and document team/context, pagination, filter, sort, include, `If-Match`, and `Idempotency-Key` behavior.
- Reuse the standard `data`, `links`, `meta`, and RFC 9457 Problem Details shapes from [API.md](../ACCOUNTING.md); do not serialize Eloquent models automatically.

### Minimal fragment example

```yaml
openapi: 3.1.0
info:
  title: accounting asset events API
  version: 1.0.0
paths:
  /api/v1/accounting/asset-events:
    get:
      operationId: accounting.asset.events.list
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
    AccountingAssetEventsResource:
      type: object
      required: [id, type, attributes]
      properties:
        id:
          type: string
          description: Opaque Liberu resource identifier.
        type:
          type: string
          const: accounting-asset-events
        attributes:
          type: object
          additionalProperties: true
    ResourceCollection:
      type: object
      requir…172152 tokens truncated….
- **Purchase/sales descriptions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Accounts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax defaults:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Units:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Costs/prices:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Ecommerce references:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-product-and-service-items-vue-inertia`package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under`resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `items-services`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `codes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `purchase-sales-descriptions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `accounts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tax-defaults`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `units`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `costs-prices`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `ecommerce-references`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router`for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match`accounting-product-and-service-items` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

```
