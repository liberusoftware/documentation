# SAP: Sales and CRM API\n\n## Canonical one-to-one API module specification\n\n**API package:** `module-sap-sales-and-crm-api` \n**Matching domain module:** `sap-sales-and-crm` \n**Application:** SAP \n**Source feature:** [Sales and CRM](../features/sales-and-crm.md) \n**Architecture:** [API.md](../SAP.md) · [MODULES.md](../SAP.md) · [TESTING.md](../SAP.md)\n\n## 1. Purpose and ownership\n\nThis optional API presentation package exposes approved HTTP operations for the Sales and CRM domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.\n\nThe domain capability includes:\n\n- Accounts\n- leads\n- opportunities\n- quotes\n- contracts\n- orders\n- customer success\n- communications\n- forecasts\n\nInstallation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.\n\n## 2. Contract design\n\n- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.\n- Use `/api/v1/sap/sales-and-crm` as the default module route prefix unless the application owns and documents a compatible façade path.\n- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.\n- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.\n- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.\n\n## 3. Endpoint examples\n\n**Base path:** `/api/v1/sap/sales-and-crm`\n\nThese examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.\n\n| Method | Endpoint | Purpose | Possible request data |\n|---|---|---|---|\n| `GET` | `/api/v1/sap/sales-and-crm?page[size]=25&sort=-created_at` | List authorized resources | Query parameters for pagination, filtering, sorting, field selection, and documented includes |\n| `GET` | `/api/v1/sap/sales-and-crm/{id}` | Retrieve one resource | Opaque resource `id` in the path; no request body |\n| `POST` | `/api/v1/sap/sales-and-crm` | Create a resource | JSON body using the module schema and required team/context fields |\n| `PATCH` | `/api/v1/sap/sales-and-crm/{id}` | Update permitted fields | JSON body containing changed fields and `If-Match` when concurrency is supported |\n| `DELETE` | `/api/v1/sap/sales-and-crm/{id}` | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted |\n| `POST` | `/api/v1/sap/sales-and-crm/{id}/<explicit-action>` | Execute a documented domain action | Action-specific JSON body and `Idempotency-Key` for retryable writes |\n\nExample create request (illustrative fields only):\n\n`json\n{\n  "accounts": "example-value",\n  "leads": "example-value",\n  "opportunities": "example-value"\n}\n`\n\nExample request headers:\n\n`http\nAccept: application/json\nAuthorization: Bearer YOUR_SANCTUM_TOKEN\nContent-Type: application/json\nIdempotency-Key: 01JEXAMPLEIDEMPOTENCYKEY\nX-Request-ID: 01JEXAMPLEREQUESTID\n`\n\nSuccessful reads and writes return the standard `data` envelope from [API.md](../SAP.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.\n\n## 4. OpenAPI sche…104272 tokens truncated…ravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.\n\n## 2. Module-specific surfaces\n\n- **Governed metrics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Semantic models:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Reports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Planning:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Forecasts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Data quality:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Lineage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Exports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **AI assistance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n\n## 3. React 19.2 + Inertia 3 implementation\n\n- Register a stable `module-sap-data-and-intelligence-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.\n- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.\n- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `governed-metrics`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `semantic-models`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `reports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `planning`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `forecasts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `data-quality`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `lineage`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `exports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `ai-assistance`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n\n## 4. API contract and Inertia consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.\n- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.\n- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `sap-data-and-intelligence` one-to-one.\n- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.\n- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical one-to-one API module specification

