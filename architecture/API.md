# Liberu API Architecture

## Canonical Design and Implementation Specification

**Applies to:** Module APIs, project/application APIs, marketplace apps, provider connectors, webhooks, generated SDKs, and internal service integrations
**Related standards:** [MODULES.md](MODULES.md) · [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) · [THEMES.md](../standards/THEMES.md) · [REPOSITORIES.md](REPOSITORIES.md) · [DOCUMENTATION.md](../standards/DOCUMENTATION.md) · [TESTING.md](../standards/TESTING.md)

## 1. Purpose

Liberu APIs expose module capabilities without exposing private implementation. They must remain consistent across independently deployable repositories, safe for tenant and financial data, usable by first-party interfaces and third parties, and evolvable without forcing coordinated upgrades of every product.

This document defines the shared API contract. Product scopes define which resources and actions exist. `MODULES.md` defines package ownership and dependency direction. `projects/boilerplate/BOILERPLATE.md` owns identity, tokens, service identities, scopes, rate-limit infrastructure, webhooks, audit, and integrations.

## 2. API principles

1. **Owner-defined:** only the module owning a record defines its authoritative write API.
2. **Explicit exposure:** installing a module does not automatically publish every model or action.
3. **Contract-first:** public behavior is described and reviewed before implementation.
4. **Consistent:** naming, errors, pagination, authentication, idempotency, and observability follow this specification.
5. **Least privilege:** credentials and scopes grant only required operations and tenant context.
6. **Provider-neutral:** product APIs never expose vendor SDK types or provider payloads as domain contracts.
7. **Asynchronous where needed:** slow, external, bulk, and failure-prone work returns an operation and runs through queues.
8. **Retry-safe:** retried writes, webhooks, imports, payments, and provisioning use idempotency and deduplication.
9. **Traceable:** requests, state changes, events, provider calls, and failures share correlation and audit context.
10. **Backward compatible:** released contracts are versioned, tested, documented, and deprecated before removal.
11. **Privacy-aware:** APIs minimize, classify, authorize, retain, and redact data by purpose.
12. **Accessible documentation:** every public API provides useful examples, schemas, errors, and a tested quick start.
13. **One module, one API adapter:** every independent domain module requiring HTTP API access has its own matching API presentation module; product-wide API packages do not absorb several independent module APIs.

## 3. API categories

| Category                | Purpose                                                                                 | Ownership                                                  |
| ----------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Module API              | Exposes exactly one independent module's supported resources, queries, and actions      | That module's matching optional API presentation package   |
| Application API         | Curates module APIs into a coherent product/project surface                             | Host application's composition layer                       |
| Internal contract API   | Synchronous PHP contract or private service endpoint used between required capabilities | Owning contract/core package                               |
| Connector API           | Connects a Liberu contract to an external provider                                      | Independent provider-adapter module                        |
| Marketplace API         | Installs, authorizes, configures, meters, and monitors third-party apps                 | Boilerplate marketplace/integration capabilities           |
| Webhook API             | Receives external facts or delivers Liberu domain events                                | Owning connector/module plus shared webhook infrastructure |
| Management API          | Operates modules, jobs, integrations, health, and deployment-safe lifecycle             | Boilerplate/authorized operations packages                 |
| Headless/Storefront API | Delivers purpose-specific public/customer content and commerce experiences              | CMS/Ecommerce presentation packages                        |

An application may expose a smaller curated surface than the sum of installed module APIs. Private/internal endpoints must not become publicly reachable through routing accidents.

## 4. Package and repository design

Domain packages do not depend on Laravel HTTP controllers, OpenAPI tools, or a specific transport. Every independent domain module requiring an HTTP API has one matching API presentation package. The package name starts with `module-`, contains the complete independent domain module name, and ends with `-api`:

```text
module-{independent-module-name}-api
```

Examples:

| Domain module      | Matching API module           |
| ------------------ | ----------------------------- |
| `cms-content`      | `module-cms-content-api`      |
| `cms-pages`        | `module-cms-pages-api`        |
| `billing-invoices` | `module-billing-invoices-api` |
| `payment-core`     | `module-payment-core-api`     |

