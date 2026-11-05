# Browser Game: World API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#world). Observed identity: [`liberusoftware/module-browser-game-world-api`](../../../modules/source/liberusoftware--module-browser-game-world-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-browser-game-world-api`
**Matching domain module:** `browser-game-world`
**Application:** Browser Game
**Source feature:** [World](../features/world.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the World domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Regions
- locations
- maps
- travel
- encounters
- NPCs
- resources
- weather
- unlocks

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
| Source package | [liberusoftware/module-browser-game-world-api](../../../modules/source/liberusoftware--module-browser-game-world-api.md) |
| Source package | [liberusoftware/module-browser-game-world](../../../modules/source/liberusoftware--module-browser-game-world.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/browser-game-world-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/world')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [WorldController::class, 'index'])->name('browser-game.world.index');
Route::post('/', [WorldController::class, 'store'])->name('browser-game.world.store');
Route::post('/travel', [WorldController::class, 'travel'])->name('browser-game.world.travel');
Route::post('/{entity}/unlock', [WorldController::class, 'unlock'])->name('browser-game.world.unlock');
Route::delete('/unlocks/{unlock}', [WorldController::class, 'revokeUnlock'])->name('browser-game.world.unlock.revoke');
Route::patch('/{entity}', [WorldController::class, 'update'])->name('browser-game.world.update');
Route::get('/{entity}', [WorldController::class, 'show'])->name('browser-game.world.show');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [WorldController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-api/src/Http/Controllers/WorldController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function travel(Request $request): JsonResponse`<br>`public function unlock(Request $request, WorldEntity $entity): JsonResponse`<br>`public function revokeUnlock(Request $request, WorldUnlock $unlock): JsonResponse`<br>`public function show(Request $request, WorldEntity $entity): JsonResponse`<br>`public function update(Request $request, WorldEntity $entity): JsonResponse` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [modules/browser-game-world-api/openapi/v1-browser-game-world.yaml](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-api/openapi/v1-browser-game-world.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#world), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
