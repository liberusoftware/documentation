# Ecommerce: Catering API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catering). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and status

Proposed one-to-one adapter `module-ecommerce-catering-api`, Composer `liberusoftware/ecommerce-catering-api`. Follow the [core contract and approval gate](../core/catering.md); operation names below are design intents, not existing endpoints. Publish the reviewed OpenAPI fragment before generating clients. The host chooses version, audiences and exposed routes.

## Operation and projection matrix

| Intent | Audience | Contract requirements |
| --- | --- | --- |
| Maintain meals, recipes, yields and packages | Authorized staff | Team/Store policy, unit/yield validation, optimistic revision, full private staff DTO |
| Submit/read event requirements | Staff or owning customer | Date/time/timezone, venue, guest count and service validation; customer-safe response |
| Revise event menu | Authorized staff; customer only if explicitly permitted | Stable meal/product refs, quantities, expected revision; invalidate/re-quote changed commercial context |
| Submit quotation | Staff | Freeze menu context, delegate version/expiry/negotiation to approved Quotes contract |
| Read/accept quotation | Authorized owning customer or delegated staff | Current unexpired quote revision, domain authorization, atomic concurrency check |
| Confirm availability/convert order | Authorized staff or approved workflow | Distinct booking result, approved transition, durable idempotency key, pending/reconciliation response and stable order reference |

Customer schemas must be explicit allowlists excluding recipes, preparation data, ingredient costs and internal notes. Never serialize an Eloquent model directly. Read/list/export/search and error payloads enforce the same projection and ownership boundaries.

## Transport behavior and evidence

Specify authentication/scopes, Team/Store derivation from trusted identity context, bounded pagination, filtering, rate limits, validation errors, correlation IDs and localized field messages. Distinguish unauthenticated/forbidden, invalid fields, stale revision, expired quote, unavailable capacity, disabled optional integration and pending upstream conversion. An idempotency-key replay returns the same result; reusing a key with changed payload fails. Document retention and replay windows before deployment.

Test actual OpenAPI request/response examples, unauthorized and cross-store access, private-field absence, stale/expired acceptance, concurrent confirmation, retries and timeout reconciliation. API code delegates all rules to the domain; it does not write Orders/Quotes/Bookings tables or call payment SDKs. Keep the adapter independently testable with the domain contracts and exercise one host end-to-end workflow.

<!-- layer-implementation-plan:start -->
## Product API backend and feature-to-operation plan

This API contract is composed into [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) ([Laravel API backends](../../../guides/LARAVEL-API-BACKENDS.md)) to serve [`project-ecommerce-next-react`](https://github.com/liberusoftware/project-ecommerce-next-react), [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue), [`project-ecommerce-mobile-react`](https://github.com/liberusoftware/project-ecommerce-mobile-react), [`project-ecommerce-mobile-flutter`](https://github.com/liberusoftware/project-ecommerce-mobile-flutter), [`project-ecommerce-dart-mobile`](https://github.com/liberusoftware/project-ecommerce-dart-mobile), and [`project-ecommerce-dart-desktop`](https://github.com/liberusoftware/project-ecommerce-dart-desktop).

| Feature / aspect | HTTP query and command contract | DTO projection, concurrency & error semantics |
| --- | --- | --- |
| **Meals and ingredient composition** | Expose workspace-scoped read query and explicit command endpoint for `meals and ingredient composition` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Recipes and preparation yields** | Expose workspace-scoped read query and explicit command endpoint for `recipes and preparation yields` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Staff-managed catering packages** | Expose workspace-scoped read query and explicit command endpoint for `staff-managed catering packages` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Event requirements and venue context** | Expose workspace-scoped read query and explicit command endpoint for `event requirements and venue context` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Immutable menu revisions** | Expose workspace-scoped read query and explicit command endpoint for `immutable menu revisions` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Reproducible quotation context** | Expose workspace-scoped read query and explicit command endpoint for `reproducible quotation context` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
| **Availability confirmation and order conversion** | Expose workspace-scoped read query and explicit command endpoint for `availability confirmation and order conversion` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |
<!-- layer-implementation-plan:end -->