The rule applies to the GitHub repository, Composer package basename, installer name, manifest identity, and installed directory. For example, `liberusoftware/module-cms-content-api` installs to `/modules/module-cms-content-api`.

```text
liberusoftware/payment-contracts
        ^
liberusoftware/payment-core
        ^
liberusoftware/module-payment-core-api  # requests, resources, routes, OpenAPI fragment
```

API packages are Composer modules installed under `/modules` according to `MODULES.md`. Each API module declares its one matching domain module as a required dependency, invokes only that module's public domain actions/queries and policies, and owns only that module's HTTP contract. It never reimplements business rules, queries another module's private tables, or exposes another independent module's resources for convenience.

An umbrella API package such as `module-cms-api` must not own endpoints for content, pages, media, navigation, publishing, and workflows when those are independent domain modules. The application composes the matching API modules and may publish a unified external specification or façade without changing their ownership.

One matching API module covers all required audiences and route groups for its domain module—public, customer, partner, staff, management, internal service, or other HTTP surfaces. It documents an audience-to-operation matrix and applies distinct authentication, scopes, policies, rate limits, and exposure rules as required.

Each independent API or connector repository includes:

- `composer.json` and `module.json` with capabilities and compatibility;
- routes, controllers/handlers, requests, resources, policies, and API tests;
- an OpenAPI fragment and examples;
- scope and permission declarations;
- changelog, migration/deprecation notes, README, generated test coverage, and operational runbook.

CI fails when an API module does not match exactly one independent domain module, declares operations owned by another module, or omits a declared audience/operation mapping. Cross-module endpoints belong to the host application's composition layer and delegate to each owning module rather than moving ownership into either API package.

## 5. Protocols and formats

### 5.1 REST default

JSON over HTTPS REST is the default public interface. Use standard HTTP semantics, status codes, conditional requests, caching, and content negotiation. State-changing operations never use `GET`.

### 5.2 GraphQL

GraphQL is optional for read-heavy, multi-resource client experiences where it materially reduces round trips. It must use the same actions, queries, policies, tenant context, rate/cost controls, and audit rules as REST.

- Use persisted/allowlisted queries for public production clients where feasible.
- Enforce query depth, complexity, pagination, field authorization, and timeouts.
- Avoid exposing Eloquent models or auto-generated mutations directly.
- Version through schema evolution and deprecation; breaking removals follow the API lifecycle.

GraphQL does not replace webhooks, domain events, bulk operations, or provider connectors.

### 5.3 Webhooks and events

Webhooks deliver facts asynchronously across trust boundaries. Internal domain events use the event/outbox rules in `MODULES.md`. A webhook payload is a stable external contract and must not be a raw internal event serialization.

### 5.4 Files and streams

Large uploads/downloads use shared Files and Media contracts, temporary signed URLs, multipart/resumable transfer where required, size/type/hash validation, malware scanning, and authorization at issuance and use. Do not place large binary data in JSON or webhook bodies.

## 6. URL and naming conventions

Public REST APIs use:

```text
https://{host}/api/v1/{module}/{resources}
```

Examples:

```text
GET  /api/v1/crm/contacts
GET  /api/v1/crm/contacts/{contact_id}
POST /api/v1/billing/subscriptions
POST /api/v1/accounting/invoices/{invoice_id}/finalize
GET  /api/v1/operations/{operation_id}
```

Rules:

- Use lowercase kebab-case URL segments and plural resource nouns.
- Use opaque stable ULID strings for Liberu resource identifiers.
- Do not expose database sequence assumptions or provider identifiers as primary IDs.
- Standard CRUD uses collection/resource routes; domain behavior uses an explicit action subresource such as `/finalize`, `/approve`, or `/cancel`.
- Avoid RPC-like generic routes such as `/execute`, `/process`, or `/update-status`.
- Nested routes express true ownership and remain shallow; filter relationships instead of creating deeply nested URLs.
- Application APIs may offer stable unprefixed product resources when the application owns the public contract and collision policy. Module ownership remains documented in OpenAPI metadata.

JSON property names use `snake_case`. Public names remain stable after release.

## 7. API versioning and lifecycle

