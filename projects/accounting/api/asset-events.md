# Accounting: Asset Events API\n\n## Canonical one-to-one API module specification\n\n**API package:** `module-accounting-asset-events-api`  \n**Matching domain module:** `accounting-asset-events`  \n**Application:** Accounting  \n**Source feature:** [Asset Events](../features/asset-events.md)  \n**Architecture:** [API.md](../ACCOUNTING.md) · [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md)\n\n## 1. Purpose and ownership\n\nThis optional API presentation package exposes approved HTTP operations for the Asset Events domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.\n\nThe domain capability includes:\n\n- Transfer\n- improvement\n- revaluation\n- impairment\n- disposal\n- sale\n- write-off\n- gain/loss\n- complete history\n\nInstallation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.\n\n## 2. Contract design\n\n- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.\n- Use `/api/v1/accounting/asset-events` as the default module route prefix unless the application owns and documents a compatible façade path.\n- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.\n- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.\n- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.\n\n## 3. Endpoint examples\n\n**Base path:** `/api/v1/accounting/asset-events`\n\nThese examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.\n\n| Method | Endpoint | Purpose | Possible request data |\n|---|---|---|---|\n| `GET` | `/api/v1/accounting/asset-events?page[size]=25&sort=-created_at` | List authorized resources | Query parameters for pagination, filtering, sorting, field selection, and documented includes |\n| `GET` | `/api/v1/accounting/asset-events/{id}` | Retrieve one resource | Opaque resource `id` in the path; no request body |\n| `POST` | `/api/v1/accounting/asset-events` | Create a resource | JSON body using the module schema and required team/context fields |\n| `PATCH` | `/api/v1/accounting/asset-events/{id}` | Update permitted fields | JSON body containing changed fields and `If-Match` when concurrency is supported |\n| `DELETE` | `/api/v1/accounting/asset-events/{id}` | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted |\n| `POST` | `/api/v1/accounting/asset-events/{id}/<explicit-action>` | Execute a documented domain action | Action-specific JSON body and `Idempotency-Key` for retryable writes |\n\nExample create request (illustrative fields only):\n\n```json\n{\n  "transfer": "example-value",\n  "improvement": "example-value",\n  "revaluation": "example-value"\n}\n```\n\nExample request headers:\n\n```http\nAccept: application/json\nAuthorization: Bearer YOUR_SANCTUM_TOKEN\nContent-Type: application/json\nIdempotency-Key: 01JEXAMPLEIDEMPOTENCYKEY\nX-Request-ID: 01JEXAMPLEREQUESTID\n```\n\nSuccessful reads and writes return the standard `data` envelope from [API.md](../ACCOUNTING.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.\n\n## 4. OpenAPI schema\n\nThis module owns a versioned OpenAPI 3.1 fragment for `accounting-asset-events`. Keep the fragment at the repository's declared OpenAPI path, normally `openapi/v1/accounting-asset-events.yaml`, and aggregate it only through the host application's API manifest. The fragment must document the base path, operation IDs, security requirements, parameters, request bodies, response envelopes, reusable schemas, errors, pagination, idempotency, concurrency, and deprecation metadata.\n\n### Required schema elements\n\n- Use stable operation IDs such as `accounting.asset.events.list`, `accounting.asset.events.get`, `accounting.asset.events.create`, `accounting.asset.events.update`, and `accounting.asset.events.delete`; use an explicit domain action ID when applicable.\n- Define the module's resource schema as `AccountingAssetEventsResource` with opaque `id`, stable `type`, field classification, relationships, state, timestamps, and only authorized attributes.\n- Document possible module fields including `transfer`, `improvement`, `revaluation`, `impairment`, `disposal`, `sale`; each field must state its type, required/nullable behavior, validation, example, sensitivity, and read/write authorization.\n- Define request schemas separately from response schemas, use `snake_case`, and document team/context, pagination, filter, sort, include, `If-Match`, and `Idempotency-Key` behavior.\n- Reuse the standard `data`, `links`, `meta`, and RFC 9457 Problem Details shapes from [API.md](../ACCOUNTING.md); do not serialize Eloquent models automatically.\n\n### Minimal fragment example\n\n```yaml\nopenapi: 3.1.0\ninfo:\n  title: accounting asset events API\n  version: 1.0.0\npaths:\n  /api/v1/accounting/asset-events:\n    get:\n      operationId: accounting.asset.events.list\n      security:\n        - sanctum: []\n      parameters:\n        - $ref: '#/components/parameters/PageSize'\n      responses:\n        '200':\n          $ref: '#/components/responses/ResourceCollection'\ncomponents:\n  parameters:\n    PageSize:\n      name: page[size]\n      in: query\n      schema:\n        type: integer\n        minimum: 1\n        maximum: 100\n  securitySchemes:\n    sanctum:\n      type: http\n      scheme: bearer\n      bearerFormat: Sanctum\n  schemas:\n    AccountingAssetEventsResource:\n      type: object\n      required: [id, type, attributes]\n      properties:\n        id:\n          type: string\n          description: Opaque Liberu resource identifier.\n        type:\n          type: string\n          const: accounting-asset-events\n        attributes:\n          type: object\n          additionalProperties: true\n    ResourceCollection:\n      type: object\n      requir…172152 tokens truncated….\n- **Purchase/sales descriptions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Accounts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Tax defaults:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Units:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Costs/prices:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Ecommerce references:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n\n## 3. Vue 3 + Inertia 3 implementation\n\n- Register a stable `module-accounting-product-and-service-items-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.\n- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.\n- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `items-services`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `codes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `purchase-sales-descriptions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `accounts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `tax-defaults`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `units`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `costs-prices`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `ecommerce-references`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n\n## 4. API contract and Inertia consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.\n- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.\n- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `accounting-product-and-service-items` one-to-one.\n- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.\n- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

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

