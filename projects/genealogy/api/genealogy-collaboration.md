# Genealogy: Genealogy Collaboration API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-collaboration). Observed identity: [`liberusoftware/module-genealogy-collaboration-api`](../../../modules/source/liberusoftware--module-genealogy-collaboration-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-genealogy-genealogy-collaboration-api`<br>
**Matching domain module:** `genealogy-collaboration`  
**Application:** Genealogy  
**Source feature:** [Genealogy Collaboration](../features/genealogy-collaboration.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Genealogy Collaboration domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Invitations
- Roles
- Branch/change proposals
- Review
- Discussions
- Watch lists
- Attribution

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

### Product API backend and client integration

This module API adapter is composed into [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-genealogy-next-react`](https://github.com/liberusoftware/project-genealogy-next-react) | [Next.js plan](../nextjs/genealogy-collaboration.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-genealogy-nuxt-vue`](https://github.com/liberusoftware/project-genealogy-nuxt-vue) | [Nuxt plan](../nuxt/genealogy-collaboration.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-genealogy-mobile-react`](https://github.com/liberusoftware/project-genealogy-mobile-react) | [React Native plan](../react-native/genealogy-collaboration.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-genealogy-mobile-flutter`](https://github.com/liberusoftware/project-genealogy-mobile-flutter) | [Flutter plan](../flutter/genealogy-collaboration.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-genealogy-dart-mobile`](https://github.com/liberusoftware/project-genealogy-dart-mobile) · [`project-genealogy-dart-desktop`](https://github.com/liberusoftware/project-genealogy-dart-desktop) | [Flutter & Dart plan](../flutter/genealogy-collaboration.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Invitations** | Expose authorized query/read projection and explicit domain transition command for `invitations` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Roles** | Expose authorized query/read projection and explicit domain transition command for `roles` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Branch/change proposals** | Expose authorized query/read projection and explicit domain transition command for `branch/change proposals` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Review** | Expose authorized query/read projection and explicit domain transition command for `review` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Discussions** | Expose authorized query/read projection and explicit domain transition command for `discussions` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Watch lists** | Expose authorized query/read projection and explicit domain transition command for `watch lists` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Attribution** | Expose authorized query/read projection and explicit domain transition command for `attribution` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-genealogy-collaboration-api](../../../modules/source/liberusoftware--module-genealogy-collaboration-api.md) |
| Source package | [liberusoftware/module-genealogy-collaboration](../../../modules/source/liberusoftware--module-genealogy-collaboration.md) |

No route file was established under the matched module roots for this spelling. That is a source-location observation, not proof that the capability has no API or UI. Review application-owned routes and the public domain boundary before proposing HTTP commands.

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core action / service source | Observed signatures |
| --- | --- |
| [AcceptCollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/AcceptCollaborationInvitation.php) | `public function execute(CollaborationInvitation $invitation, Authenticatable $actor): CollaborationMembership` |
| [CreateCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationDiscussion.php) | `public function execute(array $attributes): CollaborationDiscussion` |
| [CreateCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationProposal.php) | `public function execute(array $attributes): CollaborationProposal` |
| [CreateCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationSpace.php) | `public function execute(array $attributes): CollaborationSpace` |
| [DeleteCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationDiscussion.php) | `public function execute(CollaborationDiscussion $discussion): void` |
| [DeleteCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal): void` |
| [DeleteCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationSpace.php) | `public function execute(CollaborationSpace $space): void` |
| [InviteCollaborationMember.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/InviteCollaborationMember.php) | `public function execute(array $attributes): CollaborationInvitation` |
| [RecordCollaborationAttribution.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/RecordCollaborationAttribution.php) | `public function execute(string $type, string $id, string $action, array $metadata = [], string\|int\|null $actorId = null): CollaborationAttribution` |
| [ReviewCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/ReviewCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal, string $status, string\|int\|null $reviewerId = null): CollaborationProposal` |
| [RevokeCollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/RevokeCollaborationInvitation.php) | `public function execute(CollaborationInvitation $invitation): CollaborationInvitation` |
| [RsvpToVirtualEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/RsvpToVirtualEvent.php) | `public function execute(VirtualEvent $event, Model $user, string $status, ?string $notes = null): VirtualEventAttendee` |
| [SetCollaborationMembershipRole.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/SetCollaborationMembershipRole.php) | `public function execute(CollaborationMembership $membership, string $role): CollaborationMembership` |
| [ToggleCollaborationWatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/ToggleCollaborationWatch.php) | `public function execute(string $watchableType, string $watchableId, string\|int $userId): ?CollaborationWatch` |
| [UpdateCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/UpdateCollaborationDiscussion.php) | `public function execute(CollaborationDiscussion $discussion, array $attributes): CollaborationDiscussion` |
| [UpdateCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/UpdateCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal, array $attributes): CollaborationProposal` |
| [UpdateCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/UpdateCollaborationSpace.php) | `public function execute(CollaborationSpace $space, array $attributes): CollaborationSpace` |
| [VideoConferencingProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Contracts/VideoConferencingProvider.php) | `public function key(): string`<br>`public function isAvailable(): bool`<br>`public function createMeeting(array $meetingData): array`<br>`public function updateMeeting(array $meetingData): array`<br>`public function deleteMeeting(string $meetingId): bool`<br>`public function meetingDetails(string $meetingId): ?array`<br>`public function attendees(string $meetingId): array`<br>`public function sendInvitations(string $meetingId, array $emails): bool` |
| [VideoConferencingService.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Services/VideoConferencingService.php) | `public function createMeeting(VirtualEvent $event, iterable $providers): ?array`<br>`public function updateMeeting(VirtualEvent $event, iterable $providers): ?array`<br>`public function deleteMeeting(VirtualEvent $event, iterable $providers): bool`<br>`public function availablePlatforms(iterable $providers): Collection` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [CollaborationAttribution.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationAttribution.php) | `team_id`, `actor_id`, `attributable_type`, `attributable_id`, `action`, `metadata`, `created_at` |
| [CollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationDiscussion.php) | `team_id`, `space_id`, `proposal_id`, `author_id`, `body`, `status`, `metadata` |
| [CollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationInvitation.php) | `team_id`, `space_id`, `email`, `role`, `status`, `invited_by`, `expires_at`, `accepted_at`, `revoked_at` |
| [CollaborationMembership.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationMembership.php) | `team_id`, `space_id`, `user_id`, `role`, `status`, `joined_at` |
| [CollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationProposal.php) | `team_id`, `proposer_id`, `reviewer_id`, `title`, `description`, `status`, `reviewed_at`, `metadata` |
| [CollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationSpace.php) | `team_id`, `name`, `status`, `metadata` |
| [CollaborationWatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationWatch.php) | `team_id`, `user_id`, `watchable_type`, `watchable_id` |
| [VirtualEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/VirtualEvent.php) | `team_id`, `created_by`, `title`, `description`, `start_time`, `end_time`, `timezone`, `status`, `platform`, `meeting_id`, `meeting_password`, `meeting_url`, `join_url`, `platform_data`, `max_attendees`, `require_rsvp`, `allow_guests`, `instructions`, `host_email` |
| [VirtualEventAttendee.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/VirtualEventAttendee.php) | `virtual_event_id`, `user_id`, `person_id`, `guest_name`, `guest_email`, `rsvp_status`, `rsvp_date`, `rsvp_notes`, `attended`, `joined_at`, `left_at`, `duration_minutes`, `attendance_data`, `is_host`, `is_moderator`, `invitation_token`, `invitation_sent_at` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#genealogy-collaboration), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `genealogy-collaboration`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `genealogy-collaboration`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