The major version appears in the path (`/api/v1`). Minor compatible additions do not change the path.

### Compatible changes

- Add optional response fields, endpoints, event types, enum descriptions, or optional request properties.
- Add pagination/filter capabilities without changing existing results unexpectedly.
- Relax a validation rule only when security and domain invariants remain intact.

Clients must ignore unknown response properties. Servers must not silently reinterpret an existing property.

### Breaking changes

- Remove or rename endpoints, fields, scopes, event types, or enum values.
- Change property type, meaning, required status, default, authorization, or ordering contract.
- Change money, timezone, pagination, identifier, or error semantics.

Breaking changes require a new major API version or an approved migration strategy. Support overlapping versions for a documented period based on project policy.

Deprecated responses include standard deprecation/sunset metadata where supported, link to migration guidance, and emit usage telemetry. Changelogs identify affected clients, replacement, dates, and removal version. Security fixes may shorten the normal lifecycle with explicit communication.

## 8. OpenAPI and contract registry

REST APIs use OpenAPI 3.1 or the current organization-approved compatible version.

- Every API module owns a validated OpenAPI fragment with stable operation IDs and reusable schemas.
- The application build combines enabled fragments into one canonical specification and rejects path, operation-ID, schema, or security collisions.
- The generated specification is available as a versioned build artifact and at an authenticated/public documentation endpoint according to exposure policy.
- Implementation, examples, validation, and OpenAPI schemas must agree; CI detects drift.
- Breaking-change detection compares the proposed specification with the latest supported release.
- Public SDKs and typed clients are generated only from released specifications and include their generator/spec version.

An API catalog records owner, repository, version, audience, data classification, scopes, SLO, dependencies, support status, and documentation URL.

## 9. Request conventions

### 9.1 Headers

Use as applicable:

| Header             | Purpose                                                             |
| ------------------ | ------------------------------------------------------------------- |
| `Authorization`    | Bearer access token or approved service credential                  |
| `Accept`           | Expected JSON/problem/media representation                          |
| `Content-Type`     | Request representation, normally `application/json`                 |
| `Idempotency-Key`  | Deduplicates retryable state-changing requests                      |
| `If-Match`         | Optimistic concurrency using the current ETag                       |
| `X-Correlation-ID` | Caller-supplied trace identifier; validated or replaced when unsafe |
| `X-Request-ID`     | Unique request identifier returned/generated by the platform        |

Do not put secrets, access tokens, personal data, tenant IDs, or mutable authorization context in URLs.

### 9.2 Dates and times

- Timestamps use RFC 3339/ISO 8601 strings with timezone; persisted instants are normally returned in UTC.
- Date-only business values use `YYYY-MM-DD` and must not be coerced to midnight timestamps.
- Scheduled local time includes both local value and IANA timezone when its meaning depends on locality.
- Durations use an explicitly documented unit or ISO duration format; never an ambiguous integer.

### 9.3 Money and quantities

Money is never a binary floating-point value:

```json
{
  "amount": "125.50",
  "currency": "GBP"
}
```

Financial responses identify authoritative transaction currency and, where relevant, snapshotted rate/conversion. Quantity, rate, percentage, tax, and measurement precision are explicit strings or schemas.

### 9.4 Null, omitted, and empty

- Omitted means not supplied/not requested.
- `null` means explicitly no value only where the schema permits it.
- Empty string/list/object has its normal typed meaning and is not interchangeable with `null`.
- PATCH-like updates use an explicit documented merge-patch or operation format; omission must not erase data.

## 10. Response conventions

### 10.1 Resource response

```json
{
  "data": {
    "id": "01J...",
    "type": "contact",
    "display_name": "Example Contact",
    "created_at": "2026-08-01T12:00:00Z",
    "updated_at": "2026-08-01T12:00:00Z"
  },
  "meta": {
    "request_id": "01J..."
  }
}
```

Collection responses use `data` as a list and include `links`/`meta` for pagination. A `204 No Content` response has no envelope.

### 10.2 Status codes

Use HTTP status semantics consistently:

| Code              | Meaning                                                           |
| ----------------- | ----------------------------------------------------------------- |
| `200`             | Successful query or action with a response                        |
| `201`             | Resource created; include `Location` where meaningful             |
| `202`             | Accepted for asynchronous processing; return operation location   |
| `204`             | Successful action with no response body                           |
| `400`             | Malformed request or unsupported request semantics                |
| `401`             | Authentication missing/invalid                                    |
| `403`             | Authenticated but not authorized                                  |
| `404`             | Resource unavailable, including concealment policy where required |
| `409`             | State/idempotency/uniqueness conflict                             |
| `412`             | Conditional request/ETag precondition failed                      |
| `422`             | Well-formed request failed field/domain validation                |
| `429`             | Rate or quota limit exceeded                                      |
| `500`             | Unexpected platform failure                                       |
| `502`/`503`/`504` | Dependency unavailable, service unavailable, or timeout           |

Do not return `200` with an embedded error status.

## 11. Errors and validation

Errors use Problem Details (`application/problem+json`) with a stable Liberu extension for field violations:

```json
{
  "type": "https://docs.liberusoftware.com/problems/validation-failed",
  "title": "Validation failed",
  "status": 422,
  "detail": "One or more fields are invalid.",
  "instance": "/api/v1/crm/contacts",
  "request_id": "01J...",
  "errors": [
    {
      "code": "invalid_email",
      "pointer": "/email",
      "message": "Enter a valid email address."
    }
  ]
}
```

- `type` and `code` are stable machine-readable contracts.
- `title`, `detail`, and `message` are safe for the intended audience and may be localized.
- Never expose stack traces, SQL, secret values, provider credentials, internal paths, or unauthorized record existence.
- Provider errors are translated into Liberu problem types; safe provider reference IDs may appear in metadata.
- Documentation lists causes, retry safety, remediation, and relevant status codes for every public error.

## 12. Querying collections

### Pagination

Cursor pagination is the default for changing or large collections:

```text
GET /api/v1/crm/contacts?page[size]=50&page[after]=CURSOR
```

Responses provide opaque next/previous cursors. Offset/page pagination is permitted for stable reporting datasets when total counts are required and performance is bounded.

### Filtering, sorting, fields, and relationships

```text
?filter[status]=active
&filter[created_at][gte]=2026-01-01T00:00:00Z
&sort=-created_at,display_name
&fields[contact]=id,display_name,email
&include=owner,organization
```

- Every filter, sort, sparse field, and include is explicitly allowlisted and documented.
- Authorization applies to included relationships and individual fields.
- Default and maximum page sizes are documented per endpoint.
- Expensive queries have cost/rate controls and predictable limits.
- Search uses the shared Search capability rather than ad hoc SQL query syntax.

## 13. Authentication and credentials

| Client                     | Preferred mechanism                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| First-party browser/mobile | Shared identity session or short-lived scoped token with CSRF/PKCE protections as applicable |
| Personal automation        | Revocable personal access token with explicit scopes and expiry policy                       |
| Marketplace/public app     | OAuth 2 authorization code with PKCE and refresh-token rotation                              |
| Server-to-server           | OAuth client credentials, workload identity, or short-lived service credential               |
| Incoming webhook           | Provider signature verification, timestamp/replay controls, and source policy                |
| Internal trusted service   | Service identity with mutual trust/short-lived credentials, never a shared user token        |

- Tokens are displayed only when required, stored hashed/encrypted as appropriate, scoped, expiring, rotatable, and revocable.
- API keys in query strings are prohibited.
- Long-lived shared secrets are avoided; connector secrets use the shared encrypted credential store.
- Credential compromise, user/team removal, app uninstall, role loss, or tenant suspension revokes derived access promptly.
- Sensitive operations may require recent authentication, MFA assurance, approval, or a dedicated high-risk scope.

## 14. Authorization, scopes, and tenancy

Authentication identifies a principal; it does not grant access by itself.