| Method | Endpoint | Purpose | Possible request data |
|---|---|---|---|
| `GET` | `/api/v1/accounting/asset-events?page[size]=25&sort=-created_at` | List authorized resources | Query parameters for pagination, filtering, sorting, field selection, and documented includes |
| `GET` | `/api/v1/accounting/asset-events/{id}` | Retrieve one resource | Opaque resource `id` in the path; no request body |
| `POST` | `/api/v1/accounting/asset-events` | Create a resource | JSON body using the module schema and required team/context fields |
| `PATCH` | `/api/v1/accounting/asset-events/{id}` | Update permitted fields | JSON body containing changed fields and `If-Match` when concurrency is supported |
| `DELETE` | `/api/v1/accounting/asset-events/{id}` | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted |
| `POST` | `/api/v1/accounting/asset-events/{id}/<explicit-action>` | Execute a documented domain action | Action-specific JSON body and `Idempotency-Key` for retryable writes |

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
      required: [data]
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/AccountingAssetEventsResource'
  responses:
    ResourceCollection:
      description: Authorized paginated resources.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ResourceCollection'
```

The example is a contract outline, not a substitute for the complete module schema: replace `additionalProperties` with explicit fields and add create/update/action schemas before release. Validate the fragment, bundle it into the application specification, run breaking-change detection against the supported release, and generate typed clients only from the released specification.

**References:** [OpenAPI 3.1 specification](https://spec.openapis.org/oas/v3.1.0) · [OpenAPI and contract registry](../../../architecture/API.md#8-openapi-and-contract-registry) · [Module API design](../../../architecture/API.md#19-module-api-design) · [Response conventions](../../../architecture/API.md#10-response-conventions)

## 5. Audience and operation matrix

| Audience | Default exposure | Required controls |
|---|---|---|
| Public/anonymous | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls |
| Authenticated customer/partner | Explicit allowlist | Tenant/resource ownership, purpose-specific scopes, field policy |
| Staff/administrator | Explicit allowlist | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client | Explicit allowlist | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas |

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
- Add one-to-one architecture tests proving this package depends on and presents only `accounting-asset-events`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `accounting-asset-events`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
