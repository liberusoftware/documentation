# Boilerplate: Application Core API presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#application-core). No dedicated package name match was found for this layer in the scanned module manifests. This retained spelling maps to `application`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-application-core-api`
**Matching core package:** [`module-application-core`](../core/application-core.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Environment validation, application metadata, health/readiness, maintenance mode, identifiers, clocks, and shared service contracts.

## Adapter implementation plan

This package presents the Application Core core capability through API. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Publish versioned OpenAPI 3.1 schemas, operation IDs, scopes, pagination, rate limits, idempotency, concurrency, and RFC 9457 Problem Details.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Application Core core boundary.

<!-- observed-api-contract:start -->
## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/application](../../../modules/source/liberusoftware--application.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/application/routes/health.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/application/routes/health.php)

```php
Route::get('/ready', ReadinessController::class)->name('application.ready');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [ReadinessController.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/application/src/Http/Controllers/ReadinessController.php) | `public function __invoke(ReadinessRegistry $registry): JsonResponse` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#application-core), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

<!-- observed-api-contract:end -->
