# Social Network: Social Graph API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-graph). Observed identity: [`liberusoftware/module-social-network-social-graph-api`](../../../modules/source/liberusoftware--module-social-network-social-graph-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-social-network-social-graph-api`
**Matching domain module:** `social-network-social-graph`
**Application:** Social Network
**Source feature:** [Social Graph](../features/social-graph.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Social Graph domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Follow/friend models
- requests
- lists
- suggestions
- blocks
- relationship visibility

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-social-network-social-graph-api](../../../modules/source/liberusoftware--module-social-network-social-graph-api.md) |
| Source package | [liberusoftware/module-social-network-social-graph](../../../modules/source/liberusoftware--module-social-network-social-graph.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/social-network-social-graph-api/routes/api.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/social-graph')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.social-graph.api.')->group(function (): void {
Route::post('/me/following/{profile}', [SocialGraphController::class, 'follow'])->name('follow');
Route::post('/me/friend-requests/{profile}', [SocialGraphController::class, 'friend'])->name('friend');
Route::get('/me/relationships', [SocialGraphController::class, 'index'])->name('index');
Route::get('/me/suggestions', [SocialGraphController::class, 'suggestions'])->name('suggestions');
Route::put('/me/blocks/{profile}', [SocialGraphController::class, 'block'])->name('block');
Route::delete('/me/blocks/{profile}', [SocialGraphController::class, 'unblock'])->name('unblock');
Route::post('/me/relationships/{relationship}/accept', [SocialGraphController::class, 'accept'])->name('accept');
Route::post('/me/relationships/{relationship}/reject', [SocialGraphController::class, 'reject'])->name('reject');
Route::post('/me/relationships/{relationship}/cancel', [SocialGraphController::class, 'cancel'])->name('cancel');
Route::patch('/me/relationships/{relationship}/visibility', [SocialGraphController::class, 'visibility'])->name('visibility');
Route::get('/me/lists', [SocialGraphController::class, 'lists'])->name('lists');
Route::post('/me/lists', [SocialGraphController::class, 'createList'])->name('lists.create');
Route::put('/me/lists/{list}/profiles/{profile}', [SocialGraphController::class, 'addListMember'])->name('lists.profiles.add');
Route::delete('/me/lists/{list}/profiles/{profile}', [SocialGraphController::class, 'removeListMember'])->name('lists.profiles.remove');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [SocialGraphController.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph-api/src/Http/Controllers/SocialGraphController.php) | `public function follow(string $profile, Request $request, GetProfile $get, CreateRelationship $create): JsonResponse`<br>`public function friend(string $profile, Request $request, GetProfile $get, CreateRelationship $create): JsonResponse`<br>`public function index(Request $request, GetProfile $get, ListRelationships $list): JsonResponse`<br>`public function suggestions(Request $request, GetProfile $get, SuggestProfiles $suggest): JsonResponse`<br>`public function block(string $profile, Request $request, GetProfile $get, BlockProfile $block): JsonResponse`<br>`public function unblock(string $profile, Request $request, GetProfile $get, UnblockProfile $unblock): JsonResponse`<br>`public function accept(Relationship $relationship, Request $request, GetProfile $get, AcceptFriendship $accept): JsonResponse`<br>`public function reject(Relationship $relationship, Request $request, GetProfile $get, RejectFriendship $reject): JsonResponse`<br>`public function cancel(Relationship $relationship, Request $request, GetProfile $get, CancelFriendship $cancel): JsonResponse`<br>`public function visibility(Relationship $relationship, Request $request, GetProfile $get, UpdateRelationshipVisibility $update): JsonResponse`<br>`public function lists(Request $request, GetProfile $get, ListOwnedLists $lists): JsonResponse`<br>`public function createList(Request $request, GetProfile $get, CreateList $create): JsonResponse`<br>`public function addListMember(GraphList $list, string $profile, Request $request, GetProfile $get, AddProfileToList $add): JsonResponse`<br>`public function removeListMember(GraphList $list, string $profile, Request $request, GetProfile $get, RemoveProfileFromList $remove): JsonResponse` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [modules/social-network-social-graph-api/openapi/v1/social-network-social-graph.yaml](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph-api/openapi/v1/social-network-social-graph.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#social-graph), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

## 5. Audience and operation matrix

Expose only explicitly selected operations. Anonymous access is disabled unless the owning capability requires it; customer/partner reads and commands use record/tenant scope, staff actions use the relevant policy, and integrations use a narrow service identity. UI visibility and authentication alone do not establish authorization.

## 6. Implementation strategy

Resolve trusted actor/tenant context, validate the reviewed request and delegate to the public owning action/query. Serialize explicit authorized DTOs; preserve documented operation identity, concurrency and error semantics. Reuse existing owner APIs instead of copying their records or private model access.

## 7. Security, resilience, and observability

Apply record/field policy to lists, relationships, commands, bulk work, jobs and downloads. Use bounded retries/timeouts, durable operation/source references and explicit partial-failure recovery. Redact credentials/protected data while retaining safe request/correlation diagnostics.

## 8. Verification strategy

Verify actual route/schema parity, required input, allowed/denied/wrong-tenant requests, stale/duplicate commands, uncertain outcomes, pagination/field policy and affected owner integrations. Check the declared package/host scripts and supported versions; source/test presence is not a passing-run claim.

## 9. Definition of done

Release only after the complete reviewed request/response/error contract, version compatibility, security and owner invariants, consumer integration, migrations where owned, and operational recovery are verified. Document the actual package identity and source/release evidence in its README and changelog.
