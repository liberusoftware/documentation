# Liberu settings

## Canonical settings specification

**Status:** Source of truth
**Applies to:** Laravel 13, PHP 8.5, independent modules, APIs, Filament, Livewire, React/Inertia, Nuxt, workers, and multi-tenant applications
**Related specifications:** [MODULES.md](MODULES.md) · [TENANCY.md](TENANCY.md) · [API.md](API.md) · [FILAMENT.md](FILAMENT.md) · [LIVEWIRE.md](LIVEWIRE.md) · [REACT.md](REACT.md) · [NUXT.md](NUXT.md) · [PSR.md](PSR.md)

## Decision

Liberu owns a framework-neutral settings contract and a Laravel implementation. A setting is a typed, versioned, authorized value addressed by a stable key and an explicit scope. The core module must boot and operate without Filament, Livewire, React, Inertia, or Nuxt being installed.

Presentation packages are adapters:

```text
Application
├── settings core ───────────────> database/cache/secret providers
├── settings API adapter ────────> settings core
├── settings Filament adapter ───> settings core + Filament APIs (optional)
├── settings Livewire adapter ───> settings API/core (optional)
├── settings React/Inertia adapter > settings API (optional)
└── settings Nuxt adapter ───────> settings API (optional)
```

No settings class, controller, resource, component, or frontend may read a settings table directly. All reads and writes pass through the settings contract, which resolves scope, authorization, type, encryption, validation, cache, concurrency, and audit behavior consistently.

## What Spatie Laravel Settings provides

