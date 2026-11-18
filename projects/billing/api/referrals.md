# Billing: Referrals and Advocate Rewards API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#referrals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-billing-referrals-api`<br>
**Matching domain module:** `referrals`  
**Matching core package:** [`module-billing-referrals`](../core/referrals.md) (`liberusoftware/billing-referrals`)  
**Contracts presented:** `liberusoftware/affiliate-contracts (ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)`  
**Application:** Billing  
**Source feature:** [Referrals and Advocate Rewards](../features/referrals.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Referrals and Advocate Rewards domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies (`liberusoftware/affiliate-contracts (ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)`), and contains no other module's API logic.

The domain capability includes:

- Referral programs and two-sided reward rules
- Advocate share links and referral codes
- Referred signup and subscription qualification
- Duplicate, household, and self-referral prevention
- Automated reward fulfillment and clawback handling

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract (`/api/v1/referrals`).
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit minor-unit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

<!-- observed-api-contract:start -->
## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

### Product API backend and client integration

This module API adapter is composed into [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-billing-next-react`](https://github.com/liberusoftware/project-billing-next-react) | [Next.js plan](../nextjs/referrals.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | [Nuxt plan](../nuxt/referrals.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | [React Native plan](../react-native/referrals.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) | [Flutter plan](../flutter/referrals.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) · [`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) | [Flutter & Dart plan](../flutter/referrals.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Referral programs and two-sided reward rules** | Expose authorized query/read projection and explicit domain transition command for `referral programs and two-sided reward rules` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Advocate share links and referral codes** | Expose authorized query/read projection and explicit domain transition command for `advocate share links and referral codes` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Referred signup and subscription qualification** | Expose authorized query/read projection and explicit domain transition command for `referred signup and subscription qualification` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Duplicate, household, and self-referral prevention** | Expose authorized query/read projection and explicit domain transition command for `duplicate, household, and self-referral prevention` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Automated reward fulfillment and clawback handling** | Expose authorized query/read projection and explicit domain transition command for `automated reward fulfillment and clawback handling` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

No route file was established under the matched module roots for this spelling. That is a source-location observation, not proof that the capability has no API or UI. Review application-owned routes and the public domain boundary before proposing HTTP commands.

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#referrals), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

## 5. Audience and operation matrix

| Audience                       | Default exposure                    | Required controls                                                                      |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| Public/anonymous               | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls         |
| Authenticated customer/partner | Explicit allowlist                  | Tenant/resource ownership, purpose-specific scopes, field policy                       |
| Staff/administrator            | Explicit allowlist                  | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client     | Explicit allowlist                  | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas         |

## 6. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Add one-to-one architecture tests proving this package depends on and presents only `referrals`.
