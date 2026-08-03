# SAP: Sales and CRM API

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

## 4. OpenAPI sche…104272 tokens truncated…ravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Governed metrics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Semantic models:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Planning:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Forecasts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Data quality:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Lineage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **AI assistance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-sap-data-and-intelligence-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `governed-metrics`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `semantic-models`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `planning`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `forecasts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `data-quality`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `lineage`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `exports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `ai-assistance`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `sap-data-and-intelligence` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