**API package:** `module-sap-sales-and-crm-api`  
**Matching domain module:** `sap-sales-and-crm`  
**Application:** SAP  
**Source feature:** [Sales and CRM](../features/sales-and-crm.md)  
**Architecture:** [API.md](../SAP.md) · [MODULES.md](../SAP.md) · [TESTING.md](../SAP.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Sales and CRM domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Accounts
- leads
- opportunities
- quotes
- contracts
- orders
- customer success
- communications
- forecasts

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Use `/api/v1/sap/sales-and-crm` as the default module route prefix unless the application owns and documents a compatible façade path.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Base path:** `/api/v1/sap/sales-and-crm`

These examples show the normal REST shape. The matching OpenAPI fragment remains authoritative for exact fields, required data, permissions, response schemas, and whether an operation is exposed.

| Method   | Endpoint                                                   | Purpose                                       | Possible request data                                                                         |
| -------- | ---------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `GET`    | `/api/v1/sap/sales-and-crm?page[size]=25&sort=-created_at` | List authorized resources                     | Query parameters for pagination, filtering, sorting, field selection, and documented includes |
| `GET`    | `/api/v1/sap/sales-and-crm/{id}`                           | Retrieve one resource                         | Opaque resource `id` in the path; no request body                                             |
| `POST`   | `/api/v1/sap/sales-and-crm`                                | Create a resource                             | JSON body using the module schema and required team/context fields                            |
| `PATCH`  | `/api/v1/sap/sales-and-crm/{id}`                           | Update permitted fields                       | JSON body containing changed fields and `If-Match` when concurrency is supported              |
| `DELETE` | `/api/v1/sap/sales-and-crm/{id}`                           | Delete, archive, or deactivate when supported | Usually no body; use the documented lifecycle action when deletion is not permitted           |
| `POST`   | `/api/v1/sap/sales-and-crm/{id}/<explicit-action>`         | Execute a documented domain action            | Action-specific JSON body and `Idempotency-Key` for retryable writes                          |

Example create request (illustrative fields only):

```json
{
  "accounts": "example-value",
  "leads": "example-value",
  "opportunities": "example-value"
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

Successful reads and writes return the standard `data` envelope from [API.md](../SAP.md). A create normally returns `201`, an update or query `200`, a successful delete `204`, and a queued or provider-dependent action `202` with an operation resource. Invalid, unauthorized, forbidden, conflicting, throttled, or unavailable requests use the documented HTTP status and RFC 9457 Problem Details shape.

## 4. OpenAPI schema

This module owns a versioned OpenAPI 3.1 fragment for `sap-sales-and-crm`. Keep the fragment at the repository's declared OpenAPI path, normally `openapi/v1/sap-sales-and-crm.yaml`, and aggregate it only through the host application's API manifest. The fragment must document the base path, operation IDs, security requirements, parameters, request bodies, response envelopes, reusable schemas, errors, pagination, idempotency, concurrency, and deprecation metadata.

### Required schema elements

- Use stable operation IDs such as `sap.sales.and.crm.list`, `sap.sales.and.crm.get`, `sap.sales.and.crm.create`, `sap.sales.and.crm.update`, and `sap.sales.and.crm.delete`; use an explicit domain action ID when applicable.
- Define the module's resource schema as `SapSalesAndCrmResource` with opaque `id`, stable `type`, field classification, relationships, state, timestamps, and only authorized attributes.
- Document possible module fields including `accounts`, `leads`, `opportunities`, `quotes`, `contracts`, `orders`; each field must state its type, required/nullable behavior, validation, example, sensitivity, and read/write authorization.
- Define request schemas separately from response schemas, use `snake_case`, and document team/context, pagination, filter, sort, include, `If-Match`, and `Idempotency-Key` behavior.
- Reuse the standard `data`, `links`, `meta`, and RFC 9457 Problem Details shapes from [API.md](../SAP.md); do not serialize Eloquent models automatically.

### Minimal fragment example

```yaml
openapi: 3.1.0
info:
  title: sap sales and crm API
  version: 1.0.0
paths:
  /api/v1/sap/sales-and-crm:
    get:
      operationId: sap.sales.and.crm.list
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
    SapSalesAndCrmResource:
      type: object
      required: [id, type, attributes]
      properties:
        id:
          type: string
          description: Opaque Liberu resource identifier.
        type:
          type: string
          const: sap-sales-and-crm
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
            $ref: "#/components/schemas/SapSalesAndCrmResource"
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
- Add one-to-one architecture tests proving this package depends on and presents only `sap-sales-and-crm`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `sap-sales-and-crm`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