- OAuth/API scopes define the maximum delegated capability, using names such as `crm.contacts.read` and `billing.invoices.write`.
- Module policies also evaluate actor/service identity, organization/team, brand/site, division, resource ownership, record state, field sensitivity, consent, and entitlement.
- Scopes are additive but never override a domain policy.
- Tenant context comes from trusted credential/membership/application routing and is validated on every request. A caller-supplied tenant header alone cannot grant context.
- Cross-tenant service operations require a dedicated service identity, explicit scope, allowlisted tenants/purpose, and enhanced audit.
- List, search, include, export, aggregate, and error paths must not leak inaccessible records or counts.
- Marketplace app installation grants requested scopes only after an authorized administrator reviews purpose and data access.

## 15. Idempotency, concurrency, and transactions

### Idempotency

Require `Idempotency-Key` for retryable or high-impact creates/actions such as orders, payments, refunds, provisioning, imports, and bulk communications.

- Scope a key to credential, tenant, operation, and canonical request fingerprint.
- The same key and equivalent request returns the original status/result while retained.
- Reusing a key with a different request returns `409 Conflict`.
- Document retention and behavior while the original request is still processing.
- Provider idempotency keys derive from or map to the Liberu operation without exposing provider semantics.

### Optimistic concurrency

Mutable resources return ETags/version fields. Updates to concurrency-sensitive records require `If-Match`; stale writes return `412 Precondition Failed` with safe recovery guidance.

### Transactions

One module enforces its local invariants atomically. Cross-module workflows use commands/events and sagas with compensation; they do not attempt distributed database transactions or mutate several private schemas in one controller.

## 16. Asynchronous and bulk operations

Slow work returns `202 Accepted` and an operation resource:

```json
{
  "data": {
    "id": "01J...",
    "type": "operation",
    "status": "queued",
    "progress": null,
    "result_url": null,
    "error": null
  }
}
```

Operations support applicable states such as `queued`, `running`, `awaiting_approval`, `succeeded`, `partially_succeeded`, `failed`, and `cancelled`. They expose safe progress, timestamps, result/error links, expiry, and cancellation policy.

Bulk APIs require bounded batch size, per-item identifiers/results, validation/dry-run when material, partial-failure semantics, idempotency, approval for risky actions, exportable error reports, and resumable processing where appropriate.

## 17. Rate limits, quotas, and abuse protection

- Apply limits by credential, user/service, tenant, app, endpoint/cost class, provider, and network risk as appropriate.
- Return `429` with a retry interval and standardized limit metadata adopted by the platform.
- Separate short burst limits from sustained quotas and commercial usage entitlements.
- Expensive search, export, AI, media, messaging, and bulk endpoints use cost-aware limits.
- Do not reveal other tenants' usage or capacity.
- Marketplace apps receive documented default limits and a governed review process for increases.
- Authentication, forms, webhooks, uploads, and public endpoints also use enumeration, spam, replay, and resource-exhaustion controls.

## 18. Caching and conditional requests

- Public/read APIs declare cacheability, freshness, Vary behavior, and invalidation ownership.
- Private/customer data defaults to non-shared caching and uses correct `Cache-Control` directives.
- Use ETag/`If-None-Match` or last-modified validators for stable resources where beneficial.
- Never cache authorization results or tenant responses under keys missing relevant context.
- Module events invalidate tagged caches/read models after commit.

## 19. Module API design

Each module API specification states:

- its one matching independent domain module, audiences, resources, actions, exclusions, and source-of-truth boundaries;
- package and route prefix;
- required foundation modules and optional integrations;
- resource schemas, field classification, relationships, state machines, invariants, and permissions;
- query/filter/sort/include limits;
- commands, events, webhooks, asynchronous operations, and idempotency policy;
- errors, rate limits, SLO, telemetry, retention, and compatibility;
- examples and tests for allowed, denied, invalid, duplicate, stale, concurrent, and failed-provider paths.

The specification includes an audience-to-operation matrix covering public, customer, partner, staff, management, internal-service, or other required API access. Every declared operation maps to a controller/handler and OpenAPI operation in this package, or to an explicit approved exclusion. No row may map to another independent module's implementation.

API resource classes map domain DTOs/read models to the wire contract. They must not serialize Eloquent models automatically or expose columns merely because they exist.

## 20. Application and project APIs

A repository-based application composes module APIs through a deliberate API manifest.

