# API Module Specifications

## Canonical one-to-one API module index

Each API document describes the optional `module-{independent-module-name}-api` presentation package matching exactly one independent domain module. Applications compose these packages into unified external APIs without moving ownership.

Nuxt clients consume these API contracts through the matching one-to-one packages under [Nuxt 4 implementations](../nuxt/README.md). They must use documented routes, schemas, authentication, permissions, tenant/team context, pagination, errors, idempotency, and versioning; they must not call private Laravel implementation details.

## Implementation plan

For every listed module, implement `module-{independent-module-name}-api` as a thin Laravel 13 transport adapter over the matching `module-{independent-module-name}` core package. Keep controllers and route registration small; delegate writes to typed core actions, reads to core queries/read models, and authorization to the core policy boundary after request validation. Define OpenAPI 3.1 schemas, operation IDs, audiences, scopes, rate limits, pagination, field visibility, errors, idempotency, optimistic concurrency, and deprecation metadata as versioned contracts.

Use PHP 8.5 strict types, Form Requests or dedicated validators, API Resources/DTOs, Sanctum or approved service identity, and RFC 9457 Problem Details. Resolve tenant/team context from trusted authentication and enforce concealment-safe authorization. Queue slow, bulk, provider-dependent, and retryable work through idempotent operation resources. Test allowed and denied access, wrong tenant, scopes, validation, hidden fields, concurrency, throttling, contracts, schema drift, and failure recovery without querying core-private tables.

## Sanctum authentication

Third-party clients authenticate with Laravel Sanctum personal access tokens. First-party SPAs should use Sanctum's cookie-based SPA authentication instead of storing API tokens in browser code. See the [Laravel Sanctum documentation](https://laravel.com/docs/13.x/sanctum) for the complete configuration reference.

### Issue a token

Install and configure Sanctum in the application, then expose a protected, rate-limited token-issuance action. Jetstream applications may use their API-token UI; custom clients should use an application-owned action that requires an authenticated user and recent authentication:

```php
$token = $request->user()->createToken(
    name: $request->string('device_name')->toString(),
    abilities: ['genealogy.tree.read'],
)->plainTextToken;

return ['token' => $token];
```

Display the plain-text token once. Store only the token securely on the client; Sanctum stores a hash in the database. Never log, commit, or include tokens in URLs.

### Call a protected endpoint

Send the token in the `Authorization` header as a Bearer token. API routes must use the Sanctum guard:

```php
// bootstrap/app.php
use Illuminate\Foundation\Configuration\Middleware;
use Laravel\Sanctum\Http\Middleware\CheckAbilities;

->withMiddleware(function (Middleware $middleware): void {
    $middleware->alias(['abilities' => CheckAbilities::class]);
})

// routes/api.php
Route::get('/trees', TreeIndexController::class)
    ->middleware(['auth:sanctum', 'abilities:genealogy.tree.read']);
```

Example request:

```bash
curl --fail-with-body \\
  -H 'Accept: application/json' \\
  -H 'Authorization: Bearer YOUR_SANCTUM_TOKEN' \\
  https://api.example.test/api/v1/trees
```

The route middleware verifies authentication and token ability. The controller or domain action must still apply the relevant [policy and team checks](../../architecture/POLICY.md), including resource ownership and current-team membership. A valid token alone never grants access to every resource.

### Revoke and expire tokens

Provide an authenticated token-management action to revoke the current token or all tokens. Configure a finite expiration period for production integrations, document rotation, and schedule expired-token pruning. Treat a leaked token as a credential: revoke it immediately and issue a replacement.

For a first-party SPA, use `/sanctum/csrf-cookie`, session login, and `auth:sanctum`; do not issue long-lived personal access tokens to browser JavaScript.

| Project | Specification documents | Standard |
| --- | ---: | --- |
| [Accounting](../../projects/accounting/api/README.md) | 241 | [API](../../architecture/API.md) |
| [Automation](../../projects/automation/api/README.md) | 57 | [API](../../architecture/API.md) |
| [Billing](../../projects/billing/api/README.md) | 81 | [API](../../architecture/API.md) |
| [Boilerplate](../../projects/boilerplate/api/README.md) | 43 | [API](../../architecture/API.md) |
| [Browser Game](../../projects/browser-game/api/README.md) | 61 | [API](../../architecture/API.md) |
| [CMS](../../projects/cms/api/README.md) | 252 | [API](../../architecture/API.md) |
| [Control Panel](../../projects/control-panel/api/README.md) | 61 | [API](../../architecture/API.md) |
| [CRM](../../projects/crm/api/README.md) | 218 | [API](../../architecture/API.md) |
| [Ecommerce](../../projects/ecommerce/api/README.md) | 107 | [API](../../architecture/API.md) |
| [Genealogy](../../projects/genealogy/api/README.md) | 62 | [API](../../architecture/API.md) |
| [Liberu platform](../../projects/liberu/api/README.md) | 4 | [API](../../architecture/API.md) |
| [Maintenance](../../projects/maintenance/api/README.md) | 60 | [API](../../architecture/API.md) |
| [Real Estate](../../projects/real-estate/api/README.md) | 70 | [API](../../architecture/API.md) |
| [SAP enterprise suite](../../projects/sap/api/README.md) | 16 | [API](../../architecture/API.md) |
| [Social Network](../../projects/social-network/api/README.md) | 59 | [API](../../architecture/API.md) |

## Availability and package identities

Counts above describe Markdown specifications, not released packages or implemented features. The [source inventory](../../architecture/SOURCE-INVENTORY.md) records observed manifests and source locations. Repository slugs, design identifiers, and Composer/npm package identities can differ; install using the actual manifest name. Shared capabilities use the [canonical owner](../../architecture/SHARED-MODULES.md) rather than a separate implementation in each project.

## Liberu Music planned modules

See the [22 Music API plans](../../projects/music/api/README.md) and [DAW scope](../../projects/music/MUSIC.md). These are proposed adapters and domain boundaries, not verified package releases.