[Spatie Laravel Settings](https://github.com/spatie/laravel-settings) is a strong typed settings package. Its current design uses settings classes with public typed properties and groups, database or Redis repositories, configurable casts and encoders, settings migrations for schema changes, optional caching, locks, events, and encrypted properties. The current package supports Laravel 11–13 and PHP 8.2+; the companion [Filament settings plugin](https://github.com/filamentphp/spatie-laravel-settings-plugin) adds Filament integration but depends on Filament.

Those are useful building blocks, but the package is not the Liberu contract. Our requirements add first-class scope identity and inheritance for global, application, team, user, site, organization, or module contexts; a stable API schema; secret redaction and key rotation; policy-aware reads/writes; explicit audit and revision history; and optional presentation adapters that never make the core depend on Filament.

This is a deliberate architectural choice, not a claim that Spatie is unsuitable for ordinary application settings. A module may use its ideas or an adapter during migration, but its public behavior must follow this document.

## Setting identity and scope

Every setting has:

| Field | Requirement |
|---|---|
| Key | Stable lowercase dot notation such as `billing.invoice.prefix`; never expose a mutable database ID as the contract |
| Type | Registered scalar, enum, date/time, list, map, DTO, JSON schema, or secret type |
| Scope kind | Explicit discriminator such as `global`, `application`, `team`, `user`, `site`, `organization`, or `module` |
| Scope ID | Stable owner identifier, null only for global scope; never accepted as authorization by itself |
| Version | Contract/schema version used by migrations and readers |
| Sensitivity | `public`, `internal`, `personal`, `confidential`, or `secret` |
| Policy | Read, write, reveal, and inheritance rules owned by the module |
| Default | Typed safe default or an explicit “unset”; secrets must not have committed production defaults |

The canonical persisted identity is `(scope_kind, scope_id, key)`. Use a scope registry rather than arbitrary PHP class names in client input. A composite context is represented by an explicit scope resource or a documented scope tuple, not by ambiguous concatenated strings.

Scope resolution is deterministic and module-defined. A typical chain is:

```text
deployment default → global → application → organization/site → team → user
```

The resolver returns the first authorized value at the requested precedence and records which scope supplied it. A child setting may override a parent only when the definition permits it. `null` means an intentional value only when the type allows null; it must not silently mean “fall back”.

## Storage model

The reference implementation should use a module-owned schema similar to:

```text
setting_definitions
  key, type, version, sensitivity, allowed_scopes, policy, default, metadata

setting_values
  key, scope_kind, scope_id, value_json, value_ciphertext, key_version,
  version, etag, created_by, updated_by, created_at, updated_at

setting_revisions
  setting_value_id, old_value_digest, new_value_digest, actor_id, reason,
  request_id, occurred_at
```

Do not store plaintext secrets in `value_json`, logs, cache entries, revisions, exports, error messages, browser props, or analytics. A secret value is encrypted before persistence, has a key version, and is decrypted only inside the authorized server-side service. Prefer envelope encryption backed by the deployment secret manager or KMS; Laravel application encryption is acceptable for a first-party installation when key custody, rotation, and backup recovery are documented.

Use authenticated encryption, key rotation metadata, constant-time secret comparisons, and a migration path for re-encryption. A secret read should return a redacted marker or metadata unless the caller has an explicit reveal permission and the operation is audited. Frontends should normally support “set”, “replace”, and “clear”, never “download current secret”.

## Core module contract

The framework-neutral contract exposes operations equivalent to:

```php
interface SettingsRepository
{
    public function get(SettingAddress $address): SettingValue;

    public function put(SettingAddress $address, mixed $value, int $expectedVersion, Actor $actor): SettingValue;

    public function forget(SettingAddress $address, Actor $actor): void;
}
```

The actual package may use different names, but it must provide typed `get`, validated `put`, explicit `forget`, scoped resolution, optimistic concurrency, audit context, and cache invalidation. Definitions are registered by modules and must be collision-checked. A module cannot redefine another module's key, sensitivity, type, or allowed scopes at runtime.

All writes are transactional and:

1. resolve and authorize the scope;
2. validate the raw input against the registered type and policy;
3. normalize and serialize it canonically;
4. encrypt secret fields before persistence;
5. compare the expected version/ETag;
6. persist the value and revision atomically;
7. invalidate scope-qualified caches and publish a redacted change event.

Concurrent updates return a conflict and never overwrite silently. Cache keys include application, scope kind, scope ID, key, and version. Cache warming must never decrypt secrets into shared cache stores.

## Module ownership and migrations

Each setting key has one owning module. Definitions, defaults, validators, policies, OpenAPI schemas, migrations, and tests live with that module. A settings migration is required when a key is added, removed, renamed, retyped, encrypted, or its default/inheritance semantics change.

Migrations must be forward-compatible, idempotent where practical, tenant-aware, and explicit about secret handling. Never invent a tenant or copy one team's value into another. A migration that cannot prove ownership stops with an actionable failure. Keep old readers until all supported writers have moved, then remove compatibility in a later release.

## Authorization and tenancy

Settings are not automatically safe because they are configuration. Apply [TENANCY.md](TENANCY.md) and [POLICY.md](POLICY.md):

- global settings require global administration or an explicit public-read policy;
- application/module settings require the application capability and may still be team-scoped;
- team settings require proven membership and a team-management permission;
- user settings require the owning user or an explicitly authorized administrator;
- secret settings require a separate reveal/rotate capability from ordinary setting edit;
- a caller-supplied `scope_id` never grants access and must be checked against trusted context;
- cross-team operations require a dedicated service identity, allowlist, purpose, audit trail, and bounded selection.

The settings service must fail closed when scope or actor context is missing. A global read must be explicit; it must not be the accidental result of an unauthenticated request, missing team, queue worker, or failed route binding.

## API adapter

The API adapter is optional but follows [API.md](API.md) and OpenAPI 3.1. It exposes definitions and values only through authorized, versioned module routes, for example:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/api/v1/settings/definitions` | List definitions visible to the actor, without secret values |
| `GET` | `/api/v1/settings/{scope}/{key}` | Read one resolved or raw authorized value; secrets are redacted by default |
| `PUT` | `/api/v1/settings/{scope}/{key}` | Replace a value with `If-Match`/version and idempotency support |
| `DELETE` | `/api/v1/settings/{scope}/{key}` | Clear an allowed override and reveal the inherited value |
| `POST` | `/api/v1/settings/{scope}/{key}/rotate` | Replace a secret through an audited rotation operation |

Responses use the standard `data`, `meta`, and RFC 9457 Problem Details shapes. Never serialize the internal ciphertext, encryption key version, policy object, or unauthorized scopes. Generated clients must use the released OpenAPI contract.

## Presentation adapters

### Filament

The `module-*-settings-filament` adapter is optional and depends on the settings core plus Filament 5. It may provide schemas, tables, pages, actions, masked secret fields, scope selectors, conflict notifications, and audit views. It must call the core service, not models directly. Secret fields are write-only or reveal-protected, and the application attaches the plugin to panels explicitly. Installing the core must never require Filament.

### Livewire

The `module-*-settings-livewire` adapter uses typed public state, locked scope identity, server-side validation, explicit authorization on every action, and the core service for reads/writes. Do not put decrypted secrets in public properties or browser-visible hydration state. Handle stale versions and failed writes as recoverable conflicts.

### React/Inertia

The `module-*-settings-react-inertia` adapter consumes the API or an application-owned Inertia action. It uses typed props, `useForm`/`router`, masked secret controls, accessible validation/conflict states, and no long-lived secret storage. Scope selectors are server-authorized and never treated as client authorization.

### Nuxt

The `module-*-settings-nuxt` adapter consumes the versioned API with typed composables and SSR-safe fetching. Protected settings and decrypted secrets must not enter public runtime config, SSR payloads, prerendered output, browser storage, or logs. Use explicit cache keys containing scope context.

## Events, observability, and operations

Publish redacted events such as `SettingChanged`, `SettingCleared`, `SettingRotated`, and `SettingConflict`. Include key, scope kind/ID, actor, module, version, request/correlation ID, and outcome; include value digests rather than values. Audit reads of secrets, failed authorization, reveal, rotation, migration, and cross-scope access.

Monitor cache misses, read/write latency, conflicts, failed decryptions, key-version backlog, unauthorized attempts, and stale definitions. Backups must preserve encrypted values and the key-recovery procedure separately. A database backup without the required encryption-key recovery path is not a settings backup.

## Verification requirements

Test:

- scalar, enum, date/time, array, object, nullable, custom, and invalid values;
- every scope kind, precedence, fallback, override clearing, deleted scope, and missing context;
- team isolation across two teams, crafted scope IDs, direct IDs, route binding, caches, queues, and exports;
- plaintext absence in storage, logs, caches, events, revisions, API responses, SSR payloads, and browser state;
- key rotation, failed decryption, backup restore, secret replacement, redaction, and reveal authorization;
- optimistic concurrency, retries, idempotency, transactional rollback, cache invalidation, and event delivery;
- core installation with no presentation package, then each optional Filament, Livewire, React/Inertia, and Nuxt adapter;
- OpenAPI validation, policy tests, accessibility, localization, audit completeness, and generated-client compatibility.

## Definition of done

Settings are complete when the owning module has a registered typed definition, migration, policy, scope behavior, encrypted-secret classification where needed, API/OpenAPI contract, optional presentation adapters, audit/redaction behavior, concurrency strategy, cache invalidation, recovery procedure, and negative tests proving that another scope cannot read or change the value.

## References

- [Spatie Laravel Settings documentation and package](https://github.com/spatie/laravel-settings)
- [Spatie Laravel Settings on Packagist](https://packagist.org/packages/spatie/laravel-settings)
- [Spatie Filament settings plugin](https://github.com/filamentphp/spatie-laravel-settings-plugin)
- [Laravel encryption](https://laravel.com/docs/13.x/encryption)
- [Laravel cache](https://laravel.com/docs/13.x/cache)
- [Laravel authorization](https://laravel.com/docs/13.x/authorization)
- [OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0)