1. Select enabled API packages and supported versions.
2. Resolve path, schema, operation-ID, scope, permission, and event collisions in CI.
3. Expose only product-relevant operations; hide module administration/private endpoints.
4. Apply the application's organization/site/brand, entitlement, and rate-limit policy.
5. Publish one aggregated OpenAPI document and developer portal.
6. Run cross-module workflow and backward-compatibility tests.
7. Version the application contract independently from internal package versions.

Applications may add façade endpoints/read models for an end-to-end workflow, but the façade delegates writes to owning module actions and documents partial/asynchronous outcomes. It must not become a second source of truth.

## 21. Connector architecture

A connector is an independent provider-adapter module implementing a provider-neutral Liberu contract:

```text
Product module -> Capability contract/core <- Provider connector -> External API
```

The connector owns:

- provider authentication, consent, credential refresh/rotation, and connection health;
- capability discovery and unsupported-feature behavior;
- provider-to-Liberu field/status/identifier mapping and anti-corruption translation;
- external identifiers and webhook receipts in connector-owned storage;
- provider API versions, SDK/client, pagination, rate limits, timeouts, retries, and circuit breaking;
- incremental sync cursors/checkpoints, backfill, conflict policy, replay, and reconciliation;
- sandbox/test mode, fixtures/fakes, redacted request diagnostics, metrics, and runbooks.

Product modules never branch on provider name or store provider payloads/identifiers in their core tables.

### Sync modes

| Mode                | Use                                                                             |
| ------------------- | ------------------------------------------------------------------------------- |
| Webhook-first       | Near-real-time provider facts, followed by queued processing and reconciliation |
| Incremental pull    | Provider changes obtained through cursor/watermark                              |
| Outbound push       | Liberu changes delivered with idempotency and provider result tracking          |
| Full reconciliation | Periodic comparison to detect missing, duplicate, stale, or divergent records   |
| Backfill/import     | Bounded historical load with dry run, mapping, progress, and sign-off           |

Every connector defines its source-of-truth and conflict policy per field/object. “Last write wins” is not an acceptable undocumented default.

## 22. Incoming provider webhooks

1. Resolve connector/tenant using a trusted endpoint/credential mapping.
2. Read the raw body with bounded size and required headers.
3. Verify signature, timestamp, source policy, and replay window before parsing side effects.
4. Persist a connector-owned receipt containing provider event ID/type/version, hash, received time, verification result, and safe metadata.
5. Return promptly according to provider requirements.
6. Process asynchronously, deduplicate, map to domain commands/events, and record outcome.
7. Retry transient failures; quarantine permanent/unknown events for operator review.
8. Reconcile periodically because webhook delivery alone is not authoritative.

Unknown event types are retained safely and reported, not treated as successful domain processing. Logs never contain secrets or uncontrolled full payloads.

## 23. Outgoing Liberu webhooks

- Subscribers choose versioned event types and an HTTPS endpoint allowed by egress/SSRF policy.
- Generate a unique delivery ID and include event ID, type, version, occurrence time, tenant-safe subject reference, and minimal data.
- Sign the exact body with a rotatable per-subscription secret and include timestamp/replay protection.
- Deliver after source transaction commit through an outbox/queue.
- Retry with bounded exponential backoff and jitter; expose attempts, status, safe response summary, next attempt, replay, pause, and disable controls.
- Preserve event ordering only where explicitly guaranteed; consumers must otherwise tolerate duplicates and reordering.
- Support secret rotation overlap and test deliveries.
- Disable persistently failing or compromised endpoints according to policy and notify owners.

Webhook documentation includes signature-verification examples and warns consumers to deduplicate by event/delivery ID.

## 24. Marketplace apps

Marketplace apps use a signed/versioned manifest declaring:

- app/publisher identity, support/security contacts, category, versions, regions, and compatibility;
- OAuth redirect/logout/uninstall URLs and allowed domains;
- requested API scopes with plain-language purpose;
- subscribed webhook event types and endpoint requirements;
- data categories accessed/stored, retention/deletion, subprocessors, residency, and privacy links;
- rate/usage needs, pricing/entitlement references, configuration schema, and health endpoint;
- installation, update, suspension, uninstall, export, and cleanup behavior.

