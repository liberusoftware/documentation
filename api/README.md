# API Module Specifications

## Canonical one-to-one API module index

Each API document describes the optional `module-{independent-module-name}-api` presentation package matching exactly one independent domain module. Applications compose these packages into unified external APIs without moving ownership.

Nuxt clients consume these API contracts through the matching one-to-one packages under [Nuxt 4 implementations](../nuxt/README.md). They must use documented routes, schemas, authentication, permissions, tenant/team context, pagination, errors, idempotency, and versioning; they must not call private Laravel implementation details.

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

The route middleware verifies authentication and token ability. The controller or domain action must still apply the relevant [policy and team checks](../POLICY.md), including resource ownership and current-team membership. A valid token alone never grants access to every resource.

### Revoke and expire tokens

Provide an authenticated token-management action to revoke the current token or all tokens. Configure a finite expiration period for production integrations, document rotation, and schedule expired-token pruning. Treat a leaked token as a credential: revoke it immediately and issue a replacement.

For a first-party SPA, use `/sanctum/csrf-cookie`, session login, and `auth:sanctum`; do not issue long-lived personal access tokens to browser JavaScript.

| Application | API modules | Source |
|---|---:|---|
| [Accounting](accounting/README.md) | 105 | [ACCOUNTING.md](../ACCOUNTING.md) |
| [Automation](automation/README.md) | 11 | [AUTOMATION.md](../AUTOMATION.md) |
| [Billing](billing/README.md) | 16 | [BILLING.md](../BILLING.md) |
| [Browser Game](browser-game/README.md) | 15 | [BROWSER-GAME.md](../BROWSER-GAME.md) |
| [CMS](cms/README.md) | 81 | [CMS.md](../CMS.md) |
| [Control Panel](control-panel/README.md) | 15 | [CONTROL-PANEL.md](../CONTROL-PANEL.md) |
| [CRM](crm/README.md) | 95 | [CRM.md](../CRM.md) |
| [Ecommerce](ecommerce/README.md) | 105 | [ECOMMERCE.md](../ECOMMERCE.md) |
| [Genealogy](genealogy/README.md) | 14 | [GENEALOGY.md](../GENEALOGY.md) |
| [Maintenance](maintenance/README.md) | 14 | [MAINTENANCE.md](../MAINTENANCE.md) |
| [Real Estate](real-estate/README.md) | 15 | [REAL-ESTATE.md](../REAL-ESTATE.md) |
| [SAP](sap/README.md) | 16 | [SAP.md](../SAP.md) |
| [Social Network](social-network/README.md) | 15 | [SOCIAL-NETWORK.md](../SOCIAL-NETWORK.md) |
