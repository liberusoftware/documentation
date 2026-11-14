# Ecommerce: Catering API

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