### Lifecycle

1. Publisher verification and automated/manual security review.
2. Administrator reviews scopes, data, webhooks, pricing, and tenant/site applicability.
3. OAuth/credential setup uses state, PKCE where applicable, exact redirect matching, and secret storage.
4. Installation records app version, grants, actor, tenant/site, config, webhooks, and acceptance.
5. Runtime calls are scoped, rate-limited, audited, monitored, and attributable to app/service identity.
6. Scope/version changes require review and re-consent when access expands.
7. Suspension immediately blocks credentials and deliveries without destroying evidence.
8. Uninstall revokes tokens/secrets/webhooks, stops jobs, exports/deletes data according to policy, and preserves required audit/billing records.

Apps cannot receive super-admin equivalents, bypass module policies, access private database tables, inject arbitrary server code, or retain access after uninstall.

## 25. Automation connector actions and triggers

Marketplace connectors may expose typed Automation triggers, actions, and searches.

- Inputs/outputs use versioned JSON schemas and the provider-neutral domain vocabulary.
- Actions declare side effects, required scopes, idempotency, timeout, retry safety, cost/usage, approval risk, and test mode.
- Triggers declare delivery guarantee, deduplication key, replay/backfill support, ordering, and filters.
- Secrets are referenced by connection ID, never accepted as ordinary workflow input.
- High-risk financial, contractual, outreach, publication, access, or infrastructure actions require policy-based approval.
- Connector failure produces a recoverable workflow state, not silent completion.

## 26. Security and privacy

- HTTPS is required; approved modern TLS and security headers apply at the edge.
- Validate structure, content type, encoding, size, values, and domain invariants at every boundary.
- Prevent injection, mass assignment, broken object/field authorization, SSRF, unsafe redirects, path traversal, deserialization abuse, file attacks, replay, and credential leakage.
- Use strict outbound destination allowlists/DNS/IP checks for user-configured callbacks and webhooks.
- Redact tokens, cookies, authorization headers, personal data, payment data, message bodies, files, and provider payloads from normal logs.
- Apply purpose, consent, minimization, field-level access, retention, export, deletion, legal hold, residency, and audit requirements.
- Return consistent timing/messages where identity or resource enumeration is a risk.
- Threat-model public, authentication, payment, file, webhook, automation, AI, infrastructure, and marketplace APIs before production.
- Maintain dependency/SBOM, vulnerability scanning, credential rotation, incident response, and supported-version policy.

## 27. Observability and SLOs

Every API records safe structured telemetry for:

- request/correlation ID, API/module/operation/version, tenant/site, principal/app identity, status, latency, and response size;
- authentication/authorization outcome without secret/token content;
- rate-limit/quota decision;
- idempotency replay/conflict and concurrency failure;
- queued operation, webhook delivery, connector call, retry, circuit state, and reconciliation;
- dependency latency/error and normalized provider code;
- business outcome metrics defined by the owning module.

Define availability, latency, error-rate, freshness, and processing-time objectives by API class. Alerts must distinguish platform defects, client errors, abusive traffic, provider outages, credential expiry, backlog, and data drift.

## 28. Testing and quality gates

Required tests include:

- one-to-one boundary tests proving the API package presents exactly its matching independent domain module and contains no other module's controllers, resources, routes, schemas, or operations;
- audience-to-operation matrix tests proving all declared API surfaces are implemented and exposed only through their intended authentication, scope, policy, tenant, and rate-limit rules;
- OpenAPI/schema linting, examples, implementation drift, and breaking-change detection;
- authentication, scope, policy, tenant/site/field authorization, entitlement, and concealment;
- validation/property tests for identifiers, money, dates, enums, pagination, filtering, and state transitions;
- idempotency replay/conflict/in-progress behavior and concurrent ETag writes;
- rate limits, quotas, payload limits, timeouts, retries, cancellation, and partial failure;
- webhook signatures, rotation, timestamp/replay, duplicates, ordering, unknown events, and replay;
- connector contract suites, sandbox/fakes, mapping, cursors, backfill, outage, and reconciliation;
- marketplace install, consent, scope escalation, suspension, uninstall, cleanup, and audit;
- performance/load tests for critical endpoints and abusive query patterns;
- security tests derived from the API threat model;
- SDK generation/compile/smoke tests against the released specification.

Each API repository generates coverage in CI as required by `MODULES.md` and documents meaningful untested risk. Application CI runs representative end-to-end workflows across composed module APIs.

## 29. Documentation and developer experience

Every public API README/developer portal provides:

- purpose, audience, base URL, environments, current/supported versions, and status;
- authentication setup and least-privilege scope examples;
- copyable request/response/error examples using non-sensitive sample data;
- resource/action descriptions, pagination/filtering, idempotency, concurrency, rate limits, and async behavior;
- webhook verification, retries, replay, and event catalog;
- connector/provider capabilities, limitations, sandbox, mappings, and reconciliation;
- changelog, deprecations, migration guides, SLO/support, status, security reporting, and SDK links.

Examples run in CI or contract tests where practical. Do not publish working secrets, production IDs, or curl commands that disable TLS verification.

## 30. Implementation sequence

1. Identify the owning module, consumers, data classification, resources/actions, exclusions, and source of truth.
2. Decide whether the surface belongs in a module API package, application façade, connector, webhook, or internal PHP contract.
3. Write an ADR for protocol, version, authentication, scopes, tenancy, idempotency, async behavior, events, and compatibility.
4. Define OpenAPI/event schemas, examples, errors, permissions, limits, and operation IDs before controllers.
5. Implement domain actions/queries and policies independently of HTTP/provider transport.
6. Implement request validation and resource mapping without automatic model serialization or mass assignment.
7. Add idempotency, ETags, operations, outbox/inbox, audit, telemetry, and rate limits as required.
8. For connectors, implement credential, mapping, webhook, cursor, retry, circuit, test, and reconciliation behavior.
9. Add contract, authorization, tenant, failure, compatibility, security, performance, and breaking-change tests.
10. Aggregate into the host application manifest/specification and run cross-module workflow tests.
11. Publish README/developer docs, generated spec/SDK, changelog, runbook, dashboards, and alerts.
12. Release behind controlled enablement, monitor adoption/errors, and rehearse rollback/deprecation.

## 31. Definition of done

An API is ready when:

- it is named `module-{independent-module-name}-api`, depends on exactly its matching domain module for presentation ownership, and contains no other independent module's API logic;
- its audience-to-operation matrix is complete and enforced in CI;
- its owner, audience, contract, source-of-truth boundary, version, scopes, and exclusions are approved;
- OpenAPI/event schemas, implementation, examples, SDKs, and documentation agree;
- authentication, authorization, tenant/field isolation, consent, limits, and audit hold on every path;
- writes are idempotent/concurrency-safe where needed and long work is recoverable;
- connectors isolate provider semantics and support test mode, retries, replay, and reconciliation;
- marketplace install, scope change, suspension, and uninstall are governed;
- errors are stable and safe; telemetry contains no secrets or uncontrolled sensitive data;
- compatibility, contract, failure, security, performance, and application-composition tests pass;
- SLOs, dashboards, alerts, runbooks, changelog, migration/deprecation guidance, README, and coverage evidence exist.

## 32. GitHub issue mapping

Create one API epic for each independent domain module requiring API access, plus separate epics for application façades and connectors. Recommended child issues:

1. Matching domain-module ownership, audience-to-operation matrix, threat/data assessment, and API ADR.
2. OpenAPI/event schemas, examples, scopes, permissions, and breaking-change baseline.
3. Domain actions/queries, policies, and resource mapping.
4. Authentication, tenancy, idempotency, concurrency, rate limits, and operations.
5. Connector/webhook/marketplace lifecycle where applicable.
6. Contract, security, failure, performance, compatibility, and composition tests.
7. Aggregated specification, generated SDK, developer docs, README, and migration guide.
8. Telemetry, SLO, dashboards, alerts, reconciliation, and operational runbook.

Each issue states owning repository/package, dependencies, routes/operations/events, acceptance criteria, test evidence, data/security concerns, observability, compatibility, and explicit exclusions.
